import gradio as gr
from agents.ideator_agent import IdeatorAgent
from agents.prd_agent import PRDAgent
from agents.mvp_agent import MVPAgent
from agents.marketing_agent import MarketingAgent
from agents.social_agent import SocialAgent

idea_agent = IdeatorAgent("Ideator")
prd_agent = PRDAgent("PRD Writer")
mvp_agent = MVPAgent("MVP Builder")
marketing_agent = MarketingAgent("Marketing Genie")
social_agent = SocialAgent("Social Stylist")

def cofounder_pipeline(user_input):
    idea = idea_agent.handle(user_input)
    prd = prd_agent.handle(idea)
    mvp = mvp_agent.handle(prd)
    marketing = marketing_agent.handle(prd)
    social = social_agent.handle(marketing)
    return idea, prd, mvp, marketing, social

iface = gr.Interface(
    fn=cofounder_pipeline,
    inputs=gr.Textbox(lines=2, placeholder="Describe a problem you want to solve..."),
    outputs=[
        gr.Textbox(label="Startup Idea"),
        gr.Textbox(label="Product Requirements Doc (PRD)"),
        gr.Textbox(label="MVP Build Plan"),
        gr.Textbox(label="Marketing Copy"),
        gr.Textbox(label="Social Media Posts"),
    ],
    title="CofounderOS 🧠",
    description="Enter your startup problem and watch AI cofounders generate everything!"
)

if __name__ == "__main__":
    iface.launch()
