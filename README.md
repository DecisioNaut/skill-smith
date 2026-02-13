# Agent Builder Skill

**Build best-practice Agent Skills from online resources with systematic guidance and validation.**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Compatible-green.svg)](https://agentskills.io)

## Overview

The Agent Builder Skill helps you create high-quality [Agent Skills](https://agentskills.io) that follow the official specification. It guides you through resource gathering, skill structure design, validation, and packaging - turning documentation websites, GitHub repositories, and API references into actionable, specification-compliant skills.

**Key Features:**
- 📚 **Systematic Resource Gathering**: Templates for analyzing repos, docs, and APIs
- 🏗️ **Structure Guidance**: Choose the right complexity level (simple/medium/full)
- ✅ **Built-in Validation**: Verify compliance with Agent Skills specification
- 🎯 **Best Practices**: Learn agent-friendly instruction writing
- 🤖 **Interactive Support**: Prompts for requesting additional context
- 📦 **Ready to Share**: GitHub-ready structure with complete documentation

## Quick Start

### For AI Agents

If you're an AI agent with skills support:

1. Add this skill to your skills directory
2. Activate when the user wants to build a new skill
3. Follow the step-by-step process in [SKILL.md](SKILL.md)

### For Manual Use

If you're building skills manually:

1. Read [SKILL.md](SKILL.md) for the complete guide
2. Use [resource templates](assets/resource-templates.md) to gather context
3. Run `python scripts/generate_skill.py --name my-skill --description "..."` to scaffold
4. Validate with `python scripts/validate_skill.py path/to/skill`

## What's Included

### Core Skill (SKILL.md)

The main [SKILL.md](SKILL.md) file provides comprehensive step-by-step instructions for:
- Gathering and analyzing resources (repos, docs, APIs)
- Designing skill structure (3 complexity levels)
- Writing effective SKILL.md files with best practices
- Validating against the specification
- Adding scripts, references, and assets
- Testing and packaging for distribution

### Reference Documentation

Detailed references for deep dives:
- **[VALIDATION.md](references/VALIDATION.md)** - Complete validation rules and requirements
- **[BEST_PRACTICES.md](references/BEST_PRACTICES.md)** - Writing effective agent-friendly skills
- **[SPECIFICATION.md](references/SPECIFICATION.md)** - Agent Skills specification summary

### Tools & Scripts

Practical utilities included:
- **[validate_skill.py](scripts/validate_skill.py)** - Validate skills against specification
- **[generate_skill.py](scripts/generate_skill.py)** - Generate new skill from template

### Templates & Assets

Resource gathering templates:
- **[resource-templates.md](assets/resource-templates.md)** - 7 templates for systematic analysis

### Example Skills

Three complete examples at different complexity levels:
1. **[code-review/](examples/code-review/)** - Code review (SKILL.md only)
2. **[api-integration/](examples/api-integration/)** - API integration (with references/)
3. *(Complex example with scripts/ coming soon)*

## Usage Examples

### Example 1: Building a Simple Skill

```bash
# Generate scaffold
python scripts/generate_skill.py \
  --name markdown-formatter \
  --description "Format and lint Markdown files following best practices" \
  --complexity simple

# Edit the SKILL.md
cd markdown-formatter/
# ... add your instructions ...

# Validate
python ../scripts/validate_skill.py .
```

### Example 2: Building from Documentation

When building a skill from a documentation website:

1. Use the [Documentation Website Analysis template](assets/resource-templates.md#template-2-documentation-website-analysis)
2. Extract core concepts, common operations, and examples
3. Structure the skill based on workflow complexity
4. Reference detailed docs in `references/` if needed

### Example 3: Interactive Resource Gathering

When working with an AI agent:

**User:** "Build a skill for working with the Stripe API"

**Agent (using this skill):**
1. Asks for documentation URLs
2. Requests example repositories
3. Clarifies authentication requirements
4. Identifies common use cases
5. Builds structured skill with validation

## Repository Structure

```
agent-builder-skill/
├── SKILL.md                    # Main skill instructions
├── README.md                   # This file
├── LICENSE                     # Apache 2.0 license
├── CONTRIBUTING.md             # Contribution guidelines
├── CHANGELOG.md                # Version history
├── scripts/
│   ├── validate_skill.py       # Validation tool
│   └── generate_skill.py       # Skill generator
├── references/
│   ├── VALIDATION.md           # Validation reference
│   ├── BEST_PRACTICES.md       # Best practices guide
│   └── SPECIFICATION.md        # Specification summary
├── assets/
│   └── resource-templates.md   # Resource gathering templates
└── examples/
    ├── code-review/            # SKILL.md only example
    └── api-integration/        # With references/ example
```

## Validation

Validate any skill against the official specification:

```bash
# Validate a skill
python scripts/validate_skill.py path/to/your-skill/

# Or validate the current directory
python scripts/validate_skill.py .
```

**What's checked:**
- SKILL.md exists and has valid YAML frontmatter
- Name follows format rules (lowercase, kebab-case, 1-64 chars)
- Description is 1-1024 characters with clear intent
- Directory name matches skill name
- All optional fields are valid
- Referenced files exist

## Agent Skills Specification

This skill follows the [Agent Skills specification](https://agentskills.io/specification) v1.0:

- **Required**: `SKILL.md` with YAML frontmatter (`name`, `description`)
- **Optional**: `scripts/`, `references/`, `assets/` directories
- **Format**: YAML frontmatter + Markdown body
- **Naming**: lowercase, kebab-case, 1-64 characters
- **Progressive Disclosure**: Load metadata → instructions → resources as needed

## Use Cases

This skill helps you build skills for:

**Development Tools**
- Working with specific APIs or libraries
- Code generation and transformation
- Testing and quality assurance
- Deployment and CI/CD

**Data & Analysis**
- Data processing pipelines
- Statistical analysis
- Visualization and reporting
- Database operations

**Content & Communication**
- Document generation
- Content formatting
- Email and notification handling
- Translation and localization

**Domain Expertise**
- Legal document review
- Financial analysis
- Medical terminology
- Technical writing

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Ways to contribute:**
- Add more example skills
- Improve validation logic
- Enhance resource templates
- Update documentation
- Report issues or suggest features

## Resources

**Official Agent Skills:**
- [Agent Skills Website](https://agentskills.io)
- [Specification](https://agentskills.io/specification)
- [Example Skills](https://github.com/anthropics/skills)
- [Best Practices Guide](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

**Tools:**
- [skills-ref Library](https://github.com/agentskills/agentskills/tree/main/skills-ref) - Official Python library for validation and utilities

**Community:**
- [GitHub Discussions](https://github.com/agentskills/agentskills/discussions)
- [Contributing Guide](https://github.com/agentskills/agentskills/blob/main/CONTRIBUTING.md)

## License

Apache 2.0 - See [LICENSE](LICENSE) for details.

This skill is designed to help build skills compatible with the open [Agent Skills specification](https://agentskills.io), originally developed by [Anthropic](https://www.anthropic.com/) and maintained as an open standard.

## Acknowledgments

- Built using the [Agent Skills specification](https://agentskills.io)
- Inspired by the [skills-ref reference implementation](https://github.com/agentskills/agentskills/tree/main/skills-ref)
- Follows best practices from the [Anthropic skills repository](https://github.com/anthropics/skills)

---

**Ready to build your first skill?** Start with [SKILL.md](SKILL.md) or run:

```bash
python scripts/generate_skill.py --name my-first-skill --description "Your skill description here"
```

Questions? Check the [FAQ](#faq) below or open an [issue](../../issues).

## FAQ

**Q: Do I need to use all three directories (scripts/, references/, assets/)?**  
A: No! Start with just SKILL.md. Add directories only when needed. 80% of skills are SKILL.md only.

**Q: Can I use this skill to build skills in languages other than English?**  
A: Yes! The specification supports Unicode in skill names and descriptions. Instructions can be in any language.

**Q: How do I test if my skill works with agents?**  
A: The best way is to give your skill to an agent and ask it to perform relevant tasks. Observe where it succeeds or gets confused, then refine.

**Q: What if the skill needs to be updated later?**  
A: Update the SKILL.md, increment the version in metadata, document changes in a CHANGELOG.md, and tag the release in git.

**Q: Can I sell or commercialize skills built with this?**  
A: Yes! Skills you create are yours. This builder skill is Apache 2.0 licensed, so you're free to use it commercially.

**Q: My skill needs to access external services. How do I handle that?**  
A: Document prerequisites clearly in SKILL.md. Never hardcode credentials - use environment variables. Consider adding a `compatibility` field noting requirements.

**Q: How detailed should the description be?**  
A: Strike a balance: clear enough for discovery, concise enough to scan. Include WHAT the skill does, WHEN to use it, and relevant KEYWORDS. See [examples](examples/) for reference.

**Q: Can I combine multiple related skills into one?**  
A: Generally, keep skills focused (one capability per skill). If operations are closely related and share context, they can be combined. Err on the side of splitting.

**Q: What's the difference between this and just writing documentation?**  
A: Skills are action-oriented, structured for agent consumption, and progressively loaded. They're instructions for *doing*, not just reference material.