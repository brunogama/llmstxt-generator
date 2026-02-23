---
version: 1.0.0
when_to_use: |
  Use this skill when you need to understand or create an llms.txt file. Perfect for:
  - "What is llms.txt and how do I create one?"
  - "Show me llms.txt format and structure"
  - "How do I write a good llms.txt file?"
  - "What are best practices for llms.txt?"
  - "Help me optimize llms.txt for token efficiency"
  - "Compare my llms.txt to the spec"

trigger_phrases:
  - "llms.txt format"
  - "how to create llms.txt"
  - "llms.txt structure"
  - "llms.txt best practices"
  - "llms.txt optimization"
  - "llms.txt specification"
  - "what is llms.txt"

progressive_disclosure: true
internal: false
---

# llms.txt Format Guide

The **llms.txt** file is a standardized Markdown-based format that makes website content optimized and accessible for Large Language Models at inference time. Proposed by Jeremy Howard (Answer.AI) in September 2024, it has become the standard for LLM-consumable documentation.

## Core Concept

Instead of LLMs struggling to parse HTML or reading massive websites that exceed context windows, llms.txt provides:
- **Concise summaries** of your documentation
- **Structured navigation** with organized links
- **LLM-optimized content** ready to use in AI assistants
- **Token efficiency** by fitting documentation in smaller context windows

## Format Specification

### Basic Structure

```markdown
# [Project/Site Name]

> [Brief summary: 2-3 sentences with critical context]

[Optional: Additional details without headings - lists, paragraphs]

## [Section Name - e.g., "Documentation"]

- [Link Title](URL): Optional description
- [Another Link](URL): Brief, informative description

## [Another Section]

- [Link](URL): Description

## Optional

- [Link](URL): Can be skipped for shorter LLM context
- [Another Link](URL): Secondary resources
```

### Required Elements

**Only the H1 heading is required:**
```markdown
# My Project Name
```

Everything else is optional but recommended.

### Recommended Elements

**1. Blockquote Summary** (highly recommended)
```markdown
> FastHTML is a Python library for building server-rendered hypermedia applications with HTMX, Starlette, and Uvicorn.
```

**2. Introduction Paragraphs** (without headings)
```markdown
# My Project

> [Summary]

This project includes comprehensive API documentation, tutorials, and examples. Compatible with Python 3.8+.

- **Use Case 1**: Description
- **Use Case 2**: Description
```

**3. Section Organization** (H2 headings)
```markdown
## Getting Started

- [Installation](URL): How to install
- [Quick Start](URL): 5-minute intro

## API Reference

- [Core Functions](URL): Main API
```

**4. Link Descriptions** (concise, specific)
```markdown
# Good descriptions
- [Authentication Guide](URL): OAuth2, API keys, session management
- [CLI Reference](URL): Complete command list with examples

# Avoid vague descriptions
- [Docs](URL): Documentation
- [API](URL): API stuff
```

**5. Optional Section** (for secondary resources)
```markdown
## Optional

- [Advanced Features](URL): Beyond basics
- [Troubleshooting](URL): Fix common issues
- [Community Resources](URL): Third-party tutorials
```

The "Optional" section signals to LLMs and tools that these links can be skipped if context is limited.

## Practical Examples

### Example 1: Python Library

```markdown
# FastCore

> FastCore is a collection of utility functions and types that Fast.ai uses throughout its libraries.

Core utilities for Python development, with no dependencies beyond the Python standard library.

## Installation & Getting Started

- [Installation Guide](https://github.com/fastai/fastcore#install): Simple pip install
- [Quick Tour](https://fastcore.fast.ai/): Overview of main features

## API Documentation

- [Collections](https://fastcore.fast.ai/collections.html.md): Working with lists, dicts, sets
- [Foundation](https://fastcore.fast.ai/foundation.html.md): Core utilities and helpers
- [Functional](https://fastcore.fast.ai/functional.html.md): Functional programming utilities

## Examples

- [Foundation Examples](https://github.com/fastai/fastcore/tree/master/examples): Real-world usage

## Optional

- [API Reference (Full)](https://fastcore.fast.ai/): Comprehensive API docs
- [GitHub Repository](https://github.com/fastai/fastcore): Source code and issues
```

### Example 2: Web Framework

```markdown
# Express.js

> Express is a minimal and flexible Node.js web application framework that provides a robust set of features for building web and mobile applications.

Fast, unopinionated web framework for Node.js with powerful routing and middleware.

## Getting Started

- [Installation & Setup](https://expressjs.com/en/starter/installing.html): Get started in minutes
- [Hello World Example](https://expressjs.com/en/starter/hello-world.html): Your first app
- [Basic Routing](https://expressjs.com/en/starter/basic-routing.html): Route basics

## Guide & Documentation

- [Routing Guide](https://expressjs.com/en/guide/routing.html): Advanced routing patterns
- [Middleware](https://expressjs.com/en/guide/using-middleware.html): Using and writing middleware
- [Error Handling](https://expressjs.com/en/guide/error-handling.html): Catching and handling errors

## API Reference

- [Request Object](https://expressjs.com/en/api.html#req): req API
- [Response Object](https://expressjs.com/en/api.html#res): res API

## Optional

- [Template Engines](https://expressjs.com/en/guide/using-template-engines.html): EJS, Pug, etc.
- [Database Integration](https://expressjs.com/en/guide/database-integration.html): Connect to databases
```

