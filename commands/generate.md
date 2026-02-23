---
description: Generate an llms.txt file for a project with interactive guidance
argument-hint: "[optional: project-path]"
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
  - Grep
  - Task

tool-restrictions: |
  - Bash: Used for running Python script, checking project structure, validating Ollama connection
  - Task: Used to spawn Python execution agent for generation
  - Read/Write: For reviewing and saving generated files
  - Glob/Grep: For analyzing project documentation structure
---

# /llmstxt:generate

Interactively generate an llms.txt file for your project using Ollama LLM models. This command analyzes your documentation, connects to Ollama, generates a structured llms.txt file, validates it, and allows editing before saving.

## What This Does

1. **Analyzes** your project documentation (finds .md, .html, code comments)
2. **Auto-detects** project type (Python, Node.js, Swift, etc.)
3. **Detects** available Ollama models
4. **Guides** you through generation parameters
5. **Generates** llms.txt using Ollama LLM
6. **Validates** against llmstxt.org specification
7. **Scores** quality of generated content
8. **Lets you edit** before saving

## Usage

### Basic Usage (Interactive)

```bash
/llmstxt:generate
```

This starts an interactive workflow that guides you through all steps.

### With Project Path

```bash
/llmstxt:generate /path/to/my-project
```

Analyzes the specified project directly (skips path selection step).

## Interactive Workflow

### Step 1: Select Project Path

```
📂 Which project should we generate llms.txt for?
  → [current directory is default]
  → Enter path or press Enter for current directory
```

### Step 2: Project Analysis

```
🔍 Analyzing project structure...
  ✓ Found: FastHTML project (Python + Jupyter)
  ✓ Documentation:
    - 12 Markdown files (.md)
    - 8 HTML documentation pages
    - Code docstrings in fasthtml module
  ✓ Repo info:
    - Main language: Python
    - Framework: Starlette + HTMX
```

### Step 3: Ollama Model Selection

```
🤖 Available Ollama Models:
  1. llama2:latest (13B) ← Recommended for llms.txt
  2. mistral:latest (7B) - Faster
  3. neural-chat:latest (7B) - Conversational

  Select model (1-3) or press Enter for recommended:
  → 1
```

### Step 4: Generation Parameters

```
⚙️  Generation Settings:

  Tone: [technical/balanced/casual]
  → technical

  Verbosity: [concise/comprehensive]
  → concise

  Include external links? (y/n)
  → y

  Max links per section:
  → 10
```

### Step 5: Generation In Progress

```
⏳ Generating llms.txt using llama2...
  ↳ Analyzing documentation structure
  ↳ Generating structure and sections
  ↳ Creating link descriptions

  [████████████████░░] 75%
```

### Step 6: Review Generated Content

```
✅ Generated llms.txt:

# FastHTML

> FastHTML is a Python library for building server-rendered hypermedia applications using HTMX, Starlette, and Uvicorn. Simple to learn, powerful for production applications.

## Getting Started

- [Installation Guide](https://www.fastht.ml/docs/installation.html): Setup instructions for development and production
- [Quick Start](https://www.fastht.ml/docs/quickstart.html): 10-minute introduction with examples

## Core Concepts

- [Components & Elements](https://fastcore.fast.ai/xt_mimic.html): Building blocks for HTMX applications
...

[Show 50 lines, total file: 287 lines]
```

### Step 7: Validation Results

```
🔍 Validation Results:

Format Compliance:
  ✓ Valid H1 title
  ✓ Blockquote summary present
  ✓ Sections well organized
  ✓ All links accessible (27/27 ✓)

Quality Scoring:
  - Description clarity: 8.2/10
  - Structure organization: 9.1/10
  - External references: 8.5/10
  - Token efficiency: 8.8/10

Overall Score: 8.7/10 (Excellent)

Suggestions:
  ⚠️  Consider adding link to GitHub repository
  💡 "Optional" section could include architecture docs
```

### Step 8: Options

```
What would you like to do?

  1. ✅ Save generated llms.txt to ./llms.txt
  2. 📝 Edit before saving
  3. 🔄 Regenerate with different settings
  4. ❌ Discard and cancel

  Enter choice (1-4):
  → 2  [or 1 to save directly]
```

### Step 8b: Edit Mode (If chosen)

```
📝 Edit Mode

  Choose editing method:
  1. 🖊️  Open in text editor ($EDITOR)
  2. 🎯 Interactive CLI menu

  Enter choice (1-2):
  → 1
```

If text editor chosen, opens in `$EDITOR` (vim, nano, vs code, etc.)
If CLI menu chosen, shows interactive menu:

