"""
LiteLLM — Switch between any provider with one line change
Install: pip install litellm
"""
from litellm import completion

messages = [{"role": "user", "content": "Explain APIs in one sentence"}]

# Uncomment the provider you want to use:

# Google Gemini (free, no CC)
response = completion(model="gemini/gemini-2.0-flash", messages=messages)

# Groq (free, no CC)
# response = completion(model="groq/llama-3.3-70b-versatile", messages=messages)

# Mistral (free, no CC)
# response = completion(model="mistral/mistral-large-latest", messages=messages)

# Ollama (local, completely free)
# response = completion(model="ollama/llama3.2", messages=messages, api_base="http://localhost:11434")

# OpenAI (paid, $5 free credits)
# response = completion(model="gpt-4o-mini", messages=messages)

print(response.choices[0].message.content)
