from dataclasses import dataclass

@dataclass(frozen=True)
class ACConstraints:
    min_temp:int = 16
    max_temp:int = 30
    fan_levels: tuple = ("1","2","3","auto")