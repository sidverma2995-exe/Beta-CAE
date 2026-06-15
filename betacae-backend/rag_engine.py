import os
import logging
import time
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

logger = logging.getLogger("betacae.rag_engine")

FAISS_INDEX_PATH = "./faiss_index"


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
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )

        # Use local pipeline instead of HuggingFace Inference API
        logger.info(f"Loading LLM model: {self.llm_model}")
        start = time.time()
        tokenizer = AutoTokenizer.from_pretrained(self.llm_model)
        logger.info(f"Tokenizer loaded in {time.time() - start:.2f}s")
        start = time.time()
        model = AutoModelForCausalLM.from_pretrained(self.llm_model)
        logger.info(f"Model weights loaded in {time.time() - start:.2f}s")
        pipe = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            max_new_tokens=512,
            temperature=0.7,
            do_sample=True,
        )
        self.llm = HuggingFacePipeline(pipeline=pipe)
        logger.info("LLM pipeline ready")

    def add_document(self, text: str, filename: str):
        logger.info(f"Adding document: {filename} ({len(text)} chars)")
        chunks = self.text_splitter.split_text(text)
        logger.info(f"Document split into {len(chunks)} chunks")
        metadatas = [{"source": filename, "chunk": i} for i in range(len(chunks))]

        start = time.time()
        if self.vectorstore is None:
            logger.info("Creating new FAISS vector store")
            self.vectorstore = FAISS.from_texts(texts=chunks, embedding=self.embeddings, metadatas=metadatas)
        else:
            logger.info("Adding to existing FAISS vector store")
            self.vectorstore.add_texts(texts=chunks, metadatas=metadatas)
        logger.info(f"Embeddings created in {time.time() - start:.2f}s")

        self.vectorstore.save_local(FAISS_INDEX_PATH)
        logger.info(f"FAISS index saved to {FAISS_INDEX_PATH}")

    def query(self, question: str, mode: str = "qa") -> dict:
        logger.info(f"Query started - Mode: {mode}, Question: '{question[:80]}...'")
        context = ""
        sources = []

        # Retrieve relevant context from vector store if available
        if self.vectorstore is not None:
            try:
                logger.info("Searching FAISS for relevant documents...")
                start = time.time()
                docs = self.vectorstore.similarity_search(question, k=3)
                logger.info(f"FAISS search returned {len(docs)} docs in {time.time() - start:.2f}s")
                context = "\n\n".join(doc.page_content for doc in docs)
                sources = list(set(doc.metadata.get("source", "unknown") for doc in docs))
                logger.info(f"Context length: {len(context)} chars, Sources: {sources}")
            except Exception as e:
                logger.error(f"FAISS search failed: {e}")
        else:
            logger.info("No vector store available, querying LLM without context")

        # Build prompt based on mode
        prompt_text = self._build_prompt(question, context, mode)
        logger.info(f"Prompt built - Length: {len(prompt_text)} chars")

        try:
            logger.info("Invoking LLM for text generation...")
            start = time.time()
            response = self.llm.invoke(prompt_text)
            duration = time.time() - start
            logger.info(f"LLM response generated in {duration:.2f}s - Raw length: {len(response)} chars")
            logger.info(f"=== FULL RAW LLM RESPONSE ===\n{response}\n=== END RAW RESPONSE ===")
            # Clean up response - extract only the assistant's answer
            answer = response.strip()
            if "<|assistant|>" in answer:
                answer = answer.split("<|assistant|>")[-1].strip()
            logger.info(f"Final answer length: {len(answer)} chars")
            logger.info(f"=== FINAL ANSWER SENT TO FRONTEND ===\n{answer}\n=== END FINAL ANSWER ===")
            return {"answer": answer, "sources": sources}
        except Exception as e:
            logger.error(f"LLM invocation failed: {e}", exc_info=True)
            return {"answer": f"Error generating response: {str(e)}", "sources": []}

    def _build_prompt(self, question: str, context: str, mode: str) -> str:
        if mode == "qa":
            return f"""<|system|>
You are Beta CAE, a helpful question-answering assistant. Answer clearly and concisely.
</s>
<|user|>
Context: {context}

Question: {question}
</s>
<|assistant|>
"""
        elif mode == "chat":
            return f"""<|system|>
You are Beta CAE, a friendly and helpful AI chat assistant. Be conversational and engaging.
</s>
<|user|>
Context: {context}

{question}
</s>
<|assistant|>
"""
        else:  # code
            return f"""<|system|>
You are Beta CAE, an expert programming assistant. Provide clear, well-commented code examples with explanations.
</s>
<|user|>
Context: {context}

{question}
</s>
<|assistant|>
"""
