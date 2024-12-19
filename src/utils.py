# src/utils.py
import os
import nltk
from nltk.tokenize import sent_tokenize

def ensure_nltk_downloads():
    """Ensure required NLTK data is downloaded"""
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')

def load_text_file(file_path):
    """Load text from file"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def split_into_sentences(text):
    """Split text into sentences"""
    return [s.strip() for s in sent_tokenize(text) if s.strip()]