from transformers import pipeline
from typing import Literal
import spacy

class Summarizer:
    def __init__(self, model_name: str = "facebook/bart-large-cnn"):
        self.model = pipeline("summarization", model=model_name)
        self.nlp = spacy.load("en_core_web_sm")

    def _preprocess(self, text: str) -> str:
        """Очистка текста и удаление HTML-тегов"""
        doc = self.nlp(text)
        return " ".join([sent.text for sent in doc.sents])

    def abstractive_summarize(self, 
                            text: str,
                            max_length: int = 150,
                            temperature: float = 1.0) -> str:
        cleaned_text = self._preprocess(text)
        result = self.model(
            cleaned_text,
            max_length=max_length,
            temperature=temperature,
            do_sample=True
        )
        return result[0]['summary_text']

    def extractive_summarize(self,
                           text: str,
                           ratio: float = 0.2) -> str:
        cleaned_text = self._preprocess(text)
        doc = self.nlp(cleaned_text)
        sentences = [sent.text for sent in doc.sents]
        n_sentences = max(1, int(len(sentences) * ratio))
        return " ".join(sentences[:n_sentences])