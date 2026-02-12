from services.handlers.power import PowerHandler
from services.handlers.set_temperature import SetTemperatureHandler
from services.handlers.change_temperature import ChangeTemperatureHandler
from services.handlers.fan import FanSpeedHandler
from services.handlers.turbo import TurboHandler
from services.handlers.base import BaseCommandHandler
class CommandRouter:

    def __init__(self, manager):
        self.manager = manager
        self._handlers: BaseCommandHandler = self._register_handlers()


    def _register_handlers(self):
        """
        intent -> handler instance
        """
        return {
            "power": PowerHandler(self.manager),
            "set_temperature": SetTemperatureHandler(self.manager),
            "change_temperature": ChangeTemperatureHandler(self.manager),
            "set_fan_speed": FanSpeedHandler(self.manager),
            "turbo": TurboHandler(self.manager),
        }
    
    def route(self, command: dict) -> dict:
        intent = command.get("intent")

        handler:BaseCommandHandler = self._handlers.get(intent)
        if not handler:
            return {"status": "rejected", "reason": "unknown_intent"}

        return handler.execute(command)
