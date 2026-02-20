# Agent Skills Validation Rules

This document details validation requirements for Agent Skills based on the [official specification](https://agentskills.io/specification).

## Required: SKILL.md File

Every skill MUST contain a `SKILL.md` file at the root of the skill directory.

## YAML Frontmatter Requirements

### Format

```yaml
---
[YAML content]
---
```

- Must start with `---` on first line
- Must end with `---` on its own line
- Must be valid YAML syntax

### Required Fields

#### name

**Requirements:**
- **Type**: String
- **Length**: 1-64 characters
- **Format**: Lowercase letters (`a-z`), numbers (`0-9`), and hyphens (`-`) only
- **Constraints**:
  - Cannot start with hyphen
  - Cannot end with hyphen
  - Cannot contain consecutive hyphens (`--`)
  - Must be NFKC normalized
- **Directory Match**: Directory name must exactly match the skill name

**Valid Samples:**
```yaml
name: pdf-processing
name: data-analysis-v2
name: api-client
```

**Invalid Samples:**
```yaml
name: PDF-Processing      # Uppercase not allowed
name: -my-skill           # Cannot start with hyphen
name: my-skill-           # Cannot end with hyphen
name: my--skill           # Consecutive hyphens not allowed
name: my_skill            # Underscores not allowed
```

#### description

**Requirements:**
- **Type**: String
- **Length**: 1-1024 characters
- **Content**: Non-empty string

**Best Practices:**
- Describe BOTH what the skill does AND when to use it
- Include specific keywords that help agents identify relevant tasks
- Be concise but comprehensive

**Good Example:**
```yaml
description: Extract text and tables from PDF files, fill PDF forms, merge documents. Use when working with PDFs, forms, or document extraction.
```

**Poor Example:**
```yaml
description: Helps with PDFs.  # Too vague, missing keywords
```

### Repository-level LICENSE File

**Requirements:**
- LICENSE file must exist at repository root (NOT in the skill package folder)
- Must be an industry-standard, open-source license from https://opensource.org/licenses
- Must be complete and unmodified from the authoritative source
- All placeholders must be filled in (copyright holder, year, company name, etc.)

**Common License Choices:**

**MIT License (Most Common)**
```
File: LICENSE (at repository root)
- Simplest open-source license
- Minimal restrictions on use
- Recommended for most public skills
- Get template: https://opensource.org/licenses/MIT
- SPDX identifier: MIT
```

**Apache License 2.0**
```
File: LICENSE (at repository root)
- Like MIT but includes patent protection
- Good for enterprise/commercial projects
- Slightly more restrictive
- Get template: https://opensource.org/licenses/Apache-2.0
- SPDX identifier: Apache-2.0
```

**GPL v2 or v3 (Copyleft)**
```
File: LICENSE (at repository root)
- Requires derivatives to be open source
- Stronger open-source commitment
- Get template: https://www.gnu.org/licenses/
- SPDX identifier: GPL-2.0-only or GPL-3.0-only
```

**License Compatibility & Attribution**

**Verify compatibility with source materials:**
- [ ] Check license of ALL resources used (dependencies, code samples, documentation)
- [ ] Verify no license conflicts:
  - MIT → Can go into any open-source project ✓
  - Apache 2.0 → Can go into MIT projects (with attribution) ✓
  - GPL → Requires entire project to be GPL ✗ (unless exception)
  - Proprietary → Cannot redistribute without permission ✗
- [ ] Use https://choosealicense.com/appendix/ for compatibility matrix
- [ ] Document all source licenses in README "Attribution" section

**Attribution for Derived or Reused Code:**
```markdown
## Attribution

- [Component/Code]: Original source URL, licensed under [License]
  - Original author: [Author Name]
  - Changes: [What was changed/adapted]
```

**Validation Checklist for Repository LICENSE:**
```
✓ LICENSE file exists at repository root
✓ LICENSE is NOT in skill package subfolder
✓ License text is from authoritative source (opensource.org)
✓ License text is complete (no lines removed)
✓ Copyright year filled in (e.g., 2026)
✓ Copyright holder name filled in
✓ README.md mentions license type
✓ README.md has "Attribution" section for source materials
✓ All dependencies' licenses verified for compatibility
✓ CHANGELOG.md first entry mentions license choice
✓ License type documented in GitHub/GitLab settings if applicable
```

**Where to Get Authoritative License Templates:**
- https://opensource.org/licenses/ (Official OSI licenses)
- https://choosealicense.com/ (Interactive license selector)
- https://github.com/licenses/license-templates (GitHub's official templates)
- https://www.gnu.org/licenses/ (GPL licenses)

**Common License Errors to Avoid:**
- ❌ Using modified/altered LICENSE text (must be original)
- ❌ Forgetting to fill in copyright holder name
- ❌ Including LICENSE in skill package (should be in repository root only)
- ❌ Using GPL code without GPL license
- ❌ Using proprietary code without explicit permission
- ❌ Forgetting to document source material licenses
- ❌ License file named differently (should be LICENSE, not LICENSE.md or LICENSE.txt)

### Optional Fields

⚠️ **Important Note:** Per the Agent Skills specification, do NOT include optional fields in SKILL.md frontmatter. Only `name` and `description` should be in the YAML frontmatter.

Repository-level documentation (README.md, LICENSE, CHANGELOG.md) should be managed separately from the skill package and configured at the repository level, not in frontmatter.

The following samples show obsolete patterns that are NO LONGER RECOMMENDED:

#### license (DEPRECATED - Use repository-level LICENSE file)

**Note**: License information should be managed in a repository-level LICENSE file, not in the skill package YAML frontmatter.

#### compatibility (DEPRECATED - Rarely used)

**Samples:**
```yaml
compatibility: Requires Python 3.8+, requests library
compatibility: Designed for Claude Code (or similar products)
compatibility: Requires git, docker, jq, and internet access
```

#### metadata

**Requirements:**
- **Type**: Map (string keys to string values)
- Keys should be reasonably unique to avoid conflicts

**Example:**
```yaml
metadata:
  author: example-org
  version: "1.0.0"
  tags: api, integration
```

#### allowed-tools

**Requirements:**
- **Type**: Space-delimited list of tools
- **Status**: Experimental - support may vary

**Example:**
```yaml
allowed-tools: Bash(git:*) Bash(jq:*) Read Write
```

## Directory Structure Validation

### Skill Root

- **Required**: Directory name must match `name` field exactly
- **Required**: Must contain `SKILL.md` file

### Optional Directories

These are allowed but not required:

- `scripts/` - Executable code
- `references/` - Additional documentation
- `assets/` - Templates, images, data files

**No restrictions** on file organization within optional directories.

## File References

When referencing other files from SKILL.md:

- Use relative paths from skill root
- Keep references "one level deep" - avoid nested chains
- Ensure referenced files exist

**Samples:**
```markdown
See `references/API.md` for details.          ✓ Good
Run `scripts/process.py` to extract data.     ✓ Good
See `scripts/helpers/utils.py`                 ⚠ Acceptable but deeper
```

## Validation Tool

Use the official [skills-ref library](https://github.com/agentskills/agentskills/tree/main/skills-ref):

```bash
# Install
pip install -e git+https://github.com/agentskills/agentskills.git#egg=skills-ref&subdirectory=skills-ref

# Validate
skills-ref validate /path/to/skill

# Read properties
skills-ref read-properties /path/to/skill

# Generate prompt XML
skills-ref to-prompt /path/to/skill
```

## Common Validation Errors

### Error: Name doesn't match directory

```
Error: Directory name 'PDF-Processing' doesn't match skill name 'pdf-processing'
```

**Fix**: Rename directory to match the `name` field exactly.

### Error: Invalid name format

```
Error: Name 'my_skill' contains invalid characters
```

**Fix**: Use only lowercase letters, numbers, and hyphens.

### Error: Description too long

```
Error: Description exceeds 1024 characters
```

**Fix**: Shorten description or move details to SKILL.md body.

### Error: Missing required field

```
Error: Missing required field 'description'
```

**Fix**: Add the missing field to frontmatter.

### Error: Invalid YAML

```
Error: YAML frontmatter is not valid
```

**Fix**: Check for:
- Proper indentation (use spaces, not tabs)
- Unclosed quotes
- Invalid characters
- Missing closing `---`

## Progressive Disclosure Guidelines

While not strictly validated, follow these for performance:

- **Metadata**: ~50-100 tokens (name + description)
- **SKILL.md**: < 500 lines recommended (~5000 tokens), warn at 450
- **References**: 200-800 lines optimal, warn at 800, hard limit 1000
- Keep file references shallow (one level from SKILL.md)
- Proactively split files before exceeding limits

## Validation Checklist

Use this checklist before sharing your skill:

- [ ] SKILL.md exists at root
- [ ] YAML frontmatter starts and ends with `---`
- [ ] `name` field matches directory name
- [ ] `name` is 1-64 chars, lowercase, hyphens only
- [ ] `name` doesn't start/end with hyphen
- [ ] `name` has no consecutive hyphens
- [ ] `description` is 1-1024 characters
- [ ] `description` explains what and when
- [ ] `description` includes relevant keywords
- [ ] All referenced files exist
- [ ] SKILL.md is under 500 lines (warn at 450)
- [ ] Reference files under 1000 lines (warn at 800, split proactively)
- [ ] No files exceed 1000 lines without justification
- [ ] Runs `skills-ref validate` without errors

## Resources

- [Agent Skills Specification](https://agentskills.io/specification)
- [skills-ref Library](https://github.com/agentskills/agentskills/tree/main/skills-ref)
- [Integration Guide](https://agentskills.io/integrate-skills)
