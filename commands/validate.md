---
description: Validate and score an existing llms.txt file
argument-hint: "[optional: path-to-llms.txt]"
allowed-tools:
  - Read
  - Bash
  - Grep
---

# /llmstxt:validate

Validate an existing llms.txt file against the llmstxt.org specification. Checks format compliance, tests link accessibility, scores quality, and provides improvement suggestions.

## What This Does

1. **Format Validation** - Checks Markdown structure and format compliance
2. **Link Validation** - Tests if all URLs are accessible (HTTP requests)
3. **Quality Scoring** - Rates description clarity, structure organization, completeness
4. **Recommendations** - Suggests improvements to boost quality

## Usage

### Validate Current Directory

```bash
/llmstxt:validate
```

Looks for `./llms.txt` or `./docs/llms.txt` automatically.

### Validate Specific File

```bash
/llmstxt:validate /path/to/llms.txt
```

### Validate with Verbose Output

```bash
/llmstxt:validate --verbose
```

Shows detailed analysis including all link checks.

## Output Example

```
📄 Validating: ./llms.txt

════════════════════════════════════════════════════════════════

✅ FORMAT COMPLIANCE

[✓] H1 Title Present
    "# FastHTML" found at line 1

[✓] Blockquote Summary
    ">" summary found: "FastHTML is a Python library..."
    Length: 142 characters (Good - concise but informative)

[✓] Markdown Structure
    - H1 headings: 1 ✓
    - H2 sections: 5 ✓
    - Link format: 25/25 valid ✓
    - No mixed indentation ✓

[✓] Link Format
    - All links properly formatted: [text](url)
    - Total links: 25
    - External links: 8
    - Internal links: 17

════════════════════════════════════════════════════════════════

🔗 LINK VALIDATION

[✓] All URLs Accessible

  ✓ https://www.fastht.ml/docs/installation.html (200 OK)
  ✓ https://www.fastht.ml/docs/quickstart.html (200 OK)
  ✓ https://fastcore.fast.ai/xt_mimic.html (200 OK)
  ✓ https://github.com/AnswerDotAI/fasthtml (200 OK)
  ...
  ✓ https://llmstxt.org/ (200 OK)

  Failed/Slow: 0
  Total checked: 25
  Success rate: 100%

Timing:
  Fastest: 45ms
  Slowest: 892ms
  Average: 234ms

════════════════════════════════════════════════════════════════

⭐ QUALITY SCORING

Description Clarity: 8.5/10
  Analyzed: 25 link descriptions
  Average length: 68 characters (optimal: 60-100)
  ✓ All descriptions are specific and informative
  ⚠️  3 descriptions could be more specific

Example descriptions:
  ✓ "Setup instructions for development and production"
  ✓ "10-minute introduction with examples"
  ⚠️  "Starlette web framework" (Could add: "...used by FastHTML")

Structure Organization: 9.2/10
  ✓ Logical section progression
  ✓ Well-balanced links per section (4-6 per section)
  ✓ Clear relationship between sections
  ⚠️  Could add "Architecture" section

Link Distribution: 8.8/10
  Getting Started: 2 links ✓
  Core Concepts: 6 links ✓
  API Reference: 8 links ✓
  Examples: 4 links ✓
  Optional: 5 links ✓
  Balance: Good (well distributed)

Completeness: 8.0/10
  ✓ Has blockquote summary
  ✓ Has "Optional" section
  ✓ Covers main documentation
  ⚠️  Missing GitHub repository link
  ⚠️  Could include troubleshooting section

External Resources: 7.5/10
  Internal docs: 17 links
  External references: 8 links (32% external - Good!)
  ⚠️  Could link to HTMX official docs (currently missing)

═══════════════════════════════════════════════════════════════

📊 OVERALL SCORE: 8.5/10 ⭐ Excellent

Categories:
  Format Compliance: 10/10 ✓ Perfect
  Link Validation:   10/10 ✓ All working
  Quality:           8.5/10 ✓ Very good
  Completeness:      8.0/10 ✓ Good
  Organization:      9.2/10 ✓ Excellent

═══════════════════════════════════════════════════════════════

💡 IMPROVEMENT SUGGESTIONS

High Priority:
  1. Add GitHub repository link
     → Why: Users often want to view source code
     → Add to "Core Concepts" or new "Community" section
     → Link: https://github.com/AnswerDotAI/fasthtml

  2. Link to official HTMX documentation
     → Why: HTMX is core to FastHTML
     → Enhance section: Core Concepts
     → Link: https://htmx.org/reference/

Medium Priority:
  3. Add "Troubleshooting" section
     → Why: Common for developers
     → Suggested links: FAQ, GitHub Issues, Discord
     → Estimated impact: +0.8/10 to score

  4. Enhance 3 descriptions for clarity
     → "Starlette web framework" → "Starlette: web framework providing routing and middleware"
     → Estimated impact: +0.5/10 to score

Low Priority:
  5. Consider "Architecture" section
     → Why: Power users want to understand internals
     → Place in "Optional" for token efficiency
     → Estimated impact: +0.3/10 to score

═══════════════════════════════════════════════════════════════

✅ VALIDATION REPORT

Status: PASSED ✓

  ✓ Format: Fully compliant with llmstxt.org spec
  ✓ Links: All 25 URLs verified and working
  ✓ Quality: Excellent (8.5/10)
  ✓ Recommendations: 5 suggestions to improve

Next Steps:
  1. Review high-priority suggestions above
  2. Edit with: /llmstxt:edit
  3. Regenerate with: /llmstxt:generate
  4. Share context with Claude for questions

═══════════════════════════════════════════════════════════════

Report Generated: 2026-02-22 at 21:35 UTC
Validation Time: 4.2 seconds
```

