from services.command_router import CommandRouter
from domain.state_manager import ACStateManager
from domain.state_manager import ACState
from domain.state_manager import ACConstraints

state = ACState()
constraints = ACConstraints()

manager = ACStateManager(state, constraints)

router = CommandRouter(manager)    

command_output = router.route({
    "intent": "power",
    "state": "on"
})
print(command_output)

command_output = router.route({
    "intent": "change_temperature",
    "delta": -1
})
print(command_output)

command_output = router.route({
    "intent": "turbo",
    "state": "on"
})
print(command_output)

command_output = router.route({
    "intent": "turbo",
    "state": "on"
})
print(command_output)

command_output = router.route({
    "intent": "power",
    "state": "off"
})
print(command_output)

command_output = router.route({
    "intent": "change_temperature",
    "delta": -1
})
print(command_output)
