"""
LLM model module for text generation using Flan-T5.
"""
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from typing import List, Optional


class LLMModel:
    """
    Text generation model using Flan-T5 for answering questions.
    """
    
    # Maximum input length for tokenization
    MAX_INPUT_LENGTH = 512
    
    def __init__(self, model_name: str = "google/flan-t5-small"):
        """
        Initialize the LLM with a Flan-T5 model.
        
        Args:
            model_name: Name of the Flan-T5 model to use.
                       Default is 'google/flan-t5-small' (lightweight).
        """
        self.model_name = model_name
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
        print(f"Loading model {model_name} on {self.device}...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.model.to(self.device)
        self.model.eval()
        print(f"Model loaded successfully!")
        
    def generate(
        self, 
        prompt: str, 
        max_length: int = 256,
        num_beams: int = 4,
        **kwargs
    ) -> str:
        """
        Generate text based on a prompt.
        
        Args:
            prompt: Input prompt for text generation.
            max_length: Maximum length of generated text (default: 256).
            num_beams: Number of beams for beam search (default: 4).
            **kwargs: Additional generation parameters.
            
        Returns:
            Generated text string.
        """
        # Tokenize input
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True, max_length=self.MAX_INPUT_LENGTH)
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        
        # Generate
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_length=max_length,
                num_beams=num_beams,
                early_stopping=True,
                **kwargs
            )
        
        # Decode
        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return generated_text
    
    def answer_question(
        self, 
        question: str, 
        context: Optional[str] = None,
        max_length: int = 256
    ) -> str:
        """
        Answer a question, optionally with context.
        
        Args:
            question: The question to answer.
            context: Optional context information to use for answering.
            max_length: Maximum length of the answer (default: 256).
            
        Returns:
            Generated answer string.
        """
        if context:
            # Format prompt with context
            prompt = f"Answer the following question based on the context provided.\n\nContext: {context}\n\nQuestion: {question}\n\nAnswer:"
        else:
            # Direct question
            prompt = f"Question: {question}\n\nAnswer:"
        
        answer = self.generate(prompt, max_length=max_length)
        return answer
