import re
from typing import Dict

class EntityExtractor:
    """
    Extract parameters required to execute an intent.
    """
    # -----------------------------------
    # public API
    # -----------------------------------
    def extract(self, intent: str, text: str) -> Dict:
        method_name = f"_extract_{intent}"
        method = getattr(self, method_name, self._default)
        return method(text)

    # -----------------------------------
    # default
    # -----------------------------------
    def _default(self, text: str) -> Dict:
        return {}

    # -----------------------------------
    # power
    # -----------------------------------
    def _extract_power(self, text: str) -> Dict:
        if "on" in text or "start" in text:
            return {"state": "on"}
        if "off" in text or "stop" in text:
            return {"state": "off"}
        return {}    
    
    # -----------------------------------
    # turbo
    # -----------------------------------    
    def _extract_turbo(self, text:str) -> Dict:
        if "on" in text or "start" in text:
            return {"state": "on"}
        if "off" in text or "stop" in text:
            return {"state": "off"}
        return {}    
    
    # -----------------------------------
    # set absolute temperature
    # -----------------------------------
    def _extract_set_temperature(self, text: str) -> Dict:
        match = re.search(r"\d+", text)
        if match:
            return {"value": int(match.group())}
        return {}
    
    # -----------------------------------
    # change temperature
    # -----------------------------------
    def _extract_change_temperature(self, text: str) -> Dict:
        # default step
        delta = 1

        # explicit number
        match = re.search(r"\d+", text)
        if match:
            delta = int(match.group())

        if "decrease" in text or "cooler" in text:
            delta = -delta

        return {"delta": delta}

    # -----------------------------------
    # fan
    # -----------------------------------    
    def _extract_set_fan_speed(self, text: str) -> Dict:
        match = re.search(r"\d+", text)
        if match:
            return {"value": match.group()}

        if "auto" in text:
            return {"value": "auto"}

        return {}

    # -----------------------------------
    # timers
    # -----------------------------------
    def _extract_timer_on(self, text: str) -> Dict:
        match = re.search(r"\d+(\.\d+)?", text)
        if match:
            return {"hours": float(match.group())}
        return {}

    def _extract_timer_off(self, text: str) -> Dict:
        match = re.search(r"\d+(\.\d+)?", text)
        if match:
            return {"hours": float(match.group())}
        return {}

    # -----------------------------------
    # swing
    # -----------------------------------
    def _extract_vertical_swing(self, text: str) -> Dict:
        if "on" in text:
            return {"state": "on"}
        if "off" in text:
            return {"state": "off"}
        return {}

    def _extract_horizontal_swing(self, text: str) -> Dict:
        if "on" in text:
            return {"state": "on"}
        if "off" in text:
            return {"state": "off"}
        return {}        