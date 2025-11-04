"""
Embedder module for converting text to vector embeddings using sentence-transformers.
"""
from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List, Union


class Embedder:
    """
    Text embedder using sentence-transformers for creating vector representations.
    """
    
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initialize the embedder with a sentence-transformer model.
        
        Args:
            model_name: Name of the sentence-transformer model to use.
                       Default is 'all-MiniLM-L6-v2' (lightweight and fast).
        """
        self.model_name = model_name
        self.model = SentenceTransformer(model_name)
        
    def embed(self, texts: Union[str, List[str]]) -> np.ndarray:
        """
        Convert text(s) to embeddings.
        
        Args:
            texts: Single text string or list of text strings to embed.
            
        Returns:
            Numpy array of embeddings. Shape: (n_texts, embedding_dim)
        """
        if isinstance(texts, str):
            texts = [texts]
        
        embeddings = self.model.encode(texts, convert_to_numpy=True)
        return embeddings
    
    def get_embedding_dimension(self) -> int:
        """
        Get the dimensionality of the embeddings.
        
        Returns:
            Integer representing the embedding dimension.
        """
        return self.model.get_sentence_embedding_dimension()
