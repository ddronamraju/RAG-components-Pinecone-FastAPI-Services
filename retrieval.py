"""
Module: retrieval.py
Description: Handles Pinecone vector DB operations for upsert and retrieval.
"""
import os
import pinecone
from typing import List, Any
import json
from dotenv import load_dotenv
load_dotenv()

PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINECONE_ENV = os.getenv('PINECONE_ENV')
PINECONE_INDEX = os.getenv('PINECONE_INDEX')

# Initialize Pinecone (new API)
pc = pinecone.Pinecone(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
index = pc.Index(PINECONE_INDEX)

def upsert_vectors(ids: List[str], vectors: List[Any], metadata: List[dict] = None, batch_size: int = 100):
    """
    Upserts vectors into Pinecone index with batching and error handling.
    """
    if metadata is None:
        metadata = [{}] * len(ids)
    items = list(zip(ids, vectors, metadata))
    for i in range(0, len(items), batch_size):
        batch = items[i:i+batch_size]
        try:
            index.upsert(batch)
        except Exception as e:
            print(f"Error upserting batch to Pinecone: {e}")

def query_vector(vector: Any, top_k: int = 5):
    PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
    PINECONE_ENV = os.getenv('PINECONE_ENV')
    PINECONE_INDEX = os.getenv('PINECONE_INDEX')
    """
    Queries Pinecone index for similar vectors with error handling.
    """
    try:
        print("top_k valuesis:",top_k)
        print("Vector type:", type(vector))
        print("Vector length:", len(vector) if hasattr(vector, '__len__') else 'N/A')
        print("First 5 values:", vector[:5] if hasattr(vector, '__getitem__') else 'N/A')
        print("Querying Pinecone...")
        result = index.query(vector=vector, top_k=top_k, include_metadata=True, api_key = "pcsk_3FieSz_JW27jdpcs1MeUfvyigvLxMtSRccuNpCGMQd49jBhB8Y23BCk3qAr7sKMaokzdJY")
        print("Query result (pretty):", json.dumps(result, indent=2, default=str))
        return result.to_dict() if hasattr(result, 'to_dict') else result
    except Exception as e:
        print(f"Error querying Pinecone: {e}")
        return None
