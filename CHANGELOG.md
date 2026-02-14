# Changelog

All notable changes to Skill Smith will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-02-14

### Added
- **Multiple workflow modes** in SKILL.md:
  - UPDATE workflow for refreshing skills from changed resources
  - REFACTOR workflow for improving skill structure
  - IMPROVE workflow for adding content/features
  - VALIDATE workflow for quick compliance checks
  - Planning Document Pattern for complex multi-session work
- **New reference files:**
  - references/REFACTORING_GUIDE.md - Refactoring patterns and examples
  - references/CONSISTENCY_CHECKLIST.md - Cross-file validation checklist
  - references/STANDARD_RESOURCES.md - Official templates and authoritative sources
- **Proactive agent behavior patterns** in references/BEST_PRACTICES.md:
  - Automatic checking triggers
  - Compliance Overview Pattern for presenting complete file status
  - Mode-specific behaviors for each workflow
  - Example interactions showing proactive recommendations
- **File structure guidance** in references/BEST_PRACTICES.md:
  - Required, recommended, and forbidden files clearly listed
  - Pre-commit file structure checklist
  - .gitignore template with all common artifacts
- **Reference organization patterns** in references/BEST_PRACTICES.md:
  - Naming conventions (ALL_CAPS.md format)
  - Size guidelines (150-1000 lines per file)
  - Splitting strategies (by complexity, functional area, use case)
  - Cross-referencing best practices
  - Real-world examples from devcontainer-expert and uv-expert
- **Resource documentation requirements**:
  - README.md resources section format
  - CHANGELOG.md resource tracking
- **Final validation step** added to all workflows

### Changed
- **BREAKING**: "When to Use This Skill" section now explicitly lists all workflow modes
- **BREAKING**: Agent behavior expectations changed - agents now check compliance proactively
- **BREAKING**: Validation now covers ALL files (SKILL.md, references/, assets/, examples/)
- Step 8 renamed to "8. Document and Package" with file structure validation
- Step 9 renamed to "9. Test and Final Validation" with comprehensive checks
- Step 3 enhanced with reference organization guidance
- SKILL.md size increased to 465 lines (justified by new workflows)
- Progressive disclosure now includes validation of reference file sizes

### Fixed
- Clarified that VALIDATION.md should NOT be committed (added to .gitignore template)
- Specified exact .gitignore patterns for skill-smith artifacts
- Added guidance on when NOT to split reference files

### Breaking Changes
- Skills created with v1.0.0 won't benefit from new workflows without manual adoption
- Agent behavior expectations changed from reactive to proactive
- Workflow invocation patterns expanded (now 5 modes instead of 1)

### Migration Guide
If you have existing skills:
1. Add .gitignore with artifact exclusions
2. Check reference file organization against new patterns
3. Validate file structure against new checklist
4. Consider which workflow mode applies when making changes

## [1.0.0] - 2026-02-13

### Added
- Initial release of Skill Smith
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
