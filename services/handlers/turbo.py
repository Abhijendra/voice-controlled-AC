from .base import BaseCommandHandler


class TurboHandler(BaseCommandHandler):
    def execute(self, payload: dict) -> dict:
        state = payload.get("state")
        return self.manager.set_turbo(state)
