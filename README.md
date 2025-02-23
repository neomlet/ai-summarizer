# 🤖 AI Text Summarizer

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Hugging Face](https://img.shields.io/badge/Hugging_Face-Transformers-yellow)](https://huggingface.co/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

NLP-powered tool for automatic text summarization using state-of-the-art transformer models. Supports both **extractive** and **abstractive** summarization approaches.

![Demo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2RlM3hhaDk2c3J6Y2Z5M3l1M3Q5dGJzNnJ6dTZ0dHh1ZXV4NnZieiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LOAq4hYh0hWK4rt6su/giphy.gif)

## ✨ Features

- 📝 Поддержка текстов до 10,000 символов
- ⚡ 2 режима суммаризации:
  - **Extractive** (выделение ключевых предложений)
  - **Abstractive** (генерация нового текста)
- 🌍 Мультиязычная поддержка (EN/RU/ES/DE)
- 📊 Оценка читабельности результата
- 🔌 API endpoint для интеграций

## 🛠️ Tech Stack

**NLP Core**  
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?logo=pytorch)
![Transformers](https://img.shields.io/badge/🤗_Transformers-4.30+-FFD43B)
![Spacy](https://img.shields.io/badge/spaCy-3.6+-09A3D5?logo=spacy)

**Backend**  
![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-009688?logo=fastapi)
![Redis](https://img.shields.io/badge/Redis-7.0+-DC382D?logo=redis)

**Frontend**  
![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-FF4B4B?logo=streamlit)

## 🚀 Quick Start

1. Клонируйте репозиторий
```bash
git clone https://github.com/neomlet/ai-summarizer.git
cd ai-summarizer
```
2. Установите зависимости
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```
3. Запустите сервер
```
uvicorn api.main:app --reload
```
4. Откройте веб-интерфейс
```
streamlit run app/main.py
```
## 📂 Project Structure
```
ai-summarizer/
├── api/               # FastAPI endpoints
├── app/               # Streamlit interface
├── core/              # NLP processing logic
│   ├── models/       # Pre-trained models
│   ├── preprocess.py # Text cleaning
│   └── summarize.py  # Core algorithms
├── tests/            # Unit tests
└── requirements.txt  # Dependencies
```

## 💻 Пример использования
```python
from core.summarize import Summarizer

text = """[Ваш длинный текст здесь]"""

# Инициализация суммаризатора
summarizer = Summarizer(model_name="facebook/bart-large-cnn")

# Abstractive суммаризация
summary = summarizer.abstractive_summarize(
    text, 
    max_length=150,
    temperature=0.7
)

print(f"📄 Результат:\n{summary}")
```
