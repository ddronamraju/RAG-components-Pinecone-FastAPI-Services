"""
FastAPI service for vectorization using Hugging Face API.
"""
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Any
from vectorization import get_embeddings

app = FastAPI()

class TextsRequest(BaseModel):
    texts: List[str]

@app.post("/vectorize/")
def vectorize(request: TextsRequest) -> List[Any]:
    return get_embeddings(request.texts)
