# llmstxt-generator - Quick Start Guide

**Get your llms.txt file in 5 minutes!**

---

## 1️⃣ Install Prerequisites (2 minutes)

### Option A: macOS (Easiest)

```bash
# Download and run installer
# https://ollama.ai/download

# Or use Homebrew
brew install ollama
```

### Option B: Linux

```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

### Option C: Windows

```bash
# Download from https://ollama.ai/download/windows
# Run installer
```

### Verify Installation

```bash
ollama --version
```

---

## 2️⃣ Download an AI Model (1 minute)

```bash
# Download llama2 (recommended for llms.txt)
# ~7GB, done once, then reused
ollama pull llama2

# Or use faster alternative
ollama pull mistral  # ~5GB, faster
```

Check what you have:
```bash
ollama list
```

---

## 3️⃣ Start the Ollama Server (1 minute)

Keep this running in a terminal:

```bash
ollama serve
```

You should see:
```
Listening on 127.0.0.1:11434
```

✅ **Ollama is ready!**

---

## 4️⃣ Generate Your llms.txt (1 minute)

In **Claude Code**, run:

```bash
/llmstxt:generate
```

**What happens**:
1. ✅ Asks which project to generate for (default: current)
2. ✅ Analyzes your documentation
3. ✅ Shows available AI models
4. ✅ Generates your llms.txt
5. ✅ Validates the result
6. ✅ Offers to save it

**Follow the interactive prompts!**

---

## 5️⃣ Verify Your File (Optional)

Once generated, check quality:

```bash
/llmstxt:validate
```

You should see:
```
✅ Overall Score: 8.5/10 ⭐ Excellent

Format Compliance: 10/10 ✓
Link Validation:   10/10 ✓
Quality:           8.5/10 ✓
```

---

## 🎉 Done!

Your `llms.txt` file is ready to use!

### What's It For?

Your llms.txt makes it easy for:
- **Claude Code** - Better autocomplete and context
- **ChatGPT/Perplexity** - Discover your docs
- **Any LLM** - Optimized documentation access

---

## 📚 Learn More

Need guidance? Try these skills:

```bash
# Learn about the llms.txt format
/skill llms-format-guide

# Learn about Ollama and models
/skill ollama-integration
```

---

## 🛠️ Common Tasks

### Edit Your llms.txt

```bash
/llmstxt:edit
```

Choose:
- **Text Editor** - Edit in your favorite editor
- **CLI Menu** - Interactive guided editing

### Check Quality

```bash
/llmstxt:validate
```

Shows:
- Format compliance
- Link health
- Quality score (0-10)
- Improvement suggestions

### Regenerate (Keep It Fresh)

When your documentation changes:

```bash
/llmstxt:generate
```

Choose to update the existing file.

---

## ⚠️ Troubleshooting

### "Cannot connect to Ollama"

**Solution**: Start the Ollama server
```bash
ollama serve
```

Keep it running in a terminal while using the plugin.

### "Model not found"

**Solution**: Download it first
```bash
ollama pull llama2
# Wait for download to complete (~7GB)
```

### "Generation is very slow"

**Solution**: Use a faster model
```bash
ollama pull mistral  # Smaller, faster
/llmstxt:generate   # Choose mistral
```

### "My documentation wasn't detected"

**Solution**: Create some docs first
```bash
# Your project needs at least:
echo "# My Project" > README.md
echo "Getting started guide" > docs/guide.md

# Then try
/llmstxt:generate
```

---

## 🚀 Next Steps

### For Your Project

1. ✅ Generated llms.txt
2. → Commit it to git: `git add llms.txt && git commit -m "Add llms.txt"`
3. → Share it: Include in your project repository
4. → Update it: Run `/llmstxt:generate` when docs change

### Keep Learning

- 📖 [Read the full README](README.md)
- 🎓 [Learn the llms.txt format](/skills/llms-format-guide.md)
- 🤖 [Understand Ollama](/skills/ollama-integration.md)
- ✅ [Advanced validation](/commands/validate.md)

### Explore Features

| Feature | Command | Time |
|---|---|---|
| Generate | `/llmstxt:generate` | 5-10 min |
| Validate | `/llmstxt:validate` | 2 min |
| Edit | `/llmstxt:edit` | Varies |
| Learn Format | `/skill llms-format-guide` | 5 min |
| Learn Ollama | `/skill ollama-integration` | 5 min |

---

## 📞 Getting Help

### Documentation
- [Full User Guide](README.md)
- [Commands Reference](commands/)
- [Feature Overview](.claude-plugin/FEATURES.md)

### Community
- Discord: Claude Code community
- GitHub: Report issues or request features

### Still Stuck?

Try these quick questions:

```
"How do I install Ollama?"
"What model should I use?"
"How do I validate my llms.txt?"
"Can I edit llms.txt after generating?"
"What's llms.txt used for?"
```

---

## 💡 Quick Tips

1. **Start Simple**: Generate for current project first
2. **Test Often**: Run validate to check quality
3. **Edit if Needed**: Use `/llmstxt:edit --menu` for safe editing
4. **Keep Updated**: Regenerate when docs change
5. **Share It**: Include in your project repo

---

## ✨ You're Ready!

```bash
ollama serve          # Terminal 1: Keep running
/llmstxt:generate     # Claude Code: Generate
/llmstxt:validate     # Check quality
```

That's it! Your llms.txt is making your project more AI-friendly. 🚀

---

**Questions?** See [README.md](README.md) for comprehensive guide.

