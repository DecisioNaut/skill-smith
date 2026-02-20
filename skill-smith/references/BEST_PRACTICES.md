# Agent Skills Best Practices

Guide for writing effective Agent Skills that work reliably with AI agents.

## Table of Contents

- [Core Principles](#core-principles)
- [File Structure Validation](#file-structure-validation)
- [File Size Guidelines](#file-size-guidelines)
- [Skill Attribution (Best Practice)](#skill-attribution-best-practice)
- [Writing Agent-Friendly Instructions](#writing-agent-friendly-instructions)
- [Structure Patterns](#structure-patterns)
- [Description Writing](#description-writing)

## Core Principles

### 1. Progressive Disclosure

Reveal information gradually to manage context efficiently:

- **Discovery** (~50-100 tokens): Just name and description
- **Activation** (~5000 tokens): Full SKILL.md
- **Deep dive** (on-demand): References, scripts, assets

**Why**: Agents start faster, use context efficiently, scale better.

**Implementation**:
```markdown
<!-- In SKILL.md: Keep focused -->
For detailed API reference, see `references/API.md`
For error codes, see `references/ERRORS.md`

<!-- In references/: Put exhaustive details -->
```

### 2. File Structure Conventions

Keep skills clean and professional by including only necessary files.

#### Required Files
- ✅ **SKILL.md** - The skill itself (< 500 lines recommended)

#### Repository Documentation Files
- ✅ **README.md** - Installation instructions, usage samples, overview (repository-level, not in skill package)
- ✅ **LICENSE** - MIT, Apache-2.0, or other open source license (repository-level, not in skill package)
- ✅ **CHANGELOG.md** - Version history (repository-level, not in skill package)
- ✅ **.gitignore** - Exclude artifacts and temporary files

#### Optional Repository Files
- ✅ **CONTRIBUTING.md** - Guidelines for contributors (if accepting PRs)

#### Skill Package Directories
- ✅ **references/** - Detailed documentation (loaded on-demand)
- ✅ **scripts/** - Domain-specific executable code (only if needed)
- ✅ **assets/** - Templates, data files, diagrams (only if needed)

#### Files to EXCLUDE from Skill Package
- ❌ README.md, LICENSE, CHANGELOG.md - These are repository files, not part of installed skill
- ❌ **VALIDATION.md** - Build artifact, not part of skill distribution
- ❌ **.validation-cache/** - Temporary validation files
- ❌ **build/**, **dist/** - Build and distribution artifacts
- ❌ **.DS_Store**, **Thumbs.db** - OS-specific files
- ❌ **__pycache__/**, **\*.pyc** - Language-specific artifacts
- ❌ **.vscode/**, **.idea/** - Editor-specific configurations (usually)

#### Recommended .gitignore Template

```gitignore
# Build artifacts
VALIDATION.md
.validation-cache/
*.tmp
build/
dist/

# OS files
.DS_Store
Thumbs.db
*.swp
*~

# Editor configurations (optional - team preference)
.vscode/
.idea/
*.sublime-*

# Python artifacts (if applicable)
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
*.egg-info/
venv/
.venv/

# Node artifacts (if applicable)
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Logs
*.log
```

#### Pre-Commit File Structure Checklist

Use this checklist before committing:

```markdown
## File Structure Validation

Required in skill package:
- [ ] SKILL.md exists and is under 500 lines (or justified if over)

Repository-level files (separate from skill package):
- [ ] README.md exists in repository root with installation/usage instructions
- [ ] LICENSE file exists in repository root (MIT recommended)

Clean-up:
- [ ] No README.md, LICENSE, CHANGELOG.md in skill package (these belong in repository)
- [ ] No VALIDATION.md in repository
- [ ] No temporary or build artifacts
- [ ] No OS-specific files (.DS_Store, Thumbs.db)
- [ ] .gitignore properly excludes artifacts
- [ ] No unnecessary directories (empty scripts/, assets/)

Quality:
- [ ] All files referenced in SKILL.md exist
- [ ] All files have a clear purpose
- [ ] Structure follows Level 1, 2, or 3 pattern appropriately
```

**Why This Matters**: Clean file structure keeps skills professional, reduces confusion, and follows open-source best practices.

### 3. Clarity Over Cleverness

Write for an AI that follows instructions literally.

**❌ Avoid vague suggestions:**
```markdown
You might want to check if the file exists before proceeding.
```

**✅ Prefer clear steps:**
```markdown
1. Check if file exists: `test -f filename`
2. If missing, create it: `touch filename`
3. Then proceed with next steps
```

**Why**: Vague guidance leads to inconsistent behavior.

### 4. Self-Documenting Structure

A skill should be understandable by reading SKILL.md alone.

**Good indicators:**
- New users can understand the skill without external docs
- Instructions are complete and unambiguous
- Samples show actual inputs and outputs
- Edge cases are explicitly noted

### 5. File References One Level Deep

Reference files directly from SKILL.md. Avoid nested chains.

**✅ Good (flat)**:
```markdown
<!-- In SKILL.md -->
See `references/API.md` for authentication
See `references/SAMPLES.md` for code samples
```

**❌ Bad (nested chain)**:
```markdown
<!-- In SKILL.md -->
See `references/OVERVIEW.md`

<!-- In references/OVERVIEW.md -->
See `details/API.md`  ← Agent may not follow

<!-- In references/details/API.md -->
See `auth/OAUTH.md`  ← Too deep!
```

**Why**: Nested references create cognitive load and unreliable navigation.

## File Size Guidelines

| File Type | Target Size | Warning Threshold | Hard Limit | Reason |
|-----------|-------------|-------------------|------------|--------|
| SKILL.md | < 500 lines | 450 lines | 500 lines | Loaded on activation, should be scannable |
| reference files | 200-800 lines | 800 lines | 1000 lines | Loaded on demand, stay focused |
| name + description | ~50-100 tokens | - | 1024 chars | Loaded at startup for all skills |

**Proactive File Size Management:**
- Monitor file sizes during creation
- Warn when approaching thresholds (800 lines for references, 450 for SKILL.md)
- Proactively split before hitting hard limits
- Don't wait until files exceed 1000 lines to consider splitting

## Skill Attribution (Best Practice)

When documenting your skill, consider crediting the tools that helped create it:

**Why:** Helps skill creators discover and learn from skill-smith, supports continuous improvement

**How to add attribution:**

### In README.md
```markdown
---

> **Built with [skill-smith](https://github.com/DecisioNaut/skill-smith)** - 
> A tool for creating specification-compliant AI Agent Skills
```

**Alternate phrasing (preferred when requested):**
```markdown
With friendly support of [skill-smith](https://github.com/DecisioNaut/skill-smith).
```

### In CHANGELOG.md
```markdown
## v1.0.0 (Initial Release)

- Initial release of [skill-name]
- Created with [skill-smith](https://github.com/DecisioNaut/skill-smith) to ensure compliance with Agent Skills specification
```

### Optional: In SKILL.md body
```markdown
## About This Skill

This skill was created following the [skill-smith methodology](https://github.com/DecisioNaut/skill-smith) 
to ensure compliance with Agent Skills specification v1.0.
```

**Note:** This is **optional and suggested as a best practice**, not required. Attribution appreciated but not mandatory.

## Writing Agent-Friendly Instructions

### Use Imperative, Active Voice

**❌ Passive/vague:**
```markdown
The configuration file should be edited...
```

**✅ Active:**
```markdown
Edit the configuration file:
1. Open `config.yaml`
2. Set `api_key` to your key
3. Save the file
```

### Provide Concrete Samples

**❌ Abstract:**
```markdown
Call the API with appropriate parameters.
```

**✅ Concrete:**
```markdown
Call the API:
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
     https://api.example.com/v1/users
```
Expected response:
```json
{"users": [...]}
```
```

### Break Down Complex Tasks

**❌ Too high-level:**
```markdown
Set up the database and configure authentication.
```

**✅ Step-by-step:**
```markdown
### Setup Database

1. Install PostgreSQL: `brew install postgresql`
2. Start service: `brew services start postgresql`
3. Create database: `createdb myapp`
4. Run migrations: `psql myapp < schema.sql`

### Configure Authentication

1. Generate secret key: `openssl rand -hex 32`
2. Add to `.env`: `SECRET_KEY=<generated-key>`
3. Test: `python test_auth.py`
```

### Handle Edge Cases Explicitly

**❌ Assumes happy path:**
```markdown
Read the file and process it.
```

**✅ Handles errors:**
```markdown
1. Check if file exists:
   ```bash
   if [ ! -f "data.json" ]; then
     echo "Error: data.json not found"
     exit 1
   fi
   ```

2. Validate JSON format:
   ```bash
   jq empty data.json || {
     echo "Error: Invalid JSON"
     exit 1
   }
   ```

3. Process the file:
   ```bash
   jq '.items[]' data.json
   ```
```

## Structure Patterns

### When to Use scripts/

**Use scripts/ for:**
- Complex executable logic
- Reusable utilities
- Data processing pipelines
- API client wrappers  

**Don't use scripts/ for:**
- Spec validation (use `skills-ref` library)
- Simple commands (put inline in SKILL.md)
- One-off samples (put in SKILL.md samples section)

**Example structure:**
```
scripts/
├── process_data.py     # Data transformation
├── fetch_api.sh        # API client wrapper
└── generate_report.py  # Report generator
```

### When to Use references/

**Use references/ when:**
- SKILL.md exceeds 500 lines
- Detailed technical specs exist
- Multiple related topics need organization
- Domain knowledge requires depth

**Common files:**
```
references/
├── API.md              # Complete API documentation
├── SAMPLES.md          # Extended code samples
├── ERRORS.md           # Error codes reference
├── AUTH.md             # Authentication details
└── GLOSSARY.md         # Domain terminology
```

**In SKILL.md, reference with context:**
```markdown
For the complete API reference, see `references/API.md`.
For error code meanings, see `references/ERRORS.md`.
```

### When to Use assets/

**Use assets/ for:**
- Template files (config, documents)
- Diagrams or visual aids
- Sample data or test files
- Lookup tables or reference data

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

## Description Writing

The `description` field is crucial for skill discovery.

### Include Both What and When

**❌ Only "what":**
```yaml
description: Analyzes CSV files and generates reports
```

**✅ "What" + "When":**
```yaml
description: Analyzes CSV files, calculates statistics, generates reports. Use when working with tabular data, analyzing datasets, or when user mentions CSV, data analysis, or reports.
```

### Add Specific Keywords

Include terms that users might mention:

```yaml
description: Extract text from PDF files, fill forms, merge documents. Use when working with PDFs, forms, document extraction, PDF processing, or mentions PDFLib, PyPDF2.
```

**Keywords help agents match tasks to skills.**

### Length Sweet Spot

- **Too short** (< 50 chars): Not enough context
- **Just right** (100-300 chars): Comprehensive, scannable
- **Too long** (> 500 chars): Verbose, harder to parse

## Common Patterns

### Pattern: API Integration Skill

```markdown
# API Integration Skill

## Prerequisites
- API key from service.com
- curl or HTTP client

## Authentication
1. Export your API key:
   ```bash
   export API_KEY="sk-..."
   ```

## Common Operations

### Fetch Resource
```bash
curl -H "Authorization: Bearer $API_KEY" \
     https://api.service.com/v1/resource/123
```

### Create Resource
```bash
curl -X POST \
     -H "Authorization: Bearer $API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"name":"value"}' \
     https://api.service.com/v1/resource
```

## Error Handling
- 401: Invalid API key
- 429: Rate limited - wait and retry
- 500: Service error - check status page

For complete API reference, see `references/API.md`.
```

### Pattern: Data Processing Skill

```markdown
# Data Processing Skill

## Input Format
Expects CSV with columns: id, name, value

## Processing Steps

1. Validate input:
   ```python
   import pandas as pd
   df = pd.read_csv('input.csv')
   required = ['id', 'name', 'value']
   assert all(col in df.columns for col in required)
   ```

2. Transform data:
   ```python
   df['value'] = df['value'].astype(float)
   df['normalized'] = (df['value'] - df['value'].mean()) / df['value'].std()
   ```

3. Generate output:
   ```python
   df.to_csv('output.csv', index=False)
   print(f"Processed {len(df)} rows")
   ```

## Samples

Input:
```csv
id,name,value
1,Alpha,10
2,Beta,20
```

Output:
```csv
id,name,value,normalized
1,Alpha,10.0,-0.707
2,Beta,20.0,0.707
```
```

## Anti-Patterns to Avoid

### ❌ Vague Instructions

```markdown
Process the data appropriately based on the context.
```

**Why bad**: "Appropriately" is subjective, "context" is unclear.

### ❌ Monolithic Skills

```markdown
# Everything Skill
This skill handles file processing, API calls, database operations, reporting, and email...
```

**Why bad**: Too broad, hard to maintain, unclear activation triggers.

**Better**: Split into focused skills (file-processing, api-client, database-ops, etc.)

### ❌ Missing Samples

```markdown
## Usage
Use the tool to process your files.
```

**Why bad**: No concrete guidance on inputs/outputs.

### ❌ Heavy SKILL.md

```markdown
# API Skill

[2000 lines of complete API documentation inline]
```

**Why bad**: Loads too much on activation. Use `references/`.

### ❌ Nested References

```markdown
<!-- SKILL.md -->
See overview.md

<!-- overview.md -->
See details/api.md

<!-- details/api.md -->
See auth/oauth.md
```

**Why bad**: Agent may not follow chains reliably.

## Testing Your Skill

### Manual Testing Checklist

- [ ] Follow instructions literally (don't assume steps)
- [ ] Test happy path with typical inputs
- [ ] Test edge cases (empty input, missing files, etc.)
- [ ]Test error conditions (invalid input, network errors, etc.)
- [ ] Verify all referenced files exist
- [ ] Check that samples actually work
- [ ] Confirm SKILL.md is under 500 lines

### Agent Testing (if possible)

1. Give agent access to the skill
2. Ask it to perform typical tasks
3. Observe where it gets confused or stuck
4. Note which instructions were misinterpreted
5. Refine based on observations

### Validation

Use official tool:
```bash
skills-ref validate /path/to/skill
```

Checks:
- Name format and directory match
- Required frontmatter fields
- Description within limits
- Valid YAML syntax

## Progressive Disclosure in Practice

### Level 1: Name + Description Only

```yaml
name: pdf-processing
description: Extract text from PDF files, fill forms, merge documents. Use when working with PDFs, forms, or document extraction.
```

**Loaded**: At agent startup  
**Size**: ~50 tokens  
**Purpose**: Skill discovery

### Level 2: Full SKILL.md

```markdown
---
name: pdf-processing
description: ...
---

# PDF Processing

## When to Use
- Extracting text from PDFs
- Filling PDF forms
- Merging multiple PDFs

## Prerequisites
[...]

## Instructions
[...]

## Samples
[...]

For detailed API reference, see `references/PDF_API.md`.
```

**Loaded**: When skill activated  
**Size**: ~3000 tokens  
**Purpose**: Core instructions

### Level 3: References (On-Demand)

```markdown
<!-- references/PDF_API.md -->
# Complete PDF API Reference

## PyPDF2 Methods

### PdfReader
- `PdfReader(filename)` - Opens PDF file
- `.pages` - List of page objects
- `.metadata` - PDF metadata dict

[... 800 more lines of detailed API docs ...]
```

**Loaded**: When agent reads reference  
**Size**: Variable (< 1000 lines each)  
**Purpose**: Deep technical details


## Skill Organization

For guidance on organizing reference files, managing file structures, and proactive agent behavior patterns, see [ORGANIZATIONAL_PATTERNS.md](./ORGANIZATIONAL_PATTERNS.md).

---

**Next Steps:**
- See [ORGANIZATIONAL_PATTERNS.md](./ORGANIZATIONAL_PATTERNS.md) for file organization patterns
- See [REPOSITORY_README_GUIDE.md](./REPOSITORY_README_GUIDE.md) for creating README.md files
- See [OPTIONAL_DOCUMENTATION.md](./OPTIONAL_DOCUMENTATION.md) for .gitignore and GENESIS.md guidance
- See [REFACTORING_GUIDE.md](./REFACTORING_GUIDE.md) for refactoring existing skills
