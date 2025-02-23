from transformers import pipeline
import spacy
from typing import Optional
import readability
import torch

class Summarizer:
    def __init__(self):
        self.abstractive_model = pipeline(
            "summarization", 
            model="facebook/bart-large-cnn",
            device=0 if torch.cuda.is_available() else -1
        )
        self.nlp = spacy.load("en_core_web_sm")
        
    def preprocess_text(self, text: str) -> str:
        """Clean and normalize input text"""
        doc = self.nlp(text)
        return " ".join([sent.text for sent in doc.sents if len(sent.text.strip()) > 0])
    
    def abstractive_summarize(self, 
                            text: str,
                            max_length: int = 150,
                            temperature: float = 0.7) -> str:
        cleaned_text = self.preprocess_text(text)
        result = self.abstractive_model(
            cleaned_text,
            max_length=max_length,
            temperature=temperature,
            do_sample=True,
            truncation=True
        )
        return result[0]['summary_text']
    
    def extractive_summarize(self,
                           text: str,
                           ratio: float = 0.2) -> str:
        cleaned_text = self.preprocess_text(text)
        doc = self.nlp(cleaned_text)
        sentences = [sent.text for sent in doc.sents]
        n_sentences = max(1, int(len(sentences) * ratio))
        return " ".join(sentences[:n_sentences])
    
    def calculate_readability(self, text: str) -> float:
        """Calculate Flesch Reading Ease Score"""
        results = readability.getmeasures(text, lang='en')
        return results['readability grades']['FleschReadingEase']