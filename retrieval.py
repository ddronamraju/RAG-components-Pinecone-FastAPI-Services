"""
Module: retrieval.py
Description: Handles Pinecone vector DB operations for upsert and retrieval.
"""
import os
import pinecone
from typing import List, Any

PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINECONE_ENV = os.getenv('PINECONE_ENV')
PINECONE_INDEX = os.getenv('PINECONE_INDEX')

# Initialize Pinecone
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
index = pinecone.Index(PINECONE_INDEX)

def upsert_vectors(ids: List[str], vectors: List[Any], metadata: List[dict] = None):
    """
    Upserts vectors into Pinecone index.
    """
    # TODO: Add batching and error handling
    items = list(zip(ids, vectors, metadata or [{}]*len(ids)))
    index.upsert(items)

def query_vector(vector: Any, top_k: int = 5):
    """
    Queries Pinecone index for similar vectors.
    """
    return index.query(vector=vector, top_k=top_k, include_metadata=True)
