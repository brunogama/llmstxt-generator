---
description: Edit an existing llms.txt file with guided workflows
argument-hint: "[optional: path-to-llms.txt]"
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
---

# /llmstxt:edit

Edit an existing llms.txt file with two options: open in your text editor or use an interactive CLI menu to modify sections and links.

## What This Does

1. **Locates** your llms.txt file
2. **Offers two edit modes**:
   - **Text Editor** - Opens in `$EDITOR` (vim, nano, VSCode, etc.)
   - **CLI Menu** - Interactive menu to add/remove/edit sections
3. **Validates** format after editing
4. **Suggests** improvements

## Usage

### Edit Interactive (Choose Mode)

```bash
/llmstxt:edit
```

Prompts you to choose editing method.

### Edit with Specific File

```bash
/llmstxt:edit /path/to/llms.txt
```

### Edit with Text Editor (Direct)

```bash
/llmstxt:edit --editor
```

Opens immediately in `$EDITOR` without menu.

### Edit with CLI Menu (Direct)

```bash
/llmstxt:edit --menu
```

Opens interactive menu directly.

## Text Editor Mode

### How It Works

```bash
/llmstxt:edit --editor
```

**Step 1**: Opens llms.txt in your default editor
```
# FastHTML                              ← Line 1: Title

> FastHTML is a Python library...       ← Line 3: Summary

Full documentation available.           ← Additional intro

## Getting Started                      ← Sections

- [Installation](URL): Install guide

...editor continues...
```

**Step 2**: Edit as normal in your editor (vim, nano, VSCode, Sublime, etc.)

**Step 3**: Save and close editor (`:wq` in vim, `Ctrl+S` then close in VSCode, etc.)

**Step 4**: Validation
```
✅ Validation Results:

Format: ✓ Valid Markdown structure
Links: ✓ 25 links found
Score: 8.7/10 (Excellent)

Save changes? (y/n)
→ y

✅ Saved to ./llms.txt
```

## CLI Menu Mode

### How It Works

```bash
/llmstxt:edit --menu
```

Presents an interactive menu:

```
╔════════════════════════════════════════════════════════════╗
║            llms.txt Interactive Editor - CLI Menu          ║
╚════════════════════════════════════════════════════════════╝

📄 File: ./llms.txt
📊 Size: 4.2 KB | 25 links | Score: 8.7/10

Current Structure:

  1. 📌 Title: "FastHTML"
  2. 📝 Summary: "FastHTML is a Python library..."

  SECTIONS:
  3. 📑 Getting Started (2 links)
  4. 📑 Core Concepts (6 links)
  5. 📑 API Reference (8 links)
  6. 📑 Examples (4 links)
  7. 📑 Optional (5 links)

MENU - Choose action:

  [v] View full content
  [e] Edit section
  [a] Add section
  [d] Delete section
  [l] Edit link
  [s] View statistics
  [q] Quit (with save prompt)

Enter command (v/e/a/d/l/s/q):
→
```

### Viewing Content

```
Enter command: v

📖 Full Content:

# FastHTML

> FastHTML is a Python library for building server-rendered
> hypermedia applications using HTMX, Starlette, and Uvicorn.

[Additional intro text]

## Getting Started

- [Installation Guide](https://www.fastht.ml/docs/install.html):
  Setup instructions for dev and production
- [Quick Start](https://www.fastht.ml/docs/quickstart.html):
  10-minute intro with examples

[... continues with all sections ...]

Press Enter to continue...
```

### Editing a Section

```
Enter command: e

Which section to edit?
  1. Getting Started
  2. Core Concepts
  3. API Reference
  4. Examples
  5. Optional

Choose (1-5):
→ 2

📝 Editing: Core Concepts (6 links)

1. [Components & Elements](URL): Building blocks...
2. [Advanced Patterns](URL): Complex patterns...
3. [State Management](URL): Starlette context...
4. [Middleware](URL): Custom middleware...
5. [Form Handling](URL): Form processing...
6. [AJAX & HTMX](URL): Dynamic interactions...

ACTIONS:
  [e] Edit a link description
  [d] Delete a link
  [a] Add new link
  [m] Move link to different section
  [v] View all links with URLs
  [r] Rename section
  [b] Back to main menu

Choose action (e/d/a/m/v/r/b):
→
```

