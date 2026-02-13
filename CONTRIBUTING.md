# Contributing to Agent Builder Skill

Thank you for your interest in contributing! This document provides guidelines for contributing to the Agent Builder Skill project.

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion:

1. **Check existing issues** to avoid duplicates
2. **Open a new issue** with:
   - Clear, descriptive title
   - Detailed description of the problem or suggestion
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Environment details (if relevant)

### Suggesting Enhancements

For new features or improvements:

1. **Open an issue** describing:
   - The enhancement you'd like to see
   - Why it would be useful
   - How it fits with the Agent Skills specification
   - Example use cases

2. **Wait for discussion** before implementing large changes

### Code Contributions

#### Getting Started

1. **Fork the repository**
2. **Clone your fork**:
   ```bash
   git clone https://github.com/your-username/agent-builder-skill.git
   cd agent-builder-skill
   ```

3. **Create a branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

#### Making Changes

1. **Follow the specification**: All changes must comply with Agent Skills v1.0
2. **Keep SKILL.md focused**: Stay under 500 lines
3. **Use progressive disclosure**: Move details to references/
4. **Write agent-friendly prose**: Clear, literal, actionable instructions
5. **Include examples**: Show concrete usage patterns
6. **Test your changes**: Follow the instructions literally

#### Testing Checklist

Before submitting:

- [ ] SKILL.md is under 500 lines
- [ ] Validation passes: `skills-ref validate .`
- [ ] All referenced files exist
- [ ] Examples are complete and correct
- [ ] Instructions are clear and unambiguous
- [ ] Followed the instructions yourself to verify they work
- [ ] No typos or formatting errors

#### Validation

Always validate your changes:

```bash
# Install skills-ref if needed
pip install -e git+https://github.com/agentskills/agentskills.git#egg=skills-ref&subdirectory=skills-ref

# Validate the skill
skills-ref validate .

# Check properties
skills-ref read-properties .
```

#### Commit Messages

Use clear, descriptive commit messages:

```
feat: add troubleshooting section for API errors

- Added common API error patterns
- Included resolution steps
- Added examples for each error type
```

**Format**:
- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `refactor:` - Code restructuring
- `test:` - Test additions or changes
- `chore:` - Maintenance tasks

#### Pull Requests

1. **Push your branch**:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Open a Pull Request** with:
   - Clear title describing the change
   - Detailed description of what and why
   - Link to related issues
   - Screenshots/examples if applicable
   - Confirmation that validation passes

3. **Respond to feedback**: Be open to suggestions and iterate

### Documentation Contributions

Improvements to documentation are always welcome:

- Fix typos or unclear instructions
- Add examples or use cases
- Improve explanations
- Expand references

**Documentation changes don't require issue discussion** - just open a PR!

## Style Guidelines

### SKILL.md Writing Style

Follow these patterns:

**Use imperative, active voice**:
```markdown
✅ Create a new file
❌ A new file should be created
```

**Be concrete and specific**:
```markdown
✅ Run: `pip install stripe`
❌ Install the required package
```

**Break down complex tasks**:
```markdown
✅ 
1. Open config.yaml
2. Set api_key to your key
3. Save the file

❌ Configure the API key
```

**Handle errors explicitly**:
```markdown
✅ 
If the file doesn't exist:
  Create it: `touch config.yaml`
  
❌ Make sure the file exists
```

### Reference File Guidelines

- **Stay focused**: One topic per file
- **Use headers**: Clear hierarchy with ##, ###
- **Include examples**: Show, don't just tell
- **Keep under 1000 lines**: Split if longer
- **Link back to SKILL.md**: Reference where it's used

### Code Style

For scripts/:
- **Python**: Follow PEP 8, use type hints
- **Shell**: Use bash, include error checking
- **JavaScript**: Use modern ES6+ syntax

For examples/:
- **Complete**: Can be run as-is
- **Commented**: Explain non-obvious parts
- **Realistic**: Show real-world usage

## Review Process

1. **Initial review**: Maintainer checks compliance with guidelines
2. **Validation**: Verify skills-ref validation passes
3. **Testing**: Follow instructions to ensure they work
4. **Feedback**: Request changes if needed
5. **Approval**: Merge when ready

**Timeline**: Expect initial review within 1 week. Be patient, maintainers work on this in their spare time.

## Community Guidelines

### Be Respectful

- **Assume good intent** from contributors
- **Provide constructive feedback**, not criticism
- **Be patient** with new contributors
- **Welcome diverse perspectives**

### Focus on Quality

- **Specification compliance** is non-negotiable
- **Agent-friendly writing** is essential
- **Working examples** are required
- **Clear instructions** are paramount

### Help Others

- **Answer questions** in issues and discussions
- **Review pull requests** when you can
- **Share your experience** with the skill
- **Improve documentation** based on confusion points

## Recognition

Contributors are recognized in:
- Git commit history
- Pull request acknowledgments
- Release notes (for significant contributions)
- README (for major features)

## Questions?

- **Specification questions**: See https://agentskills.io
- **Contribution questions**: Open an issue with "Question:" prefix
- **General discussion**: Use GitHub Discussions

## License

By contributing, you agree that your contributions will be licensed under the MIT License, the same license as this project.

## Getting Help

If you're stuck:

1. **Read the specification**: https://agentskills.io
2. **Check references/**: Detailed guides are there
3. **Look at examples/**: See how it's done
4. **Open an issue**: We're happy to help!

## Thank You!

Every contribution, no matter how small, helps make this skill better for everyone. We appreciate your effort and look forward to your contributions! 🎉
