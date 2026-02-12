from domain.ac_state import ACState
from domain.ac_constraints import ACConstraints


class ACStateManager:

    def __init__(self, state:ACState, constraints:ACConstraints):
        self._state = state
        self._constraints = constraints

    def _is_ac_off(self):
        if self._state.power == "off":
            return True
        return False

    def snapshot(self):
        return self._state
    
    def set_power(self, value:str):
        if value not in ("off", "on"):
            raise ValueError("Invalid power state")
        
        if self._state.power == value:
            return {"status":"no_change", "reason": "already_in_state"}
        
        self._state.power = value
    
        if value == "off":
            self._state.turbo = "off"

        return {"status": "success", "message": f"ac turned {value}"}
    
    def set_temperature(self, value):
        if self._is_ac_off():
            return {"status": "blocked", "reason": "ac_off"}
        
        if not (self._constraints.min_temp < value and self._constraints.max_temp > value):
            return {"status": "rejected",
                    "reason": "out_of_range",
                    "allowed": [self._constraints.min_temp, self._constraints.max_temp]
                    }
        
        self._state.temperature_set = value
        return {"status": "success", "message": f"temperature set to {value}"}
    
    def change_temperature(self, delta:int):
        changed_temp = self._state.temperature_set + delta 
        return self.set_temperature(changed_temp)

    def set_fan_speed(self, level:str):
        if self._is_ac_off():
            return {"status": "blocked", "reason": "ac_off"}
        if level not in self._constraints.fan_levels:
            return {"status": "rejected", "reason": "invalid_fan_speed"}

        self._state.fan_speed = level
        return {"status": "success", "message": f"fan speed set to {level}"}
    
    def set_vertical_swing(self, state:str):
        if self._is_ac_off():
            return {"status": "blocked", "reason": "ac_off"}
        if state not in ("on", "off"):
            raise ValueError("Invalid vertical swing state")
        self._state.vertical_swing = state
        return {"status": "success", "message": f"vertical swing set to {state}"}

    def set_horizontal_swing(self, state: str):
        if self._is_ac_off():
            return {"status": "blocked", "reason": "ac_off"}    
        if state not in ("on", "off"):
            raise ValueError("Invalid horizontal swing state")
        self._state.horizontal_swing = state
        return {"status": "success", "message": f"horizontal swing set to {state}"}

    def set_turbo(self, state:str):
        if self._is_ac_off():
            return {"status": "blocked", "reason": "ac_off"}
                
        if state not in ("on", "off"):
            raise ValueError("Invalid horizontal swing state")
        
        self._state.turbo = state
        return {"status": "success", "message": f"turbo set to {state}"}
    
    def set_timer_off(self, hours: float):
        if self._is_ac_off():
            return {"status": "blocked", "reason": "ac_off"}        
        self._state.timer_off_hours = hours
        return {"status": "success", "message": f"off timer set for {hours} hours"}
    
    def set_timer_on(self, hours: float):
        if self._is_ac_off():
            return {"status": "blocked", "reason": "ac_off"}        
        self._state.timer_on_hours = hours
        return {"status": "success", "message": f"on timer set for {hours} hours"}
    
# state = ACState()
# constraints = ACConstraints()
# manager = ACStateManager(state, constraints)

# print(manager.set_power("on"))
# print(manager.change_temperature(-1))
# print(manager.set_turbo("on"))

# print(manager.snapshot())
    
        

        

        