### Example 3: Documentation Site

```markdown
# Claude Code Documentation

> Claude Code is Anthropic's official command-line interface for Claude, the AI assistant. It includes features for file management, Git operations, AI-powered analysis, and plugin development.

Comprehensive documentation for building with Claude through the CLI.

## Quick Start

- [Installation](https://claude.dev/docs/installation): Get started in 5 minutes
- [First Steps](https://claude.dev/docs/first-steps): Your first Claude Code session

## Core Concepts

- [Commands Overview](https://claude.dev/docs/commands): All available commands
- [Tools Reference](https://claude.dev/docs/tools): Built-in tools and capabilities
- [Projects Structure](https://claude.dev/docs/projects): Organizing your work

## Advanced

- [Plugin Development](https://claude.dev/docs/plugins): Create custom plugins
- [MCP Integration](https://claude.dev/docs/mcp): Connect external services
- [Hooks & Automation](https://claude.dev/docs/hooks): Automate workflows

## Examples

- [Plugin Examples](https://github.com/anthropics/claude-code-plugins): Real plugin code
- [Sample Projects](https://github.com/anthropics/claude-code-examples): Tutorial projects

## Optional

- [Troubleshooting](https://claude.dev/docs/troubleshooting): Common issues
- [Community Plugins](https://marketplace.claude-code.dev): Community-built plugins
```

## Best Practices

### 1. Write Clear, Specific Summaries

**Good Summary:**
> FastHTML is a Python library for building server-rendered hypermedia applications with HTMX and Starlette. It's NOT compatible with FastAPI syntax, but enables rapid development of dynamic web apps.

**Weak Summary:**
> FastHTML is a library for web development.

**Why?** The good summary clarifies what it IS, what it's NOT, and why it matters—exactly what an LLM needs.

### 2. Organize Logically by User Journey

Structure sections in the order users encounter them:
1. **Getting Started** / **Quick Start** (what user needs first)
2. **Core Concepts** / **Guides** (deeper understanding)
3. **API Reference** (technical details)
4. **Examples** (real usage)
5. **Advanced** / **Optional** (supplementary)

### 3. Use Descriptive Link Text

**Good:**
```markdown
- [Authentication: OAuth2, API Keys, JWT](URL)
- [Error Handling: Try/catch, middleware, recovery](URL)
```

**Poor:**
```markdown
- [Auth](URL)
- [Errors](URL)
```

**Why?** Descriptions help LLMs understand what's in each link without fetching it.

### 4. Include External Resources

llms.txt can link outside your domain:
```markdown
- [HTMX Documentation](https://htmx.org/): Understand HTMX attributes and capabilities
- [HTTP Status Codes](https://httpwg.org/specs/rfc9110.html): Official HTTP spec reference
```

### 5. Avoid Redundancy

If information is in your summary, don't repeat it in linked descriptions:
```markdown
# Good
> FastHTML uses HTMX and Starlette for server-rendered apps.

## Frameworks
- [HTMX](URL): JavaScript library for dynamic interactions
- [Starlette](URL): Web framework providing routing and middleware

# Avoid
> FastHTML uses HTMX and Starlette.
- [HTMX: JavaScript library from Fast.ai](URL): Understand HTMX
- [Starlette: Web framework used by FastHTML](URL): Server framework
```

### 6. Test with LLMs

Generate your llms-ctx-full.txt and test:
```bash
llms_txt2ctx https://your-site.com/llms.txt -o context.xml
```

Then ask Claude, ChatGPT questions using that context to verify accuracy.

### 7. Keep Descriptions Under 100 Characters

Descriptions should be concise:
```markdown
# Good (clear, specific, ~60 chars)
- [Installation](URL): Simple pip install with no dependencies

# Too verbose (150+ chars)
- [Installation Guide](URL): Complete instructions on how to install the package using Python's package manager with detailed troubleshooting steps for common issues
```

## Token Optimization

Token efficiency is critical since context windows are limited. Here's how to optimize:

### 1. Use the "Optional" Section

Primary docs should fit in most context windows. Put supplementary content in "Optional":

```markdown
## Core APIs
- [Request](URL): Request object reference
- [Response](URL): Response object reference

## Optional
- [Legacy Endpoints](URL): Deprecated endpoints (usually not needed)
- [Internal Implementation](URL): Architecture details
```

