from abc import ABC, abstractmethod
from domain.state_manager import ACStateManager

class BaseCommandHandler(ABC):

    def __init__(self, manager:ACStateManager):
        self.manager = manager

    @abstractmethod
    def execute(self, payload:dict) -> dict:
        pass 