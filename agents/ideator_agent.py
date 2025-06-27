from agents.base_agent import BaseAgent  
from utils.gemini import generate_text

class IdeatorAgent(BaseAgent):
    def handle(self, input_data):
        prompt = f"Brainstorm a unique startup idea that solves this problem: {input_data}"
        idea = generate_text(prompt)
        self.respond(idea)
        return idea