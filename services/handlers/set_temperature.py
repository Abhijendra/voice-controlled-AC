from .base import BaseCommandHandler


class SetTemperatureHandler(BaseCommandHandler):
    def execute(self, payload: dict) -> dict:
        value = payload.get("value")
        return self.manager.set_temperature(value)