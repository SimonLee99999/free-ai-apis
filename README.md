# Awesome Free AI APIs [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> AI APIs with a real free tier. Rate limits listed so you know what you're working with before you start building.

PRs welcome — limits change often, keeping this accurate is the whole point.

## Contents

- [LLMs](#llms)
- [Image Generation](#image-generation)
- [Speech and Audio](#speech-and-audio)
- [Embeddings](#embeddings)
- [Vector Databases](#vector-databases)
- [Multi-modal](#multi-modal)
- [Local and Self-hosted](#local-and-self-hosted)
- [Expiring Credits](#expiring-credits)
- [Examples](#examples)

## LLMs

Permanent free tiers — no expiry, no credit card unless noted.

- [Google AI Studio](https://aistudio.google.com) - Gemini 2.0 Flash and 2.5 Pro. 1,500 requests/day, 1M TPM, 1M token context. No CC required.
- [Groq](https://console.groq.com) - Llama 3.3 70B and Mixtral 8x7B. Rate-limited but fast (~300 tokens/sec). OpenAI-compatible endpoint. No CC required.
- [Mistral](https://console.mistral.ai) - Large, Codestral, and Pixtral models all included on the free plan, rate-limited. No CC required.
- [Cerebras](https://cloud.cerebras.ai) - Llama 3.3 70B. Very fast inference, 128k context. No CC required.
- [Hugging Face Inference API](https://huggingface.co/inference-api) - Thousands of open-source models. Rate limits vary by model. No CC required.
- [OpenRouter](https://openrouter.ai) - Routes to 100+ models, many with their own free tiers. No CC required.
- [CoderPlan](https://coderplan.ai) - OpenAI-compatible API gateway for Claude Code, Cursor, and AI coding tools. Free tier with sign-up bonus. 50+ models including Claude, GPT, Gemini, DeepSeek. No CC required.

## Image Generation

- [Ideogram](https://ideogram.ai) - Version 2.0. 10 images/day. Good at rendering text inside images. No CC required.
- [Stability AI](https://stability.ai) - Stable Diffusion 3. 25 credits/month. No CC required.
- [Hugging Face Image Models](https://huggingface.co/models?pipeline_tag=text-to-image) - FLUX, SDXL, and others. Rate-limited. No CC required.
- [Fal.ai](https://fal.ai) - FLUX and AnimateDiff. $0.10 free credit on signup. No CC required.

## Speech and Audio

- [ElevenLabs](https://elevenlabs.io) - Text-to-speech and voice cloning. 10,000 characters/month free. No CC required.
- [Deepgram](https://deepgram.com) - Speech-to-text. $200 credit on signup. No CC required.
- [AssemblyAI](https://assemblyai.com) - Speech-to-text with speaker detection and auto-summaries. 100 hours free. No CC required.
- [Whisper](https://github.com/openai/whisper) - OpenAI's open-weights speech-to-text model. Run locally for free. No CC required.
- [Kokoro TTS](https://github.com/hexgrad/kokoro) - Open-weights text-to-speech. Self-hosted, no limits. No CC required.

## Embeddings

- [Google Embeddings API](https://ai.google.dev/gemini-api/docs/embeddings) - Text embedding model (text-embedding-004). 1,500 requests/day, 768 dimensions. No CC required.
- [Cohere Embed](https://cohere.com/embeddings) - English and multilingual embedding models. 1M tokens/month, 1024 dimensions. No CC required.
- [Jina AI](https://jina.ai) - Multilingual embeddings (jina-embeddings-v3). 1M tokens/month, 1024 dimensions. No CC required.
- [Mistral Embeddings](https://docs.mistral.ai/capabilities/embeddings/) - Included in the free plan. 1024 dimensions. No CC required.
- [Hugging Face Embedding Models](https://huggingface.co/models?pipeline_tag=feature-extraction) - BGE, E5, Nomic Embed, and others. Rate-limited. No CC required.

## Vector Databases

- [Qdrant Cloud](https://cloud.qdrant.io) - 1GB free storage. Can also self-host without limits.
- [Pinecone](https://pinecone.io) - 2GB storage, one index. Easiest to get started with.
- [Chroma](https://trychroma.com) - Fully open-source, self-hosted only. No limits.
- [Weaviate Cloud](https://weaviate.io) - 14-day free trial.

## Multi-modal

- [Gemini Vision API](https://ai.google.dev/gemini-api/docs/vision) - Text, image, audio, and video input. 1,500 requests/day. No CC required.
- [Mistral Vision](https://docs.mistral.ai/capabilities/vision/) - Text and image input via Pixtral. Included in the free plan. No CC required.

## Local and Self-hosted

No API key, no rate limits, no cost. Everything runs on your own machine.

- [Ollama](https://ollama.com) - Run Llama, Mistral, Gemma, and Phi locally. Simplest setup.
- [LM Studio](https://lmstudio.ai) - Desktop app for running any GGUF model with a GUI.
- [vLLM](https://github.com/vllm-project/vllm) - High-throughput inference server for production use.
- [GPT4All](https://gpt4all.io) - Desktop app, focused on privacy.

## Expiring Credits

These expire — grab them before starting a new project.

- [Together AI](https://together.ai) - Up to $100 credit, valid 90 days. No CC required.
- [xAI](https://x.ai/api) - $25 credit, valid 90 days. No CC required.
- [Cohere](https://cohere.com/pricing) - $75 credit, no expiry. No CC required.
- [DeepSeek](https://platform.deepseek.com) - 5M tokens on signup, valid 30 days. No CC required.
- [Fireworks AI](https://fireworks.ai) - $1 credit, valid 30 days. No CC required.
- [Anthropic](https://console.anthropic.com) - $5 credit, no expiry. CC required.
- [OpenAI](https://platform.openai.com) - $5 credit, valid 3 months. CC required.

## Examples

### Gemini — 1,500 requests/day, no CC

```python
import google.generativeai as genai

genai.configure(api_key="YOUR_KEY")
model = genai.GenerativeModel("gemini-2.0-flash")
print(model.generate_content("hello").text)
```

### Groq — OpenAI-compatible, no CC

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key="YOUR_KEY")
resp = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "hello"}],
)
print(resp.choices[0].message.content)
```

### Ollama — local, no key needed

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

### Switch providers without rewriting your code

```python
from litellm import completion

messages = [{"role": "user", "content": "hello"}]

completion(model="gemini/gemini-2.0-flash", messages=messages)
completion(model="groq/llama-3.3-70b-versatile", messages=messages)
completion(model="ollama/llama3.2", messages=messages, api_base="http://localhost:11434")
```
