import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key="your api key")

model = genai.GenerativeModel("gemini-2.0-flash")

def generate_text(prompt):
    response = model.generate_content(prompt)
    return response.text
