from agents.base_agent import BaseAgent
from utils.gemini import generate_text

class SocialAgent(BaseAgent):
    def handle(self, input_data):
        prompt = f"""
        Based on the following marketing copy, generate 3 short social media posts (Twitter + LinkedIn style) that are catchy and likely to go viral. Keep them punchy and engaging:

        {input_data}
        """
        social_posts = generate_text(prompt)
        self.respond(social_posts)
        return social_posts
