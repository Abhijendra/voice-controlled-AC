from dataclasses import dataclass
from typing import Optional

# ==============================
# Data Layer
# ==============================

@dataclass
class ACState:
    power: str = "off"                     # on/off
    temperature_set: int = 24
    mode: str = "cool"
    fan_speed: str = "auto"                # 1,2,3,auto
    vertical_swing: str = "off"
    horizontal_swing: str = "off"
    turbo: str = "off"
    lamp_display: str = "on"
    timer_on_hours: Optional[float] = None
    timer_off_hours: Optional[float] = None 

    # read-only / sensor type
    room_temperature: Optional[int] = None
    aqi: Optional[int] = None 

if __name__ == "__main__":

    state = ACState()
    print(state.power)