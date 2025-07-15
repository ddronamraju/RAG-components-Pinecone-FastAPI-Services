"""
Module: vectorization.py
Description: Handles vectorization of content using Hugging Face API endpoints.
"""
import os
import requests
from typing import List, Any

HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')

# Updated Hugging Face embedding endpoint to a free public model
EMBEDDING_ENDPOINT = 'https://y1ygf4rn4t2jorrs.us-east-1.aws.endpoints.huggingface.cloud'

def get_embeddings(texts: List[str], batch_size: int = 8) -> List[Any]:
    """
    Sends a list of texts to the Hugging Face API and returns their embeddings.
    Handles batching and error handling.
    """
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    embeddings = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i+batch_size]
        print(f"[DEBUG] Sending batch to Hugging Face: {batch}")
        try:
            response = requests.post(
                EMBEDDING_ENDPOINT,
                headers=headers,
                json={"inputs": batch},  # always send a list
                timeout=30
            )
            print(f"[DEBUG] Hugging Face API status: {response.status_code}")
            print(f"[DEBUG] Hugging Face API raw response: {response.text}")
            print(f"[DEBUG] Request headers: {response.request.headers}")
            print(f"[DEBUG] Request body: {response.request.body}")
            response.raise_for_status()
            data = response.json()
            print(f"[DEBUG] Parsed response JSON: {data}")
            # Hugging Face returns a list of embeddings
            if isinstance(data, list):
                for item in data:
                    embeddings.append(item)
            else:
                print(f"[DEBUG] Unexpected response format: {data}")
                embeddings.extend([None] * len(batch))
        except Exception as e:
            print(f"Error in Hugging Face API call: {e}")
            if 'response' in locals():
                print(f"[DEBUG] Error response content: {response.text}")
            embeddings.extend([None] * len(batch))
    return embeddings
