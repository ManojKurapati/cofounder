from agents.base_agent import BaseAgent
from utils.gemini import generate_text

class PRDAgent(BaseAgent):
    def handle(self, input_data):
        prompt = f"Convert the following startup idea into a detailed product requirements document (PRD): {input_data}"
        prd = generate_text(prompt)
        self.respond(prd)
        return prd
