 import string
from collections import Counter

def clean_text(text: str) -> str:
    """Удаляет пунктуацию и приводит к нижнему регистру."""
    translator = str.maketrans('', '', string.punctuation)
    return text.lower().translate(translator)

def get_word_frequency(text: str) -> dict:
    """Возвращает частотность слов."""
    words = clean_text(text).split()
    return dict(Counter(words).most_common(10))

def count_sentences(text: str) -> int:
    """Примерный подсчёт предложений по знакам .!?"""
    return sum(1 for ch in text if ch in '.!?')
