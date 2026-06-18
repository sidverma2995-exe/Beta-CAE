import os
import re
import logging
import time
import threading
import torch
from html.parser import HTMLParser
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, TextIteratorStreamer

logger = logging.getLogger("betacae.rag_engine")

FAISS_INDEX_PATH = "./faiss_index"

# Navigation / index pages that contain no real documentation — pure noise.
# These pollute retrieval (e.g. genindex.html is just an alphabetical list of
# every symbol name) so they are skipped at index time and penalised at query time.
_NOISE_SOURCE_RE = re.compile(
    r'(?:^|[\\/])(?:genindex|py-modindex|modindex|search|searchindex)\b',
    re.IGNORECASE,
)

# Matches qualified API identifiers in a user question, e.g. "ansa.base.CollectEntities"
# or a bare CamelCase function name like "CollectEntities".
_QUERY_API_RE = re.compile(r'\b(?:ansa|meta|sdm|guitk)\.[\w.]+|\b[A-Z][a-zA-Z0-9]{3,}\b')


def _is_noise_source(source: str) -> bool:
    return bool(_NOISE_SOURCE_RE.search(source or ""))


# ---------------------------------------------------------------------------
# HTML stripping (stdlib only, no extra dependency)
# ---------------------------------------------------------------------------
class _HTMLStripper(HTMLParser):
    # These tags have paired open/close — safe to track depth
    _SKIP_TAGS = {"script", "style", "head", "noscript", "nav", "footer", "header"}
    # Void elements that must NOT affect skip depth (no closing tag in HTML5)
    _VOID_ELEMENTS = {"area", "base", "br", "col", "embed", "hr", "img",
                      "input", "link", "meta", "param", "source", "track", "wbr"}
    _BLOCK_TAGS = {"p", "div", "li", "td", "th", "h1", "h2", "h3", "h4",
                   "h5", "h6", "tr", "br", "section", "article", "pre"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self._parts: list[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag in self._VOID_ELEMENTS:
            return  # void element — no depth change
        if tag in self._SKIP_TAGS:
            self._skip_depth += 1
        elif tag in self._BLOCK_TAGS and self._skip_depth == 0:
            self._parts.append("\n")

    def handle_endtag(self, tag):
        if tag in self._VOID_ELEMENTS:
            return
        if tag in self._SKIP_TAGS:
            self._skip_depth = max(0, self._skip_depth - 1)
        elif tag in self._BLOCK_TAGS and self._skip_depth == 0:
            self._parts.append("\n")

    def handle_data(self, data):
        if self._skip_depth == 0:
            self._parts.append(data)

    def get_text(self) -> str:
        text = "".join(self._parts)
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()


def _clean_html(raw: str) -> str:
    stripper = _HTMLStripper()
    try:
        stripper.feed(raw)
    except Exception:
        pass
    return stripper.get_text()


def _preprocess_text(text: str, ext: str) -> str:
    """Clean raw file content before chunking."""
    if ext in (".html", ".htm"):
        return _clean_html(text)
    return text


# Regex that matches the start of a Beta CAE API entry in cleaned HTML text.
# Each entry begins with the function/class name line followed by "NAME:" or
# a Sphinx autodoc qualified name like "ansa.base.FunctionName(".
_API_ENTRY_RE = re.compile(
    r'(?m)(?=^(?:[A-Za-z_][\w ,]+\(function\)|'
    r'(?:class |exception )?'
    r'(?:ansa|meta|sdm|guitk)\.\w[\w.]*\s*(?:\(|$)))',
)

# Section headers that delimit parts of an API entry — keep these together
_API_SECTIONS = ("NAME:", "SYNOPSIS:", "DESCRIPTION:", "ARGUMENTS:",
                 "EXCEPTIONS:", "RETURN TYPE:", "RETURN VALUE:", "EXAMPLE:",
                 "Parameters:", "Returns:", "Return type:", "Raises:", "Example:")


def _split_api_entries(text: str, max_chunk: int = 4000) -> list[str] | None:
    """
    Split Beta CAE API documentation text on function/class entry boundaries.
    Each returned chunk covers exactly one API entry (NAME … EXAMPLE).
    Returns None when no API entry pattern is detected.
    """
    has_api_format = any(s in text for s in ("NAME:", "SYNOPSIS:", "ARGUMENTS:"))
    has_sphinx_format = bool(_API_ENTRY_RE.search(text))
    if not has_api_format and not has_sphinx_format:
        return None

    if has_api_format:
        # Manual-style: split on the header line before each NAME: block
        parts = re.split(r'(?m)^(?=\S[^\n]*\n\s*NAME:)', text)
    else:
        # Sphinx autodoc-style: split on qualified API name starts
        parts = _API_ENTRY_RE.split(text)

    chunks: list[str] = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if len(part) <= max_chunk:
            chunks.append(part)
        else:
            # Entry is larger than max_chunk — split by section then by chars
            # First try splitting on section headers to preserve coherence
            section_parts = re.split(
                r'(?m)^(?=' + '|'.join(re.escape(s) for s in _API_SECTIONS) + r')',
                part
            )
            buf = ""
            for sp in section_parts:
                if len(buf) + len(sp) <= max_chunk:
                    buf = (buf + "\n" + sp).strip() if buf else sp.strip()
                else:
                    if buf:
                        chunks.append(buf)
                    buf = sp.strip()
            if buf:
                chunks.append(buf)

    return chunks or None


def _get_splitter(ext: str) -> RecursiveCharacterTextSplitter:
    """Return a fallback splitter for non-API content."""
    CODE_EXTS = {
        ".py": Language.PYTHON,
        ".js": Language.JS,
        ".ts": Language.JS,
    }
    if ext in CODE_EXTS:
        return RecursiveCharacterTextSplitter.from_language(
            language=CODE_EXTS[ext],
            chunk_size=800,
            chunk_overlap=100,
        )
    # Prose / HTML fallback — larger chunks, more overlap
    return RecursiveCharacterTextSplitter(
        chunk_size=1200,
        chunk_overlap=200,
        length_function=len,
        separators=["\n\n", "\n", ". ", " ", ""],
    )


class RAGEngine:
    def __init__(self):
        self.embedding_model = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
        self.llm_model = os.getenv("LLM_MODEL", "TinyLlama/TinyLlama-1.1B-Chat-v1.0")

        logger.info(f"Loading embedding model: {self.embedding_model}")
        start = time.time()
        self.embeddings = HuggingFaceEmbeddings(model_name=self.embedding_model)
        logger.info(f"Embedding model loaded in {time.time() - start:.2f}s")

        # Load existing FAISS index or start with None
        if os.path.exists(FAISS_INDEX_PATH):
            logger.info(f"Loading existing FAISS index from {FAISS_INDEX_PATH}")
            self.vectorstore = FAISS.load_local(
                FAISS_INDEX_PATH, self.embeddings, allow_dangerous_deserialization=True
            )
            logger.info("FAISS index loaded successfully")
        else:
            logger.info("No existing FAISS index found, starting fresh")
            self.vectorstore = None

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=150,
            length_function=len,
        )

        # Use local pipeline instead of HuggingFace Inference API
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f"Using device: {self.device}")

        logger.info(f"Loading LLM model: {self.llm_model}")
        start = time.time()
        self.tokenizer = AutoTokenizer.from_pretrained(self.llm_model)
        logger.info(f"Tokenizer loaded in {time.time() - start:.2f}s")
        start = time.time()
        self.model = AutoModelForCausalLM.from_pretrained(
            self.llm_model,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        )
        self.model.to(self.device)
        logger.info(f"Model weights loaded in {time.time() - start:.2f}s")
        pipe = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            max_new_tokens=512,
            do_sample=False,
        )
        self.llm = HuggingFacePipeline(pipeline=pipe)
        logger.info("LLM pipeline ready")

    def add_document(self, text: str, filename: str):
        """Blocking add — used by the plain /upload endpoint."""
        self.add_document_with_progress(text, filename)

    def add_document_with_progress(self, text: str, filename: str, progress_cb=None, batch_size: int = 50):
        """
        Index a document, optionally reporting progress via progress_cb.
        progress_cb(step, message, current=0, total=0)
        """
        def report(step, message, current=0, total=0):
            logger.info(message)
            if progress_cb:
                progress_cb(step, message, current, total)

        ext = os.path.splitext(filename)[1].lower()

        report("chunking", f"Cleaning and splitting '{filename}'...")
        clean_text = _preprocess_text(text, ext)

        # Try API-aware chunking first (keeps each API function as one chunk)
        chunks = _split_api_entries(clean_text)
        if chunks is None:
            splitter = _get_splitter(ext)
            chunks = splitter.split_text(clean_text)

        # Drop empty/whitespace-only chunks
        chunks = [c.strip() for c in chunks if c.strip()]
        total_chunks = len(chunks)
        report("chunking", f"Split into {total_chunks} chunks", total_chunks, total_chunks)

        metadatas = [{"source": filename, "chunk": i} for i in range(total_chunks)]

        start = time.time()
        for batch_start in range(0, total_chunks, batch_size):
            batch_end = min(batch_start + batch_size, total_chunks)
            batch_chunks = chunks[batch_start:batch_end]
            batch_meta = metadatas[batch_start:batch_end]

            report("embedding", f"Embedding chunks {batch_end}/{total_chunks}...", batch_end, total_chunks)

            if self.vectorstore is None:
                self.vectorstore = FAISS.from_texts(
                    texts=batch_chunks, embedding=self.embeddings, metadatas=batch_meta
                )
            else:
                self.vectorstore.add_texts(texts=batch_chunks, metadatas=batch_meta)

        logger.info(f"All embeddings created in {time.time() - start:.2f}s")

        report("saving", "Saving index to disk...")
        self.vectorstore.save_local(FAISS_INDEX_PATH)
        report("done", f"'{filename}' indexed successfully ({total_chunks} chunks)", total_chunks, total_chunks)

    def _get_context(self, question: str):
        """Returns (context_str, sources_list, chunks_list) using hybrid retrieval.

        Strategy:
          1. Pull a wide pool of candidates by raw vector similarity (with scores).
          2. Drop navigation/index pages (genindex, modindex, search) — pure noise.
          3. Re-rank: start from the vector distance, then apply boosts for chunks
             that literally contain the API identifiers in the question and for
             real reference pages, so the exact function doc wins over short index
             entries that merely mention the name.
        """
        context = ""
        sources = []
        chunks = []  # list of {"source": ..., "content": ...}
        if self.vectorstore is None:
            logger.info("No vector store available, querying LLM without context")
            return context, sources, chunks

        try:
            logger.info("Searching FAISS for relevant documents...")
            start = time.time()

            # 1. Wide candidate pool with similarity scores (lower distance = better)
            scored = self.vectorstore.similarity_search_with_score(question, k=30)
            logger.info(f"FAISS returned {len(scored)} candidates in {time.time() - start:.2f}s")

            # Identifiers the user is asking about (e.g. "CollectEntities", "ansa.base.X")
            query_terms = {t.lower() for t in _QUERY_API_RE.findall(question)}

            ranked = []
            for doc, dist in scored:
                source = doc.metadata.get("source", "unknown")
                if _is_noise_source(source):
                    continue  # 2. skip index/navigation pages entirely

                content_l = doc.page_content.lower()
                # 3. Lower score is better — start from vector distance, subtract boosts.
                score = float(dist)
                # Boost chunks that literally contain the requested identifier(s).
                if query_terms and any(term in content_l for term in query_terms):
                    score -= 0.35
                # Prefer the actual API reference pages over prose / getting-started.
                if "reference" in source.lower() and "generated" in source.lower():
                    score -= 0.10
                # Slightly favour substantial chunks over one-line stubs.
                if len(doc.page_content) > 300:
                    score -= 0.05

                ranked.append((score, doc))

            ranked.sort(key=lambda x: x[0])
            top_docs = [doc for _, doc in ranked[:4]]

            context = "\n\n---\n\n".join(doc.page_content for doc in top_docs)
            sources = list(dict.fromkeys(doc.metadata.get("source", "unknown") for doc in top_docs))
            chunks = [
                {"source": doc.metadata.get("source", "unknown"), "content": doc.page_content}
                for doc in top_docs
            ]
            logger.info(f"Context length: {len(context)} chars, Sources: {sources}")
        except Exception as e:
            logger.error(f"FAISS search failed: {e}", exc_info=True)
        return context, sources, chunks

    def query_stream(self, question: str, mode: str, output_queue, loop):
        """Run streaming generation in a background thread, pushing tokens to an asyncio Queue."""
        # Tokens that signal the model is starting a new conversation turn — stop there.
        STOP_SEQS = ("<|user|>", "<|system|>", "</s>")

        try:
            context, sources, chunks = self._get_context(question)
            prompt_text = self._build_prompt(question, context, mode)
            streamer = TextIteratorStreamer(
                self.tokenizer, skip_prompt=True, skip_special_tokens=True
            )
            inputs = self.tokenizer(prompt_text, return_tensors="pt")
            inputs = {k: v.to(self.device) for k, v in inputs.items()}

            gen_thread = threading.Thread(
                target=lambda: self.model.generate(
                    **inputs,
                    streamer=streamer,
                    max_new_tokens=512,
                    do_sample=False,
                ),
                daemon=True,
            )
            gen_thread.start()

            # Buffer the first tokens to handle the case where skip_prompt didn't work
            # and the model echoes back the prompt (containing <|assistant|>).
            head_buf = ""
            head_done = False  # once True, we are streaming real assistant tokens

            for token in streamer:
                if not head_done:
                    head_buf += token
                    # If model echoed the prompt, find the last <|assistant|> and stream from there
                    if "<|assistant|>" in head_buf:
                        head_done = True
                        after = head_buf.split("<|assistant|>")[-1]
                        if after:
                            loop.call_soon_threadsafe(output_queue.put_nowait, ("token", after))
                    elif len(head_buf) > 100:
                        # No echo detected after 100 chars — skip_prompt is working fine
                        head_done = True
                        loop.call_soon_threadsafe(output_queue.put_nowait, ("token", head_buf))
                    continue

                # Stop generation if model starts a new conversation turn
                if any(s in token for s in STOP_SEQS):
                    break

                loop.call_soon_threadsafe(output_queue.put_nowait, ("token", token))

            loop.call_soon_threadsafe(output_queue.put_nowait, ("done", {"sources": sources, "chunks": chunks}))
            gen_thread.join()
        except Exception as e:
            logger.error(f"Streaming generation failed: {e}", exc_info=True)
            loop.call_soon_threadsafe(output_queue.put_nowait, ("error", str(e)))

    def query(self, question: str, mode: str = "qa") -> dict:
        logger.info(f"Query started - Mode: {mode}, Question: '{question[:80]}...'")
        context, sources, chunks = self._get_context(question)

        # Build prompt based on mode
        prompt_text = self._build_prompt(question, context, mode)
        logger.info(f"Prompt built - Length: {len(prompt_text)} chars")

        try:
            logger.info("Invoking LLM for text generation...")
            start = time.time()
            response = self.llm.invoke(prompt_text)
            duration = time.time() - start
            logger.info(f"LLM response generated in {duration:.2f}s - Raw length: {len(response)} chars")
            # Clean up response - extract only the assistant's answer
            answer = response.strip()
            # Extract only the assistant's reply (handles prompt echo)
            if "<|assistant|>" in answer:
                answer = answer.split("<|assistant|>")[-1].strip()
            # Stop at the next conversation turn if the model continues generating
            for stop in ("<|user|>", "<|system|>", "</s>"):
                if stop in answer:
                    answer = answer.split(stop)[0].strip()
            logger.info(f"Final answer length: {len(answer)} chars")
            return {"answer": answer, "sources": sources, "chunks": chunks}
        except Exception as e:
            logger.error(f"LLM invocation failed: {e}", exc_info=True)
            return {"answer": f"Error generating response: {str(e)}", "sources": [], "chunks": []}

    def _build_prompt(self, question: str, context: str, mode: str) -> str:
        has_context = bool(context.strip())
        ctx_block = f"""Relevant documentation:
{context}

""" if has_context else ""

        if mode == "qa":
            return f"""<|system|>
You are Beta CAE Assistant, an expert on Beta CAE software (ANSA, META, EPILYSIS).
Answer ONLY using the provided documentation. Give a clear, summarized explanation in plain English.
Describe what the function/feature does, its key parameters, and its return value in prose.
Do NOT output any code, code blocks, or example scripts — only a written summary.
If the answer is not in the documentation, say "I don't have information about that in the current documentation."
Do NOT make up function names, parameters, or behaviour.
</s>
<|user|>
{ctx_block}Question: {question}
</s>
<|assistant|>
"""
        elif mode == "chat":
            return f"""<|system|>
You are Beta CAE Assistant, an expert on Beta CAE software (ANSA, META, EPILYSIS).
Use the provided documentation to answer accurately in a friendly, conversational way.
Explain things in plain English as a summary. Do NOT output code or example scripts — describe the answer in words only.
If the answer is not in the documentation, say so honestly.
</s>
<|user|>
{ctx_block}{question}
</s>
<|assistant|>
"""
        else:  # code
            return f"""<|system|>
You are a Beta CAE Python scripting assistant. Your final output MUST be a single valid .py file that can be saved and run directly — raw Python code only, no markdown, no triple backticks, no prose outside of code comments.

Reason step by step, but express EVERY part of your reasoning as Python comments (lines starting with #) at the top of the file. Follow this exact chain of thought before writing any executable code:

# Step 1 — Goal: restate the user's task in one comment line.
# Step 2 — Relevant API: list the exact function name(s) from the documentation below that solve the task. If none exist, stop and output only:
#   # ERROR: Required API not found in documentation.
#   # Upload the relevant reference file and try again.
# Step 3 — Plan: outline the ordered steps the script will perform, one comment line per step.
# Step 4 — Implementation: write the executable Python code that carries out the plan.

Hard rules:
- Use ONLY the API functions visible in the documentation below; never invent names, parameters, or behaviour.
- Adapt the documentation example to the user's specific task.
- Keep every reasoning sentence inside a # comment so the whole file stays runnable.
- Add a short inline comment on each non-trivial line of executable code.
</s>
<|user|>
{ctx_block}Task: {question}
</s>
<|assistant|>
# Step 1 — Goal:"""
