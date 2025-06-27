from agents.base_agent import BaseAgent
from utils.gemini import generate_text

class MarketingAgent(BaseAgent):
    def handle(self, input_data):
        prompt = f"""
        Based on the following PRD, create a brand name, tagline, and a short paragraph of marketing copy to describe the product to new users:

        {input_data}
        """
        marketing_material = generate_text(prompt)
        self.respond(marketing_material)
        return marketing_material
