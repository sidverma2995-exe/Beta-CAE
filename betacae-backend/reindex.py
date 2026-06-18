"""
Rebuild the FAISS index from scratch using all HTML files in the Coding_User_Guide.
Run this once after the rag_engine.py improvements:
    python reindex.py
"""
import os
import glob
import time

# Adjust this path if needed
DOCS_ROOT = os.path.join(
    os.path.dirname(__file__),
    "..", "Coding_User_Guide", "python_api", "html"
)
FAISS_INDEX_PATH = "./faiss_index"

print("Loading RAG engine (this loads the embedding model)...")
from rag_engine import RAGEngine, _clean_html, _get_splitter, _split_api_entries, _is_noise_source

engine = RAGEngine.__new__(RAGEngine)

# Minimal init — only embedding model, no LLM needed for indexing
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

engine.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
engine.vectorstore = None

# Wipe old index files so we start clean
for fname in ("index.faiss", "index.pkl"):
    fpath = os.path.join(FAISS_INDEX_PATH, fname)
    if os.path.exists(fpath):
        try:
            os.remove(fpath)
            print(f"Removed {fpath}")
        except PermissionError:
            print(f"WARNING: Could not remove {fpath} (file in use). Will overwrite on save.")
os.makedirs(FAISS_INDEX_PATH, exist_ok=True)

# Collect all HTML files
html_files = glob.glob(os.path.join(DOCS_ROOT, "**", "*.html"), recursive=True)
print(f"Found {len(html_files)} HTML files to index\n")

BATCH_SIZE = 50
total_chunks_all = 0
t_start = time.time()

for i, filepath in enumerate(sorted(html_files), 1):
    rel_name = os.path.relpath(filepath, DOCS_ROOT)
    ext = ".html"

    # Skip navigation / index pages (genindex, modindex, search) — pure noise.
    if _is_noise_source(rel_name):
        print(f"  [{i}/{len(html_files)}] SKIP (noise/index page): {rel_name}")
        continue

    with open(filepath, encoding="utf-8", errors="ignore") as f:
        raw = f.read()

    clean = _clean_html(raw)
    if not clean.strip():
        print(f"  [{i}/{len(html_files)}] SKIP (empty after cleaning): {rel_name}")
        continue

    splitter = _get_splitter(ext)
    chunks = _split_api_entries(clean) or splitter.split_text(clean)
    chunks = [c.strip() for c in chunks if c.strip()]
    total_chunks_all += len(chunks)

    metadatas = [{"source": rel_name, "chunk": j} for j in range(len(chunks))]

    for b in range(0, len(chunks), BATCH_SIZE):
        batch_chunks = chunks[b:b + BATCH_SIZE]
        batch_meta = metadatas[b:b + BATCH_SIZE]
        if engine.vectorstore is None:
            engine.vectorstore = FAISS.from_texts(
                texts=batch_chunks, embedding=engine.embeddings, metadatas=batch_meta
            )
        else:
            engine.vectorstore.add_texts(texts=batch_chunks, metadatas=batch_meta)

    print(f"  [{i}/{len(html_files)}] {rel_name} → {len(chunks)} chunks")

print(f"\nSaving index ({total_chunks_all} total chunks)...")
engine.vectorstore.save_local(FAISS_INDEX_PATH)
print(f"Done in {time.time() - t_start:.1f}s — index saved to {FAISS_INDEX_PATH}")
