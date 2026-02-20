# Standard External Resources

**Reference for:** Authoritative external sources for licenses, formats, and standards used in Agent Skills

> **Related:** See [BEST_PRACTICES.md](./BEST_PRACTICES.md) for usage patterns and [SPECIFICATION.md](./SPECIFICATION.md) for requirements

## Overview

When creating or validating skills, use these official external resources to ensure compliance with standards and best practices.

## Table of Contents

- [Overview](#overview)
- [License Templates](#license-templates)
- [Changelog Format](#changelog-format)
- [Semantic Versioning](#semantic-versioning)
- [Agent Skills Specification](#agent-skills-specification)
- [README.md Best Practices](#readmemd-best-practices)
- [.gitignore Templates](#gitignore-templates)
- [Resource Documentation in Skills](#resource-documentation-in-skills)
- [Using These Resources](#using-these-resources)
- [Resources](#resources)

## License Templates

### MIT License

**Official Source:** https://opensource.org/license/mit

**Use When:**
- Maximum permissiveness desired
- No patent concerns
- Simplest license option
- Most common for skills

**Template Location:** https://opensource.org/license/mit

**Agent Behavior:**
1. Fetch official template from OSI
2. Replace `[year]` with **actual current year** (e.g., if today is February 2026, use 2026 - NOT 2024 or any past year)
3. Replace `[fullname]` with author name
4. **Do NOT** modify license text in any other way
5. Verify complete text present (not abbreviated)

**Critical:** Always use the CURRENT year when creating a new skill, not a hardcoded or past year.

**Verification:**
- [ ] Year matches the CURRENT year (e.g., 2026 if created in 2026, not 2024)
- [ ] Author name filled in (not `[fullname]` placeholder)
- [ ] Complete MIT text present
- [ ] No modifications to standard text
- [ ] SKILL.md frontmatter says `license: MIT`

### Apache License 2.0

**Official Source:** https://www.apache.org/licenses/LICENSE-2.0.txt

**Use When:**
- Patent protection desired
- Larger or commercial projects
- Explicit contributor license desired

**Template Location:** https://www.apache.org/licenses/LICENSE-2.0.txt

**Additional Requirements:**
- May require NOTICE file
- Must preserve copyright notices
- Must state modifications if made

**Agent Behavior:**
1. Fetch complete text from Apache foundation
2. Use verbatim (don't abbreviate)
3. Add copyright notice at top
4. Check if NOTICE file required
5. **Do NOT** modify license text

**Verification:**
- [ ] Complete Apache 2.0 text present (not summary)
- [ ] Copyright notice included
- [ ] NOTICE file present if required
- [ ] SKILL.md frontmatter says `license: Apache-2.0`

### Other Open Source Licenses

**Browse Options:** https://opensource.org/licenses

**Common Alternatives:**
- **BSD 3-Clause** - Similar to MIT with added clause
- **GPL v3** - Strong copyleft
- **ISC** - Similar to MIT, simpler language

**Agent Behavior:**
- Always fetch from official source
- Use complete, unmodified text
- Never create custom licenses
- When in doubt, suggest MIT (simplest)

## Changelog Format

**Specification:** https://keepachangelog.com/

**Version:** 1.1.0

**Format Structure:**

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- New features not yet released

### Changed
- Changes to existing functionality

## [1.0.0] - 2026-02-14

### Added
- Initial release features

### Changed
- Improvements to existing features

### Deprecated
- Features being phased out

### Removed
- Features removed

### Fixed
- Bug fixes

### Security
- Security improvements

[Unreleased]: https://github.com/user/repo/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/user/repo/releases/tag/v1.0.0
```

**Categories (in order):**
1. **Added** - New features
2. **Changed** - Changes to existing functionality
3. **Deprecated** - Soon-to-be removed features
4. **Removed** - Removed features
5. **Fixed** - Bug fixes
6. **Security** - Vulnerability fixes

**Agent Behavior:**
- Follow Keep a Changelog format exactly
- Use YYYY-MM-DD date format
- Keep [Unreleased] section for work in progress
- Link version numbers to tags (if Git repo)
- Write from user perspective (not developer perspective)
- Group related changes together
- Be specific about what changed

**Example Entry:**
```markdown
## [1.2.0] - 2026-02-14

### Added
- New REFACTOR workflow for improving existing skills
- CONSISTENCY_CHECKLIST.md for validation
- Proactive compliance checking in agents

### Changed
- Step 8 now includes file structure validation
- "When to Use" section now lists all workflow modes

### Fixed
- Corrected .gitignore template to exclude VALIDATION.md
```

## Semantic Versioning

**Specification:** https://semver.org/

**Format:** MAJOR.MINOR.PATCH

**Version Increment Rules:**

**MAJOR (1.0.0 → 2.0.0):**
- Breaking changes
- Incompatible API changes
- Fundamental restructuring
- Users must adapt their usage

**Samples:**
- Changing required frontmatter fields
- Removing features users depend on
- Changing skill invocation pattern
- Major workflow changes

**MINOR (1.0.0 → 1.1.0):**
- New functionality
- Backward compatible additions
- New features or sections
- Enhanced capabilities

**Samples:**
- Adding new workflow modes
- Adding new reference files
- Expanding existing sections
- New optional features

**PATCH (1.0.0 → 1.0.1):**
- Bug fixes
- Backward compatible fixes
- Typo corrections
- Documentation clarifications

**Samples:**
- Fixing broken links
- Correcting code samples
- Updating outdated screenshots
- Minor documentation improvements

**Agent Behavior:**
1. Ask user what changed
2. Determine appropriate version increment:
   - Adding breaking feature? → MAJOR
   - Adding new feature? → MINOR
   - Just fixing bugs? → PATCH
3. Update SKILL.md frontmatter version
4. Create matching CHANGELOG.md entry
5. Verify version consistent across all files

**Version Format:**
```yaml
# In SKILL.md frontmatter
metadata:
  version: "1.2.3"  # Always quoted string
```

## Agent Skills Specification

**Current Version:** 1.0

**Authoritative Source:** Agent Skills format specification

**Key Requirements:**
- SKILL.md with required frontmatter
- Name format: lowercase, hyphens, 1-64 chars
- Description: 1-1024 chars
- Progressive disclosure (SKILL.md < 500 lines)
- References loaded on-demand

**Validation Tool:**
```bash
skills-ref validate path/to/skill
```

**Repository:** agentskills/agentskills

**Agent Behavior:**
- Reference full specification in skill-smith/references/SPECIFICATION.md
- Run `skills-ref validate` when available
- Check name format matches directory
- Verify frontmatter completeness
- Ensure SKILL.md under 500 lines (recommended)
- Validate progressive disclosure used properly

## README.md Best Practices

**Guidelines:**
- **GitHub's README Guide:** https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
- **Make a README:** https://www.makeareadme.com/

**Standard Sections:**

```markdown
# Skill Name

Brief description (1-2 sentences explaining what the skill does)

## Installation

How to install or use the skill:
- Copy to skills directory
- Required dependencies
- Configuration steps

## Usage

Quick samples showing skill activation and basic usage

## Features

What this skill provides:
- Feature 1: Description
- Feature 2: Description
- Feature 3: Description

## Resources Used

**This skill was built from** (last updated: YYYY-MM-DD):
- [Official Documentation](URL) - What it covers
- [GitHub Repository](URL) - Samples and patterns
- [API Reference](URL) - API endpoints

See CHANGELOG.md for resource update history.

## Contributing

Guidelines for contributors (if applicable):
- How to report issues
- How to submit improvements
- Development workflow

## License

[License Name] - See [LICENSE](LICENSE) file for details
```

**Agent Behavior:**
- Include all standard sections
- Link to SKILL.md from README
- Document installation clearly
- Provide realistic usage samples
- List resources used with dates
- Link to LICENSE file

## .gitignore Templates

**Official Templates:** https://github.com/github/gitignore

**Useful Templates:**
- **macOS:** https://github.com/github/gitignore/blob/main/Global/macOS.gitignore
- **Windows:** https://github.com/github/gitignore/blob/main/Global/Windows.gitignore
- **JetBrains IDEs:** https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
- **VS Code:** https://github.com/github/gitignore/blob/main/Global/VisualStudioCode.gitignore

**Skill-Specific Pattern:**

```gitignore
# Build artifacts (skill-smith specific)
VALIDATION.md
.validation-cache/
*.tmp
.tmp/
build/
dist/
PLANNING.md

# OS files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db
*.swp
*~

# IDE configurations (optional - team preference)
.vscode/
.idea/
*.sublime-project
*.sublime-workspace

# Python artifacts (if applicable)
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
*.egg-info/
venv/
.venv/
ENV/

# Node artifacts (if applicable)
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.npm

# Logs
*.log
logs/
```

**Agent Behavior:**
- Start with skill-specific patterns
- Add OS-specific patterns (macOS, Windows)
- Add language-specific if needed (Python, Node)
- Add IDE patterns if team uses specific editors
- Comment each section clearly
- Verify VALIDATION.md excluded
- Test that artifacts are ignored

## Resource Documentation in Skills

**When creating/updating skills**, document resources used:

**In README.md:**
```markdown
## Resources Used

This skill was built from the following sources (last updated: 2026-02-14):

### Official Documentation
- [Main Documentation](URL) - Core concepts and API reference
- [GitHub Repository](URL) - Samples and patterns
- [API Reference](URL) - Complete endpoint documentation

### Additional Resources
- [Community Guide](URL) - Best practices and patterns
- [Tutorial](URL) - Getting started guide

**Note:** See CHANGELOG.md for resource update history.
```

**In CHANGELOG.md (when updating):**
```markdown
## [1.1.0] - 2026-02-14

### Changed
- Updated API documentation from v1.5 to v2.0
- Refreshed samples to match current patterns

### Resources Updated
- API docs: v1.5 → v2.0 (breaking changes documented)
- GitHub repo: commit abc123 → tag v1.5.0
- Added new tutorial resource
```

**Agent Behavior:**
- Document all resources used during creation
- Include last updated date
- Track resource changes in CHANGELOG
- Note version changes or breaking updates
- Link directly to specific versions when possible
- Update README when resources change

## Using These Resources

### When Creating Skills

**For LICENSE:**
```
1. Ask user which license to use (suggest MIT as simplest)
2. Fetch official template from authoritative source
3. Fill in [year] and [fullname] placeholders
4. Never modify standard license text
5. Verify SKILL.md frontmatter matches LICENSE file
```

**For CHANGELOG.md:**
```
1. Create using Keep a Changelog format
2. Start with [1.0.0] entry for initial release
3. Keep [Unreleased] section at top
4. Use proper categories (Added, Changed, Fixed, etc.)
5. Include dates in YYYY-MM-DD format
```

**For version numbers:**
```
1. Start at 1.0.0 for first release
2. Use semantic versioning rules for increments
3. Update version in SKILL.md frontmatter
4. Create matching CHANGELOG.md entry
5. Tag release in git
```

### When Validating Skills

**Verify licenses (comprehensive):**

**Step 1: Choose Appropriate License**
- [ ] License matches skill's purpose and source materials
- [ ] License is industry-standard (MIT, Apache-2.0, GPL, etc.) from https://opensource.org/licenses
- [ ] If distributing code: choose permissive (MIT, Apache) or copyleft (GPL) based on requirements
- [ ] If only documentation: consider Creative Commons or Apache 2.0

**Common License Choices:**
```
MIT License
  - Most permissive, minimal restrictions
  - Good for: General-purpose skills, libraries, tools
  - Use when: Maximum adoption desired, risk tolerance is high

Apache 2.0
  - Permissive with explicit patent protection
  - Good for: Enterprise tools, code with patents
  - Use when: Patent indemnification needed

GPL (v2 or v3)
  - Copyleft: derivatives must also be open source
  - Good for: Ensuring derivatives stay open
  - Use when: Strong open-source commitment required

None / Proprietary
  - All rights reserved, no public use
  - Good for: Internal-only skills, closed-source projects
  - Use when: Commercial license needed
```

**Step 2: Verify License Compatibility with Source Materials**
- [ ] Check licenses of all dependencies and source materials used
- [ ] Verify your license is compatible with source licenses:
  - MIT code can be used in Apache 2.0 projects ✓
  - GPL code requires your project also use GPL ✗ (unless you are an exception)
  - Apache 2.0 code can be used in MIT projects (but attribution needed) ✓
  - Proprietary code cannot be freely redistributed ✗
- Use https://choosealicense.com/appendix/ for detailed compatibility matrix
- Use SPDX license identifier: https://spdx.org/licenses/

**Step 3: Get and Verify License File**
- [ ] LICENSE file exists in repository root (not in skill package)
- [ ] LICENSE text is complete and unmodified from official source
- [ ] No lines removed or altered
- [ ] All placeholders filled in (copyright year, copyright holder name)
- [ ] For MIT: verify "Permission is hereby granted..." clause is intact
- [ ] For Apache 2.0: verify all sections present (TERMS AND CONDITIONS, appendix)
- [ ] Get authoritative templates from:
  - https://opensource.org/licenses (official texts)
  - https://github.com/licenses/license-templates/tree/master/templates (GitHub's official templates)
  - https://choosealicense.com/ (interactive license selector)

**Step 4: Add License Information to Documentation**
- [ ] README.md mentions license: "This project is licensed under [License Name]. See LICENSE file for details."
- [ ] CHANGELOG.md first entry mentions license choice
- [ ] Attribution for reused code documented in README "Attribution" or "Credits" section
- [ ] Copyright year is current (e.g., "Copyright (c) 2026 [Your Name]")

**Step 5: Comprehensive License Validation Checklist**
```
✓ LICENSE file exists at repository root (not in skill package)
✓ License is from authoritative source (opensource.org or GitHub)
✓ License text is complete and unchanged
✓ Copyright holder name is filled in
✓ Copyright year is current or date range is correct
✓ License choice documented in README
✓ All source material licenses verified for compatibility
✓ Attribution for reused code is documented
✓ No GPL code used without GPL license (if applicable)
✓ No proprietary code without explicit permission
```

**Verify CHANGELOG:**
```
1. Check format matches Keep a Changelog
2. Verify dates are YYYY-MM-DD format
3. Check version numbers match SKILL.md
4. Ensure changes described from user perspective
5. Confirm proper categories used
```

**Verify versions:**
```
1. Extract version from SKILL.md frontmatter
2. Extract latest version from CHANGELOG.md
3. Verify they match exactly
4. Check version follows semantic versioning
5. Verify increment appropriate for changes
```

## Resources

- **Licenses:** https://opensource.org/licenses
- **Changelog:** https://keepachangelog.com/
- **Versioning:** https://semver.org/
- **.gitignore:** https://github.com/github/gitignore
- **README:** https://www.makeareadme.com/
