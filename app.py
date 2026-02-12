from services.command_router import CommandRouter
from domain.state_manager import ACStateManager
from domain.state_manager import ACState
from domain.state_manager import ACConstraints

from nlp.interpreter import CommandInterpreter

interpreter = CommandInterpreter()
intent_json = interpreter.interpret("switch on the AC please")

state = ACState()
constraints = ACConstraints()

manager = ACStateManager(state, constraints)

router = CommandRouter(manager)    

command_output = router.route(intent_json)
print(command_output)

# command_output = router.route({
#     "intent": "power",
#     "state": "on"
# })

# command_output = router.route({
#     "intent": "change_temperature",
#     "delta": -1
# })
# print(command_output)

# command_output = router.route({
#     "intent": "turbo",
#     "state": "on"
# })
# print(command_output)

# command_output = router.route({
#     "intent": "turbo",
#     "state": "on"
# })
# print(command_output)

# command_output = router.route({
#     "intent": "power",
#     "state": "off"
# })
# print(command_output)

# command_output = router.route({
#     "intent": "change_temperature",
#     "delta": -1
# })
# print(command_output)