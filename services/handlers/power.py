from .base import BaseCommandHandler

class PowerHandler(BaseCommandHandler):

    def execute(self, payload:dict) -> dict:
        state = payload.get("state")
        return self.manager.set_power(state)
    
    