```
📋 Edit Sections

  Current sections:
  1. Getting Started (5 links)
  2. Core Concepts (6 links)
  3. API Reference (8 links)
  4. Examples (4 links)
  5. Optional (2 links)

  Choose action:
    [a]dd section
    [e]dit section
    [d]elete section
    [s]how full content
    [d]one editing

  Enter command:
  → e 3

  Editing: API Reference
    1. - [Request Object](URL): req object
    2. - [Response Object](URL): res object
    ...
```

### Step 9: Final Confirmation

```
💾 Ready to save!

Output file: ./llms.txt
File size: 4.2 KB
Sections: 5
Total links: 25

✓ Save to ./llms.txt?
  (y)es / (n)o / (c)opy path to clipboard
```

### Step 10: Success

```
✅ llms.txt generated successfully!

📍 Location: /path/to/project/llms.txt
📊 Size: 4.2 KB
🔗 Links: 25
⏱️  Time: 12 seconds

💡 Next steps:
  1. Review the file (cat llms.txt)
  2. Test with Claude: Share context and ask questions
  3. Commit: git add llms.txt && git commit -m "Add llms.txt"
  4. Regenerate: When docs update, run /llmstxt:generate again

📚 Learn more:
  - /llmstxt:validate - Check quality
  - /llmstxt:edit - Edit existing llms.txt
  - /skill llms-format-guide - Understand the format
```

## Configuration

Settings can be configured in `.claude/llmstxt-generator.local.md`:

```markdown
# Generation Settings
- default_model: llama2
- output_path: ./llms.txt
- default_tone: technical
- default_verbosity: concise
- max_links_per_section: 10
```

## Examples

### Example 1: Generate for Python Project

```bash
/llmstxt:generate ~/my-python-lib

# Detects:
# - Python project
# - Sphinx/pdoc documentation
# - GitHub repository
# Generates appropriately for Python ecosystem
```

### Example 2: Generate for Web Documentation

```bash
/llmstxt:generate ~/docs-site

# Detects:
# - VitePress/Docusaurus/Next.js docs
# - HTML pages
# - Markdown files
# Generates with web-focused structure
```

### Example 3: Advanced Parameters

```bash
/llmstxt:generate /path --model mistral --tone casual --links 15

# Options:
# --model: llama2, mistral, neural-chat, etc.
# --tone: technical, balanced, casual
# --verbosity: concise, comprehensive
# --links: max links per section (default 10)
```

## Troubleshooting

### "Error: Cannot connect to Ollama"

**Problem**: Ollama not running

**Solution**:
```bash
# Start Ollama in separate terminal
ollama serve

# Or on macOS, ensure the app is running
open /Applications/Ollama.app
```

### "Model not found: llama2"

**Problem**: Model hasn't been downloaded yet

**Solution**:
```bash
# Download the model (one-time, ~7GB)
ollama pull llama2

# Then retry /llmstxt:generate
```

### "Generation timeout after 60 seconds"

**Problem**: Ollama taking too long

**Solution**:
1. Use faster model: mistral instead of llama2
2. Reduce project size (exclude node_modules, build, etc.)
3. Increase timeout in `.claude/llmstxt-generator.local.md`: `timeout: 120`

### "No documentation found in project"

**Problem**: Couldn't find .md, .html, or docstrings

**Solution**:
1. Create some documentation first
2. Or specify custom paths in config:
   ```markdown
   - include_patterns:
       - "docs/**/*.md"
       - "my-docs/*.rst"
   ```

## Tips & Best Practices

### 1. Review Generated Content

Always review the generated llms.txt before using:
- Verify factual accuracy
- Check that descriptions match reality
- Ensure links are authoritative sources

### 2. Edit When Necessary

Don't hesitate to edit the generated file:
- Update descriptions to better match your docs
- Reorganize sections
- Remove or add links as needed

### 3. Regenerate Regularly

When your documentation changes significantly, regenerate:
```bash
/llmstxt:generate
# Updates existing llms.txt with new structure
```

### 4. Test with Claude

After generating, test your llms.txt:
```bash
# In Claude Code:
Share your llms.txt content, then ask questions
# Claude will use the structure to provide better answers
```

### 5. Commit to Git

Track llms.txt in version control:
```bash
git add llms.txt
git commit -m "Add llms.txt for AI-optimized documentation"
```

## Related Commands

- **`/llmstxt:validate`** - Validate and score existing llms.txt
- **`/llmstxt:edit`** - Edit llms.txt with guided interface
- **`/skill llms-format-guide`** - Learn the llms.txt format
- **`/skill ollama-integration`** - Setup and configure Ollama

## See Also

- **llmstxt-generator Hook** - Auto-regenerate on doc changes
- **llmstxt-analyzer Agent** - Proactive suggestions
- **generate_llmstxt.py** - Python script for advanced usage
- **https://llmstxt.org** - Format specification
