from domain.state_manager import ACState
from domain.state_manager import ACConstraints
from domain.state_manager import ACStateManager
from services.command_router import CommandRouter
from nlp.interpreter import CommandInterpreter

state = ACState()
constraints = ACConstraints()

manager = ACStateManager(state, constraints)
router = CommandRouter(manager)    
interpreter = CommandInterpreter()

print("\nAC Assistant Started...")
print("Type 'exit' to quit.\n")
def main():
    while True:
        user_input = input("Input Your Command : ")
        if user_input.lower() in ("exit", "quit"):
            print("Bye.")
            break

        # NLP
        command = interpreter.interpret(user_input)
        print("Intent:", command)

        # if rejected by interpreter
        if command.get("status") == "rejected":
            print("System:", command)
            continue

        # Execute
        result = router.route(command)
        print("Execution:", result)

        # Show updated state
        print("State:", manager.snapshot())
        print("-" * 50)



if __name__ == "__main__":
    main()