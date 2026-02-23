# llmstxt-generator - Testing Guide

**Version**: 0.1.0
**Date**: 2026-02-22
**Coverage**: All components

---

## Setup for Testing

### Prerequisites

```bash
# 1. Verify Python 3.8+
python --version

# 2. Verify Ollama installed
ollama --version

# 3. Install/download a model
ollama pull llama2  # ~7GB, one-time
ollama pull mistral # (optional, smaller alternative)

# 4. Start Ollama (keep running during tests)
ollama serve

# 5. Install uv for Python script testing
pip install uv
```

### Copy Plugin for Testing

```bash
# Copy to local test location
cp -r /tmp/llmstxt-generator ~/.claude/plugins/llmstxt-generator-test

# Or use symlink for development
ln -s /tmp/llmstxt-generator ~/.claude/plugins/llmstxt-generator
```

---

## Test Execution Plan

### Phase 1: Skills Testing (15 minutes)

#### Test S1: llms-format-guide Skill

**Trigger Phrase**:
```
/skill llms-format-guide
```

**Expected**: Loads skill documentation

**Verify**:
- [ ] Skill loads successfully
- [ ] Content displays (format spec section visible)
- [ ] Examples are clear and readable
- [ ] Markdown renders correctly
- [ ] Navigation links work

**Test Variations**:
```
# Additional trigger questions
"What is llms.txt?"
"Show me llms.txt format"
"How do I write a good llms.txt?"
"Explain llms.txt best practices"
"Help me optimize llms.txt for tokens"
```

**Pass Criteria**:
- ✓ Skill loads on all trigger phrases
- ✓ Content is relevant to question
- ✓ Examples are helpful and accurate

---

#### Test S2: ollama-integration Skill

**Trigger Phrase**:
```
/skill ollama-integration
```

**Expected**: Loads Ollama setup guide

**Verify**:
- [ ] Skill loads successfully
- [ ] Installation instructions are clear
- [ ] Model selection guide is comprehensive
- [ ] Troubleshooting section is helpful
- [ ] Examples are relevant

**Test Variations**:
```
# Additional trigger questions
"How do I install Ollama?"
"What Ollama model should I use?"
"Which model is best for llms.txt?"
"How do I troubleshoot Ollama?"
"How do I run Ollama locally?"
```

**Pass Criteria**:
- ✓ Skill loads on all trigger phrases
- ✓ Model recommendations are appropriate
- ✓ Troubleshooting solves common issues
- ✓ Instructions are OS-specific and correct

---

### Phase 2: Commands Testing (45 minutes)

#### Test C1: /llmstxt:generate Command

**Test C1.1: Interactive Mode**

```bash
/llmstxt:generate
```

**Expected Flow**:
1. Prompts for project directory (default: current)
2. Analyzes project structure
3. Shows detected documentation
4. Offers Ollama model selection
5. Prompts for generation parameters
6. Starts generation with progress
7. Shows generated content (preview)
8. Validates format and shows score
9. Offers save/edit/regenerate/discard options
10. Saves to specified location

**Verify**:
- [ ] Project detection works
- [ ] Models listed correctly
- [ ] Generation completes without errors
- [ ] Generated content is valid Markdown
- [ ] Generated content has H1 title
- [ ] Generated content has blockquote summary
- [ ] Generated content has sections with links
- [ ] Quality score displayed (0-10)
- [ ] File saved successfully

**Pass Criteria**:
- ✓ Workflow completes end-to-end
- ✓ Generated file is valid llms.txt
- ✓ Generated file meets spec
- ✓ Quality score 7.0+

---

**Test C1.2: With Project Path Argument**

```bash
/llmstxt:generate ~/sample-project
```

**Expected**:
- Analyzes specified project
- Skips path selection step
- Continues with flow

**Verify**:
- [ ] Accepts path argument
- [ ] Analyzes correct project
- [ ] Output file location is correct

---

**Test C1.3: Error Handling**

```bash
# Test with Ollama not running
# Test with invalid project path
# Test with missing model
```

**Verify**:
- [ ] Error messages are clear
- [ ] Suggests solutions (e.g., "ollama serve")
- [ ] Graceful exit with helpful message

---

#### Test C2: /llmstxt:validate Command

**Test C2.1: Validate Generated File**

```bash
# First generate a file
/llmstxt:generate

# Then validate it
/llmstxt:validate
```

**Expected**:
- Finds llms.txt in current directory
- Runs validation checks
- Shows quality report with score
- Lists improvement suggestions

**Verify**:
- [ ] Format validation passes
- [ ] Link validation completes
- [ ] Quality score calculated (0-10)
- [ ] Suggestions are specific and actionable
- [ ] Report shows all metrics

