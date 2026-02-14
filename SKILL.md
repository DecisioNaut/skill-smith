---
name: skill-smith
description: Build specification-compliant Agent Skills from documentation sites, GitHub repos, and APIs. Systematically gather resources, design SKILL.md structure, validate naming rules, and package for sharing. Use when user mentions creating skills, building agent capabilities, SKILL.md files, agent skills format, or skill development.
license: MIT
metadata:
  version: "2.0.0"
  author: skill-smith contributors
compatibility: Designed for filesystem-based agents with web access
---

# Skill Smith

This skill helps you create high-quality Agent Skills that follow the official [Agent Skills specification](https://agentskills.io/specification). Use this when you need to build new skills from online resources like documentation websites, open source repositories, API references, or example code.

## When to Use This Skill

Activate this skill when:
- **Creating a new skill** from documentation, repos, or APIs
- **Refactoring an existing skill** to improve structure or reduce size
- **Adding features** to an existing skill  
- **Updating a skill** when source resources have changed
- **Validating a skill** for compliance with Agent Skills specification
- User mentions: creating skills, building agent capabilities, SKILL.md files, agent skills format, skill development, or skill refactoring

## Overview of Agent Skills

Agent Skills are folders containing a `SKILL.md` file with instructions that teach agents how to perform specific tasks. They use **progressive disclosure**:

1. **Discovery**: Agents load only name and description at startup (~50-100 tokens)
2. **Activation**: When relevant, agents read the full SKILL.md (~500-5000 tokens)
3. **Execution**: Agents follow instructions and access bundled resources as needed

### Directory Structure

```plaintext
skill-name/
├── SKILL.md          # Required: metadata + instructions (< 500 lines)
├── scripts/          # Optional: executable code
├── references/       # Optional: detailed docs (loaded on demand)
└── assets/           # Optional: templates, data, images
```

**Key Principle**: Keep SKILL.md under 500 lines (~5000 tokens). Move detailed reference material to separate files for on-demand loading.

## Building a New Skill: Step-by-Step Process

### 1. Gather Context and Requirements

**Ask the user these questions:**

1. **What should the skill do?** (specific task or capability)
2. **What resources are available?** (documentation URLs, GitHub repos, API references)
3. **Who is the target user?** (developers, data analysts, specific domain experts)
4. **What's the expected complexity?** (simple instructions-only vs. scripts/assets needed)

**Systematically Gather Resources Using Available Tools:**

For each resource URL provided, use `fetch_webpage` or similar tools to:

1. **Fetch the initial page** and extract:
   - Navigation links and site structure
   - Table of contents or section links
   - Links to key pages (Quick Start, API Reference, Examples, Tutorials)

2. **Follow and fetch important linked pages**:
   - Getting Started / Quick Start guides
   - API Reference or technical documentation
   - Examples and code samples
   - Best practices or troubleshooting sections
   - FAQ or common issues pages

3. **For GitHub repositories**, explore:
   - README.md (main overview)
   - docs/ or documentation/ directories
   - examples/ or samples/ directories
   - Key source code files showing patterns
   - CONTRIBUTING.md for development guidelines

**Use the Resource Gathering Templates** in `assets/resource-templates.md` to systematically document:
- Documentation sites analyzed (including multiple pages visited)
- Example repositories studied
- API references or technical specs
- Existing similar skills for inspiration

### 2. Analyze Resources Thoroughly

For each resource provided, **fetch and read multiple pages** to get comprehensive understanding:

**For GitHub Repositories:**
1. **Fetch and examine README.md** for overview and setup instructions
2. **Navigate to and fetch examples/ or docs/ directories** - read actual example files
3. **Fetch key source files** to understand code structure and patterns
4. **Check for CONTRIBUTING.md, LICENSE, and other documentation files**
5. Note dependencies, requirements, and prerequisites
6. Identify common patterns and best practices from actual code

**For Documentation Sites:**
1. **Fetch the main/landing page** and identify navigation structure
2. **Systematically fetch key sections** (don't rely on just the initial URL):
   - Quick Start or Getting Started page
   - Core concepts or fundamentals
   - API Reference or technical details
   - Code examples and tutorials
   - Troubleshooting or FAQ
3. **Extract from each page fetched**:
   - Step-by-step procedures
   - Code examples and patterns
   - Prerequisites and setup requirements
   - Common errors and solutions
4. **Map the site structure** - which sections are foundational vs. advanced

**For API References:**
1. **Fetch authentication/authorization documentation**
2. **Fetch endpoint documentation** for core operations
3. **Fetch examples page** if available
4. **Gather from all fetched pages**:
   - Authentication methods and credential requirements
   - Core endpoints and their methods
   - Request/response patterns and examples
   - Rate limits, quotas, or usage constraints
   - Error codes and handling strategies

**Ask clarifying questions if:**
- Resources conflict or show different approaches
- Critical information is missing after thorough exploration
- The scope is unclear or too broad
- Dependencies or prerequisites aren't documented
- You need access to pages behind authentication

### 3. Design the Skill Structure

Choose the appropriate level of complexity:

**Level 1: Instructions Only** (80% of skills)
- Just SKILL.md with clear step-by-step instructions
- Good for: processes, best practices, conceptual guidance
- Example: code-review-skill, documentation-writing

**Level 2: Instructions + References** (15% of skills)
- SKILL.md + references/ directory with detailed docs
- Good for: complex APIs, technical specs, domain knowledge
- Example: api-integration-skill with REFERENCE.md for full API docs
- **Reference organization**: Use ALL_CAPS.md naming (SECURITY.md, NETWORKING.md)
- **Size guidance**: 150-1000 lines per file (see references/BEST_PRACTICES.md)

**Level 3: Full Structure** (5% of skills)
- SKILL.md + scripts/ + references/ + assets/
- Good for: executable workflows, data processing, multi-step automation
- Example: data-analysis-skill with Python scripts and templates

**When organizing references/**:
- Use descriptive, specific names (not MISC.md or OTHER.md)
- Split by complexity (TOPIC.md + TOPIC_ADVANCED.md) if needed
- Keep each file focused on one clear topic
- Cross-reference between related files
- See references/BEST_PRACTICES.md for detailed patterns

### 4. Create the SKILL.md File

**Required YAML Frontmatter:**

```yaml
---
name: your-skill-name          # lowercase, hyphens only, 1-64 chars
description: Clear description of what this skill does and when to use it. Include specific keywords that help agents identify relevant tasks. 1-1024 characters.
---
```

**Optional Frontmatter Fields:**

```yaml
license: MIT                   # or Apache-2.0, or path to LICENSE.txt
compatibility: Requires Python 3.8+, requests library, internet access
metadata:
  author: your-name
  version: "1.0.0"
  tags: api, integration
allowed-tools: Bash(curl:*) Bash(python3:*) Read Write
```

**Body Structure (Recommended):**

```markdown
# Skill Name

[Brief overview paragraph]

## When to Use This Skill

[Clear criteria for when agents should activate this skill]

## Prerequisites

[Required tools, libraries, access, or setup steps]

## Core Concepts

[Key terminology or concepts agents need to understand]

## Step-by-Step Instructions

### Task 1: [Clear action verb]

1. [Specific, actionable step]
2. [Include concrete examples]
3. [Note common pitfalls or edge cases]

### Task 2: [Another clear action]

[Continue with more tasks...]

## Examples

### Example 1: [Common use case]

[Show complete example with input and expected output]

### Example 2: [Edge case or variation]

[Show how to handle less common scenarios]

## Troubleshooting

**Problem:** [Common error or issue]
**Solution:** [How to resolve it]

## Reference Files

- See `references/REFERENCE.md` for detailed API documentation
- See `references/FORMS.md` for request/response templates
```

**Writing Best Practices:**

1. **Use clear, actionable language**: Prefer direct instructions ("Run the script") over vague guidance ("You might want to consider running")

2. **Include concrete examples**: Show actual code, commands, or data rather than just describing them

3. **Structure for scanning**: Use headings, lists, and code blocks. Agents should quickly find relevant sections

4. **Front-load important info**: Put the most critical instructions early

5. **Be specific about edge cases**: Don't assume agents will infer error handling or special cases

6. **Keep SKILL.md under 500 lines** (~5000 tokens recommended): Move detailed reference material to references/

7. **Test readability**: Instructions should be clear if read by a human OR an agent

8. **Keep file references shallow**: Reference files should be "one level deep" from SKILL.md. Avoid nested reference chains like SKILL.md → REF1.md → REF2.md

### 5. Validate the Skill

**Check naming rules:**
- Name is lowercase letters, numbers, and hyphens only
- Name is 1-64 characters
- Name doesn't start or end with hyphen
- Name has no consecutive hyphens (`--`)
- Directory name matches the `name` field in frontmatter

**Check description:**
- Description is 1-1024 characters
- Description explains BOTH what the skill does AND when to use it
- Description includes specific keywords for agent matching

**Check structure:**
- SKILL.md exists and starts with `---`
- YAML frontmatter is valid and closed with `---`
- Frontmatter includes required fields: `name`, `description`
- All referenced files actually exist (scripts, references, assets)

**Use the official validation tool:**

Instead of creating custom validation scripts, use the official [skills-ref library](https://github.com/agentskills/agentskills/tree/main/skills-ref):

```bash
# Install skills-ref
pip install -e git+https://github.com/agentskills/agentskills.git#egg=skills-ref&subdirectory=skills-ref

# Validate your skill
skills-ref validate path/to/your-skill

# Generate agent prompt XML
skills-ref to-prompt path/to/your-skill
```

**For custom skill-specific validation** (beyond spec compliance), you may add scripts/ directory with domain-specific checks.

### 6. Add Optional Components

Most skills (95%) only need SKILL.md and optionally references/. Only add these directories if your skill genuinely needs them.

**scripts/ directory** (only if you have domain-specific executable code):
- **When to create**: Only if your skill needs data processing, API wrappers, or complex automation that's better as executable code
- **Examples**: Data transformation pipelines, API client libraries, file converters
- **NOT for**: Spec validation (use skills-ref library), simple commands (put inline in SKILL.md)
- Include clear error messages and help text
- Document dependencies at the top of each script
- Use common scripting languages (Python, Bash, JavaScript)
- Name scripts descriptively: `extract_data.py`, not `script1.py`

**Note**: For Agent Skills specification validation, always use the official `skills-ref` library rather than custom scripts. Don't create an empty scripts/ directory "just in case" - add it only when you have actual code to include.

**references/ directory** (create if SKILL.md exceeds ~400 lines):
- **When to create**: When you have detailed documentation that would make SKILL.md too long
- `REFERENCE.md`: Detailed technical reference (API docs, function signatures)
- `FORMS.md`: Templates for structured data (JSON schemas, API request formats)
- Domain-specific files: `database.md`, `authentication.md`, etc.
- Keep files focused and under 1000 lines each

**assets/ directory** (only if you have template files or static resources):
- **When to create**: Only if your skill needs config templates, diagrams, or sample data files
- **Examples**: Document templates (.md, .txt, .json), configuration examples, diagrams (.png, .svg), sample data for testing
- **NOT for**: Text documentation (use references/), examples (put in SKILL.md or references/)

### 7. Test the Skill

**Manual testing:**
1. Try to use the skill yourself to accomplish the task
2. Follow instructions literally - don't assume implied steps
3. Test with common use cases and edge cases
4. Verify that referenced files are accessible and clear
5. Check that SKILL.md is under 500 lines

**Agent testing (if possible):**
1. Give an agent access to the skill
2. Ask it to perform relevant tasks
3. Observe where it gets confused or stuck
4. Refine instructions based on agent behavior

**Security considerations:**
- If skill includes scripts, consider sandboxing requirements
- Document any dangerous operations that need user confirmation
- Avoid hardcoding credentials or sensitive data
- Note required network access in `compatibility` field
- Consider allow-listing approach for tool execution

### 8. Document and Package

**Create supporting files:**

- **README.md**: Installation instructions, usage examples, links to SKILL.md
- **LICENSE**: Choose MIT (most permissive), Apache 2.0 (patent protection), or other
- **CHANGELOG.md**: Track versions and changes
- **CONTRIBUTING.md**: Guidelines for contributors (if accepting contributions)
- **.gitignore**: Exclude artifacts (see template in references/BEST_PRACTICES.md)

**Validate file structure:**

After creating documentation:
1. Review files against recommended structure (see references/BEST_PRACTICES.md)
2. Remove any build artifacts or temporary files (VALIDATION.md, .tmp files, etc.)
3. Verify .gitignore excludes all artifact patterns
4. Check for empty directories that should be removed
5. Ensure no OS-specific files are committed

**Common files to remove:**
- ❌ VALIDATION.md (validation artifact)
- ❌ Temporary validation or build files
- ❌ .DS_Store, Thumbs.db (OS files)
- ❌ Empty directories (scripts/, assets/, examples/ with no files)

**Verify license compliance:**
- Check licenses of resources you used
- Ensure your chosen license is compatible
- Include proper attribution if required

**Prepare for sharing:**
- Verify all validation checks pass below
- Test installation instructions
- Write clear README with examples

### 9. Test and Final Validation

**Manual testing:**
1. Try to use the skill yourself to accomplish the task
2. Follow instructions literally - don't assume implied steps
3. Test with common use cases and edge cases
4. Verify that referenced files are accessible and clear
5. Check that SKILL.md is under 500 lines

**Specification validation:**

Run official validation:
```bash
skills-ref validate path/to/your-skill
```

**File structure validation (before committing):**

Use the checklist from references/BEST_PRACTICES.md:
- [ ] Required files present (SKILL.md, README.md, LICENSE)
- [ ] No build artifacts (VALIDATION.md, .tmp files)
- [ ] No OS files (.DS_Store, Thumbs.db)
- [ ] .gitignore configured properly
- [ ] Only include directories that have content
- [ ] All referenced files exist

**Final cleanup:**
```bash
# Check for unwanted files
git status

# Remove any artifacts
rm VALIDATION.md  # if present
rm -rf .validation-cache/  # if present

# Verify clean state
git status
```

**Tag version:**
```bash
git add .
git commit -m "feat: Initial release of skill-name v1.0.0"
git tag v1.0.0
```

## Alternative Workflows

The 9-step process above is for **creating new skills**. Use these alternative workflows for other scenarios:

### Refactoring an Existing Skill

**When:** Improving structure/organization of an existing skill

1. **Analyze Current State** - Check SKILL.md line count, list all files, run `skills-ref validate`
2. **Identify Issues** - Is SKILL.md > 500 lines? Unwanted artifacts? Poorly organized references?
3. **Plan Improvements** - Decide what moves to references/, plan file names
4. **Execute Changes** - Create reference files, update SKILL.md links, remove artifacts
5. **Validate** - Verify SKILL.md under 500 lines, all references work, run validation
6. **Document** - Update CHANGELOG.md, increment version
7. **Final Validation** - Run consistency check across ALL files (see references/CONSISTENCY_CHECKLIST.md)

### Adding Content to Existing Skill

**When:** Adding new features/documentation to existing skill

1. **Assess Impact** - Note current SKILL.md line count, estimate lines to add
2. **Decide Placement** - Core concepts → SKILL.md (if space), detailed docs → references/
3. **Add Content** - Maintain consistency with existing style
4. **Update References** - Add links, check cross-references
5. **Validate and Document** - Check size, run validation, update CHANGELOG.md
6. **Final Validation** - Check consistency across all files

### Updating an Existing Skill

**When:** Source resources have changed or skill needs refreshing

1. **Identify Original Resources** - Check README.md, CHANGELOG.md for resource list
2. **Verify Resources Valid** - Check URLs work, repos exist, APIs current
3. **Check for Changes** - Re-fetch docs, check for new features/deprecations
4. **Identify Additional Resources** - Any new official resources?
5. **Plan Updates** - List content to add/update/remove, decide placement
6. **Execute Updates** - Update outdated content, add new, remove deprecated
7. **Update Documentation** - Update version, CHANGELOG.md, README.md
8. **Validate** - Run skills-ref validate, test examples, check links
9. **Final Validation** - Complete consistency check

**Versioning for Updates:**
- **Patch (1.0.0 → 1.0.1)**: Minor fixes, updated examples
- **Minor (1.0.0 → 1.1.0)**: New features, expanded coverage
- **Major (1.0.0 → 2.0.0)**: Breaking changes, major restructuring

### Quick Validation Check

**When:** Verify existing skill compliance

```bash
# 1. Specification validation
skills-ref validate path/to/skill

# 2. Check SKILL.md size
wc -l path/to/skill/SKILL.md

# 3. Check for artifacts
ls -la path/to/skill/

# 4. Verify file structure
# Required: SKILL.md, README.md, LICENSE
# No: VALIDATION.md, .tmp files, .DS_Store
```

**Common Issues:**
- [ ] SKILL.md under 500 lines?
- [ ] No VALIDATION.md or build artifacts?
- [ ] All file references exist?
- [ ] .gitignore excludes artifacts?
- [ ] Version matches CHANGELOG?

### Planning Document Pattern

**For complex work:** Create PLANNING.md to track progress across sessions

**Template:**
```markdown
# [Skill Name] Planning

**Workflow Mode**: REFACTOR / IMPROVE / UPDATE
**Goal**: [What you're achieving]

## Issues Identified
- Issue 1: [problem and solution]
- Issue 2: [problem and solution]

## Implementation Plan
- [ ] Task 1
- [ ] Task 2

## Decisions & Notes
- Key decisions and rationale
```

**Remember:** Delete PLANNING.md before final commit (add to .gitignore)

**Benefits:** Maintains context, tracks progress, becomes source for CHANGELOG.md

## Troubleshooting

### Problem: Validation fails with "name doesn't match directory"

**Solution**: Ensure the directory name exactly matches the `name` field in SKILL.md frontmatter. Both must be lowercase with hyphens only.

```bash
# If validation says: "Directory name 'PDF-Processing' doesn't match skill name 'pdf-processing'"
mv PDF-Processing pdf-processing
```

### Problem: SKILL.md is too large (> 500 lines)

**Solution**: Move detailed content to references/:
- API documentation → `references/API_REFERENCE.md`
- Long examples → `references/EXAMPLES.md`
- Technical details → `references/TECHNICAL.md`

Keep SKILL.md focused on core instructions and reference these files.

### Problem: Description too vague, agent doesn't activate skill

**Solution**: Add specific keywords and use cases to description:
- ❌ "Helps with PDFs"
- ✅ "Extract text from PDF files, fill forms, merge documents. Use when working with PDF documents or user mentions PDFs, forms, extraction."

### Problem: Can't fetch GitHub repository content

**Solution**: 
1. Check if repo is public (private repos need authentication)
2. Use raw GitHub URLs for direct file access: `https://raw.githubusercontent.com/user/repo/main/file.md`
3. Ensure fetch_webpage tool has network access

### Problem: Resources conflict or show different approaches

**Solution**: Ask user for clarification:
- "I found two different authentication methods. Which should I use?"
- "The documentation shows approach A but the examples use approach B. Which is preferred?"

## Common Patterns and Anti-Patterns

### ✅ Good Practices

- **Progressive disclosure**: Start with SKILL.md only, add complexity as needed
- **Concrete examples**: Show actual code/commands with expected output
- **Clear scope**: One skill = one well-defined capability
- **Validation-ready**: Follow naming rules and structure from the start
- **Self-documenting**: Someone should understand the skill by reading SKILL.md

### ❌ Anti-Patterns to Avoid

- **Vague descriptions**: "Helps with coding" instead of "Generates Python unit tests following pytest conventions"
- **Monolithic skills**: Trying to do too much in one skill (split into multiple skills)
- **Heavy SKILL.md**: Putting 2000 lines of reference docs in SKILL.md (use references/)
- **Unclear structure**: Random mix of instructions, examples, and references
- **Missing validation**: Not checking naming rules and frontmatter format
- **Implicit knowledge**: Assuming agents will "figure out" what to do

## Detailed References

For comprehensive information, see these reference files:

- **[VALIDATION_RULES.md](references/VALIDATION_RULES.md)**: Complete validation rules and requirements
- **[BEST_PRACTICES.md](references/BEST_PRACTICES.md)**: Writing effective skills and agent-friendly instructions
- **[ORGANIZATIONAL_PATTERNS.md](references/ORGANIZATIONAL_PATTERNS.md)**: File organization and proactive agent behavior
- **[SPECIFICATION.md](references/SPECIFICATION.md)**: Full Agent Skills specification summary

## Example Skills

See the `examples/` directory for complete skill examples at different complexity levels:

1. **`examples/code-review/`**: Simple skill (SKILL.md only) for code review best practices
2. **`examples/api-integration/`**: Medium complexity skill with references/ for REST API integration

## Practical Walkthrough Example

**Scenario**: User asks "Create a skill for working with the Stripe API"

**Step 1 - Gather requirements:**
```plaintext
Agent: "I'll help you build a Stripe API skill. A few questions:
1. What Stripe operations should this cover? (payments, subscriptions, customers, etc.)
2. Do you have documentation URLs to analyze?
3. Should this include example code or just guidance?"

User provides: https://stripe.com/docs/api
```

**Step 2 - Resource gathering:**
```plaintext
Agent fetches:
- https://stripe.com/docs/api (main page)
- https://stripe.com/docs/api/authentication
- https://stripe.com/docs/api/charges
- Examples from docs

Extracts: authentication patterns, common endpoints, error codes
```

**Step 3 - Design structure:**
```plaintext
Decision: Level 2 (SKILL.md + references/)
- SKILL.md: Core instructions for authentication and common operations
- references/API_REFERENCE.md: Full endpoint documentation
- references/ERROR_CODES.md: Stripe error handling
```

**Step 4 - Create SKILL.md:**
```yaml
---
name: stripe-api-integration
description: Integrate with Stripe API for payments, subscriptions, and customer management. Use when working with Stripe, processing payments, or user mentions Stripe API, charges, subscriptions.
compatibility: Requires Stripe API key, curl or HTTP client
---
```

**Step 5 - Validate:**
```bash
skills-ref validate stripe-api-integration/
✓ Name valid: stripe-api-integration
✓ Description includes keywords: API, payments, Stripe
✓ Directory name matches
✓ Frontmatter valid
```

**Result**: Production-ready skill in ~367 lines, under 500 line limit, with references for detailed docs.

## Additional Resources

- [Agent Skills Website](https://agentskills.io)
- [Specification](https://agentskills.io/specification)
- [Example Skills Repository](https://github.com/anthropics/skills)
- [Reference Library](https://github.com/agentskills/agentskills/tree/main/skills-ref)

---

**Need help?** If you're stuck or need clarification while building a skill, ask! I can:
- Analyze additional resources
- Clarify ambiguous documentation
- Suggest better structure or organization
- Help validate your skill against the spec
- Provide more examples or templates
