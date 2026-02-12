from typing import Optional, Dict, List

class IntentDetectorKeyword:
    """
    Detects which intent the user wants to trigger.
    Works on preprocessed text.
    """

    def __init__(self):
        # intent -> keywords/phrases
        self.intent_keywords: Dict[str, List[str]] = {
            "power": [
                "turn on",
                "turn off",
                "switch on",
                "switch off",
                "power on",
                "power off",
                "start",
                "stop",
            ],
            "set_temperature": [
                "set temperature",
                "make temperature",
            ],
            "change_temperature": [
                "increase temperature",
                "decrease temperature",
                "make it cooler",
                "make it warmer",
                "cooler",
                "warmer",
                "increase",
                "decrease",
            ],
            "set_fan_speed": [
                "fan speed",
                "set fan",
            ],
            "vertical_swing": [
                "vertical swing",
            ],
            "horizontal_swing": [
                "horizontal swing",
            ],
            "turbo": [
                "turbo",
            ],
            "timer_on": [
                "timer on",
                "turn on after",
            ],
            "timer_off": [
                "timer off",
                "turn off after",
            ],
            "get_room_temperature": [
                "room temperature",
                "current temperature",
            ],
            "get_aqi": [
                "aqi",
                "air quality",
            ],
        }

    # -----------------------------------
    # public API
    # -----------------------------------
    def detect(self, text: str) -> Optional[str]:
        """
        Returns detected intent or None.
        """
        for intent, keywords in self.intent_keywords.items():
            for phrase in keywords:
                if phrase in text:
                    return intent

        return None
