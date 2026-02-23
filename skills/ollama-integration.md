---
version: 1.0.0
when_to_use: |
  Use this skill when you need help with Ollama setup and model selection for llms.txt generation:
  - "How do I install Ollama?"
  - "What Ollama model should I use?"
  - "How do I run Ollama locally?"
  - "Which model is best for llms.txt generation?"
  - "How to connect to Ollama from a script?"
  - "Troubleshoot Ollama connection issues"
  - "What's the difference between Ollama models?"

trigger_phrases:
  - "ollama installation"
  - "ollama models"
  - "ollama setup"
  - "which model for"
  - "ollama local"
  - "ollama api"
  - "ollama connection"

progressive_disclosure: true
internal: false
---

# Ollama Integration Guide

**Ollama** is a lightweight local LLM runtime that lets you run large language models on your machine without cloud dependencies. The llmstxt-generator plugin uses Ollama to intelligently generate llms.txt files.

## What is Ollama?

Ollama is an open-source project that makes running LLMs locally simple and fast:
- **Free and open-source** - No API costs or rate limits
- **Privacy-first** - All processing happens on your machine
- **Simple CLI** - Easy to install and manage models
- **Fast inference** - Optimized for consumer hardware
- **API server** - Can be used programmatically

**Official Site**: https://ollama.ai
**GitHub**: https://github.com/ollama/ollama

## Installation

### macOS

**Option 1: Download App** (Easiest)
1. Visit https://ollama.ai/download
2. Download macOS installer
3. Run the installer
4. Ollama runs as a background service

**Option 2: Homebrew**
```bash
brew install ollama
ollama serve  # Start the server
```

### Linux

**Option 1: Installation Script**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
ollama serve
```

**Option 2: Docker**
```bash
docker run -d -v ollama:/root/.ollama -p 11434:11434 \
  --name ollama ollama/ollama:latest
```

### Windows

1. Download: https://ollama.ai/download/windows
2. Run installer
3. Ollama starts automatically on background

## Verify Installation

```bash
# Check if Ollama is running
ollama list

# Should show available models, or empty list initially
```

If you see "Connection refused", Ollama isn't running:
```bash
# macOS/Linux
ollama serve

# Or check if service is running
ps aux | grep ollama
```

## Model Selection for llms.txt Generation

Different Ollama models have different characteristics. Here's a guide for generating llms.txt:

### Recommended Models

#### **llama2** (13B) - ⭐ BEST FOR LLMS.TXT
- **Size**: 13B parameters, ~7GB disk
- **Speed**: Fast (reasonable on consumer hardware)
- **Quality**: Excellent - good structure and descriptions
- **Use Case**: Default choice for llms.txt generation
- **Memory**: ~8GB RAM recommended

```bash
ollama pull llama2
```

**Best for**: Balanced generation quality and speed

---

#### **mistral** (7B) - Fast & Capable
- **Size**: 7B parameters, ~5GB disk
- **Speed**: Very fast, good for quick generation
- **Quality**: Good - slightly less verbose than llama2
- **Memory**: ~4GB RAM sufficient
- **Instruction Following**: Excellent

```bash
ollama pull mistral
```

**Best for**: Quick generation on limited hardware

---

#### **neural-chat** (7B) - Conversational
- **Size**: 7B parameters, ~5GB disk
- **Speed**: Very fast
- **Quality**: Excellent for conversational content
- **Memory**: ~4GB RAM
- **Focus**: Optimized for chat and instruction tasks

```bash
ollama pull neural-chat
```

**Best for**: Natural, conversational link descriptions

---

#### **dolphin-mixtral** (8x7B MoE) - Advanced
- **Size**: 8x7B mixture-of-experts, ~32GB disk
- **Speed**: Slower (requires more compute)
- **Quality**: Excellent - comprehensive and accurate
- **Memory**: ~20GB RAM needed (not recommended for most)

```bash
ollama pull dolphin-mixtral
```

**Best for**: Maximum quality when resources available

---

### Not Recommended for llms.txt

**Too Small**:
- **tinyllama** - Lower quality content for complex docs

**Too Slow**:
- **llama2:70b** - Overkill for llms.txt (slow on consumer hardware)
- **openchat-3.5-orca** - Slower than alternatives without quality benefit

**Specialized**:
- **codeup** - Optimized for code, not documentation
- **magicoder** - For coding tasks, not general content

## Downloading Models

Each model is a one-time download that stores locally:

```bash
# Download (first time only)
ollama pull llama2
# ~7GB download, ~15 min depending on internet

