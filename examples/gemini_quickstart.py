"""
Google Gemini 2.0 Flash — Free tier quickstart
Get your free API key at: https://aistudio.google.com
No credit card required.
"""
import google.generativeai as genai

API_KEY = "YOUR_GEMINI_API_KEY"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

# Simple text generation
response = model.generate_content("Explain what an API is in simple terms")
print(response.text)

# Multi-turn conversation
chat = model.start_chat()
r1 = chat.send_message("What is machine learning?")
print(r1.text)
r2 = chat.send_message("Give me a Python example")
print(r2.text)
