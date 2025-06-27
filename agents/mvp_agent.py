from agents.base_agent import BaseAgent
from utils.gemini import generate_text

class MVPAgent(BaseAgent):
    def handle(self, input_data):
        prompt = f"Based on this PRD, generate an MVP implementation plan with technical stack recommendations: {input_data}"
        mvp_plan = generate_text(prompt)
        self.respond(mvp_plan)
        return mvp_plan
