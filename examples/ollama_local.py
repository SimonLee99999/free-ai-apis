"""
Ollama — 100% local, completely free, no API key, no rate limits
Install: https://ollama.com
Then run: ollama pull llama3.2

Works with the OpenAI SDK — just point base_url to localhost.
"""
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # required by SDK but not used by Ollama
)

response = client.chat.completions.create(
    model="llama3.2",
    messages=[{"role": "user", "content": "What is the capital of Canada?"}],
)
print(response.choices[0].message.content)

# Streaming example
stream = client.chat.completions.create(
    model="llama3.2",
    messages=[{"role": "user", "content": "Count to 10 slowly"}],
    stream=True,
)
for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)
print()
