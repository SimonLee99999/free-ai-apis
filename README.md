# free-ai-apis

A list of AI APIs that have a real free tier. No paywalls, no "contact sales". Rate limits are listed so you know what you're working with before you start building.

PRs welcome — limits change often, keeping this accurate is the whole point.

---

## Contents

- [LLMs](#llms)
- [Image Generation](#image-generation)
- [Speech and Audio](#speech-and-audio)
- [Embeddings](#embeddings)
- [Vector Databases](#vector-databases)
- [Multi-modal](#multi-modal)
- [Local / Self-hosted](#local--self-hosted)
- [Free Credits (with expiry)](#free-credits-with-expiry)
- [Examples](#examples)

---

## LLMs

Providers with a permanent free tier (no expiry, no credit card unless noted).

| Provider | Models | Free limit | Context | CC required |
|----------|--------|-----------|---------|-------------|
| [Google AI Studio](https://aistudio.google.com) | Gemini 2.0 Flash, 2.5 Pro | 1,500 req/day, 1M TPM | 1M tokens | No |
| [Groq](https://console.groq.com) | Llama 3.3 70B, Mixtral 8x7B | Rate-limited | 32k tokens | No |
| [Mistral](https://console.mistral.ai) | Mistral Large, Codestral, Pixtral | Rate-limited | 128k tokens | No |
| [Cerebras](https://cloud.cerebras.ai) | Llama 3.3 70B | Rate-limited | 128k tokens | No |
| [Hugging Face](https://huggingface.co/inference-api) | Thousands of open models | Rate-limited, varies by model | Varies | No |
| [OpenRouter](https://openrouter.ai) | 100+ models, many with free tier | Per-model limits | Varies | No |

Notes:
- Groq is genuinely fast — ~300 tokens/sec. Good for prototyping when latency matters.
- Mistral's free plan includes all their models including Codestral. Useful if you need a code-focused model.
- OpenRouter lets you route to whichever free model is least congested. Worth knowing about.

---

## Image Generation

| Provider | Models | Free limit | CC required |
|----------|--------|-----------|-------------|
| [Ideogram](https://ideogram.ai) | Ideogram 2.0 | 10 images/day | No |
| [Stability AI](https://stability.ai) | Stable Diffusion 3 | 25 credits/month | No |
| [Hugging Face](https://huggingface.co/inference-api) | FLUX, SDXL, many others | Rate-limited | No |
| [Fal.ai](https://fal.ai) | FLUX, AnimateDiff | $0.10 free credit | No |

---

## Speech and Audio

| Provider | Capability | Free limit | CC required |
|----------|-----------|-----------|-------------|
| [ElevenLabs](https://elevenlabs.io) | TTS, voice cloning | 10k chars/month | No |
| [Deepgram](https://deepgram.com) | Speech-to-text | $200 credit on signup | No |
| [AssemblyAI](https://assemblyai.com) | STT + speaker detection, summaries | 100 hours free | No |
| [Whisper](https://github.com/openai/whisper) | STT | Unlimited (self-hosted) | No |
| [Kokoro TTS](https://github.com/hexgrad/kokoro) | TTS | Unlimited (self-hosted) | No |

---

## Embeddings

| Provider | Model | Free limit | Dimensions | CC required |
|----------|-------|-----------|-----------|-------------|
| [Google](https://aistudio.google.com) | text-embedding-004 | 1,500 req/day | 768 | No |
| [Cohere](https://cohere.com) | embed-english-v3 | 1M tokens/month | 1024 | No |
| [Jina AI](https://jina.ai) | jina-embeddings-v3 | 1M tokens/month | 1024 | No |
| [Mistral](https://console.mistral.ai) | mistral-embed | Included in free plan | 1024 | No |
| [Hugging Face](https://huggingface.co/inference-api) | BGE, E5, Nomic Embed | Rate-limited | 768–1536 | No |

---

## Vector Databases

| Service | Free tier | Notes |
|---------|-----------|-------|
| [Qdrant Cloud](https://cloud.qdrant.io) | 1GB storage | Can also self-host for free |
| [Pinecone](https://pinecone.io) | 2GB, 1 index | Easiest to set up |
| [Chroma](https://trychroma.com) | Unlimited | Self-hosted only |
| [Weaviate Cloud](https://weaviate.io) | 14-day trial | |

---

## Multi-modal

| Provider | Input types | Free limit | CC required |
|----------|------------|-----------|-------------|
| [Google Gemini 2.0 Flash](https://aistudio.google.com) | Text, image, audio, video | 1,500 req/day | No |
| [Mistral Pixtral](https://console.mistral.ai) | Text, image | Included in free plan | No |

---

## Local / Self-hosted

No API key, no rate limits, no cost. Runs on your machine.

| Tool | Description |
|------|-------------|
| [Ollama](https://ollama.com) | Run Llama, Mistral, Gemma, Phi locally. Easiest setup. |
| [LM Studio](https://lmstudio.ai) | Desktop app for running any GGUF model |
| [vLLM](https://github.com/vllm-project/vllm) | Production-grade inference server |
| [GPT4All](https://gpt4all.io) | Desktop app, privacy-focused |

---

## Free Credits (with expiry)

These expire, so use them first before burning through your actual budget.

| Provider | Amount | Expiry | CC required |
|----------|--------|--------|-------------|
| [Together AI](https://together.ai) | up to $100 | 90 days | No |
| [xAI](https://x.ai/api) | $25 | 90 days | No |
| [Cohere](https://cohere.com) | $75 | None | No |
| [Fireworks AI](https://fireworks.ai) | $1 | 30 days | No |
| [DeepSeek](https://platform.deepseek.com) | 5M tokens | 30 days | No |
| [OpenAI](https://platform.openai.com) | $5 | 3 months | Yes |
| [Anthropic](https://console.anthropic.com) | $5 | None | Yes |

---

## Examples

### Gemini (no CC, 1500 req/day)

```python
import google.generativeai as genai

genai.configure(api_key="YOUR_KEY")
model = genai.GenerativeModel("gemini-2.0-flash")
print(model.generate_content("hello").text)
```

### Groq (no CC, OpenAI-compatible)

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key="YOUR_KEY")
resp = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "hello"}],
)
print(resp.choices[0].message.content)
```

### Ollama (local, no key needed)

```bash
ollama run llama3.2
```

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
resp = client.chat.completions.create(
    model="llama3.2",
    messages=[{"role": "user", "content": "hello"}],
)
print(resp.choices[0].message.content)
```

### Switch providers without rewriting your code (LiteLLM)

```python
from litellm import completion

messages = [{"role": "user", "content": "hello"}]

completion(model="gemini/gemini-2.0-flash", messages=messages)
completion(model="groq/llama-3.3-70b-versatile", messages=messages)
completion(model="ollama/llama3.2", messages=messages, api_base="http://localhost:11434")
```

---

## Contributing

If a limit is wrong or a provider is missing, open a PR. Include a link to the pricing page so the change is easy to verify.
