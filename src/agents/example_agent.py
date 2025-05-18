class ExampleAgent:
    def __init__(self):
        self.responses = {
            "hello": "Hi there! How can I assist you today?",
            "bye": "Goodbye! Have a great day!",
            "default": "I'm sorry, I didn't understand that."
        }

    def process_input(self, user_input):
        user_input = user_input.lower()
        return self.generate_response(user_input)

    def generate_response(self, user_input):
        return self.responses.get(user_input, self.responses["default"])


def process_input(input_data):
    if not input_data:
        return "No input provided."
    if "<script>" in input_data:
        return "Input contains unsafe characters."
    return f"Processing input: {input_data}"

def generate_response(input_data):
    if input_data == "What is your name?":
        return "I am an AI agent."
    elif input_data == "How are you?":
        return "I am functioning as expected."
    else:
        return "I'm not programmed for jokes."