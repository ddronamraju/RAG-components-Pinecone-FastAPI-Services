"""
FastAPI service for PDF data ingestion.
"""
from fastapi import FastAPI, UploadFile, File
from typing import Dict, Any
import shutil
import os
from data_ingestion import extract_pdf_content

app = FastAPI()

@app.post("/ingest_pdf/")
def ingest_pdf(file: UploadFile = File(...)) -> Dict[str, Any]:
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    content = extract_pdf_content(temp_path)
    os.remove(temp_path)
    return content
