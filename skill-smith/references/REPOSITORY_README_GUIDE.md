# Repository README Guide

**Reference for:** Writing effective README.md files for skill repositories

> **Cross-references:** See [OPTIONAL_DOCUMENTATION.md](./OPTIONAL_DOCUMENTATION.md) for GENESIS.md and .gitignore guidance | See [BEST_PRACTICES.md](./BEST_PRACTICES.md) for skill package structure

## Overview

README.md is the **first thing potential users see**. It should answer:
- What does this skill do?
- How do I install it?
- How do I use it?
- What do I need to know?

**Important:** Every published skill repository should have a README.md at the repository root.

## Complete README.md Template

```markdown
# [Skill Name]

[One-line description of what this skill does]

## Overview

[2-3 paragraph explanation of the skill's purpose and capabilities]

This repository contains the `[skill-name]` Agent Skill that helps users [specific task].

**Key Features:**
- [Feature or capability 1]
- [Feature or capability 2]
- [Feature or capability 3]

## Quick Start

### Installation

Users can install this skill by:

1. Clone or download this repository:
   ```bash
   git clone https://github.com/[user]/[skill-name].git
   ```

2. Add the skill to their agent configuration:
   ```bash
   # Copy the skill-name/ folder to your agent skills directory
   cp -r [skill-name]/[skill-name]/ ~/.agent/skills/
   ```

3. Verify installation:
   ```bash
   ls ~/.agent/skills/[skill-name]/
   # Should show: SKILL.md, references/, scripts/, assets/ (as applicable)
   ```

### Basic Usage

[Provide 1-2 concrete samples of the skill in action]

**Sample 1: [Common Use Case]**
```
User: [What user asks]
Agent with skill: [What agent does/returns]
```

**Sample 2: [Another Common Use Case]**
```
User: [What user asks]
Agent with skill: [What agent does/returns]
```

## Skill Structure

The `[skill-name]/` folder contains the installable skill:

```
[skill-name]/
├── SKILL.md                          # Core skill instructions and metadata
├── references/                       # Detailed documentation
│   ├── [TOPIC1].md
│   └── [TOPIC2].md
├── scripts/                          # Executable code (if applicable)
│   └── [helper_script].py
└── assets/                           # Templates and resources (if applicable)
    └── [template].json
```

**For complete skill documentation**, see the [skill name](./[skill-name]/SKILL.md) file.

## Installation & Setup

### Prerequisites

Before using this skill, ensure you have:

- [Tool/Library 1]: [version requirement, e.g., "Python 3.8+"]
- [Tool/Library 2]: [version requirement, e.g., "curl or similar HTTP client"]
- [Access/Config]: [e.g., "API key from service.example.com"]

### Development Setup (if contributing)

To develop or modify this skill:

1. Clone the repository:
   ```bash
   git clone https://github.com/[user]/[skill-name].git
   cd [skill-name]
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt  # If applicable
   ```

3. Run validation:
   ```bash
   pip install -e git+https://github.com/agentskills/agentskills.git#egg=skills-ref&subdirectory=skills-ref
   skills-ref validate [skill-name]/
   ```

## Usage

### When to Use This Skill

Activate this skill when:
- [Scenario 1: When to use]
- [Scenario 2: When to use]
- [Scenario 3: When to use]

For detailed activation guidance and full skill documentation, see [SKILL.md](.)/[skill-name]/SKILL.md).

### Common Operations

**Operation 1: [Action Verb]**
```
[Command or example]
Expected result: [What happens]
```

**Operation 2: [Action Verb]**
```
[Command or example]
Expected result: [What happens]
```

For more samples and advanced patterns, see:
- `[skill-name]/SKILL.md` - Core instructions
- `[skill-name]/references/[SAMPLES].md` - Extended samples (if available)

## Key Concepts

**[Concept 1]:**
[Brief explanation]

**[Concept 2]:**
[Brief explanation]

**[Concept 3]:**
[Brief explanation]

For deeper conceptual coverage, see [SKILL.md](.)/[skill-name]/SKILL.md#core-concepts).

## Validation

This skill follows the [Agent Skills Specification v1.0](https://agentskills.io/specification).

**To validate locally:**
```bash
skills-ref validate [skill-name]/
```

**Output:**
- ✅ All checks pass: Skill is ready to use/distribute
- ❌ Errors: Review error messages and fix issues before sharing

## Contributing

We welcome contributions! Please review our [CONTRIBUTING.md](./CONTRIBUTING.md) guidelines before submitting pull requests.

**Quick contribution checklist:**
- [ ] Skill follows [BEST_PRACTICES.md]([skill-name]/references/BEST_PRACTICES.md)
- [ ] `skills-ref validate` passes
- [ ] SKILL.md is under 500 lines
- [ ] All referenced files exist
- [ ] Tested with an agent (if possible)
- [ ] CHANGELOG.md updated with your changes

## Troubleshooting

### Common Issues

**Issue: [Common problem]**
```
Error message: [What error appears]
```
**Solution:**
[How to fix it]

**Issue: [Another common problem]**
```
Error message: [What error appears]
```
**Solution:**
[How to fix it]

For more troubleshooting, see:
- [skill-name]/SKILL.md#troubleshooting
- [skill-name]/references/TROUBLESHOOTING.md (if available)

## Attribution

[Optional: Add if using skill-smith or other tools]

> **Built with [skill-smith](https://github.com/DecisioNaut/skill-smith)** - 
> A tool for creating specification-compliant Agent Skills

## License

This project is licensed under the [LICENSE Type] License. See [LICENSE](./LICENSE) for details.

## Changelog

See [CHANGELOG.md](./CHANGELOG.md) for version history and updates.

## Resources

- **Agent Skills Specification**: [https://agentskills.io/specification](https://agentskills.io/specification)
- **integration Guide**: [https://agentskills.io/integrate-skills](https://agentskills.io/integrate-skills)
- **skills-ref Library**: [https://github.com/agentskills/agentskills](https://github.com/agentskills/agentskills)

---

**Questions or Issues?** Please open an issue on GitHub.
```