**Pass Criteria**:
- ✓ Validation completes without errors
- ✓ Score is 7.0+ for generated file
- ✓ All checks pass or have clear reasons
- ✓ Suggestions are relevant

---

**Test C2.2: Specific File Path**

```bash
/llmstxt:validate /path/to/other/llms.txt
```

**Verify**:
- [ ] Accepts file path argument
- [ ] Validates correct file
- [ ] Results are accurate for that file

---

**Test C2.3: Verbose Mode**

```bash
/llmstxt:validate --verbose
```

**Verify**:
- [ ] Shows additional detail
- [ ] Includes all link checks
- [ ] Shows individual scores
- [ ] More information than default

---

**Test C2.4: Quality Score Examples**

Test with different llms.txt files:

| File Type | Expected Score | Test |
|---|---|---|
| Generated (good) | 8.0-9.0 | ✓ |
| Well-maintained | 8.5-9.5 | ✓ |
| Minimal llms.txt | 6.0-7.0 | ✓ |
| Poorly structured | 4.0-6.0 | ✓ |

---

#### Test C3: /llmstxt:edit Command

**Test C3.1: Edit Mode Selection**

```bash
/llmstxt:edit
```

**Expected**:
- Prompts to choose edit mode
- Offers "Text Editor" or "CLI Menu"

**Verify**:
- [ ] Presents both options clearly
- [ ] Accepts user choice

---

**Test C3.2: Text Editor Mode**

```bash
/llmstxt:edit --editor
```

**Expected**:
- Opens llms.txt in $EDITOR
- Can edit naturally
- Saves to file
- Validates on save

**Verify**:
- [ ] Opens in correct editor ($EDITOR)
- [ ] File content displays correctly
- [ ] Can save changes
- [ ] Format validation after save
- [ ] Saved changes persist

**Test with Different Editors**:
```bash
# Test with different editors
EDITOR=vim /llmstxt:edit --editor
EDITOR=nano /llmstxt:edit --editor
EDITOR=code /llmstxt:edit --editor  # VS Code
```

---

**Test C3.3: CLI Menu Mode**

```bash
/llmstxt:edit --menu
```

**Expected**:
- Shows interactive menu
- Presents edit options

**Menu Commands to Test**:

```
v - View full content
  [ ] Shows complete file
  [ ] Readable formatting
  [ ] Proper line breaks

e - Edit section
  [ ] Lists sections
  [ ] Can select section
  [ ] Shows links in section
  [ ] Can edit link descriptions

a - Add section
  [ ] Prompts for section name
  [ ] Prompts for links
  [ ] Creates new section
  [ ] Validates structure

d - Delete section
  [ ] Confirms deletion
  [ ] Prevents accidental deletion
  [ ] Section removed correctly

l - Edit link
  [ ] Lists all links
  [ ] Can select link
  [ ] Can edit title/URL/description
  [ ] Preview before saving

s - Statistics
  [ ] Shows file stats
  [ ] Shows link count
  [ ] Shows quality metrics
  [ ] Shows suggestions

q - Quit
  [ ] Prompts to save
  [ ] Saves changes correctly
  [ ] Validates format
```

**Verify**:
- [ ] All menu commands work
- [ ] Changes save correctly
- [ ] Format validation works
- [ ] Previews before changes
- [ ] Can undo by quitting without save

---

### Phase 3: Agent Testing (20 minutes)

#### Test A1: llmstxt-analyzer Agent

**Test A1.1: Proactive Detection**

```
Open a project directory with documentation but no llms.txt

Expected: Agent proactively suggests "Should I create llms.txt?"
```

**Verify**:
- [ ] Agent detects documentation
- [ ] Agent suggests generation
- [ ] Suggestion is appropriate
- [ ] Offers clear next steps
- [ ] Can run /llmstxt:generate from suggestion

---

**Test A1.2: Manual Invocation**

```
Ask directly: "Should I create an llms.txt for my project?"
Ask: "Analyze my documentation structure"
Ask: "Does my llms.txt need updating?"
```

**Verify**:
- [ ] Agent provides analysis
- [ ] Analysis is specific to project
- [ ] Recommendations are concrete
- [ ] Suggests appropriate commands

---

**Test A1.3: Enhancement Suggestions**

```
Run: /llmstxt:validate (get quality score)
Ask agent: "How can I improve my llms.txt?"
```

**Verify**:
- [ ] Agent provides specific suggestions
- [ ] Suggestions match validation report
- [ ] Agent ranks by priority
- [ ] Suggests appropriate edits

---

### Phase 4: Hook Testing (15 minutes)

#### Test H1: Post-commit Hook

**Setup**:
```bash
cd /tmp/test-project
git init
git config user.name "Test"
git config user.email "test@example.com"

# Create some docs
mkdir docs
echo "# My Project" > README.md
echo "## Getting Started" > docs/guide.md

# Create initial llms.txt
/llmstxt:generate
git add .
git commit -m "Initial commit"
```

