# llmstxt-generator Plugin

Intelligent `llms.txt` file generator for Claude Code. Automatically generate, validate, and maintain llms.txt files for documentation sites using local Ollama LLM models.

## Overview

The `llms.txt` standard (proposed by Answer.AI/Jeremy Howard, September 2024) provides a lightweight, Markdown-based format for making website content LLM-accessible at inference time. This plugin automates the creation and maintenance of llms.txt files by:

- **Auto-analyzing** documentation structure (Markdown, HTML, code comments)
- **Generating** structured llms.txt with Ollama LLM models
- **Validating** compliance with llmstxt.org specification
- **Maintaining** llms.txt automatically on documentation changes
- **Editing** llms.txt with guided workflows

## Features

### 📝 Skills
- **llms-format-guide** - Comprehensive guide to llms.txt format, best practices, and token optimization
- **ollama-integration** - Setup and usage guide for Ollama model selection and integration

### 🎯 Commands
- **`/llmstxt:generate`** - Interactive guided generation with project analysis
- **`/llmstxt:validate`** - Validate format compliance, check links, score quality
- **`/llmstxt:edit`** - Edit with text editor or interactive CLI menu

### 🤖 Agent
- **llmstxt-analyzer** - Proactively analyzes documentation and suggests generation/enhancement

### 🔗 Hooks
- **post-commit** - Auto-regenerates llms.txt when documentation changes (smart mode)

### 🐍 Python Script
- **generate_llmstxt.py** - Core engine that analyzes files and uses Ollama for generation

## Prerequisites

### Required
- **Claude Code** (v1.0.0+)
- **Ollama** - Local LLM runtime
  - Installation: https://ollama.ai
  - Verify: `ollama list` (shows available models)
  - Default: runs on `http://localhost:11434`

### Optional
- **Python 3.8+** (for standalone script usage)
- **uv** (for automatic dependency resolution in script)

## Installation

### Via Claude Code Plugins Directory

```bash
# Copy plugin to Claude Code plugins directory
cp -r llmstxt-generator ~/.claude/plugins/

# Or use symlink for development
ln -s $(pwd)/llmstxt-generator ~/.claude/plugins/
```

### Quick Test

```bash
# Verify plugin loads
cc --plugin-dir ./llmstxt-generator --list-commands | grep llmstxt
```

## Configuration

### Settings File

Create `.claude/llmstxt-generator.local.md` in your project:

```markdown
# llmstxt-generator Configuration

## Ollama Settings
- host: http://localhost:11434
- default_model: llama2

## Generation Preferences
- output_path: ./llms.txt
- include_patterns:
  - "**/*.md"
  - "**/*.html"
  - "src/**/*.{py,ts,swift}"
- exclude_patterns:
  - "node_modules/**"
  - ".git/**"
  - "build/**"

## Style Preferences
- tone: technical
- verbosity: concise
- include_external_links: true
- max_links_per_section: 10
```

All settings are optional. Defaults will be used if not specified.

## Usage

### Generate llms.txt (Interactive)

```bash
/llmstxt:generate
```

This triggers an interactive workflow:
1. Select project directory to analyze
2. Choose Ollama model (auto-detected options)
3. Specify output location
4. Choose generation style (concise/comprehensive)
5. Review generated llms.txt
6. Auto-validate against spec
7. Option to edit or confirm

### Validate Existing llms.txt

```bash
/llmstxt:validate
```

Validates:
- Format compliance with llmstxt.org spec
- All links are accessible (HTTP checks)
- Quality scoring (description clarity, structure quality)
- Suggestions for improvement

### Edit llms.txt

```bash
/llmstxt:edit
```

Choose editing mode:
1. **Text Editor** - Opens llms.txt in `$EDITOR`
2. **CLI Menu** - Interactive menu to add/remove/edit sections

### Using the Python Script Directly

```bash
# With uv (automatic dependencies)
uvx --from llmstxt-generator generate_llmstxt.py \
  --project /path/to/project \
  --model llama2 \
  --output ./llms.txt

# With Python directly
python scripts/generate_llmstxt.py \
  --project /path/to/project \
  --model llama2 \
  --output ./llms.txt \
  --verbose
```

### Agent Auto-Suggestions

The agent automatically:
- Detects when a project has documentation but no llms.txt
- Suggests generating an initial llms.txt
- Detects existing llms.txt files
- Offers to enhance/refresh existing files
- Runs on project load (with opt-out)

## Examples

### Example 1: Generate for FastHTML-style Docs

```markdown
# FastHTML

> FastHTML is a python library which brings together Starlette, Uvicorn, HTMX, and fastcore's FT into a library for creating server-rendered hypermedia applications.

## Docs

- [FastHTML quick start](https://fastht.ml/docs/tutorials/quickstart.html.md): Quick overview of FastHTML features
- [HTMX reference](https://htmx.org/reference/): Complete HTMX attribute reference

## Examples

- [Todo list application](https://github.com/AnswerDotAI/fasthtml/blob/main/examples/adv_app.py): Complete CRUD app walkthrough

## Optional

- [Starlette documentation](https://www.starlette.io/): Starlette web framework (FastHTML uses Starlette)
```

