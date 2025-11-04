"""
Main GeoResearch Assistant module combining retrieval and generation.
"""
from typing import List, Dict, Optional, Any
from embedder import Embedder
from retriever import Retriever
from llm_model import LLMModel


class GeoAssistant:
    """
    Geography and Climate Research Assistant using RAG (Retrieval-Augmented Generation).
    """
    
    def __init__(
        self, 
        embedder_model: str = "all-MiniLM-L6-v2",
        llm_model: str = "google/flan-t5-small"
    ):
        """
        Initialize the GeoResearch Assistant.
        
        Args:
            embedder_model: Name of the sentence-transformer model for embeddings.
            llm_model: Name of the Flan-T5 model for text generation.
        """
        print("Initializing GeoResearch Assistant...")
        self.embedder = Embedder(model_name=embedder_model)
        self.retriever = Retriever(embedder=self.embedder)
        self.llm = LLMModel(model_name=llm_model)
        print("GeoResearch Assistant initialized successfully!")
        
    def load_knowledge_base(self, documents: List[str]):
        """
        Load geographic and climate knowledge into the assistant.
        
        Args:
            documents: List of text documents containing geographic/climate information.
        """
        print(f"Loading {len(documents)} documents into knowledge base...")
        self.retriever.add_documents(documents)
        print("Knowledge base loaded successfully!")
        
    def ask(
        self, 
        question: str, 
        top_k: int = 3,
        max_answer_length: int = 256,
        return_context: bool = False
    ) -> Dict[str, Any]:
        """
        Ask a question about geography or climate.
        
        Args:
            question: The question to ask.
            top_k: Number of relevant documents to retrieve (default: 3).
            max_answer_length: Maximum length of the generated answer (default: 256).
            return_context: Whether to return retrieved context in the result (default: False).
            
        Returns:
            Dictionary containing 'question', 'answer', and optionally 'context' and 'retrieved_docs'.
        """
        # Retrieve relevant documents
        retrieved_docs = self.retriever.retrieve(question, top_k=top_k)
        
        # Combine retrieved documents as context
        if retrieved_docs:
            context = "\n\n".join([doc['text'] for doc in retrieved_docs])
        else:
            context = None
        
        # Generate answer
        answer = self.llm.answer_question(
            question=question,
            context=context,
            max_length=max_answer_length
        )
        
        # Build result
        result = {
            'question': question,
            'answer': answer
        }
        
        if return_context:
            result['context'] = context
            result['retrieved_docs'] = retrieved_docs
        
        return result
    
    def get_knowledge_base_info(self) -> Dict[str, Any]:
        """
        Get information about the loaded knowledge base.
        
        Returns:
            Dictionary with knowledge base statistics.
        """
        docs = self.retriever.get_all_documents()
        return {
            'num_documents': len(docs),
            'embedding_dimension': self.embedder.get_embedding_dimension()
        }
