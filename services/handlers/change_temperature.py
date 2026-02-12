from .base import BaseCommandHandler


class ChangeTemperatureHandler(BaseCommandHandler):
    def execute(self, payload: dict) -> dict:
        delta = payload.get("delta")
        return self.manager.change_temperature(delta)
