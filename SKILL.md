---
name: agent-builder-skill
description: Build best-practice Agent Skills from online resources like documentation sites, repositories, and examples. Guides you through resource gathering, skill structure design, validation, and creating complete, specification-compliant skills ready for sharing.
license: MIT
metadata:
  version: "1.0.0"
  author: agent-builder-skill contributors
  compatibility: Designed for filesystem-based agents with web access
---

# Agent Builder Skill

This skill helps you create high-quality Agent Skills that follow the official [Agent Skills specification](https://agentskills.io/specification). Use this when you need to build new skills from online resources like documentation websites, open source repositories, API references, or example code.

## When to Use This Skill

Activate this skill when the user wants to:
- Create a new Agent Skill from online resources
- Build skills based on documentation websites or GitHub repositories
- Structure a skill following best practices and the official specification
- Validate existing skill implementations against the spec
- Package skills for sharing via GitHub or other platforms

## Overview of Agent Skills

Agent Skills are folders containing a `SKILL.md` file with instructions that teach agents how to perform specific tasks. They use **progressive disclosure**:

1. **Discovery**: Agents load only name and description at startup
2. **Activation**: When relevant, agents read the full SKILL.md
3. **Execution**: Agents follow instructions and access bundled resources as needed

### Directory Structure

```
skill-name/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: detailed documentation
└── assets/           # Optional: templates, data, images
```

## Building a New Skill: Step-by-Step Process

### 1. Gather Context and Requirements

Before building a skill, understand what you're building:

**Ask the user these questions:**

1. **What should the skill do?** (specific task or capability)
2. **What resources are available?** (documentation URLs, GitHub repos, API references)
3. **Who is the target user?** (developers, data analysts, specific domain experts)
4. **What's the expected complexity?** (simple instructions-only vs. scripts/assets needed)

**Use the Resource Gathering Templates** in `assets/resource-templates.md` to systematically collect:
- Documentation sites to analyze
- Example repositories to study
- API references or technical specs
- Existing similar skills for inspiration

### 2. Analyze Resources

For each resource provided:

**For GitHub Repositories:**
- Examine README.md for overview and setup instructions
- Review code structure and key files
- Look for examples/ or docs/ directories
- Note dependencies and requirements
- Identify common patterns and best practices

**For Documentation Sites:**
- Parse the navigation structure (what topics are covered?)
- Identify the most frequently referenced sections
- Extract code examples and common patterns
- Note any prerequisites or setup steps
- Look for quick-start guides vs. detailed references

**For API References:**
- Understand authentication and authorization
- Identify core endpoints and methods
- Note common request/response patterns
- Look for rate limits or usage constraints
- Find example code snippets

**Ask clarifying questions if:**
- Resources conflict or show different approaches
- Critical information is missing (authentication, error handling)
- The scope is unclear or too broad
- Dependencies or prerequisites aren't documented

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

**Level 3: Full Structure** (5% of skills)
- SKILL.md + scripts/ + references/ + assets/
- Good for: executable workflows, data processing, multi-step automation
- Example: data-analysis-skill with Python scripts and templates

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
license: Apache-2.0            # or path to LICENSE.txt
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

- See [REFERENCE.md](references/REFERENCE.md) for detailed API documentation
- See [FORMS.md](references/FORMS.md) for request/response templates
```

**Writing Best Practices:**

1. **Use clear, actionable language**: Prefer direct instructions ("Run the script") over vague guidance ("You might want to consider running")

2. **Include concrete examples**: Show actual code, commands, or data rather than just describing them

3. **Structure for scanning**: Use headings, lists, and code blocks. Agents should quickly find relevant sections

4. **Front-load important info**: Put the most critical instructions early

5. **Be specific about edge cases**: Don't assume agents will infer error handling or special cases

6. **Keep main SKILL.md under 500 lines**: Move detailed reference material to references/

7. **Test readability**: Instructions should be clear if read by a human OR an agent

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

**Use validation script:**
See `scripts/validate_skill.py` for automated validation against the specification.

### 6. Add Optional Components

**scripts/ directory:**
- Create executable code that agents can run
- Include clear error messages and help text
- Document dependencies at the top of each script
- Use common scripting languages (Python, Bash, JavaScript)
- Name scripts descriptively: `extract_data.py`, not `script1.py`

**references/ directory:**
- `REFERENCE.md`: Detailed technical reference (API docs, function signatures)
- `FORMS.md`: Templates for structured data (JSON schemas, API request formats)
- Domain-specific files: `database.md`, `authentication.md`, etc.
- Keep files focused and under 1000 lines each

**assets/ directory:**
- Document templates (.md, .txt, .json)
- Configuration examples
- Diagrams or visual aids (.png, .svg)
- Sample data for testing

### 7. Test the Skill

**Manual testing:**
1. Try to use the skill yourself to accomplish the task
2. Follow instructions literally - don't assume implied steps
3. Test with common use cases and edge cases
4. Verify that referenced files are accessible and clear

**Agent testing (if possible):**
1. Give an agent access to the skill
2. Ask it to perform relevant tasks
3. Observe where it gets confused or stuck
4. Refine instructions based on agent behavior

### 8. Document and Package

**Update README.md:** (see examples in `examples/`)
- Describe what the skill does
- Show installation/usage instructions
- Link to the main SKILL.md
- Include examples of tasks it can help with
- Credit sources and provide relevant links

**Prepare for sharing:**
- Ensure LICENSE file is present
- Add .gitignore for temporary files
- Write CONTRIBUTING.md if accepting contributions
- Tag version if using git: `git tag v1.0.0`

## Interactive Resource Gathering

When building a skill, if you need more context or resources, **ask the user** these structured questions:

### About the Skill Scope

- "What specific tasks should this skill enable? Please list 3-5 concrete examples."
- "Are there existing skills or tools that do something similar?"
- "What level of expertise should users have? (beginner, intermediate, expert)"

### About Resources

- "Can you provide links to:
  - Official documentation website
  - GitHub repositories with examples
  - API references or technical specifications
  - Tutorials or guides"
- "Are there any required accounts, API keys, or paid services?"
- "What programming languages or tools does this skill involve?"

### About Constraints

- "Are there platform requirements? (OS, specific agents, network access)"
- "Should this skill create files, run commands, or just provide guidance?"
- "Are there security considerations? (API keys, sensitive data, sandboxing)"

### About Validation

- "Can I test this skill with a real example?"
- "What would success look like? Can you describe an ideal outcome?"
- "Are there common mistakes or failure modes to watch for?"

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

- **[VALIDATION.md](references/VALIDATION.md)**: Complete validation rules and requirements
- **[BEST_PRACTICES.md](references/BEST_PRACTICES.md)**: Writing effective skills and agent-friendly instructions
- **[SPECIFICATION.md](references/SPECIFICATION.md)**: Full Agent Skills specification summary

## Quick Reference: SKILL.md Template

Use this as a starting point:

```markdown
---
name: my-skill-name
description: What this skill does and when agents should use it. Be specific and include keywords.
---

# My Skill Name

Brief overview of what this skill enables.

## When to Use This Skill

Use this skill when:
- [Clear criterion 1]
- [Clear criterion 2]

## Prerequisites

- [Required tool or access]
- [Another requirement]

## Instructions

### Step 1: [Action Name]

1. [Specific step]
2. [Another specific step]

### Step 2: [Next Action]

[Continue...]

## Examples

### Example: [Common Use Case]

Input:
\`\`\`
[Sample input]
\`\`\`

Output:
\`\`\`
[Expected output]
\`\`\`

## Troubleshooting

**Issue:** [Common problem]
**Solution:** [How to fix]
```

## Example Skills

See the `examples/` directory for complete skill examples at different complexity levels:

1. **`examples/code-review/`**: Simple skill (SKILL.md only) for code review best practices
2. **`examples/api-integration/`**: Medium complexity skill with references/ for REST API integration

## Additional Resources

- [Agent Skills Website](https://agentskills.io)
- [Specification](https://agentskills.io/specification)
- [Example Skills Repository](https://github.com/anthropics/skills)
- [Reference Library](https://github.com/agentskills/agentskills/tree/main/skills-ref)
- [Best Practices Guide](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

---

**Need help?** If you're stuck or need clarification while building a skill, ask! I can:
- Analyze additional resources
- Clarify ambiguous documentation
- Suggest better structure or organization
- Help validate your skill against the spec
- Provide more examples or templates
