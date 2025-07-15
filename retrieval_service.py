"""
FastAPI service for Pinecone retrieval and upsert.
"""
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Any, Dict
from retrieval import upsert_vectors, query_vector

app = FastAPI()

class UpsertRequest(BaseModel):
    ids: List[str]
    vectors: List[Any]
    metadata: List[Dict] = None

class QueryRequest(BaseModel):
    vector: Any
    top_k: int = 5

@app.post("/upsert/")
def upsert(request: UpsertRequest):
    upsert_vectors(request.ids, request.vectors, request.metadata)
    return {"status": "upserted"}

@app.post("/query/")
def query(request: QueryRequest):
    return query_vector(request.vector, request.top_k)