## Quality Metrics Explained

### Description Clarity (0-10)

Evaluates if link descriptions are:
- **Specific**: "OAuth2, API keys, JWT" vs "Authentication"
- **Informative**: Tells reader what's in the link
- **Concise**: Under 100 characters
- **Actionable**: Helps user decide if they need it

```markdown
# Good (9/10)
- [Authentication Guide](URL): OAuth2, API keys, JWT, session management

# Fair (6/10)
- [Auth](URL): How to authenticate

# Poor (3/10)
- [Stuff](URL): Different methods
```

### Structure Organization (0-10)

Evaluates:
- **Logical flow**: Sections progress from basic to advanced
- **Balance**: Even distribution of links per section
- **Naming**: Clear, descriptive section names
- **Hierarchy**: Clear relationship between sections

Good structure:
1. Getting Started (intro)
2. Core Concepts (fundamentals)
3. API Reference (detailed)
4. Examples (practical)
5. Optional (supplementary)

### Link Distribution (0-10)

Evaluates balance:
- Too few total links (< 5): Incomplete
- Too many per section (> 15): Overwhelming
- Uneven distribution: 1 link in one section, 20 in another

Ideal:
- Total links: 15-30
- Per section: 4-8 links
- All sections represented

### Completeness (0-10)

Checks for expected elements:
- [ ] H1 title
- [ ] Blockquote summary
- [ ] Multiple sections
- [ ] "Optional" section
- [ ] External resources
- [ ] Examples/tutorials
- [ ] API reference

### External Resources (0-10)

Evaluates link distribution:
- **Internal only** (0/10): Missing outside perspectives
- **Mostly internal** (5/10): Limited external references
- **Balanced** (8-10/10): Mix of internal docs and external standards

Ideal: 20-30% external links (standards, other projects, GitHub, etc.)

## Common Issues and Fixes

### ❌ Issue: Low Description Clarity

**Problem**: Descriptions are vague
```markdown
- [Docs](URL): Documentation
- [API](URL): API stuff
```

**Fix**: Be specific
```markdown
- [REST API Reference](URL): Endpoints, authentication, error codes
- [GraphQL API](URL): Schema, queries, mutations
```

### ❌ Issue: Broken Links

**Problem**: Some URLs return 404 or timeout
```
✗ https://old-docs.example.com/api (404 Not Found)
✗ https://example.com/slow-page (timeout after 10s)
```

**Fix**: Update or remove broken links
```bash
/llmstxt:edit
# Then select and fix/remove broken links
```

### ❌ Issue: Poor Organization

**Problem**: Links seem randomly distributed
- Section 1: 1 link
- Section 2: 15 links
- Section 3: 2 links

**Fix**: Reorganize with balanced sections
```bash
/llmstxt:generate
# Regenerate for better organization
```

### ❌ Issue: Missing Important Links

**Problem**: Score low for completeness - missing GitHub, examples, etc.

**Fix**: Add missing resources
```bash
/llmstxt:edit
# Use CLI menu to add sections and links
```

## Validation Flags

### `--verbose` or `-v`

Shows detailed analysis:
```bash
/llmstxt:validate --verbose

# Includes:
# - Line-by-line format checks
# - Individual link HTTP headers
# - Full text of each description
# - Detailed quality analysis
```

### `--no-links` or `-n`

Skip HTTP link checking (faster):
```bash
/llmstxt:validate --no-links

# Skips:
# - HTTP requests to URLs
# - Accessibility checks
# - Response times

# Still checks:
# - Format compliance
# - Quality scoring
# - Structure validation
```

### `--compare` or `-c`

Compare against another llms.txt:
```bash
/llmstxt:validate --compare ./docs/llms.txt

# Shows:
# - Differences in structure
# - Link count comparison
# - Quality score delta
# - Style differences
```

## Interpreting Scores

### Overall Score Ranges

| Score | Rating | Meaning |
|---|---|---|
| 9.0-10.0 | 🟢 Excellent | Production-ready, high quality |
| 8.0-8.9 | 🟢 Very Good | Minor improvements possible |
| 7.0-7.9 | 🟡 Good | Some improvements suggested |
| 6.0-6.9 | 🟡 Fair | Consider suggested improvements |
| < 6.0 | 🔴 Needs Work | Major issues to address |

### What Score Means for Use

- **8.5+**: Ready for production and sharing with users
- **7.5-8.4**: Good, but consider implementing suggestions
- **6.5-7.4**: Will work, but improvements recommended
- **5.5-6.4**: Needs work before using in production
- **< 5.5**: Regenerate or substantially edit

## Tips & Best Practices

### 1. Validate After Editing

```bash
# Edit your llms.txt
/llmstxt:edit

# Then validate to see improvements
/llmstxt:validate

# Repeat until score is 8.0+
```

### 2. Monitor Link Health Regularly

```bash
# Weekly link check (especially for external links)
/llmstxt:validate --no-links  # Fast format check
/llmstxt:validate             # Full validation monthly
```

### 3. Use Suggestions as Roadmap

Priority suggestions by impact:
- **High**: Implement these first (biggest score improvement)
- **Medium**: Good to have
- **Low**: Nice to have

### 4. Track Score Over Time

Keep validation history:
```bash
# Save validation reports
/llmstxt:validate > validation-report-2026-02-22.txt

# Compare reports over time to track quality trends
```

## Related Commands

- **`/llmstxt:generate`** - Create new llms.txt
- **`/llmstxt:edit`** - Edit existing llms.txt
- **`/skill llms-format-guide`** - Understand the format

## See Also

- **llmstxt Specification**: https://llmstxt.org
- **Quality Standards**: Built on llmstxt.org guidelines
- **Link Validation**: HTTP/HTTPS checking for accessibility
