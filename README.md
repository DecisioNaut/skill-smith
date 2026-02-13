# Skill Smith

Build specification-compliant Agent Skills from documentation sites, GitHub repos, and APIs. Systematically gather resources, design SKILL.md structure, validate naming rules, and package for sharing.

## What is This?

This skill helps AI agents (and developers) create high-quality [Agent Skills](https://agentskills.io) that follow the v1.0 specification. It provides step-by-step guidance for:

- Gathering resources from documentation sites, GitHub repos, APIs
- Designing clear, agent-friendly instructions
- Structuring skills with progressive disclosure
- Validating compliance with the specification
- Creating examples, references, and scripts

## Features

- ✅ **Specification-compliant**: Follows Agent Skills v1.0 spec precisely
- ✅ **Comprehensive resource gathering**: Multi-page documentation exploration
- ✅ **Progressive disclosure**: Efficient context management
- ✅ **Validation support**: Uses official skills-ref library
- ✅ **Best practices**: Agent-friendly writing patterns
- ✅ **Examples included**: Simple and complex skill examples
- ✅ **Templates provided**: GitHub, docs, API analysis templates

## Quick Start

### Installation

1. **Add to your agent skills folder**:
   ```bash
   # Clone or copy this skill to your workspace
   mkdir -p .agents/skills
   cp -r skill-smith .agents/skills/
   ```

2. **Verify installation**:
   ```bash
   ls .agents/skills/skill-smith/SKILL.md
   ```

3. **Install validation tool** (optional):
   ```bash
   pip install -e git+https://github.com/agentskills/agentskills.git#egg=skills-ref&subdirectory=skills-ref
   ```

### Usage

#### For AI Agents

When an agent has access to this skill, it will automatically activate when you mention:
- "Create a skill for..."
- "Build an agent skill..."
- "Help me develop a skill..."
- "I need a skill that..."

The agent will follow the 8-step process defined in `SKILL.md`.

#### For Developers

1. **Read the main instructions**:
   ```bash
   cat .agents/skills/skill-smith/SKILL.md
   ```

2. **Review examples**:
   - Simple: `examples/code-review-helper/SKILL.md`
   - Complex: `examples/stripe-api-integration/SKILL.md`

3. **Use resource templates**:
   ```bash
   cat assets/resource-templates.md
   ```

4. **Check best practices**:
   ```bash
   cat references/BEST_PRACTICES.md
   ```

5. **Validate your skill**:
   ```bash
   skills-ref validate /path/to/your-skill
   ```

## Skill Structure

```
skill-smith/
├── SKILL.md                    # Main instructions (< 500 lines)
├── references/                 # Detailed references
│   ├── SPECIFICATION.md        # Agent Skills spec summary
│   ├── VALIDATION.md           # Validation rules
│   └── BEST_PRACTICES.md       # Agent-friendly writing tips
├── assets/                     # Templates and resources
│   └── resource-templates.md   # GitHub/docs/API analysis templates
├── examples/                   # Example skills
│   ├── code-review-helper/     # Simple example
│   └── stripe-api-integration/ # Complex example with references
├── README.md                   # This file
├── LICENSE                     # MIT License
├── CONTRIBUTING.md             # Contribution guidelines
└── CHANGELOG.md                # Version history
```

## How It Works

### The 8-Step Process

1. **Clarify Requirements** - Understand what the skill should do
2. **Gather Resources** - Systematically collect documentation, examples, code
3. **Design Structure** - Plan SKILL.md with progressive disclosure
4. **Write SKILL.md** - Create clear, agent-friendly instructions
5. **Validate** - Check compliance with specification
6. **Add Optional Components** - Scripts, references, assets, examples
7. **Create Documentation** - README, LICENSE, etc.
8. **Final Validation** - Verify everything works

See [SKILL.md](SKILL.md) for complete details.

### Progressive Disclosure

Agent Skills use progressive disclosure for efficient context management:

- **Level 1**: Name + description (~50-100 tokens) - Loaded at startup
- **Level 2**: Full SKILL.md (~5000 tokens) - Loaded when skill activates  
- **Level 3**: References, scripts, assets - Loaded on-demand

This allows agents to discover skills quickly without loading full documentation upfront.

## Examples

### Simple Skill: Code Review Helper

A minimal skill showing basic structure:
- Single SKILL.md file
- No external references
- Direct, actionable instructions
- Common language-specific patterns

See: [examples/code-review-helper/](examples/code-review-helper/)

### Complex Skill: Stripe API Integration

A comprehensive skill demonstrating:
- SKILL.md with references
- Separate reference files
- Multiple examples
- Error handling patterns
- Testing strategies

See: [examples/stripe-api-integration/](examples/stripe-api-integration/)

## Key Concepts

### Agent-Friendly Writing

Write instructions for literal interpretation:

❌ **Vague**: "You might want to check if the file exists."
✅ **Clear**: "1. Check if file exists: `test -f filename`"

See [references/BEST_PRACTICES.md](references/BEST_PRACTICES.md) for more patterns.

### File Size Guidelines

- **SKILL.md**: < 500 lines (~5000 tokens)
- **Reference files**: < 1000 lines each
- **Name + description**: ~50-100 tokens

### File References (One Level Deep)

Reference files directly from SKILL.md. Avoid chains:

✅ Good: `SKILL.md` → `references/API.md`
❌ Bad: `SKILL.md` → `references/OVERVIEW.md` → `details/API.md`

### Validation

Use official skills-ref library:

```bash
# Validate skill structure
skills-ref validate path/to/skill

# Extract properties
skills-ref read-properties path/to/skill

# Convert to prompt format
skills-ref to-prompt path/to/skill
```

See [references/VALIDATION.md](references/VALIDATION.md) for complete rules.

## FAQ

### Q: Where should I install skills?

**A**: In the `.agents/skills/` directory at your workspace root. This is the convention for agent skills discovery.

```bash
workspace/
└── .agents/
    └── skills/
        └── your-skill-name/
            └── SKILL.md
```

### Q: How do I validate my skill?

**A**: Use the official skills-ref library:

```bash
pip install -e git+https://github.com/agentskills/agentskills.git#egg=skills-ref&subdirectory=skills-ref
skills-ref validate path/to/your-skill
```

Don't write custom validation scripts - use the official tool.

### Q: What license should I use?

**A**: MIT is recommended for maximum permissiveness and compatibility. This skill uses MIT.

### Q: Can I use scripts/ for validation?

**A**: No. The scripts/ directory is for domain-specific executable code (data processing, API wrappers, etc.), NOT for specification validation. Use the official skills-ref library for validation.

### Q: How long should SKILL.md be?

**A**: Keep it under 500 lines (approximately 5000 tokens). Move detailed documentation to `references/` files.

### Q: Should I bundle dependencies?

**A**: No. List dependencies in prerequisites and let users install them. Don't bundle external libraries or tools.

### Q: How do I handle multiple programming languages?

**A**: Either:
1. Create separate skills per language (recommended)
2. Use sections in one skill with clear language-specific instructions

### Q: Can I reference external URLs?

**A**: Yes, but provide enough context in SKILL.md that users can complete tasks without visiting URLs. External links are supplementary.

### Q: How do I test my skill?

**A**: 
1. Follow the instructions literally (don't assume steps)
2. Test with an AI agent if possible
3. Run: `skills-ref validate path/to/skill`
4. Check that examples actually work

### Q: How do I share my skill?

**A**: 
1. Create a Git repository
2. Include README, LICENSE, examples
3. Validate with skills-ref
4. Share the repository URL
5. Users can clone to their `.agents/skills/` directory

### Q: What's the difference between references/ and assets/?

**A**:
- `references/`: Text documentation (API docs, guides, troubleshooting)
- `assets/`: Template files, diagrams, sample data, lookup tables

### Q: How do I gather resources from documentation sites?

**A**: Use the fetch_webpage tool systematically:
1. Fetch homepage
2. Identify navigation structure
3. Fetch each major section
4. Fetch sub-pages (don't stop at index pages)
5. Continue until comprehensive

See [assets/resource-templates.md](assets/resource-templates.md) for detailed templates.

## Troubleshooting

### Validation Fails with "Invalid name format"

**Problem**: Skill name doesn't follow naming rules

**Solution**: 
- Use only lowercase letters and hyphens
- 1-64 characters
- No consecutive hyphens
- No leading/trailing hyphens
- Directory name must match skill name

Example: `my-api-skill` ✅, `My-API-Skill` ❌, `my_api_skill` ❌

### "Description too long" Error

**Problem**: Description exceeds 1024 characters

**Solution**: Shorten description to essential "what" and "when" information. Full details go in SKILL.md body.

### Agent Doesn't Find My Skill

**Problem**: Skill not discovered by agent

**Solution**:
- Ensure skill is in `.agents/skills/` directory
- Verify SKILL.md has valid YAML frontmatter
- Check that `name` and `description` fields are present
- Restart agent to reload skills

### SKILL.md Too Long

**Problem**: SKILL.md exceeds 500 lines

**Solution**: Move detailed content to `references/`:
- API documentation → `references/API.md`
- Error codes → `references/ERRORS.md`
- Extended examples → `references/EXAMPLES.md`
- Best practices → `references/BEST_PRACTICES.md`

### Unclear When Skill Should Activate

**Problem**: Agent doesn't know when to use the skill

**Solution**: Add specific keywords to description:
```yaml
description: Analyzes CSV files. Use when working with CSV, data analysis, tabular data, or when user mentions pandas, Excel exports.
```

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Quick contribution workflow:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with skills-ref
5. Submit a pull request

## Resources

### Official Documentation
- [Agent Skills Specification](https://agentskills.io/specification)
- [Integration Guide](https://agentskills.io/integrate-skills)
- [skills-ref Library](https://github.com/agentskills/agentskills/tree/main/skills-ref)

### Reference Skills
- [Anthropic Skills Repository](https://github.com/anthropics/skills)
- [Agent Skills Examples](https://github.com/agentskills/agentskills/tree/main/examples)

### This Skill's Resources
- [Specification Summary](references/SPECIFICATION.md)
- [Validation Rules](references/VALIDATION.md)
- [Best Practices](references/BEST_PRACTICES.md)
- [Resource Templates](assets/resource-templates.md)
- [Code Review Example](examples/code-review-helper/)
- [Stripe API Example](examples/stripe-api-integration/)

## License

MIT License - see [LICENSE](LICENSE) file for details.

Free to use, modify, and distribute. Attribution appreciated but not required.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

## Support

- **Issues**: Open an issue for bugs or feature requests
- **Discussions**: Use GitHub Discussions for questions
- **Specification**: See https://agentskills.io for spec questions

## Acknowledgments

Built using the Agent Skills v1.0 specification from [agentskills.io](https://agentskills.io).

Inspired by the need for high-quality, specification-compliant agent skills that work reliably across different AI agents.

## Origin Story

Want to know how this skill came to be? Read [GENESIS.md](GENESIS.md) for the complete story of how this skill was built, refined through meta-testing, and ultimately rebuilt using its own instructions - the ultimate validation!

---

**Built with this skill**: This skill was rebuilt using its own instructions - the ultimate meta-test! ✨
