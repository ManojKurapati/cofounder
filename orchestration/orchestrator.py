

from agents.ideator_agent import IdeatorAgent
from agents.prd_agent import PRDAgent
from agents.mvp_agent import MVPAgent
from agents.marketing_agent import MarketingAgent
from agents.social_agent import SocialAgent

def main():
    print("👋 Welcome to CofounderOS — Your AI Startup Co-founder\n")
    user_input = input("💡 Enter the problem you'd like to solve: ")

    # Step 1: Idea generation
    idea_agent = IdeatorAgent("Ideator Agent")
    idea = idea_agent.handle(user_input)

    # Step 2: PRD generation
    prd_agent = PRDAgent("PRD Agent")
    prd = prd_agent.handle(idea)

    # Step 3: MVP planning
    mvp_agent = MVPAgent("MVP Agent")
    mvp_plan = mvp_agent.handle(prd)

    # Step 4: Marketing content
    marketing_agent = MarketingAgent("Marketing Agent")
    marketing_material = marketing_agent.handle(prd)

    # Step 5: Social media generation
    social_agent = SocialAgent("Social Media Agent")
    social_posts = social_agent.handle(marketing_material)

    print("\n🚀 All done! Your startup has been ideated, planned, and launched in minutes.")
    print("\n📝 Summary:")
    print("- Startup Idea:\n", idea)
    print("- Product Requirements Document:\n", prd)
    print("- MVP Plan:\n", mvp_plan)
    print("- Marketing Materials:\n", marketing_material)
    print("- Social Media Posts:\n", social_posts)

if __name__ == "__main__":
    main()
