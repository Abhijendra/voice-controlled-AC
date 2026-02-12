
class IntentBuilder:

    def build_intent_json(self, intent, parameter):
        
        print(f"intent: {intent}")
        print(f"parameter: {parameter}")

        build_json = {"intent": intent, }
        
        print(build_json)
        return build_json
    