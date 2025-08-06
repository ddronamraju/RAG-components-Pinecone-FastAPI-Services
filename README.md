# Modular RAG with Pinecone & FastAPI

This project implements a modular Retrieval-Augmented Generation (RAG) pipeline using FastAPI, Pinecone, and Hugging Face API endpoints. It supports PDF ingestion (including text, images, tables), vectorization, and retrieval, with each functionality in a separate module and service.

## Project Structure

- `.env` — Store your Hugging Face and Pinecone API keys and configuration.
- `requirements.txt` — Python dependencies for the project.
- `data_ingestion.py` — Extracts text, images, and tables from PDF documents.
- `vectorization.py` — Sends extracted content to Hugging Face API for embeddings.
- `retrieval.py` — Handles Pinecone vector DB operations (upsert, query).
- `data_ingestion_service.py` — FastAPI service for PDF ingestion.
- `vectorization_service.py` — FastAPI service for vectorization.
- `retrieval_service.py` — FastAPI service for Pinecone upsert and retrieval.
- `sample_client.py` — Example client script to interact with the services.

## Setup

1. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

2. **Configure environment variables:**
   - Edit `.env` and add your Hugging Face and Pinecone API keys and configuration.

3. **Run FastAPI services:**
   Open three separate terminals and run each service (activate the virtual environment in each terminal first):
   
   **Terminal 1:**
   ```powershell
   .\venv\Scripts\Activate
   uvicorn data_ingestion_service:app --reload --port 8000
   ```
   
   **Terminal 2:**
   ```powershell
   .\venv\Scripts\Activate
   uvicorn vectorization_service:app --reload --port 8001
   ```
   
   **Terminal 3:**
   ```powershell
   .\venv\Scripts\Activate
   uvicorn retrieval_service:app --reload --port 8002
   ```

4. **Test the pipeline:**
   - Use `sample_client.py` to upload a PDF, vectorize its content, upsert to Pinecone, and query for similar documents.
   ```powershell
   python sample_client.py
   ```

## Interacting via Browser

Each FastAPI service provides an interactive API documentation (Swagger UI) in your browser:

- After starting a service, open your browser and go to:
  - [http://localhost:8000/docs](http://localhost:8000/docs) for PDF ingestion
  - [http://localhost:8001/docs](http://localhost:8001/docs) for vectorization
  - [http://localhost:8002/docs](http://localhost:8002/docs) for Pinecone retrieval

You can use these pages to test endpoints, upload files, and view request/response formats without writing any client code.

## File Descriptions

- **data_ingestion.py**: PDF parsing logic (text, images, tables).
- **vectorization.py**: Embedding generation via Hugging Face API.
- **retrieval.py**: Pinecone upsert/query logic.
- **data_ingestion_service.py**: FastAPI endpoint `/ingest_pdf/` for PDF upload and extraction.
- **vectorization_service.py**: FastAPI endpoint `/vectorize/` for embedding generation.
- **retrieval_service.py**: FastAPI endpoints `/upsert/` and `/query/` for Pinecone operations.
- **sample_client.py**: Example client for end-to-end workflow.

## Notes
- Make sure to update the Hugging Face model endpoint in `vectorization.py`.
- The PDF extraction logic is a placeholder; you may need to enhance it for images/tables.
- Ensure Pinecone index and environment are correctly set in `.env`.
