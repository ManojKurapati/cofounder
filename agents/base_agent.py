class BaseAgent:
    def __init__(self, name):
        self.name = name

    def handle(self, input_data):
        raise NotImplementedError

    def respond(self, output_data):
        print(f"[{self.name}] Output: {output_data}")
