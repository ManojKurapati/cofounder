# 🤖 CofounderOS — Your AI Startup Co-founder

CofounderOS is a multi-agent AI system that acts like your startup's co-founder. Built using Google's `google-adk`, it automates:
- 💡 Brainstorming ideas
- 📄 Writing product requirement documents (PRDs)
- ⚙️ Planning MVP builds

## 🧠 Powered By:
- Google Agent Development Kit (`google-adk`)
- Python 3.11+
- Modular agent architecture

## 🚀 Architecture

[IdeatorAgent] → [PRDAgent] → [MVPAgent]

shell
Copy
Edit

Each agent performs a dedicated task and passes it downstream.

## 📁 Project Structure

cofounderos_google_adk/
├── agents/
│ ├── ideator.py
│ ├── prd.py
│ └── mvp.py
├── main.py # Starts the agent runtime
└── send_task.py # Sends a problem to Ideator

bash
Copy
Edit

## 🛠️ How to Run

```bash
git clone https://github.com/YOUR_USERNAME/cofounderos_google_adk.git
cd cofounderos_google_adk

# Make sure google-adk is installed
pip install google-adk

# Start the agent runtime
python main.py

# Send your startup problem
python send_task.py