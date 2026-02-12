from typing import Dict

from nlp.preprocessor import TextPreprocessor
from nlp.intent_detector_kw import IntentDetectorKeyword
from nlp.entity_extractor import EntityExtractor

class CommandInterpreter:
    """
    High-level NLP entry point.

    Converts raw user text into structured intent JSON.
    """

    def __init__(self):
        self.preprocessor = TextPreprocessor()
        self.intent_detector = IntentDetectorKeyword()
        self.entity_extractor = EntityExtractor()


    # -----------------------------------
    # public API
    # -----------------------------------
    def interpret(self, raw_text: str) -> Dict:
        """
        Main method to convert user input → intent JSON.
        """

        cleaned_text = self.preprocessor.process(raw_text)

        intent = self.intent_detector.detect(cleaned_text)
        if not intent:
            return {
                "status": "rejected",
                "reason": "unknown_intent",
                "text": cleaned_text,
            }

        entities = self.entity_extractor.extract(intent, cleaned_text)

        command = {
            "intent": intent,
            **entities,
        }

        return command
    