**Test H1.1: Hook Activation on Doc Change**

```bash
# Modify a documentation file
echo "## More Content" >> docs/guide.md

# Commit the change
git add docs/guide.md
git commit -m "Update guide"
```

**Expected**:
- Hook detects documentation change
- Shows prompt asking to regenerate
- Offers options

**Verify**:
- [ ] Hook fires after commit
- [ ] Detects doc file change
- [ ] Prompt is clear
- [ ] Options are available (regenerate/validate/skip)
- [ ] Can select option and action executes

---

**Test H1.2: Hook Ignores Non-Doc Changes**

```bash
# Modify non-doc file
echo "garbage" > .gitignore

# Commit
git add .gitignore
git commit -m "Update gitignore"
```

**Expected**:
- Hook does NOT trigger (no doc files changed)

**Verify**:
- [ ] Hook does not prompt
- [ ] No unnecessary notifications

---

**Test H1.3: Hook Config**

```bash
# Edit .claude/llmstxt-generator.local.md
# Set: auto_commit_regenerate: true

# Then commit docs
echo "## More" >> docs/guide.md
git add docs/guide.md
git commit -m "Docs updated"
```

**Expected**:
- Hook auto-regenerates llms.txt
- No manual prompt needed
- File automatically saved

**Verify**:
- [ ] Config option works
- [ ] Auto-regenerate activates
- [ ] File is regenerated
- [ ] Changes are committed or staged

---

### Phase 5: Python Script Testing (20 minutes)

#### Test P1: Direct Script Execution

**Test P1.1: Help Output**

```bash
uv run /tmp/llmstxt-generator/scripts/generate_llmstxt.py --help
```

**Verify**:
- [ ] Help displays
- [ ] All options shown
- [ ] Usage examples provided
- [ ] Clear descriptions

---

**Test P1.2: Ollama Connection Check**

```bash
# With Ollama running
uv run /tmp/llmstxt-generator/scripts/generate_llmstxt.py

# Verify: Shows "✓ Connected to Ollama"
```

```bash
# Stop Ollama (stop the ollama serve terminal)
# Then run script again

uv run /tmp/llmstxt-generator/scripts/generate_llmstxt.py

# Verify: Shows error with helpful message
```

---

**Test P1.3: Model Detection**

```bash
uv run /tmp/llmstxt-generator/scripts/generate_llmstxt.py
```

**Verify**:
- [ ] Lists available models
- [ ] Suggests default model
- [ ] Can select from list
- [ ] Error if model not found

---

**Test P1.4: Project Analysis**

```bash
uv run /tmp/llmstxt-generator/scripts/generate_llmstxt.py --project ~/sample-project
```

**Verify**:
- [ ] Analyzes project structure
- [ ] Detects project type
- [ ] Finds documentation files
- [ ] Shows file count

---

**Test P1.5: Generation**

```bash
uv run /tmp/llmstxt-generator/scripts/generate_llmstxt.py \
  --project . \
  --model llama2 \
  --output ./test-llms.txt
```

**Verify**:
- [ ] Generates llms.txt
- [ ] Saves to specified path
- [ ] Output file is valid
- [ ] Shows success message

---

**Test P1.6: Verbose Output**

```bash
uv run /tmp/llmstxt-generator/scripts/generate_llmstxt.py \
  --project . \
  --verbose
```

**Verify**:
- [ ] Shows detailed output
- [ ] Displays prompt sent to Ollama
- [ ] Shows generation progress
- [ ] More information than default

---

### Phase 6: Integration Testing (20 minutes)

#### Test I1: End-to-End Workflow

**Workflow**: Generate → Validate → Edit → Regenerate

```bash
# Step 1: Generate
/llmstxt:generate

# Verify: File created, score displayed

# Step 2: Validate
/llmstxt:validate

# Verify: Quality report, suggestions shown

# Step 3: Edit
/llmstxt:edit --menu

# Add a section or improve descriptions
# Save changes

# Step 4: Validate again
/llmstxt:validate

# Verify: Score improved

# Step 5: Regenerate
/llmstxt:generate

# Choose to overwrite existing file
# Verify: New version created

# Step 6: Final validation
/llmstxt:validate

# Verify: Score is good (8.0+)
```

**Pass Criteria**:
- ✓ All steps complete without errors
- ✓ File persists through workflow
- ✓ Quality improves through iteration
- ✓ All commands work together

---

#### Test I2: Multi-Project Workflow