# Future runs use local copy (instant)
ollama list
# Shows: NAME              ID              SIZE      MODIFIED
#        llama2:latest     91ab59b18b92    3.8 GB    2 minutes ago
```

### Managing Disk Space

```bash
# Remove a model to free space
ollama rm llama2

# Check disk usage
du -sh ~/.ollama/

# Show all models
ollama list
```

## Starting Ollama Server

The llmstxt-generator plugin communicates with Ollama via API (default: `http://localhost:11434`).

### Automatic (macOS with App)

Ollama starts automatically as a background service after installation.

```bash
# Verify it's running
ollama list
```

### Manual Start (Linux/macOS)

```bash
# In terminal window 1
ollama serve

# In terminal window 2
ollama list
```

### With Docker

```bash
docker run -d \
  -v ollama:/root/.ollama \
  -p 11434:11434 \
  --name ollama \
  ollama/ollama:latest

# Download a model
docker exec ollama ollama pull llama2
```

## API Connection

The llmstxt-generator plugin connects to Ollama's API. Here's how it works:

### Default Configuration

```bash
# Ollama API endpoint (default)
http://localhost:11434

# Generate request example (what the plugin does)
curl http://localhost:11434/api/generate \
  -d '{
    "model": "llama2",
    "prompt": "Create an llms.txt structure for FastHTML library",
    "stream": false
  }'
```

### Custom Configuration

If Ollama runs on different host/port, configure in `.claude/llmstxt-generator.local.md`:

```markdown
# llmstxt-generator Configuration

## Ollama Settings
- host: http://192.168.1.100:11434
- default_model: llama2
```

### Testing Connection

```bash
# Test if Ollama is accessible
curl http://localhost:11434/api/tags

# Should return:
# {"models":[{"name":"llama2:latest",...}]}
```

## Model Performance Guide

### Generation Speed

On typical hardware (MacBook Pro M1, 16GB RAM):

| Model | First Token | Full llms.txt | Quality |
|---|---|---|---|
| mistral (7B) | ~100ms | ~2-3 seconds | Good |
| neural-chat (7B) | ~100ms | ~2-3 seconds | Excellent |
| llama2 (13B) | ~200ms | ~4-6 seconds | Excellent |
| dolphin-mixtral (8x7B) | ~500ms | ~15-20 seconds | Superior |

**Note**: Speeds vary by hardware. GPU acceleration greatly improves performance.

### Output Quality Examples

For the prompt: "Create an llms.txt link description for an authentication guide":

**mistral**:
> "Complete OAuth2 implementation with JWT tokens, refresh logic"

**llama2**:
> "Comprehensive OAuth2, API key, and JWT authentication patterns with examples"

**neural-chat**:
> "Step-by-step OAuth2, API keys, and JWT authentication with error handling"

**dolphin-mixtral**:
> "Complete authentication guide: OAuth2 flows, API key management, JWT tokens, session handling, security best practices"

All are good; llama2 and neural-chat offer best balance.

## Troubleshooting

### Error: "Cannot connect to Ollama at localhost:11434"

**Cause**: Ollama isn't running

**Solution**:
```bash
# Start Ollama
ollama serve

# Or check if it's running
lsof -i :11434
```

### Error: "Model 'llama2' not found"

**Cause**: Model hasn't been downloaded yet

**Solution**:
```bash
# Download the model
ollama pull llama2

# List available models
ollama list
```

### Error: "Out of memory"

