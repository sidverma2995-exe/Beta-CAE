import logging
import time
import io
from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os

from rag_engine import RAGEngine

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("betacae.main")

logger.info("Starting Beta CAE Backend...")

app = FastAPI(title="Beta CAE Backend", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger.info("Initializing RAG Engine...")
rag_engine = RAGEngine()
logger.info("RAG Engine initialized successfully")


class QueryRequest(BaseModel):
    query: str
    mode: str  # 'qa', 'chat', or 'code'


class QueryResponse(BaseModel):
    answer: str
    sources: list[str] = []


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    logger.info(f"Incoming request: {request.method} {request.url.path}")
    response = await call_next(request)
    duration = time.time() - start_time
    logger.info(f"Request completed: {request.method} {request.url.path} - Status: {response.status_code} - Duration: {duration:.2f}s")
    return response


@app.get("/health")
async def health_check():
    logger.info("Health check requested")
    return {"status": "healthy"}


@app.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    logger.info(f"Query received - Mode: {request.mode}, Query: '{request.query[:100]}...'")
    if not request.query.strip():
        logger.warning("Empty query received, returning 400")
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    start_time = time.time()
    result = rag_engine.query(request.query, request.mode)
    duration = time.time() - start_time
    logger.info(f"Query processed in {duration:.2f}s - Answer length: {len(result['answer'])} chars, Sources: {result.get('sources', [])}")
    return QueryResponse(answer=result["answer"], sources=result.get("sources", []))


@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    logger.info(f"Upload request received - Filename: {file.filename}")
    if not file.filename:
        logger.warning("No filename provided in upload request")
        raise HTTPException(status_code=400, detail="No file provided")

    allowed_extensions = {".txt", ".pdf", ".md", ".py", ".js", ".ts", ".html", ".css"}
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in allowed_extensions:
        logger.warning(f"Unsupported file type: {ext}")
        raise HTTPException(
            status_code=400,
            detail=f"File type {ext} not supported. Allowed: {allowed_extensions}"
        )

    content = await file.read()
    file_size = len(content)
    logger.info(f"File read - Size: {file_size / 1024:.1f} KB")

    # Limit file size to 10MB
    # if file_size > 10 * 1024 * 1024:
    #     logger.warning(f"File too large: {file_size / (1024*1024):.1f} MB")
    #     raise HTTPException(status_code=400, detail="File too large. Max 10MB.")

    if ext == ".pdf":
        try:
            import fitz  # PyMuPDF
            logger.info("Extracting text from PDF...")
            pdf_doc = fitz.open(stream=content, filetype="pdf")
            text_content = ""
            total_pages = pdf_doc.page_count
            for page_num, page in enumerate(pdf_doc):
                page_text = page.get_text()
                text_content += page_text
                # logger.info(f"PDF page {page_num + 1}: {len(page_text)} chars extracted")
            pdf_doc.close()
            logger.info(f"PDF total extracted text: {len(text_content)} chars from {total_pages} pages")
            if not text_content.strip():
                raise HTTPException(status_code=400, detail="Could not extract text from PDF. The PDF may be image-based.")
        except ImportError:
            logger.error("PyMuPDF not installed")
            raise HTTPException(status_code=500, detail="PDF processing not available. Install PyMuPDF.")
    else:
        text_content = content.decode("utf-8", errors="ignore")

    logger.info(f"Indexing document: {file.filename} ({len(text_content)} chars)")
    start_time = time.time()
    rag_engine.add_document(text_content, file.filename)
    duration = time.time() - start_time
    logger.info(f"Document indexed successfully in {duration:.2f}s: {file.filename}")

    return {"message": f"Document '{file.filename}' uploaded and indexed successfully."}


if __name__ == "__main__":
    import uvicorn
    logger.info("Starting Uvicorn server on http://0.0.0.0:8000 with auto-reload")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
