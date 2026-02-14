# Agent Skills Best Practices

Guide for writing effective Agent Skills that work reliably with AI agents.

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

#### Highly Recommended Files
- ✅ **README.md** - Installation instructions, usage examples, overview
- ✅ **LICENSE** - MIT, Apache-2.0, or other open source license

#### Recommended Files
- ✅ **CHANGELOG.md** - Version history following Keep a Changelog format
- ✅ **.gitignore** - Exclude artifacts and temporary files

#### Optional Files
- ✅ **CONTRIBUTING.md** - Guidelines for contributors (if accepting PRs)

#### Optional Directories
- ✅ **references/** - Detailed documentation (loaded on-demand)
- ✅ **scripts/** - Domain-specific executable code (only if needed)
- ✅ **assets/** - Templates, data files, diagrams (only if needed)
- ✅ **examples/** - Example skills or usage patterns (only if applicable)

#### Files to EXCLUDE (Never Include)
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

Required:
- [ ] SKILL.md exists and is under 500 lines (or justified if over)
- [ ] README.md exists with installation/usage instructions
- [ ] LICENSE file exists (MIT recommended)

Clean-up:
- [ ] No VALIDATION.md in repository
- [ ] No temporary or build artifacts
- [ ] No OS-specific files (.DS_Store, Thumbs.db)
- [ ] .gitignore properly excludes artifacts
- [ ] No unnecessary directories (empty scripts/, assets/, examples/)

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
- Examples show actual inputs and outputs
- Edge cases are explicitly noted

### 5. File References One Level Deep

Reference files directly from SKILL.md. Avoid nested chains.

**✅ Good (flat)**:
```markdown
<!-- In SKILL.md -->
See `references/API.md` for authentication
See `references/EXAMPLES.md` for code samples
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

| File Type | Recommended | Reason |
|-----------|-------------|--------|
| SKILL.md | < 500 lines | Loaded on activation, should be scannable |
| reference files | < 1000 lines each | Loaded on demand, stay focused |
| name + description | ~50-100 tokens | Loaded at startup for all skills |

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

### Provide Concrete Examples

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
- One-off examples (put in SKILL.md examples section)

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
├── EXAMPLES.md         # Extended code examples
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

## Examples

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

### ❌ Missing Examples

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
- [ ] Check that examples actually work
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

## Examples
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

## Reference File Organization

When skills grow complex, organize reference files systematically based on real-world patterns.

### Naming Conventions

**Standard Format:** `TOPIC.md` or `TOPIC_SUBTOPIC.md`

**Rules:**
- ALL_CAPS with underscores separating words
- Descriptive and specific (not generic)
- Related files use same prefix

**Examples:**
- ✅ AUTHENTICATION.md - Clear single topic
- ✅ DOCKER_COMPOSE.md - Specific feature
- ✅ NETWORKING.md + NETWORKING_ADVANCED.md - Progressive complexity
- ❌ MISC.md - Too generic
- ❌ authentication.md - Wrong case

### Size Guidelines

**Target Range:** 200-800 lines (optimal for readability)
**Acceptable Range:** 150-1000 lines
**Consider Splitting:** Over 1000 lines (evaluate case-by-case)

**Real-world data from production skills:**
- devcontainer-expert: 9 files, 365-574 lines each
- uv-expert: 11 files, 155-1026 lines (1 slightly over, acceptable)

**When NOT to split:**
- Topic is cohesive and splitting would fragment understanding
- File is only slightly over (1000-1200 range often acceptable)
- Content needs to be referenced together

### Splitting Strategies

**By Complexity Level:**
- Pattern: `TOPIC.md` + `TOPIC_ADVANCED.md`
- Example: NETWORKING.md (basics) + NETWORKING_ADVANCED.md (advanced patterns)
- Benefits: Clear learning path, beginners not overwhelmed

**By Functional Area:**
- Pattern: `TOPIC_AREA1.md` + `TOPIC_AREA2.md`
- Example: CONFIGURATION_BASICS.md + CONFIGURATION_ADVANCED.md
- Benefits: Clear separation of concerns

**By Feature Category:**
- Pattern: Distinct files for distinct features
- Example: PROJECTS.md, SCRIPTS_TOOLS.md, PYTHON_MANAGEMENT.md
- Benefits: Each file has clear, single purpose

### Reference File Structure

**Standard Template:**
```markdown
# Descriptive Title

**Reference for:** One-sentence description of content

> **Cross-references:** Links to related files

## Table of Contents (for files > 400 lines)
- [Section 1](#section-1)
- [Section 2](#section-2)

## Main Content

Clear hierarchical organization with examples...
```

**Key Elements:**
1. **Title** - Matches file name (proper case)
2. **Purpose Statement** - "**Reference for:** [what this covers]"
3. **Cross-References** - Link prerequisites and related files
4. **Table of Contents** - For files > 400 lines
5. **Content** - Clear hierarchy, code examples with language tags

### Cross-Referencing

**Link Prerequisites:**
```markdown
> **Prerequisites:** Read [BASICS.md](./BASICS.md) for fundamentals.
```

**Link to Advanced Content:**
```markdown
> **For advanced topics**, see [ADVANCED.md](./ADVANCED.md).
```

**Use Relative Paths:**
- `[FILE.md](./FILE.md)` from same directory
- `[FILE.md](../references/FILE.md)` from SKILL.md

### Organizational Anti-Patterns

**❌ Avoid:**
- Catch-all files (MISC.md, OTHER.md)
- Overly generic names (DOCUMENTATION.md - documentation about what?)
- Feature mixing (DOCKER_AND_KUBERNETES.md)
- Artificial splitting (SECURITY_PART1.md, SECURITY_PART2.md)

**✅ Instead:**
- Specific, focused files
- Clear topic per file
- Natural boundaries (basics vs. advanced)
- Topic-based organization

## Proactive Agent Behavior

When skill-smith is active, agents should automatically check best practices and offer recommendations. Don't wait for users to ask - be proactive!

### Automatic Checking Pattern

**Workflow:**
```
Agent automatically checks → Identifies issues → Presents recommendations → Asks for user input
```

**Core Principle:** Agents should be helpful collaborators, not passive executors.

### When to Check Automatically

**After file modifications:**
- ✅ Check SKILL.md line count
- ✅ Verify file structure (no artifacts)
- ✅ Check all file references still valid
- ✅ Verify .gitignore covers artifacts

**After refactoring:**
- ✅ Run skills-ref validate
- ✅ Check consistency across files
- ✅ Verify reference organization follows patterns
- ✅ Check for duplicate content

**After content additions:**
- ✅ Check if SKILL.md approaching/exceeding 500 lines
- ✅ Suggest where new content should go
- ✅ Check version number needs update
- ✅ Remind about CHANGELOG.md entry

**Before committing:**
- ✅ Full compliance check
- ✅ File structure validation
- ✅ Verify no artifacts present
- ✅ Check consistency across files

### Example Interactions

**After modifying SKILL.md:**
```
User: "I've updated the SKILL.md with new authentication section"

Agent: 
✅ Checking best practices...

Issues found:
1. SKILL.md is now 571 lines (71 over 500-line guideline)
2. New authentication content is 85 lines

Recommendations:
• Move authentication details to references/AUTHENTICATION.md
• Keep only quick start auth in SKILL.md (est. 15-20 lines)
• This would bring SKILL.md to ~506 lines (still slightly over)
• Consider moving another section to stay under 500

Would you like me to:
A) Create references/AUTHENTICATION.md and move the content
B) Suggest additional sections to move
C) Keep as-is (572 lines is acceptable for this complexity)
D) You have another approach in mind

What do you prefer?
```

**During refactoring:**
```
User: "Let's refactor this skill"

Agent:
✅ Analyzing current state...

Current Structure:
- SKILL.md: 687 lines
- No reference files
- VALIDATION.md present (should remove)

Refactoring Recommendations:
1. Move API documentation (230 lines) → references/API_REFERENCE.md
2. Move examples (120 lines) → references/EXAMPLES.md
3. Remove VALIDATION.md artifact
4. Add .gitignore to exclude artifacts

This would bring SKILL.md to ~337 lines.

Shall I proceed with these changes?
```

### Compliance Overview Pattern

When checking compliance, present complete picture:

```
Agent: "Running comprehensive compliance check...

📊 Compliance Overview:

SKILL.md:
  ✅ 447 lines (under 500-line guideline)

Reference Files:
  ✅ AUTHENTICATION.md: 234 lines
  ✅ API_REFERENCE.md: 456 lines
  ⚠️ EXAMPLES.md: 1,103 lines (103 over 1000-line recommendation)
  
Assets:
  ✅ 2 templates, both referenced

Summary:
  ✅ SKILL.md: Compliant
  ⚠️ 1 reference file slightly over recommendation
  
Recommendations:
  • EXAMPLES.md could split into BASIC_EXAMPLES.md + ADVANCED_EXAMPLES.md
  • Or keep as-is since only slightly over

Would you like to:
A) Keep as-is (slightly over but acceptable)
B) Split EXAMPLES.md
C) Review specific sections to decide"
```

**Why This Works:**
- Shows ALL files, not just problems
- Visual organization (SKILL.md, references, assets)
- Clear status indicators (✅ ⚠️ ❌)
- Context for decisions ("slightly over" vs "way over")
- User empowerment (present options, let user decide)
- Acknowledges trade-offs (sometimes slightly over is fine)

### Behavior by Workflow Mode

**During CREATE mode:**
- Check SKILL.md size at Step 4 (after writing)
- Suggest splits if approaching 500 lines
- Validate before Step 9
- Final check before commit

**During REFACTOR mode:**
- Automatically check after each change
- Present issues with specific recommendations
- Suggest reorganization patterns
- Validate when refactoring complete

**During IMPROVE mode:**
- Check impact before adding content
- Alert if additions will exceed 500 lines
- Suggest placement (SKILL.md vs references/)
- Validate after additions

**During UPDATE mode:**
- Check what has changed in resources
- Identify content that needs updating
- Suggest versioning strategy
- Validate after updates

**During VALIDATE mode:**
- Run full compliance check immediately
- Present comprehensive findings
- Prioritize issues by severity
- Suggest specific fixes with examples

### Key Principles

1. **Automatic Checking** - Don't wait for user to ask "is this compliant?"
2. **Clear Communication** - Present findings in structured format
3. **Actionable Recommendations** - Offer specific solutions, not just problems
4. **User Choice** - Always give options (A/B/C/D) including "other ideas"
5. **Collaborative** - Agent recommends, user decides
6. **Complete Picture** - Show all files when checking compliance
7. **Context Matters** - "Slightly over" is different from "way over"

### What to Check After Modifications

```markdown
After any skill file modification:
- [ ] SKILL.md line count (warn if >450, alert if >500)
- [ ] File structure (check for artifacts)
- [ ] File references (verify all exist)
- [ ] .gitignore covers artifacts
- [ ] Frontmatter valid
- [ ] Version number appropriate for changes

Present findings like:
✅ SKILL.md: 447 lines (under limit)
✅ No artifacts found
⚠️ Found reference to 'references/MISSING.md' that doesn't exist
❌ .gitignore missing VALIDATION.md pattern

Recommendations:
1. Create references/MISSING.md or remove reference
2. Add 'VALIDATION.md' to .gitignore

Would you like me to fix these issues?
```

### Error Handling

**If unclear which approach is best:**
```
Agent: "I notice SKILL.md is 571 lines. I see several sections that could 
potentially move to references:

1. Authentication (85 lines) - Detailed, good candidate
2. Configuration (120 lines) - Mix of essential + details
3. Troubleshooting (95 lines) - Could split into references

I'm not sure which approach is best for this skill. What's your preference?
- Move all three to references/
- Move just authentication?
- Move authentication + troubleshooting?
- Different sections entirely?

Let me know and I'll make the changes."
```

**When presenting options:**
- Always include "other ideas" or "different approach"
- Be humble about recommendations
- Explain trade-offs
- Let user make final decision

## Summary: Quick Wins

To improve any skill instantly:

1. **Add concrete examples** with actual inputs/outputs
2. **Break complex instructions** into numbered steps
3. **Handle errors explicitly** (don't assume success)
4. **Keep SKILL.md focused** (< 500 lines)
5. **Use progressive disclosure** (move details to references/)
6. **Write for literal interpretation** (no vague language)
7. **Include specific keywords** in description
8. **Keep file references flat** (one level deep)
9. **Validate with skills-ref** before sharing
10. **Test by following literally** (don't assume steps)

## Resources

- [Agent Skills Specification](https://agentskills.io/specification)
- [Integration Guide](https://agentskills.io/integrate-skills)
- [Example Skills](https://github.com/anthropics/skills)
- [skills-ref Library](https://github.com/agentskills/agentskills/tree/main/skills-ref)
