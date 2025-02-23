import re
import html
from typing import List

def clean_text(text: str) -> str:
    """Комплексная очистка текста"""
    # Удаление HTML-тегов
    text = re.sub(r'<[^>]+>', ' ', text)
    
    # Декодирование HTML-сущностей
    text = html.unescape(text)
    
    # Удаление специальных символов
    text = re.sub(r'[^\w\s.,!?\-:;\'"()]', ' ', text)
    
    # Нормализация пробелов
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def split_paragraphs(text: str, min_sentence_length: int = 50) -> List[str]:
    """Разделение текста на осмысленные предложения"""
    sentences = []
    current_sentence = []
    
    for word in text.split():
        current_sentence.append(word)
        if len(current_sentence) > min_sentence_length and word.endswith(('.', '!', '?')):
            sentences.append(' '.join(current_sentence))
            current_sentence = []
    
    if current_sentence:
        sentences.append(' '.join(current_sentence))
    
    return sentences