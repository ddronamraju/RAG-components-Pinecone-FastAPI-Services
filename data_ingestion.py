"""
Module: data_ingestion.py
Description: Handles PDF ingestion, extracting text, images, and tables from PDF documents.
"""
import os
from typing import List, Dict, Any
import pdfplumber

def extract_pdf_content(pdf_path: str) -> Dict[str, Any]:
    """
    Extracts text and tables from a PDF file. Ignores images.
    Returns a dictionary with keys: 'text', 'images', 'tables'.
    """
    text = ""
    tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # Extract text
            text += page.extract_text() or ""
            # Extract tables
            page_tables = page.extract_tables()
            for table in page_tables:
                tables.append(table)
    return {
        'text': text,
        'images': [],  # Images ignored
        'tables': tables
    }
