# Agent Skills Validation Rules

This document provides a complete reference for validating Agent Skills against the official specification.

## SKILL.md Requirements

### File Location

- Must be named `SKILL.md` (uppercase preferred) or `skill.md` (lowercase accepted)
- Must be located in the root of the skill directory
- File must be UTF-8 encoded text

### YAML Frontmatter

**Structure:**
```yaml
---
name: skill-name
description: Description text
---
```

**Rules:**
- Must start with `---` on the first line
- Must end with `---` on its own line
- Must contain valid YAML (use YAML parsers to validate)
- Must be a YAML mapping (dictionary/object), not a list or scalar
- Content between `---` markers is parsed as YAML

**Common YAML Errors:**
```yaml
# ❌ Invalid: missing closing ---
---
name: test
description: test

# ❌ Invalid: list instead of mapping
---
- name: test
- description: test
---

# ✅ Valid: proper mapping structure
---
name: test
description: test
---
```

## Required Fields

### `name` Field

**Format Rules:**
- **Required**: Must be present
- **Length**: 1-64 characters (after NFKC normalization)
- **Characters**: Unicode lowercase letters, numbers, and hyphens only
  - Valid: `a-z`, `0-9`, `-`
  - Invalid: uppercase, spaces, underscores, special characters
- **Hyphens**: Cannot start or end with hyphen
- **Consecutive hyphens**: Cannot contain `--`
- **Normalization**: Names are NFKC normalized before validation

**Valid Examples:**
```yaml
name: pdf-processing
name: data-analysis
name: code-review
name: api-integration-v2
name: café  # Unicode characters allowed (normalized to NFC)
```

**Invalid Examples:**
```yaml
name: PDF-Processing        # ❌ Uppercase not allowed
name: -my-skill            # ❌ Cannot start with hyphen
name: my-skill-            # ❌ Cannot end with hyphen
name: my--skill            # ❌ Consecutive hyphens not allowed
name: my_skill             # ❌ Underscores not allowed
name: my skill             # ❌ Spaces not allowed
name: my.skill             # ❌ Dots not allowed
name:                      # ❌ Empty name not allowed
name: a-really-long-skill-name-that-exceeds-the-maximum-allowed-length  # ❌ Too long (>64 chars)
```

**Directory Name Matching:**
- The skill directory name MUST match the `name` field
- Both are NFKC normalized before comparison
- Example: If `name: my-skill`, directory must be named `my-skill/`

### `description` Field

**Format Rules:**
- **Required**: Must be present
- **Length**: 1-1024 characters
- **Type**: Non-empty string
- **Content**: Should describe what the skill does AND when to use it

**Good Descriptions:**
```yaml
# ✅ Specific and keyword-rich
description: Extracts text and tables from PDF files, fills PDF forms, and merges multiple PDFs. Use when working with PDF documents or when the user mentions PDFs, forms, or document extraction.

# ✅ Clear scope and triggers
description: Analyzes Python code for common bugs, security vulnerabilities, and style issues. Use when reviewing Python code, performing security audits, or enforcing coding standards.

# ✅ Includes context keywords
description: Creates professional slide presentations with charts and diagrams. Use when generating presentations, creating pitch decks, or visualizing data in slide format.
```

**Poor Descriptions:**
```yaml
# ❌ Too vague
description: Helps with PDFs.

# ❌ Doesn't explain when to use
description: This skill processes data and generates reports.

# ❌ Too technical/internal
description: Implements the PDF extraction pipeline using pdfplumber backend.

# ❌ Too long (over 1024 characters)
description: [1100 character rambling description...]

# ❌ Empty
description: 
```

## Optional Fields

### `license` Field

**Rules:**
- Optional
- String value
- No length limit specified
- Should reference a commonly known license identifier OR point to a bundled license file

**Examples:**
```yaml
license: Apache-2.0
license: MIT
license: Proprietary. See LICENSE.txt
license: BSD-3-Clause
```

### `compatibility` Field

**Rules:**
- Optional
- String value
- Maximum 500 characters
- Should describe environment requirements, platform needs, or tool dependencies

**When to Use:**
Use this field ONLY if your skill has specific requirements like:
- Specific agent products (e.g., "Designed for Claude Code")
- System dependencies (e.g., "Requires docker and jq")
- Network access needs
- Specific OS requirements

**Examples:**
```yaml
# ✅ Clear requirements
compatibility: Requires Python 3.8+, requests library, internet access

# ✅ Platform specification
compatibility: Designed for Claude Code (or similar products with filesystem access)

# ✅ System dependencies
compatibility: Requires git, docker, jq, and access to the internet

# ✅ Combined requirements
compatibility: macOS or Linux. Requires Python 3.9+, ollama installed, and GPU with 8GB+ VRAM
```

**Invalid:**
```yaml
# ❌ Too long (>500 chars)
compatibility: [550 character description...]
```

### `metadata` Field

**Rules:**
- Optional
- Must be a YAML mapping (dictionary)
- Keys must be strings
- Values must be strings
- Use for client-specific or custom properties not in the Agent Skills spec

**Examples:**
```yaml
metadata:
  author: john-doe
  version: "1.0.0"
  created: "2026-02-13"
  tags: api, integration, rest
  
metadata:
  org: example-corp
  team: platform-engineering
  cost-center: "12345"
  internal-id: skill-098
```

**Best Practices:**
- Use reasonably unique key names to avoid conflicts
- Store version info here if tracking versions
- Add tags or categories for organization
- Include author/maintainer information

### `allowed-tools` Field

**Rules:**
- Optional and **experimental**
- Space-delimited list of tool patterns
- Support varies between agent implementations
- Specifies pre-approved tools the skill may use

**Format:**
```yaml
allowed-tools: Bash(git:*) Bash(python3:*) Read Write
```