### Example 2: Command Flow

```bash
# 1. Generate initial file
/llmstxt:generate

# 2. Agent suggests enhancement based on docs analysis
# → "I detected 5 new documentation pages. Refresh llms.txt?"

# 3. Validate and score quality
/llmstxt:validate

# 4. Edit if needed
/llmstxt:edit
```

## How It Works

### Architecture

```
User Command (/llmstxt:generate)
    ↓
Claude Agent (llmstxt-analyzer)
    ↓
Python Script (generate_llmstxt.py)
    ├→ Auto-detect project type
    ├→ Analyze documentation files
    ├→ Extract structure and content
    ↓
Ollama LLM Model
    ├→ Generate llms.txt structure
    ├→ Create link descriptions
    ↓
Validation Engine
    ├→ Check format compliance
    ├→ Test link accessibility
    ├→ Score quality
    ↓
Generated llms.txt
    ↓
User Review & Edit
```

### Project Type Detection

- **Python** - nbdev, Sphinx, pdoc, MkDocs
- **JavaScript/TypeScript** - VitePress, Docusaurus, Gatsby, Next.js docs
- **Swift/iOS** - DocC, Swift Documentation
- **Other** - Generic Markdown analysis

### Ollama Model Guidance

**Recommended Models by Size**:
- **Small/Fast**: mistral, neural-chat (7B)
- **Balanced**: llama2 (13B) - recommended default
- **Comprehensive**: llama2:13b, neural-chat-7b (higher quality)

Models auto-detected from `ollama list` output.

## Troubleshooting

### Ollama Connection Error

```
Error: Cannot connect to Ollama at http://localhost:11434
```

**Solution**:
```bash
# Start Ollama if not running
ollama serve

# Or verify config
ollama list
```

### Model Not Found

```
Error: Model 'llama2' not found
```

**Solution**:
```bash
# List available models
ollama list

# Download a model if needed
ollama pull llama2
```

### Generation Timeout

If generation takes too long:
- Use a smaller model (mistral vs llama2:13b)
- Reduce project size by adjusting exclude_patterns
- Set reasonable timeouts in config

### Link Validation Slow

Disable link checking in validation:
- Edit `.claude/llmstxt-generator.local.md`
- Set `validate_links: false`

## Best Practices

### For Generated llms.txt

1. **Review before committing** - Verify Ollama-generated content is accurate
2. **Keep summaries concise** - 2-3 sentences max in blockquote
3. **Test with Claude** - Ask questions using your llms.txt context
4. **Update regularly** - Re-generate when docs change significantly
5. **Link to authoritative sources** - Prefer official docs over tutorials

### Configuration Tips

1. **Exclude build artifacts** - Use exclude_patterns for node_modules, dist/, build/
2. **Include code examples** - Set include_patterns to capture .py, .ts, .swift files
3. **Set realistic timeouts** - Ollama may be slow on first requests
4. **Monitor token usage** - Use concise tone to reduce token count

## Development

### Structure

```
llmstxt-generator/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   ├── llms-format-guide.md
│   └── ollama-integration.md
├── commands/
│   ├── generate.md
│   ├── validate.md
│   └── edit.md
├── agents/
│   └── llmstxt-analyzer.md
├── hooks/
│   └── hooks.json
├── scripts/
│   └── generate_llmstxt.py
├── examples/
│   └── sample_llms.txt
├── README.md
└── .gitignore
```

### Local Testing

```bash
# Copy to plugins for testing
cp -r . ~/.claude/plugins/llmstxt-generator

# Test in Claude Code
cc

# In Claude: /llmstxt:generate
```

### Contributing

1. Fork the plugin repository
2. Make changes to scripts, skills, or commands
3. Test thoroughly
4. Submit pull request with description

## Known Limitations

- Ollama model quality varies by model size
- Link validation requires internet connectivity
- Large projects may take time to analyze
- Some HTML structures may not parse perfectly

## Roadmap

- [ ] Support for GPT-4/Claude API as alternative to Ollama
- [ ] Web UI for llms.txt editor
- [ ] Integration with CI/CD (GitHub Actions, GitLab CI)
- [ ] Support for multiple llms.txt variants (llms-full.txt, llms-ctx.txt)
- [ ] Automated A/B testing of generated content
- [ ] Multi-language support

## References

- **llms.txt Specification** - https://llmstxt.org
- **Answer.AI Blog** - https://www.answer.ai/posts/2024-09-03-llmstxt.html
- **Ollama** - https://ollama.ai
- **Jeremy Howard** - Co-founder, Answer.AI

## License

MIT License - See LICENSE file for details

## Support

- **Issues** - Report bugs at GitHub repository
- **Discussions** - Community discussions on Claude Code Discord
- **Documentation** - Full docs at https://llmstxt.org

---

**Plugin Version**: 0.1.0
**Created**: 2026-02-22
**Last Updated**: 2026-02-22
