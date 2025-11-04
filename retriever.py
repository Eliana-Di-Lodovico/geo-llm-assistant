"""
Retriever module for finding relevant documents based on semantic similarity.
"""
import numpy as np
from typing import List, Dict, Tuple, Any, Optional
from embedder import Embedder


class Retriever:
    """
    Retrieval system for finding relevant documents using semantic similarity.
    """
    
    def __init__(self, embedder: Embedder):
        """
        Initialize the retriever with an embedder.
        
        Args:
            embedder: An Embedder instance for creating embeddings.
        """
        self.embedder = embedder
        self.documents: List[str] = []
        self.document_embeddings: Optional[np.ndarray] = None
        
    def add_documents(self, documents: List[str]):
        """
        Add documents to the retrieval system and compute their embeddings.
        
        Args:
            documents: List of text documents to add to the retrieval system.
        """
        self.documents.extend(documents)
        new_embeddings = self.embedder.embed(documents)
        
        if self.document_embeddings is None:
            self.document_embeddings = new_embeddings
        else:
            self.document_embeddings = np.vstack([self.document_embeddings, new_embeddings])
    
    def retrieve(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """
        Retrieve the most relevant documents for a given query.
        
        Args:
            query: The search query text.
            top_k: Number of top documents to retrieve (default: 3).
            
        Returns:
            List of dictionaries containing 'text', 'score', and 'index' for each result.
        """
        if not self.documents:
            return []
        
        # Embed the query
        query_embedding = self.embedder.embed(query)
        
        # Calculate cosine similarity
        similarities = self._cosine_similarity(query_embedding, self.document_embeddings)
        
        # Get top-k indices
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        # Build results
        results = []
        for idx in top_indices:
            results.append({
                'text': self.documents[idx],
                'score': float(similarities[idx]),
                'index': int(idx)
            })
        
        return results
    
    # Normalization epsilon for numerical stability
    EPSILON = 1e-10
    
    def _cosine_similarity(self, vec1: np.ndarray, vec2: np.ndarray) -> np.ndarray:
        """
        Calculate cosine similarity between vectors.
        
        Args:
            vec1: First vector or matrix (query embedding).
            vec2: Second vector or matrix (document embeddings).
            
        Returns:
            Array of similarity scores.
        """
        # Normalize vectors
        vec1_norm = vec1 / (np.linalg.norm(vec1, axis=-1, keepdims=True) + self.EPSILON)
        vec2_norm = vec2 / (np.linalg.norm(vec2, axis=-1, keepdims=True) + self.EPSILON)
        
        # Calculate dot product
        if vec1_norm.ndim == 1:
            vec1_norm = vec1_norm.reshape(1, -1)
        
        similarities = np.dot(vec1_norm, vec2_norm.T).flatten()
        return similarities
    
    def get_all_documents(self) -> List[str]:
        """
        Get all documents in the retrieval system.
        
        Returns:
            List of all document texts.
        """
        return self.documents
    
    def clear(self):
        """
        Clear all documents and embeddings from the retrieval system.
        """
        self.documents = []
        self.document_embeddings = None