**Note:** This field is experimental. Most skills should not use it. Only include if you have specific tool restrictions to declare.

## Field Validation Summary

| Field | Required | Max Length | Valid Characters | Notes |
|-------|----------|------------|------------------|-------|
| `name` | Yes | 64 | `a-z`, `0-9`, `-` | Lowercase, no leading/trailing/consecutive hyphens |
| `description` | Yes | 1024 | Any | Non-empty string |
| `license` | No | None | Any | License identifier or file reference |
| `compatibility` | No | 500 | Any | Only if specific requirements exist |
| `metadata` | No | N/A | Mapping of string→string | Custom key-value pairs |
| `allowed-tools` | No | None | Space-delimited | Experimental, rarely used |

## Unknown Fields

**Rule:** Only the fields listed above are allowed in frontmatter.

**Invalid:**
```yaml
---
name: my-skill
description: My skill
author: Someone          # ❌ Use metadata.author instead
version: 1.0              # ❌ Use metadata.version instead
tags:                     # ❌ Use metadata.tags instead
  - api
  - integration
---
```

**Valid:**
```yaml
---
name: my-skill
description: My skill
metadata:
  author: Someone
  version: "1.0"
  tags: api, integration
---
```

## Directory Structure Validation

### Required

- `SKILL.md` (or `skill.md`) must exist in the skill root

### Optional Directories

If present, these should follow conventions:

**`scripts/`**
- Contains executable code
- Scripts should have clear names
- Include error handling and documentation

**`references/`**
- Contains additional documentation files
- Common files: `REFERENCE.md`, `FORMS.md`
- Keep files focused and under 1000 lines

**`assets/`**
- Contains templates, images, data files
- Should be referenced from SKILL.md or scripts/

### Forbidden

- No deeply nested skill directories
- No duplicate SKILL.md files in subdirectories
- Referenced files must exist (don't reference `scripts/missing.py`)

## Validation Checklist

Use this checklist when creating or reviewing a skill:

### Frontmatter
- [ ] File starts with `---`
- [ ] Frontmatter ends with `---`
- [ ] Valid YAML syntax
- [ ] `name` field present and valid format
- [ ] `description` field present and 1-1024 chars
- [ ] No unknown/disallowed fields (unless in `metadata`)

### Name Validation
- [ ] Name is 1-64 characters
- [ ] Name is all lowercase
- [ ] Name uses only letters, numbers, hyphens
- [ ] Name doesn't start or end with hyphen
- [ ] Name has no `--` consecutive hyphens
- [ ] Directory name matches frontmatter name

### Description Validation
- [ ] Description is non-empty
- [ ] Description explains what skill does
- [ ] Description explains when to use skill
- [ ] Description includes relevant keywords
- [ ] Description is under 1024 characters

### Optional Fields
- [ ] `license` is appropriate (if present)
- [ ] `compatibility` is under 500 chars (if present)
- [ ] `metadata` is a string→string mapping (if present)
- [ ] `allowed-tools` is space-delimited (if present)

### File Structure
- [ ] SKILL.md exists in root
- [ ] Referenced files exist
- [ ] Directory structure is clean and organized

## Automated Validation

Use the reference library or provided validation script:

**Python (skills-ref library):**
```python
from skills_ref import validate

errors = validate("path/to/skill")
if errors:
    for error in errors:
        print(f"❌ {error}")
else:
    print("✅ Valid skill!")
```

**Command Line:**
```bash
python scripts/validate_skill.py path/to/skill
```

**Reference Library Tool:**
```bash
skills-ref validate path/to/skill
```

## Common Validation Errors

### Error: "Missing required field in frontmatter: name"
- **Cause**: No `name` field in YAML frontmatter
- **Fix**: Add `name: your-skill-name` to frontmatter

### Error: "Skill name 'MySkill' must be lowercase"
- **Cause**: Name contains uppercase letters
- **Fix**: Change to `my-skill` (all lowercase)

### Error: "Skill name cannot start or end with a hyphen"
- **Cause**: Name is `-my-skill` or `my-skill-`
- **Fix**: Remove leading/trailing hyphens

### Error: "Skill name cannot contain consecutive hyphens"
- **Cause**: Name contains `--` like `my--skill`
- **Fix**: Use single hyphens only: `my-skill`

### Error: "Directory name doesn't match skill name"
- **Cause**: Directory is `my_skill/` but name is `my-skill`
- **Fix**: Rename directory to match: `my-skill/`

### Error: "Description exceeds 1024 character limit"
- **Cause**: Description is too long
- **Fix**: Shorten description, move details to SKILL.md body

### Error: "SKILL.md must start with YAML frontmatter (---)"
- **Cause**: File doesn't start with `---`
- **Fix**: Add frontmatter at the top of the file

### Error: "SKILL.md frontmatter not properly closed with ---"
- **Cause**: Missing closing `---` line
- **Fix**: Add `---` after your frontmatter fields

### Error: "Invalid YAML in frontmatter"
- **Cause**: YAML syntax error (indentation, colons, quotes)
- **Fix**: Validate YAML syntax, check for proper colons and indentation

## Testing Your Skill

After validation, test your skill:

1. **Read through as a human**: Does it make sense?
2. **Follow instructions literally**: Can you complete the task?
3. **Check examples**: Do they work as shown?
4. **Test edge cases**: What if inputs are unusual?
5. **Verify references**: Do linked files exist and help?

## Further Reading

- [Agent Skills Specification](https://agentskills.io/specification)
- [Reference Library](https://github.com/agentskills/agentskills/tree/main/skills-ref)
- [Validation Source Code](https://github.com/agentskills/agentskills/tree/main/skills-ref/src/skills_ref/validator.py)