**Impact**: ~40% smaller default context without losing essential info.

### 2. Consolidate Related Links

Instead of 10 individual endpoint docs:
```markdown
# Less efficient (many small links)
- [GET /users](URL): Get users
- [POST /users](URL): Create user
- [PUT /users/:id](URL): Update user
- [DELETE /users/:id](URL): Delete user

# More efficient (single comprehensive link)
- [User API Reference](URL): All user endpoints (GET, POST, PUT, DELETE)
```

### 3. Avoid Duplicate Content

Each link should be unique. Remove links to the same content:
```markdown
# Redundant
- [API Documentation](URL)
- [Complete API Reference](URL)
- [API Docs](URL)

# Better
- [API Reference](URL): All endpoints, authentication, error handling
```

### 4. Link to Summarized or Single-Page Docs

When possible, link to consolidated docs rather than multiple small pages:
```markdown
# Efficient (one page summary)
- [Quickstart Guide](URL): Installation, first request, common patterns (5 min read)

# Less efficient (requires multiple fetches)
- [Installation](URL)
- [Your First Request](URL)
- [Configuration](URL)
```

### 5. Use Markdown Versions When Available

llms.txt can reference `.md` or `.html.md` versions of pages:
```markdown
# Good (clean markdown)
- [API Reference](https://docs.example.com/api-ref.html.md): Markdown version

# Less efficient (HTML parsing required)
- [API Reference](https://docs.example.com/api-ref.html): HTML version
```

### Token Comparison Example

**Project with 50 pages of documentation:**

Without llms.txt:
- LLM tries to fetch all pages
- ~2MB HTML content
- Estimated ~500k tokens
- **Exceeds typical context windows**

With llms.txt (optimized):
- llms.txt: ~2KB with 15 curated links
- Tokens for llms.txt: ~500
- User-selected relevant pages: ~50KB (5 pages × 10KB avg)
- Estimated tokens for selected content: ~12k
- **Total: ~12.5k tokens = 97.5% reduction**

## Validation Checklist

Before publishing your llms.txt, verify:

- [ ] **H1 Title**: Clear project name as main heading
- [ ] **Blockquote**: 2-3 sentence summary with key context
- [ ] **Sections**: Organized with descriptive H2 headings
- [ ] **Links**: All URLs are accurate and accessible
- [ ] **Descriptions**: Concise (under 100 chars), specific, valuable
- [ ] **Structure**: At least one "Optional" section if you have many links
- [ ] **No Jargon**: Unexplained acronyms are avoided or defined
- [ ] **External Links**: Valid and current (GitHub, standards, etc.)
- [ ] **LLM Tested**: Asked Claude/ChatGPT questions using llms.txt context
- [ ] **Quality**: Descriptions are informative, not promotional

## Common Mistakes to Avoid

### ❌ Vague Link Text
```markdown
- [Docs](URL)
- [API](URL)
- [More Info](URL)
```
**Why Bad**: LLMs can't tell what's in these links. Use specific titles.

### ❌ Overly Long Descriptions
```markdown
- [Installation Guide](URL): This comprehensive guide covers all the detailed steps required for installing the package on various operating systems including Windows, macOS, and Linux, along with troubleshooting for specific versions and configurations.
```
**Why Bad**: Wastes tokens. Keep under 100 characters.

### ❌ Redundant Sections
```markdown
## Documentation
- [Docs](URL)
- [Documentation](URL)
- [Full Docs](URL)
```
**Why Bad**: Same content linked 3 ways. Choose one authoritative link.

### ❌ Promotional Language
```markdown
- [Amazing Quickstart](URL): The fastest way to get up and running!
- [Awesome API Reference](URL): Everything you need to know!
```
**Why Bad**: Emotional language doesn't help LLMs. Be factual.

### ❌ Missing "Optional" Section
```markdown
## Advanced Features
- [Internal Implementation](URL): How we built this
- [Legacy APIs](URL): Old endpoints
- [Experiments](URL): Research docs
```
**Why Bad**: These aren't essential. Put in "Optional" to let LLMs skip if needed.

## Integration with Generate

The **llmstxt-generator plugin** uses this format to:
1. Parse your llms.txt structure
2. Validate against this specification
3. Score quality of descriptions
4. Suggest improvements

When you run `/llmstxt:generate`, the Python script creates llms.txt following these best practices automatically using Ollama LLM models.

## Resources

- **Official Spec**: https://llmstxt.org
- **Answer.AI Blog**: https://www.answer.ai/posts/2024-09-03-llmstxt.html
- **Example llms.txt Files**: https://llmstxthub.com
- **Validation Tools**: https://github.com/AnswerDotAI/llms-txt

## See Also

- **Ollama Integration Skill**: Learn how to set up and use Ollama for generation
- **llmstxt-generator Plugin**: Automate llms.txt creation and maintenance
- **llms.txt Specification**: Full formal specification at llmstxt.org