## Writing Effective README Sections

### 1. Overview Section

**What to include:**
- What problem this skill solves
- Key capabilities (2-5 bullet points)
- Who would use it (target audience)

**Example (good):**
```markdown
## Overview

The `pdf-processing` skill helps users extract text, fill forms, and merge PDF documents programmatically. 

**Key Features:**
- Extract text from any PDF file
- Fill editable PDF forms with data
- Merge multiple PDF files into one
- Preserve formatting and metadata

Perfect for document automation, data extraction, or batch processing workflows.
```

### 2. Quick Start Section

**Must include:**
- Installation steps (copy-paste ready)
- 1-2 concrete usage samples
- Expected output

**Sample (good):**
```markdown
### Basic Usage

**Sample 1: Extract Text from PDF**
```
User: "Extract the text from invoice.pdf"
Agent response: [Extracts and returns all text from the PDF]
```

**Sample 2: Merge Multiple PDFs**
```bash
python scripts/merge_pdfs.py file1.pdf file2.pdf output.pdf
# Creates output.pdf containing all pages from both files
```
```

### 3. Prerequisites Section

**Must include:**
- External dependencies (tools, libraries)
- Version requirements
- Required access/credentials

**Example (good):**
```markdown
### Prerequisites

- **Python**: 3.8 or higher
- **Libraries**: pdf2image, PyPDF2 (installed via `pip install -r requirements.txt`)
- **System**: macOS, Linux, or Windows with Python installed

Optional:
- **API Key**: Get from api.example.com (only needed for advanced features)
```

### 4. Installation & Setup Section

**Must include:**
- Step-by-step clone/download instructions
- Copy-paste commands users can run
- Verification step to confirm success

**Example (good):**
```markdown
### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/user/pdf-processing.git
   cd pdf-processing
   ```

2. Install the skill in your agent:
   ```bash
   cp -r pdf-processing/ ~/.agent/skills/
   ```

3. Verify installation:
   ```bash
   ls ~/.agent/skills/pdf-processing/
   ```
   Should show: SKILL.md, references/, scripts/
```

### 5. Key Concepts Section

**Should explain:**
- Domain-specific terminology
- Assumptions users should know
- Conceptual foundations

**Example (good):**
```markdown
## Key Concepts

**PDF Extraction:** The process of pulling text from PDF files. PDFs can contain text in various encodings; this skill handles most common formats.

**Form Filling:** PDF forms have editable fields. This skill can programmatically populate these fields with data.

**Metadata:** Information about the PDF file (author, creation date, etc.). This skill preserves existing metadata during operations.
```

## Common README Mistakes to Avoid

### ❌ Too Technical

```markdown
# PDF Processing

Utilizes PyPDF2 and pdf2image libraries with JPEG compression algorithms...
```

**Better:**
```markdown
# PDF Processing

Extract text and merge PDF files. Works with all standard PDF formats.
```

### ❌ Missing Samples

```markdown
## Usage

Use this skill to process PDFs.
```

**Better:**
```markdown
## Usage

**Extract text from a PDF:**
```bash
python scripts/extract.py document.pdf
# Output: Extracted text saved to document_text.txt
```
```

### ❌ Unclear Prerequisites

```markdown
## Setup

Install required dependencies.
```

**Better:**
```markdown
## Prerequisites

- Python 3.8+
- pip and pip install -r requirements.txt

## Setup

1. Clone: `git clone https://github.com/user/pdf-skill.git`
2. Install: `pip install -r requirements.txt`
3. Verify: `python scripts/test.py`
```

### ❌ No Troubleshooting

README that doesn't mention common problems leaves users stuck.

**Better - Always include:**
```markdown
## Troubleshooting

**Error: "Module not found"**
- Solution: Run `pip install -r requirements.txt`

**Error: "Permission denied"**
- Solution: Ensure script has execute permissions: `chmod +x scripts/process.py`
```

## README Size & Organization

Typical structure:
- **Header** (title + one-liner): 2 lines
- **Overview** (what/why): 150-200 words
- **Quick Start**: 100-150 words + code
- **Installation**: 100-150 words + commands
- **Usage**: 150-300 words + samples
- **Key Concepts**: 100-200 words
- **Troubleshooting**: 100-200 words (optional but recommended)
- **Contributing/License/Resources**: 50-100 words

**Total: 700-1,500 words typical** (includes code blocks and commands)

## README Template Checklist

Before publishing, verify:

- [ ] Title clearly states what the skill does
- [ ] One-line description in repository settings matches skill description
- [ ] Installation instructions are copy-paste ready
- [ ] At least 2 concrete samples with expected output
- [ ] Prerequisites clearly listed (versions, tools, access)
- [ ] Setup steps are sequential and complete
- [ ] Troubleshooting covers 2-3 most common issues
- [ ] License file is mentioned and linked
- [ ] All links work (test them!)
- [ ] Code blocks have syntax highlighting (markdown language tags)
- [ ] No screenshot-required steps (keep text-based)
- [ ] README is ~1000 words or less (scannable, not overwhelming)

## When README Isn't Needed

In rare cases, a README might not be essential:
- **Temporary skills** not meant for distribution
- **Internal/private** skills for specific organizations
- **Teaching samples** that are intentionally bare-bones

In all other cases: **Always create a README.md**.

---

**Next Steps:**
- Create your README.md using the template above
- Test installation instructions before publishing
- Collect feedback from early users for improvement