**Cause**: Model is too large for available RAM

**Solution**:
1. Use smaller model (mistral or neural-chat instead of llama2:70b)
2. Close other applications
3. Try `ollama serve --num-gpu 0` to use CPU only (slower)

### Generation is Very Slow

**Cause**: Model running on CPU instead of GPU, or model too large

**Solution**:
```bash
# Check if GPU is enabled (look for "metal" or "cuda")
ollama serve

# If using CPU only:
# - Reduce context size
# - Use smaller model (mistral)
# - Add GPU support (check ollama.ai for hardware)
```

### Model Downloaded But Not Appearing

**Solution**:
```bash
# Refresh model list
ollama list

# If still not showing, restart Ollama
pkill ollama
ollama serve
```

## Advanced: Custom Model Files

For advanced users, you can use custom quantized models:

```bash
# Create Modelfile (custom model config)
cat > Modelfile << EOF
FROM ./model.gguf
PARAMETER temperature 0.7
PARAMETER top_p 0.9
EOF

# Create custom model
ollama create mymodel -f Modelfile

# Use in generation
ollama run mymodel "prompt"
```

## Performance Tips

### 1. Use GPU Acceleration

Ollama automatically uses GPU if available:
- **macOS**: Metal acceleration (automatic on Apple Silicon)
- **Linux/Windows**: NVIDIA CUDA (install CUDA toolkit)
- **Check**: Look for "metal" or "cuda" in `ollama serve` output

### 2. Adjust Context Window

Smaller context = faster generation:

```bash
# Generate with smaller context (faster)
curl http://localhost:11434/api/generate \
  -d '{
    "model": "llama2",
    "prompt": "...",
    "num_ctx": 512
  }'
```

### 3. Use Streaming for Feedback

For long-running generation, stream responses:

```bash
# Stream mode (get output as it generates)
curl http://localhost:11434/api/generate \
  -d '{
    "model": "llama2",
    "prompt": "...",
    "stream": true
  }'
```

### 4. Pre-warm Model

First inference is slower. Subsequent requests are faster:

```bash
# Pre-warm to cache model in memory
ollama run llama2 "What is llms.txt?" > /dev/null
```

## Model Selection Decision Tree

```
Do you have GPU acceleration?
├─ Yes (GPU)
│  └─ Use: llama2 (best quality/speed balance)
│     └─ Or: dolphin-mixtral (maximum quality)
│
└─ No (CPU only)
   ├─ Generation takes >10 seconds?
   │  └─ Use: mistral (fast, good quality)
   │
   └─ Generation is fast enough?
      └─ Use: neural-chat (excellent for descriptions)
```

## Configuration for llmstxt-generator

In `.claude/llmstxt-generator.local.md`:

```markdown
# Ollama Settings

## Connection
- host: http://localhost:11434
- timeout: 60  # seconds

## Model Selection
- default_model: llama2
- allow_model_selection: true

## Generation Parameters
- temperature: 0.7        # 0-1: Lower = deterministic, Higher = creative
- top_p: 0.9             # Nucleus sampling (0-1)
- top_k: 40              # Diversity control
- num_ctx: 2048          # Context window size
- num_predict: 512       # Max tokens to generate
- repeat_penalty: 1.1    # Prevent repetition
```

## Next Steps

1. **Install Ollama** - https://ollama.ai/download
2. **Pull a model** - `ollama pull llama2`
3. **Generate llms.txt** - Use `/llmstxt:generate` in Claude Code
4. **Monitor performance** - Adjust settings based on speed/quality

## Resources

- **Ollama Official**: https://ollama.ai
- **Model Library**: https://ollama.ai/library
- **GitHub**: https://github.com/ollama/ollama
- **Community**: https://discord.com/invite/ollama
- **Model Benchmarks**: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard

## See Also

- **llms-format-guide**: Format specification and best practices
- **llmstxt-generator Plugin**: Automated generation with Ollama
- **Python Script**: `generate_llmstxt.py` for advanced usage