### Editing a Link

```
Choose action: e

Which link to edit?
  1. [Components & Elements](URL): Building blocks...
  2. [Advanced Patterns](URL): Complex patterns...
  ... [continues] ...

Choose (1-6):
→ 1

📋 Current Link:

Title:  Components & Elements
URL:    https://fastcore.fast.ai/xt_mimic.html
Description: Building blocks for HTMX applications

EDIT OPTIONS:
  [t] Edit title
  [u] Edit URL
  [d] Edit description
  [r] Replace entire link
  [v] View in browser (if possible)
  [b] Back to section menu

Choose (t/u/d/r/v/b):
→ d

Current: Building blocks for HTMX applications

New description (or leave empty to keep):
→ Core elements and components for building HTMX apps

✓ Updated!
Description: Core elements and components for building HTMX apps

Continue editing? (e/d/a/m/v/r/b):
→ b
```

### Adding a Link

```
Choose action: a

Add link to "Core Concepts" section

Link title:
→ Custom Hooks

URL (full URL including https://):
→ https://fastcore.fast.ai/foundation.html#custom_hooks

Description (under 100 chars):
→ Creating custom HTMX-compatible hooks

Preview:
  - [Custom Hooks](https://fastcore.fast.ai/foundation.html#custom_hooks):
    Creating custom HTMX-compatible hooks

✓ Add this link? (y/n):
→ y

✓ Added to "Core Concepts"
New section size: 7 links

Continue editing? (e/d/a/m/v/r/b):
→ b
```

### Adding a Section

```
Enter command: a

Add new section

Section name (e.g., "Troubleshooting", "Community"):
→ Troubleshooting

Position in document:
  1. Before "Getting Started"
  2. After "Getting Started"
  3. After "Core Concepts"
  4. After "API Reference"
  5. After "Examples"
  6. At end (before "Optional")
  7. As new "Optional" section

Choose position (1-7):
→ 6

Links to add (you can add zero and add them later):

Link 1 title (or press Enter to skip):
→ Common Issues

URL:
→ https://github.com/AnswerDotAI/fasthtml/issues

Description:
→ GitHub issues and discussions

Add another link? (y/n):
→ n

Preview new section:

## Troubleshooting

- [Common Issues](https://github.com/AnswerDotAI/fasthtml/issues):
  GitHub issues and discussions

Create this section? (y/n):
→ y

✓ Section "Troubleshooting" added at position 6

Continue editing? (e/d/a/m/v/r/b):
→ q
```

### Deleting a Section

```
Enter command: d

Which section to delete?
  1. Getting Started
  2. Core Concepts
  3. API Reference
  4. Examples
  5. Optional

Choose (1-5):
→ 5

Delete section "Optional"?

  This section contains 5 links:
    - [Legacy APIs](URL)
    - [Deprecated Features](URL)
    - [Internal Implementation](URL)
    - [Research Papers](URL)
    - [Contributing Guide](URL)

  Warning: This will remove these links from llms.txt

  Delete? (yes/no):
  → no

✓ Section kept
```

### Statistics

```
Enter command: s

📊 Statistics:

Document Structure:
  - Title: FastHTML
  - Summary: Present (142 chars)
  - Sections: 5
  - Total links: 25

Content Analysis:
  - Average links per section: 5.0
  - Avg description length: 68 chars
  - External links: 8 (32%)
  - Internal links: 17 (68%)

Quality:
  - Format compliance: 100%
  - Accessibility (link check): 100%
  - Quality score: 8.7/10

Optimization:
  - Optional section: Yes ✓
  - Token efficiency: Good
  - Estimated context: 2,500 tokens

Suggestions:
  - Consider adding "Community" section
  - All links are healthy
  - Quality is excellent

Continue editing? (v/e/a/d/l/s/q):
→ q
```

### Quitting

