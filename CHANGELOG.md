# Changelog

All notable changes to the Agent Builder Skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2024-01-XX

### Changed
- **BREAKING**: Updated validation approach to use official skills-ref library instead of custom scripts
- Clarified scripts/ directory purpose: domain-specific code only, not spec validation
- Enhanced resource gathering instructions with explicit multi-page exploration guidance
- Improved description with specific trigger keywords
- Restructured to follow own improved methodology

### Added
- Comprehensive troubleshooting section (5 common problems with solutions)
- Security considerations section
- Practical Stripe API walkthrough example
- Complete reference documentation (SPECIFICATION.md, VALIDATION.md, BEST_PRACTICES.md)
- Resource gathering templates for GitHub, docs sites, APIs, CLIs
- Two complete example skills (code-review-helper, stripe-api-integration)
- Progressive disclosure diagram and explanation
- Best practices for agent-friendly writing
- FAQ section in README
- Contributing guidelines

### Fixed
- Removed unnecessary custom validation scripts
- Clarified file reference guidelines (one level deep)
- Updated all examples to use skills-ref validate
- Improved SKILL.md to stay under 500 line guideline (487 lines)

### Improved
- Step-by-step process now more explicit about using fetch_webpage for multi-page docs
- Validation step references official tools with installation instructions
- Description now includes comprehensive "when to use" keywords
- Better distinction between references/ (docs) and assets/ (templates)

## [1.0.0] - 2024-01-XX

### Added
- Initial release of Agent Builder Skill
- Complete 7-step process for building agent skills
- SKILL.md with basic instructions
- Basic references directory
- Simple validation script
- MIT License
- Basic README
- Installation instructions for .agents/skills/

### Features
- Resource gathering guidance
- SKILL.md structure design
- Validation support
- Progressive disclosure explanation
- Basic examples

---

## Release Notes

### Version 2.0.0 - The Meta Release

This version was created by **using the skill to rebuild itself** - the ultimate validation that the instructions actually work! Key improvements focus on:

1. **Official Tool Integration**: Reference skills-ref library instead of bundling custom validation
2. **Enhanced Resource Gathering**: Explicit multi-page exploration instructions
3. **Comprehensive Documentation**: Added troubleshooting, security, examples
4. **Progressive Disclosure**: Clear explanation with practical examples
5. **Best Practices**: Agent-friendly writing patterns codified

This release represents a complete refinement of the methodology through practical application.

### Version 1.0.0 - Initial Release

First public release providing the foundation for building specification-compliant agent skills. Includes core process, basic validation, and essential documentation.
