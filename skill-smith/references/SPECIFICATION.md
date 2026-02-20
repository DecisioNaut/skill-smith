# Agent Skills Specification Summary

Complete, authoritative specification: [https://agentskills.io/specification](https://agentskills.io/specification)

## Table of Contents

- [What is an Agent Skill?](#what-is-an-agent-skill)
- [Core Concepts](#core-concepts)
- [Directory Structure](#directory-structure)
- [SKILL.md Format](#skillmd-format)
- [Optional Directories](#optional-directories)
- [File References](#file-references)
- [Integration with Agents](#integration-with-agents)
- [Best Practices](#best-practices)
- [Validation](#validation)
- [Related Resources](#related-resources)
- [Quick Reference](#quick-reference)

## What is an Agent Skill?

An **Agent Skill** is a directory containing instructions, scripts, and resources that teach AI agents how to perform specific tasks. Skills use **progressive disclosure** to load only what's needed, when it's needed.

## Core Concepts

### Progressive Disclosure

```
┌─────────────────────────────────────────────┐
│ Startup: Load name + description (~100 tokens) │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ Activation: Load full SKILL.md (~5000 tokens)  │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ Deep Dive: Load references/scripts on demand   │
└─────────────────────────────────────────────┘
```

This approach keeps agents fast while providing deep knowledge when needed.

## Directory Structure

### Minimal (Required)

```
my-skill/
└── SKILL.md          # Required: metadata + instructions
```

### Full Structure (All Optional)

```
my-skill/
├── SKILL.md          # Required: metadata + instructions (< 500 lines)
├── scripts/          # Optional: executable code
│   ├── process.py
│   └── validate.sh
├── references/       # Optional: detailed docs (loaded on demand)
│   ├── API.md
│   ├── SAMPLES.md
│   └── ERRORS.md
├── assets/           # Optional: templates, data, images
│   ├── templates/
│   │   └── config.yaml
│   └── diagrams/
│       └── workflow.png
├── README.md         # Recommended: user-facing docs
└── LICENSE           # Recommended: license info
```

## SKILL.md Format

### Structure

```markdown
---
[YAML Frontmatter]
---

[Markdown Body]
```

### Frontmatter Fields

#### Required

| Field | Type | Constraints |
|-------|------|-------------|
| `name` | string | 1-64 chars, lowercase + hyphens only, must match directory name |
| `description` | string | 1-1024 chars, describes what and when |

#### Optional

| Field | Type | Notes |
|-------|------|-------|
| `license` | string | License identifier or file reference |
| `compatibility` | string | 1-500 chars, environment requirements |
| `metadata` | map | String key-value pairs for custom data |
| `allowed-tools` | string | Space-delimited list (experimental) |

### Example Frontmatter

```yaml
---
name: api-integration
description: Integrate with REST APIs including authentication, request handling, and error management. Use when connecting to web services, APIs, or when user mentions REST, HTTP requests, API calls.
license: MIT
metadata:
  version: "1.0.0"
  author: example-org
compatibility: Requires curl or HTTP client library
allowed-tools: Bash(curl:*) Read Write
---
```

### Body Content

The Markdown body contains instructions for agents. **No format restrictions** - write whatever helps agents perform the task.

**Recommended sections:**
- What the skill does
- When to use it
- Prerequisites
- Step-by-step instructions
- Samples with inputs/outputs
- Common edge cases
- Troubleshooting

**Key principle**: Keep SKILL.md < 500 lines. Move detailed material to `references/`.

## Optional Directories

### scripts/

Contains executable code that agents can run.

**Guidelines:**
- Self-contained or clearly document dependencies
- Include helpful error messages
- Handle edge cases gracefully
- Supported languages: Python, Bash, JavaScript (depends on agent)

**Example:**
```python
#!/usr/bin/env python3
"""Extract data from API and format as JSON."""

import sys
import requests

def main():
    if len(sys.argv) < 2:
        print("Usage: extract.py <api-url>")
        sys.exit(1)
    # ... implementation
```

### references/

Contains additional documentation loaded on demand.

**Common files:**
- `REFERENCE.md` - Complete API/technical documentation
- `SAMPLES.md` - Extended samples
- `ERRORS.md` - Error codes and handling
- Domain-specific: `AUTH.md`, `DATABASE.md`, etc.

**Guidelines:**
- Keep files focused (< 1000 lines each)
- One topic per file
- Reference from SKILL.md with relative paths

**Example reference:**
```markdown
<!-- In SKILL.md -->
For complete API documentation, see `references/API.md`.
For authentication details, see `references/AUTH.md`.
```

### assets/

Contains static resources.

**Common contents:**
- Templates (configuration, documents)
- Images (diagrams, screenshots)
- Data files (schemas, lookup tables)
- Sample data for testing

**Example:**
```
assets/
├── templates/
│   ├── config.yaml.template
│   └── report.md.template
├── diagrams/
│   └── auth-flow.png
└── data/
    └── test-dataset.json
```

## File References

When referencing files from SKILL.md:

```markdown
✓ Good: See `references/API.md` for details
✓ Good: Run `scripts/process.py` to extract
⚠ Acceptable: See `references/auth/oauth.md`
✗ Avoid: Deep nesting (SKILL.md → REF1 → REF2 → REF3)
```

**Keep references "one level deep"** from SKILL.md for clarity.

## Integration with Agents

### Discovery

Agents scan configured directories (typically `.agents/skills/`) for folders containing `SKILL.md` files.

### Loading Metadata

At startup, agents parse only the frontmatter to build a skill catalog:

```xml
<available_skills>
  <skill>
    <name>api-integration</name>
    <description>Integrate with REST APIs...</description>
    <location>/path/to/.agents/skills/api-integration/SKILL.md</location>
  </skill>
</available_skills>
```

### Activation

When a task matches a skill's description, the agent loads the full SKILL.md into context and follows the instructions.

### Execution

As needed, the agent:
- Reads referenced files (`references/*.md`)
- Executes scripts (`scripts/*.py`)
- Uses assets (`assets/templates/*`)

## Best Practices

### For Performance

- Keep SKILL.md under 500 lines
- Use progressive disclosure (move details to references/)
- Keep file references shallow

### For Clarity

- Write for literal interpretation
- Include concrete samples
- Note edge cases explicitly
- Provide complete error handling

### For Compatibility

- Follow naming rules strictly
- Use standard file formats
- Document dependencies clearly
- Test with multiple agents if possible

## Validation

Use the official validation tool:

```bash
skills-ref validate /path/to/skill
```

This checks:
- Frontmatter validity
- Required field presence
- Name format rules
- Description length
- File existence

## Related Resources

- **Specification**: [https://agentskills.io/specification](https://agentskills.io/specification)
- **Integration Guide**: [https://agentskills.io/integrate-skills](https://agentskills.io/integrate-skills)
- **Example Skills**: [https://github.com/anthropics/skills](https://github.com/anthropics/skills)
- **skills-ref Library**: [https://github.com/agentskills/agentskills/tree/main/skills-ref](https://github.com/agentskills/agentskills/tree/main/skills-ref)
- **Best Practices**: See `BEST_PRACTICES.md` in this directory

## Quick Reference

| Aspect | Guideline |
|--------|-----------|
| **Skill name** | 1-64 chars, lowercase + hyphens, matches directory |
| **Description** | 1-1024 chars, what + when + keywords |
| **SKILL.md size** | < 500 lines recommended |
| **Reference files** | < 1000 lines each recommended |
| **File references** | Keep "one level deep" from SKILL.md |
| **Metadata load** | ~50-100 tokens |
| **SKILL.md load** | ~5000 tokens |
| **Validation** | Use `skills-ref validate` |
