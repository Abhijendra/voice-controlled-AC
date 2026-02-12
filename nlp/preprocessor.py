import re
from typing import Dict


class TextPreprocessor:
    """
    Cleans raw user input so that downstream 
    NLP components can work with predictable text.
    """

    def __init__(self):
        # initiate a set using curly braces {} for non-empty sets 
        self.stop_words = {
            "please",
            "pls",
            "plz",
            "kindly",
            "hey",
            "hi",
        }
        
        # replacements / expansions
        self.replacements: Dict[str, str] = {
            "temp": "temperature",
            "ac": "air conditioner",
            "fan speed": "fan",
            "incr": "increase",
            "decr": "decrease"
        }

    def process(self, text:str) -> str: 
        text = self._to_lower(text)
        text = self._remove_punctuation(text)
        text = self._normalize_spaces(text)
        text = self._apply_replacements(text)
        text = self._remove_stopwords(text)
        text = self._normalize_spaces(text)
        return text.strip()
    
    def _to_lower(self, text:str) -> str:
        return text.lower()
    
    def _remove_punctuation(self, text:str) -> str:
        return re.sub(r"[^\w\s]", " ", text)

    def _normalize_spaces(self, text: str) -> str:
        return re.sub(r"\s+", " ", text)

    def _apply_replacements(self, text: str) -> str:        
        words = text.split()
        replaced = [self.replacements.get(w, w) for w in words]
        return " ".join(replaced)
    
    def _remove_stopwords(self, text:str) -> str:
        words = text.split()
        filtered = [w for w in words if w not in self.stop_words]
        return " ".join(filtered)