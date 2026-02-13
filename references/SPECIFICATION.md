# Agent Skills Specification Summary

This document summarizes the official [Agent Skills specification](https://agentskills.io/specification). For the complete, authoritative specification, refer to the official documentation.

## What is an Agent Skill?

An Agent Skill is a **directory** containing instructions, scripts, and resources that teach agents how to perform specific tasks. The core is a `SKILL.md` file with YAML frontmatter and Markdown instructions.

**Key Characteristics:**
- **Portable**: Works across different skills-compatible agents
- **Self-documenting**: Readable by humans and agents
- **Modular**: One skill, one well-defined capability
- **Versioned**: Can be tracked with git, published to repositories
- **Progressive**: Loads only what's needed, when it's needed

## Directory Structure

### Minimal Structure

```
my-skill/
└── SKILL.md          # Required
```

### Full Structure (All Optional Components)

```
my-skill/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
│   ├── main.py
│   └── helper.sh
├── references/       # Optional: detailed documentation
│   ├── REFERENCE.md
│   ├── FORMS.md
│   └── api_docs.md
├── assets/           # Optional: templates, data, images
│   ├── templates/
│   │   └── config.yaml
│   └── diagrams/
│       └── workflow.png
├── README.md         # Recommended: user-facing documentation
└── LICENSE           # Recommended: license information
```

## SKILL.md Format

### Structure

```markdown
---
[YAML frontmatter]
---

[Markdown body]
```

### Required Frontmatter Fields

#### name

**Format:**
- 1-64 characters
- Lowercase letters, numbers, hyphens only (`a-z`, `0-9`, `-`)
- Cannot start or end with hyphen
- Cannot contain consecutive hyphens (`--`)
- Must match parent directory name
- NFKC normalized

**Examples:**
```yaml
name: pdf-processing        # ✅ Valid
name: data-analysis-v2      # ✅ Valid
name: PDF-Processing        # ❌ Invalid: uppercase
name: my--skill             # ❌ Invalid: consecutive hyphens
```

#### description

**Format:**
- 1-1024 characters
- Non-empty string
- Should describe what the skill does AND when to use it
- Should include relevant keywords for discovery

**Example:**
```yaml
description: Extract text and tables from PDF files, fill PDF forms, merge documents. Use when working with PDFs, forms, or document extraction.
```

### Optional Frontmatter Fields

#### license

**Format:**
- String (no length limit)
- License identifier or reference to license file

**Examples:**
```yaml
license: Apache-2.0
license: MIT
license: Proprietary. See LICENSE.txt
```

#### compatibility

**Format:**
- String, max 500 characters
- Describes environment requirements
- Only include if specific requirements exist

**Examples:**
```yaml
compatibility: Requires Python 3.8+, requests library, internet access
compatibility: Designed for Claude Code (or similar products)
```

#### metadata

**Format:**
- YAML mapping (dictionary)
- Keys and values must be strings
- Used for client-specific or custom properties

**Example:**
```yaml
metadata:
  author: jane-doe
  version: "1.0.0"
  tags: api, integration
```

#### allowed-tools

**Format:**
- Space-delimited list of tool patterns
- Experimental field
- Support varies between agents

**Example:**
```yaml
allowed-tools: Bash(git:*) Bash(python3:*) Read Write
```

### Markdown Body

**No specific restrictions.** Write whatever helps agents perform the task effectively.

**Recommended sections:**
- Overview or introduction
- When to use this skill
- Prerequisites and requirements
- Step-by-step instructions
- Examples with inputs and outputs
- Troubleshooting and common errors
- References to additional files

**Best practices:**
- Keep under 500 lines (move details to `references/`)
- Use clear headings for navigation
- Include concrete examples
- Address edge cases explicitly
- Link to related files with relative paths

## Optional Directories

### scripts/

**Purpose:** Executable code that agents can run

**Guidelines:**
- Self-contained or clearly document dependencies
- Include helpful error messages
- Handle edge cases gracefully
- Name files descriptively

**Supported languages:** Depends on agent implementation. Common: Python, Bash, JavaScript

**Example:**
```
scripts/
├── extract_data.py       # Python data extraction
├── process.sh            # Bash pipeline
└── validate_schema.js    # JavaScript validator
```

### references/

**Purpose:** Additional documentation loaded on demand

**Common files:**
- `REFERENCE.md` - Detailed technical reference
- `FORMS.md` - Form templates, structured data formats
- Domain-specific files (`api.md`, `database.md`, etc.)

**Guidelines:**
- Keep files focused (one topic per file)
- Aim for under 1000 lines per file
- Use clear headings for navigation
- Reference from SKILL.md with relative paths

**Example:**
```
references/
├── REFERENCE.md      # Complete API documentation
├── FORMS.md          # JSON schemas, templates
├── ERRORS.md         # Error code reference
└── GLOSSARY.md       # Domain terminology
```

### assets/

**Purpose:** Static resources like templates, images, data

**Common contents:**
- Templates (document templates, config templates)
- Images (diagrams, screenshots, examples)
- Data files (lookup tables, schemas, sample data)

**Example:**
```
assets/
├── templates/
│   ├── config.yaml.template
│   └── report.md.template
├── diagrams/
│   └── architecture.png
└── sample_data/
    └── test_dataset.json
```

## Progressive Disclosure Model

Skills use a three-stage loading pattern:

### 1. Discovery (Startup)

**What's loaded:** `name` and `description` only

**When:** Agent starts up

**Purpose:** Agent knows what skills exist without loading full content

**Typical format (XML for Claude):**
```xml
<available_skills>
  <skill>
    <name>pdf-processing</name>
    <description>Extract text and tables from PDFs...</description>
    <location>/path/to/skill/SKILL.md</location>
  </skill>
</available_skills>
```

### 2. Activation (Task Matched)

**What's loaded:** Full `SKILL.md` body

**When:** Agent determines skill is relevant to current task

**Purpose:** Agent reads complete instructions

**How:** Agent reads file at `<location>` path

### 3. Execution (As Needed)

**What's loaded:** Referenced files (scripts, references, assets)

**When:** Instructions direct agent to access specific files

**Purpose:** Deep dive into details or execute code

**How:** Agent reads/executes files referenced in SKILL.md

## File References

**Use relative paths from skill root:**

```markdown
<!-- In SKILL.md -->
See API documentation in `references/REFERENCE.md` for details.

Run the extraction script:
```bash
python scripts/extract_data.py
```

Load the template:
```bash
cp assets/templates/config.yaml.template config.yaml
```
```

**Best practices:**
- Keep references one level deep
- Don't create deep nesting (avoid `references/subsection/detail/file.md`)
- Ensure referenced files exist
- Use descriptive link text

## Validation

### Using skills-ref Library

**Install:**
```bash
pip install skills-ref
```

**Validate a skill:**
```bash
skills-ref validate /path/to/skill
```

**Read properties:**
```bash
skills-ref read-properties /path/to/skill
```

**Generate prompt XML:**
```bash
skills-ref to-prompt /path/to/skill-a /path/to/skill-b
```

### Python API

```python
from pathlib import Path
from skills_ref import validate, read_properties, to_prompt

# Validate
errors = validate(Path("my-skill"))
if errors:
    for error in errors:
        print(f"❌ {error}")
else:
    print("✅ Valid!")

# Read properties
props = read_properties(Path("my-skill"))
print(f"{props.name}: {props.description}")

# Generate prompt
xml = to_prompt([Path("my-skill")])
print(xml)
```

## Integration with Agents

### For Filesystem-Based Agents

**Skills as files:**
- Skills exist in directories on filesystem
- Agent uses shell commands to access them: `cat /path/to/skill/SKILL.md`
- Scripts run via shell: `python /path/to/skill/scripts/main.py`

**Advantages:**
- Most capable option
- Natural file operations
- Easy script execution

### For Tool-Based Agents

**Skills via tools:**
- Skills accessed through custom tools
- Agent calls `activate_skill(name)` or similar
- Implementation-specific

**Advantages:**
- Works without filesystem access
- Can add sandboxing/security controls
- Portable across environments

## Security Considerations

### For Skill Authors

- **Don't hardcode secrets**: Use environment variables
- **Validate inputs**: Sanitize user-provided data
- **Warn about destructive operations**: Mark dangerous actions clearly
- **Document requirements**: State what permissions/access are needed

### For Skill Integrators

- **Sandbox script execution**: Run scripts in isolated environments
- **Allowlist skills**: Only execute trusted skills
- **Require confirmation**: Ask users before dangerous operations
- **Log executions**: Track what skills run and when
- **Review skill content**: Audit skills before use

## Common Patterns

### Pattern 1: Simple Text Instructions

**When to use:** Process guidance, best practices, conceptual teaching

**Structure:**
```
skill-name/
└── SKILL.md
```

**Example:** code-review-skill, documentation-writing-skill

### Pattern 2: Instructions + Detailed Reference

**When to use:** Complex APIs, technical specs, extensive documentation

**Structure:**
```
skill-name/
├── SKILL.md
└── references/
    ├── REFERENCE.md
    └── FORMS.md
```

**Example:** api-integration-skill, database-query-skill

### Pattern 3: Full Workflow with Scripts

**When to use:** Executable workflows, data processing, automation

**Structure:**
```
skill-name/
├── SKILL.md
├── scripts/
│   ├── main.py
│   └── helper.sh
├── references/
│   └── REFERENCE.md
└── assets/
    └── templates/
```

**Example:** data-analysis-skill, deployment-automation-skill

## Naming Conventions

### Skill Names (kebab-case)

```
# ✅ Good names
pdf-processing
data-analysis
api-integration-v2
code-review

# ❌ Bad names
PDFProcessing         # uppercase
pdf_processing        # underscores
pdf.processing        # dots
process-pdfs-and-images-and-documents  # too long, vague
```

### File Names

**SKILL.md:** Uppercase (preferred) or lowercase accepted

**Scripts:** Descriptive, snake_case or kebab-case
```
extract_data.py       # ✅ Clear purpose
helper.sh             # ❌ Too vague
script1.py            # ❌ Non-descriptive
```

**References:** ALL_CAPS for standard files, descriptive for others
```
REFERENCE.md          # ✅ Standard reference
FORMS.md              # ✅ Standard forms
api_endpoints.md      # ✅ Specific content
docs.md               # ❌ Too vague
```

## Metadata Best Practices

### Version Tracking

```yaml
metadata:
  version: "1.0.0"    # Semantic versioning
```

**Versioning scheme:**
- Major: Breaking changes
- Minor: New features, backwards compatible
- Patch: Bug fixes, doc updates

### Author Information

```yaml
metadata:
  author: jane-doe
  organization: example-corp
  contact: jane@example.com
```

### Tags and Categories

```yaml
metadata:
  tags: api, integration, rest
  category: development-tools
```

### Custom Fields

```yaml
metadata:
  internal-id: skill-12345
  cost-center: engineering
  support-team: platform
```

**Tip:** Use unique key names to avoid conflicts with other skills or tools.

## Example Complete Skill

```
weather-forecast-skill/
├── SKILL.md
├── scripts/
│   └── fetch_weather.py
├── references/
│   ├── REFERENCE.md          # Complete API docs
│   └── ERRORS.md             # Error codes
├── assets/
│   └── templates/
│       └── forecast.json
├── README.md
└── LICENSE
```

**SKILL.md:**
```markdown
---
name: weather-forecast-skill
description: Fetches weather forecasts from OpenWeather API with temperature, conditions, and multi-day predictions. Use when getting weather data, forecasts, or when user mentions weather.
license: Apache-2.0
compatibility: Requires Python 3.8+, requests library, OpenWeather API key
metadata:
  version: "1.0.0"
  author: weather-team
---

# Weather Forecast Skill

Fetch weather forecasts from the OpenWeather API.

## Prerequisites

- Python 3.8+
- `requests` library: `pip install requests`
- OpenWeather API key from https://openweathermap.org/api

## Setup

1. Get API key from OpenWeather
2. Set environment variable:
   ```bash
   export OPENWEATHER_API_KEY="your-key"
   ```

## Fetch Current Weather

Run the script:
```bash
python scripts/fetch_weather.py --city "San Francisco" --current
```

Output:
```json
{
  "city": "San Francisco",
  "temperature": 15.5,
  "conditions": "Partly Cloudy",
  "humidity": 65
}
```

## Fetch 5-Day Forecast

Run the script:
```bash
python scripts/fetch_weather.py --city "San Francisco" --forecast
```

See `references/REFERENCE.md` for complete API documentation.
See `references/ERRORS.md` for error handling.
```

## Compliance Checklist

Before publishing or sharing a skill:

- [ ] `SKILL.md` exists in skill root
- [ ] Frontmatter starts and ends with `---`
- [ ] Valid YAML in frontmatter
- [ ] `name` field present and follows rules (lowercase, 1-64 chars, kebab-case)
- [ ] `description` field present and 1-1024 characters
- [ ] Directory name matches `name` field
- [ ] No disallowed fields in frontmatter (use `metadata` for custom fields)
- [ ] Referenced files actually exist
- [ ] Instructions are clear and actionable
- [ ] Examples are complete and tested
- [ ] LICENSE file present (if distributing)
- [ ] README.md present (recommended for GitHub)

## Resources

**Official Documentation:**
- [Agent Skills Website](https://agentskills.io)
- [Specification](https://agentskills.io/specification)
- [Integration Guide](https://agentskills.io/integrate-skills)
- [Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

**Tools:**
- [skills-ref Library](https://github.com/agentskills/agentskills/tree/main/skills-ref) - Validation and utilities
- [Example Skills](https://github.com/anthropics/skills) - Official examples

**Community:**
- [GitHub Repository](https://github.com/agentskills/agentskills) - Specification and discussion
- [Contributing](https://github.com/agentskills/agentskills/blob/main/CONTRIBUTING.md) - How to contribute

## Quick Reference Card

| Aspect | Requirement | Details |
|--------|-------------|---------|
| **Directory** | Required | Must contain SKILL.md |
| **name** | Required | 1-64 chars, lowercase, kebab-case |
| **description** | Required | 1-1024 chars, what + when + keywords |
| **license** | Optional | License identifier or file reference |
| **compatibility** | Optional | Max 500 chars, environment requirements |
| **metadata** | Optional | Custom key-value pairs (string→string) |
| **allowed-tools** | Optional | Experimental, space-delimited tools |
| **SKILL.md body** | Required | Markdown, no restrictions, ~500 lines recommended |
| **scripts/** | Optional | Executable code |
| **references/** | Optional | Detailed docs, loaded on demand |
| **assets/** | Optional | Templates, images, data |

## Version History

This summary is based on the Agent Skills specification as of February 2026.

**Specification maintained by:** Anthropic and the Agent Skills community

**License:** Specification is open standard, implementations may vary

For the most current specification, always refer to: https://agentskills.io/specification