```
Enter command: q

Changes made:
  - Modified 1 section
  - Added 3 links
  - Updated 2 descriptions

Save changes? (y/n):
→ y

Validating...
✅ Format valid
✅ All links format correct
⚠️  4 new links not checked (need HTTP)

Run /llmstxt:validate to check links

✓ Saved to ./llms.txt
```

## Side-by-Side Comparison

### Text Editor Mode

**Pros**:
- ✅ Full control and power
- ✅ Natural editing experience
- ✅ Easy for large rewrites
- ✅ All your editor shortcuts work

**Cons**:
- ⚠️ Need to know Markdown syntax
- ⚠️ Easy to break format if not careful
- ⚠️ No built-in validation prompts

**Best for**: Users comfortable with Markdown and their editor

### CLI Menu Mode

**Pros**:
- ✅ Guided step-by-step
- ✅ Hard to make format mistakes
- ✅ Shows previews before changes
- ✅ Interactive feedback

**Cons**:
- ⚠️ Slower for large edits
- ⚠️ Less powerful for complex changes
- ⚠️ Menu-based navigation

**Best for**: Users who want guidance and safety

## Examples

### Example 1: Add a Troubleshooting Section

```bash
/llmstxt:edit --menu

# Then:
# a (add section)
# Name: Troubleshooting
# Position: After Examples
# Add links for issues, FAQ, Discord, etc.
```

### Example 2: Update All Descriptions

```bash
/llmstxt:edit --editor

# Opens in vim/nano
# Use find-replace to enhance descriptions
# Save and close
```

### Example 3: Reorganize Sections

```bash
/llmstxt:edit --menu

# View current structure: v
# Edit sections to move links between sections
# Add new sections as needed
# Delete empty sections
```

## Tips & Best Practices

### 1. Always Validate After Editing

```bash
/llmstxt:edit

# Make changes...

/llmstxt:validate  # Check quality and links
```

### 2. Use Editor for Large Changes

If rewriting 50%+ of file, use text editor for speed.

### 3. Use Menu for Precise Changes

Adding one link or tweaking descriptions? Menu is faster.

### 4. Test with Claude

After editing, share context with Claude to verify changes work:

```bash
# Share updated llms.txt, then ask:
# "Using this documentation structure, how do I install the library?"
```

### 5. Keep "Optional" at End

Always put supplementary links in "Optional" section for token efficiency.

## Keyboard Shortcuts (Editor Mode)

**Vim**:
- `i` - Insert mode
- `:wq` - Save and quit
- `:q!` - Quit without saving
- `dd` - Delete line
- `yy` - Copy line

**Nano**:
- `Ctrl+X` - Exit
- `Ctrl+S` - Save (in some versions)
- `Ctrl+K` - Cut
- `Ctrl+U` - Paste

**VS Code** (if set as $EDITOR):
- `Ctrl+S` - Save
- `Ctrl+H` - Find/Replace
- `Ctrl+K Ctrl+0` - Fold all

## Troubleshooting

### "Editor not found / $EDITOR not set"

**Problem**: Can't open text editor

**Solution**:
```bash
# Set default editor
export EDITOR=vim  # or nano, code, etc.

# Or use CLI menu instead
/llmstxt:edit --menu
```

### "Format error after editing"

**Problem**: Broke Markdown while editing

**Solution**:
```bash
# Run validation to see errors
/llmstxt:validate

# Undo with git
git checkout llms.txt

# Try again with CLI menu for safety
/llmstxt:edit --menu
```

### "Can't find llms.txt"

**Problem**: File not in expected location

**Solution**:
```bash
/llmstxt:edit /path/to/correct/llms.txt

# Or specify in config:
# .claude/llmstxt-generator.local.md
# - output_path: ./docs/llms.txt
```

## Related Commands

- **`/llmstxt:generate`** - Create new llms.txt
- **`/llmstxt:validate`** - Check quality and links
- **`/skill llms-format-guide`** - Learn the format

## See Also

- **llmstxt Specification**: https://llmstxt.org
- **Text Editor Guides**: Vim/Nano/VSCode documentation
