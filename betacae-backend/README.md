# Beta CAE Backend

A RAG (Retrieval Augmented Generation) backend built with FastAPI, LangChain, and free HuggingFace LLMs.

## Setup

1. **Create a virtual environment:**
   ```bash
   cd betacae-backend
   python -m venv venv
   venv\Scripts\activate    # Windows
   # source venv/bin/activate  # Linux/Mac
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment:**
   - Copy `.env.example` to `.env`
   - Get a free HuggingFace API token from https://huggingface.co/settings/tokens
   - Paste your token in the `.env` file

4. **Run the server:**
   ```bash
   python main.py
   ```
   The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /health` - Health check
- `POST /query` - Query the RAG system
  - Body: `{ "query": "your question", "mode": "qa|chat|code" }`
- `POST /upload` - Upload a document to the knowledge base
  - Multipart form with file field

## Free LLM

This app uses the HuggingFace Inference API which provides free access to models like:
- `mistralai/Mistral-7B-Instruct-v0.3` (default)
- `google/gemma-2b-it`
- `meta-llama/Llama-2-7b-chat-hf`

The embedding model (`all-MiniLM-L6-v2`) runs locally and requires no API key.