```bash
# Create project A
mkdir ~/project-a
echo "# Project A" > ~/project-a/README.md
/llmstxt:generate ~/project-a

# Create project B
mkdir ~/project-b
echo "# Project B" > ~/project-b/README.md
/llmstxt:generate ~/project-b

# Validate both
/llmstxt:validate ~/project-a/llms.txt
/llmstxt:validate ~/project-b/llms.txt
```

**Verify**:
- [ ] Can work with multiple projects
- [ ] Files don't interfere with each other
- [ ] Each has appropriate content

---

### Phase 7: Error & Edge Cases (15 minutes)

#### Test E1: Error Handling

**E1.1: Missing Ollama**

```bash
# Stop Ollama
# Run: /llmstxt:generate
# Verify: Clear error message with solution
```

**E1.2: Model Not Found**

```bash
/llmstxt:generate
# Select model that doesn't exist
# Verify: Error message lists available models
```

**E1.3: Missing Documentation**

```bash
# Create empty project
mkdir ~/empty-project
/llmstxt:generate ~/empty-project
# Verify: Handles gracefully
```

**E1.4: Existing File Overwrite**

```bash
# Generate once
/llmstxt:generate

# Generate again to same location
/llmstxt:generate
# Verify: Prompts before overwriting
```

---

#### Test E2: Edge Cases

**E2.1: Large Projects**

```bash
# Test with project with 50+ doc files
/llmstxt:generate ~/large-project
# Verify: Handles efficiently, completes in reasonable time
```

**E2.2: Special Characters**

```bash
# Project with special chars in names/paths
# Verify: Handles correctly (escaping, etc.)
```

**E2.3: Unicode Content**

```bash
# Docs with unicode/emoji characters
# Verify: Generated file handles correctly
```

---

### Phase 8: Performance Testing (10 minutes)

#### Test PE1: Generation Time

```bash
# Time different project sizes
time /llmstxt:generate ~/small-project
time /llmstxt:generate ~/large-project

# Record times
# Verify: Reasonable performance
```

**Expected Times**:
- Small project: 5-10 seconds
- Medium project: 10-15 seconds
- Large project: 15-30 seconds

---

#### Test PE2: Validation Speed

```bash
# Time validation
time /llmstxt:validate

# Record time
# Verify: Quick feedback (< 10 seconds without link checks)
```

**Expected Times**:
- Format check only: 100-500ms
- Full validation (with links): 5-10 seconds

---

## Test Results Template

```markdown
# Test Results - llmstxt-generator v0.1.0

## Date
2026-02-22

## Environment
- OS: [macOS/Linux/Windows]
- Python: 3.x.x
- Ollama: [version]
- Models: [list tested models]

## Skills Testing
- [x] llms-format-guide: PASS / FAIL
- [x] ollama-integration: PASS / FAIL

## Commands Testing
- [x] /llmstxt:generate: PASS / FAIL
- [x] /llmstxt:validate: PASS / FAIL
- [x] /llmstxt:edit: PASS / FAIL

## Agent Testing
- [x] llmstxt-analyzer: PASS / FAIL

## Hook Testing
- [x] post-commit: PASS / FAIL

## Script Testing
- [x] generate_llmstxt.py: PASS / FAIL

## Integration Testing
- [x] End-to-end workflow: PASS / FAIL
- [x] Multi-project workflow: PASS / FAIL

## Error Handling
- [x] Error cases: PASS / FAIL
- [x] Edge cases: PASS / FAIL

## Performance
- [x] Generation time: PASS / FAIL
- [x] Validation time: PASS / FAIL

## Overall: PASS / FAIL

## Notes
[Any observations, issues, or suggestions]
```

---

## Troubleshooting During Testing

### Command Not Found

**Problem**: `/llmstxt:generate` command not recognized

**Solution**:
- Verify plugin is in `~/.claude/plugins/`
- Restart Claude Code
- Check plugin.json is valid

### Ollama Connection Failed

**Problem**: "Cannot connect to Ollama"

**Solution**:
```bash
# Start Ollama
ollama serve

# Verify it's running
curl http://localhost:11434/api/tags
```

### Generation Takes Too Long

**Problem**: Generation timeout

**Solution**:
- Use faster model (mistral instead of llama2)
- Reduce project size
- Check system resources

### Validation Hangs on Links

**Problem**: Link validation stuck

**Solution**:
- Use `--no-links` flag to skip link checking
- Check internet connectivity
- Verify URLs are accessible

---

## Test Coverage Summary

| Area | Tests | Coverage |
|---|---|---|
| Skills | 2 | 100% |
| Commands | 3 | 100% |
| Agent | 1 | 100% |
| Hook | 1 | 100% |
| Script | 1 | 100% |
| Integration | 2 | 100% |
| Error Handling | 4 | 100% |
| Performance | 2 | 100% |

**Total Test Cases**: 50+
**Expected Pass Rate**: 95%+ (some environment-specific edge cases)

