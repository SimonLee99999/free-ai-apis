# Free AI APIs 🆓

> A curated, developer-tested list of AI APIs with **genuine free tiers** — no credit card required unless noted.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Last Updated](https://img.shields.io/badge/updated-May%202026-blue.svg)]()
[![Stars](https://img.shields.io/github/stars/yourusername/free-ai-apis?style=social)]()

**Why this list?** Blog posts go stale. This repo is community-maintained and PR-driven. Every entry lists real rate limits so you can plan before you code.

---

## Contents

- [Large Language Models (LLMs)](#large-language-models)
- [Image Generation](#image-generation)
- [Speech & Audio](#speech--audio)
- [Embeddings & Vector Search](#embeddings--vector-search)
- [Code Generation](#code-generation)
- [Computer Vision](#computer-vision)
- [Multi-Modal](#multi-modal)
- [Free Credit Bundles](#free-credit-bundles)
- [Tools & SDKs](#tools--sdks)
- [Quick Start Examples](#quick-start-examples)
- [Contributing](#contributing)

---

## Large Language Models

> Sorted by free tier generosity. "No CC" = no credit card required to start.

### Tier 1 — Most Generous Free Tiers

| Provider | Model(s) | Free Limit | Context | No CC | Notes |
|----------|---------|------------|---------|-------|-------|
| **Google Gemini** | Gemini 2.0 Flash, 2.5 Pro | 1,500 req/day · 1M TPM | 1M tokens | ✅ | Best overall free tier; multimodal |
| **Groq** | Llama 3.3 70B, Mixtral 8x7B | Rate-limited (generous) | 32k tokens | ✅ | Fastest inference (~300 tok/s); OpenAI-compatible |
| **Mistral AI** | Mistral Large, Codestral, Pixtral | Unlimited (rate-limited) | 128k tokens | ✅ | All models included on free plan |
| **Cerebras** | Llama 3.3 70B | Rate-limited | 128k tokens | ✅ | Extremely fast; great for edge |
| **Hugging Face** | 1000s of models | Varies by model | Varies | ✅ | Widest model catalog; serverless inference |

### Tier 2 — Signup Credits (No CC)

| Provider | Model(s) | Free Credits | Expiry | Notes |
|----------|---------|-------------|--------|-------|
| **DeepSeek** | DeepSeek-V3, R1 | 5M tokens | 30 days | Exceptionally cheap after free tier |
| **Together AI** | 50+ models | $1–$100 | 90 days | Open-source model hub |
| **OpenRouter** | 100+ models | $1 credit | None | Route to cheapest free model automatically |
| **Fireworks AI** | Llama, Mixtral, Phi | $1 | 30 days | Extremely fast inference |

### Tier 3 — Small Credits (CC Required for Verification)

| Provider | Model(s) | Free Credits | Notes |
|----------|---------|-------------|-------|
| **OpenAI** | GPT-4o Mini, o1-mini | $5 | Industry standard; requires CC |
| **Anthropic** | Claude Haiku 4.5 | $5 | Best for agentic tasks |
| **xAI (Grok)** | Grok-3 | $25 | Twitter/X context access |
| **Cohere** | Command R+ | $75 | Excellent RAG + embeddings |

---

## Image Generation

| Provider | Model | Free Limit | No CC | Notes |
|----------|-------|-----------|-------|-------|
| **Stability AI** | Stable Diffusion 3 | 25 credits/month | ✅ | High quality; local run option |
| **Hugging Face** | FLUX, SDXL, many more | Rate-limited | ✅ | Free via Inference API |
| **Ideogram** | Ideogram 2.0 | 10 images/day | ✅ | Excellent text rendering in images |
| **Replicate** | Any open model | $0.002/run credit | Needs CC | Huge model library |
| **Fal.ai** | FLUX, AnimateDiff | $0.10 free | ✅ | Fast async image/video generation |

---

## Speech & Audio

| Provider | Capability | Free Limit | No CC | Notes |
|----------|-----------|-----------|-------|-------|
| **ElevenLabs** | TTS, Voice Cloning | 10k chars/month | ✅ | Best voice quality |
| **OpenAI Whisper** | STT (transcription) | Self-host free | ✅ | Open weights; run locally |
| **Deepgram** | STT | $200 credit | ✅ | Real-time + batch |
| **AssemblyAI** | STT + Intelligence | 100 hours free | ✅ | Speaker detection, summaries |
| **Kokoro TTS** | TTS | Open weights | ✅ | Run locally; high quality |

---

## Embeddings & Vector Search

| Provider | Model | Free Limit | Dimensions | No CC |
|----------|-------|-----------|-----------|-------|
| **Google** | text-embedding-004 | 1,500 req/day | 768 | ✅ |
| **Hugging Face** | BGE, E5, Nomic Embed | Rate-limited | 768–1536 | ✅ |
| **Cohere** | embed-english-v3 | 1M tokens/month | 1024 | ✅ |
| **Jina AI** | jina-embeddings-v3 | 1M tokens/month | 1024 | ✅ |
| **Mistral** | mistral-embed | Included in free plan | 1024 | ✅ |

**Free Vector Databases:**

| Service | Free Tier | Notes |
|---------|-----------|-------|
| **Qdrant Cloud** | 1GB storage | Best open-source option |
| **Pinecone** | 2GB (1 index) | Easy to start |
| **Chroma** | Self-hosted | Fully free; no limits |
| **Weaviate Cloud** | 14-day trial | Powerful GraphQL interface |

---

## Code Generation

| Provider | Model | Free Limit | No CC | Notes |
|----------|-------|-----------|-------|-------|
| **Mistral Codestral** | Codestral | Unlimited (rate-limited) | ✅ | Best free code model |
| **DeepSeek Coder** | DeepSeek-V3 | 5M tokens (signup) | ✅ | Excellent code quality |
| **Groq** | Llama 3.3 70B | Rate-limited | ✅ | Very fast code generation |
| **Hugging Face** | StarCoder2, CodeGemma | Rate-limited | ✅ | Many open code models |
| **GitHub Copilot** | GPT-4o | Free for students | ✅ | Via GitHub Student Pack |

---

## Computer Vision

| Provider | Capability | Free Limit | No CC | Notes |
|----------|-----------|-----------|-------|-------|
| **Google Vision API** | OCR, Labels, Objects | 1,000 req/month | ✅ | Industry-grade accuracy |
| **Clarifai** | Image classification | 1,000 ops/month | ✅ | Many pre-built models |
| **Roboflow** | Object detection | 1,000 credits/month | ✅ | Dataset tools included |
| **OpenCV** | Full CV library | Unlimited (local) | ✅ | Open-source; self-hosted |

---

## Multi-Modal

| Provider | Capabilities | Free Limit | No CC | Notes |
|----------|-------------|-----------|-------|-------|
| **Google Gemini 2.0 Flash** | Text + Image + Audio + Video | 1,500 req/day | ✅ | Best free multimodal |
| **Mistral Pixtral** | Text + Image | Included in free plan | ✅ | Good vision understanding |
| **OpenRouter (free models)** | Varies | $1 credit | ✅ | Route to free multimodal models |
| **Hugging Face** | BLIP, LLaVA, many | Rate-limited | ✅ | Wide model selection |

---

## Free Credit Bundles

> Collect these before you spend a dollar. No CC unless noted.

| Provider | Amount | Expiry | Requires CC? | Link |
|----------|--------|--------|-------------|------|
| Google AI Studio | Unlimited free tier | Ongoing | ❌ | [→](https://aistudio.google.com) |
| Groq | Generous rate limits | Ongoing | ❌ | [→](https://groq.com) |
| Together AI | Up to $100 | 90 days | ❌ | [→](https://together.ai) |
| xAI | $25 | 90 days | ❌ | [→](https://x.ai/api) |
| Cohere | $75 | Ongoing | ❌ | [→](https://cohere.com) |
| Fireworks AI | $1 | 30 days | ❌ | [→](https://fireworks.ai) |
| OpenAI | $5 | 3 months | ✅ | [→](https://platform.openai.com) |
| Anthropic | $5 | Ongoing | ✅ | [→](https://console.anthropic.com) |

**Total potential free credits: $200+**

---

## Tools & SDKs

### Unified API Clients (switch providers with one line)

| Tool | Language | Notes |
|------|---------|-------|
| **LiteLLM** | Python | Call 100+ LLMs with OpenAI format |
| **OpenRouter SDK** | JS/Python | Auto-route to cheapest available model |
| **LangChain** | Python/JS | Full LLM application framework |
| **Vercel AI SDK** | TypeScript | Best for Next.js + streaming |

### Local / Self-Hosted (completely free, no API limits)

| Tool | Models | Notes |
|------|--------|-------|
| **Ollama** | Llama, Mistral, Gemma, Phi | Easiest local LLM runner |
| **LM Studio** | Any GGUF model | Desktop GUI for local inference |
| **vLLM** | Any HuggingFace model | Production-grade local serving |
| **GPT4All** | Many models | Desktop app; privacy-focused |

---

## Quick Start Examples

### Google Gemini (Free, No CC)

```python
import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")  # Free at aistudio.google.com
model = genai.GenerativeModel("gemini-2.0-flash")
response = model.generate_content("Explain quantum computing in one paragraph")
print(response.text)
```

### Groq (Free, No CC, OpenAI-Compatible)

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="YOUR_GROQ_API_KEY",  # Free at groq.com
)
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

### Mistral (Free, No CC)

```python
from mistralai import Mistral

client = Mistral(api_key="YOUR_MISTRAL_API_KEY")  # Free at console.mistral.ai
response = client.chat.complete(
    model="mistral-large-latest",
    messages=[{"role": "user", "content": "Write a Python function to sort a list"}]
)
print(response.choices[0].message.content)
```

### Ollama (Fully Local, No API Key)

```bash
# Install and run locally — completely free, no rate limits
curl -fsSL https://ollama.com/install.sh | sh
ollama run llama3.2
```

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
response = client.chat.completions.create(
    model="llama3.2",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

### LiteLLM — Switch Providers Instantly

```python
from litellm import completion

# Switch providers by changing one string
response = completion(model="gemini/gemini-2.0-flash", messages=[...])
response = completion(model="groq/llama-3.3-70b-versatile", messages=[...])
response = completion(model="mistral/mistral-large-latest", messages=[...])
```

---

## Decision Guide

```
Need the most tokens for free?  → Google Gemini 2.0 Flash
Need the fastest response?      → Groq
Need best code generation?      → Mistral Codestral
No internet / privacy required? → Ollama (local)
Need image generation?          → Stability AI or Ideogram
Need speech to text?            → Whisper (local) or Deepgram
Building a RAG system?          → Cohere Embed + Qdrant Cloud
Need OpenAI compatibility?      → Groq or OpenRouter
Student with GitHub Education?  → GitHub Copilot (free)
```

---

## How Limits Work

| Term | Meaning |
|------|---------|
| **RPM** | Requests per minute |
| **TPM** | Tokens per minute |
| **req/day** | Maximum API calls per 24 hours |
| **Free tier** | Always free, no expiry |
| **Free credits** | Expires; use them first |

---

## Contributing

This list is maintained by the community. Entries go stale — PRs to update limits are just as valuable as adding new providers.

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Criteria to be included:**
- Must have a genuinely usable free tier (not just a trial)
- Must be publicly accessible (no invite-only)
- Rate limits must be documented

---

## License

[MIT](LICENSE) · Made with ❤️ by developers, for developers
