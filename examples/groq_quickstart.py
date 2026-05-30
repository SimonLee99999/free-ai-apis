"""
Groq — Free tier quickstart (OpenAI-compatible, 300+ tokens/sec)
Get your free API key at: https://console.groq.com
No credit card required.
"""
from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="YOUR_GROQ_API_KEY",
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a haiku about programming"},
    ],
    temperature=0.7,
    max_tokens=200,
)

print(response.choices[0].message.content)
print(f"\nTokens used: {response.usage.total_tokens}")
