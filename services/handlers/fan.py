from .base import BaseCommandHandler


class FanSpeedHandler(BaseCommandHandler):
    def execute(self, payload: dict) -> dict:
        level = payload.get("value")
        return self.manager.set_fan_speed(level)
