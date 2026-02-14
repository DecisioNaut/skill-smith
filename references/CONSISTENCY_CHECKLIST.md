# Consistency Checklist

**Reference for:** Complete validation checklist for Agent Skills covering all files and consistency dimensions

> **Related:** See [REFACTORING_GUIDE.md](./REFACTORING_GUIDE.md) for refactoring patterns and [SPECIFICATION.md](./SPECIFICATION.md) for requirements

## Overview

This checklist ensures consistency across ALL skill files: SKILL.md, references/, assets/, and examples/. Use this before finalizing any skill or after major changes.

## Table of Contents

- [Overview](#overview)
- [Cross-File Consistency](#cross-file-consistency)
- [Terminology Consistency](#terminology-consistency)
- [Code and Example Consistency](#code-and-example-consistency)
- [SKILL.md Validation](#skillmd-validation)
- [Reference Files Validation](#reference-files-validation)
- [Assets and Examples](#assets-and-examples)
- [Link and Reference Validation](#link-and-reference-validation)
- [Git and Distribution](#git-and-distribution)
- [Version Control](#version-control)
- [Final Validation](#final-validation)
- [Pre-Commit Validation](#pre-commit-validation)
- [Compliance Overview Pattern](#compliance-overview-pattern)
- [Resources](#resources)

## Cross-File Consistency

### Skill Name

- [ ] Skill name in SKILL.md frontmatter matches directory name exactly
- [ ] Directory name is lowercase with hyphens only
- [ ] Name used consistently in README.md
- [ ] Name matches in all internal documentation
- [ ] No variations (my-skill vs myskill vs my_skill)

**Example Check:**
```bash
# Directory: api-integration-skill/
# SKILL.md frontmatter: name: api-integration-skill
# README.md: "# API Integration Skill" (proper case OK)
```

### Version Numbers

- [ ] Version in SKILL.md frontmatter matches CHANGELOG.md latest entry
- [ ] Version in README.md (if mentioned) matches SKILL.md
- [ ] Version follows semantic versioning (MAJOR.MINOR.PATCH)
- [ ] Version increment appropriate for changes made
- [ ] No future versions or placeholder versions

**Verify:**
```bash
# SKILL.md: version: "1.2.0"
# CHANGELOG.md: ## [1.2.0] - 2026-02-14
# Both must match exactly
```

### Author and License

- [ ] Author name consistent in SKILL.md frontmatter and LICENSE
- [ ] License type in SKILL.md matches LICENSE file content
- [ ] Copyright year in LICENSE matches current year (e.g., 2026 if created in 2026, not past years)
- [ ] Copyright holder name specified (not placeholder)
- [ ] LICENSE contains complete, unmodified standard text
- [ ] All placeholders ([year], [fullname]) replaced in LICENSE

**License Verification:**
```bash
# SKILL.md: license: MIT
# LICENSE file must contain complete MIT License text
# Copyright (c) 2026 John Doe (not [year] [fullname])
```

### Dates

- [ ] CHANGELOG.md dates are in YYYY-MM-DD format
- [ ] Dates are chronologically ordered (newest first)
- [ ] No future dates (except testing)
- [ ] LICENSE copyright year makes sense
- [ ] README.md "last updated" accurate if present

## Terminology Consistency

### Technical Terms

- [ ] Product/service names use official capitalization
- [ ] Technical terms spelled consistently throughout
- [ ] Abbreviations used uniformly (don't mix API/api)
- [ ] Hyphenation consistent (e.g., "command-line" not sometimes "command line")

**Common Issues:**
```markdown
❌ Inconsistent:
- "GitHub repo" vs "Github repository" vs "git repository"
- "Docker container" vs "docker Container" vs "container"

✅ Consistent:
- Always "GitHub repository"
- Always "Docker container"
```

### File References

- [ ] File paths use consistent format
- [ ] References use proper relative paths
- [ ] All referenced files actually exist
- [ ] Markdown links formatted consistently
- [ ] No broken links to moved/renamed files

**Check:**
```markdown
✅ Good:
- See [AUTHENTICATION.md](./AUTHENTICATION.md)
- See [references/API.md](references/API.md) from SKILL.md

❌ Bad:
- See AUTHENTICATION.md (no link)
- See [API](API.md) (wrong path from SKILL.md)
```

## Code and Example Consistency

### Syntax Highlighting

- [ ] All code blocks specify language (```bash, ```python, ```json)
- [ ] Same type of code uses same language tag throughout
- [ ] No generic ``` without language for code
- [ ] Language tags are lowercase (bash not Bash)

**Example:**
```markdown
✅ Consistent:
```bash
curl -X GET https://api.example.com
```

```bash
curl -X POST https://api.example.com
```

❌ Inconsistent:
```sh
curl -X GET https://api.example.com
```

```bash
curl -X POST https://api.example.com
```
```

### Examples and Output

- [ ] Examples use current, working syntax
- [ ] Deprecated patterns removed
- [ ] Expected outputs match current versions
- [ ] Placeholder values clearly marked (YOUR_KEY, example.com)
- [ ] Examples work as documented

### Commands and Paths

- [ ] Shell commands specify shell if ambiguous
- [ ] Platform-specific commands noted (macOS, Linux, Windows)
- [ ] File paths use appropriate separators
- [ ] Installation commands match documented method

## SKILL.md Validation

### Size and Structure

- [ ] SKILL.md under 500 lines (or justified if over)
- [ ] Has required frontmatter (name, description)
- [ ] Frontmatter is valid YAML
- [ ] "When to Use This Skill" section present
- [ ] Core instructions clear and complete
- [ ] No duplicate content from references

### Content Quality

- [ ] Instructions are specific and actionable
- [ ] Examples include inputs and outputs
- [ ] Prerequisites clearly listed
- [ ] Edge cases and errors handled
- [ ] No vague language ("you might want to...")

## Reference Files Validation

### File Size

- [ ] Individual reference files under 1000 lines (or justified)
- [ ] Files over 400 lines have table of contents
- [ ] No artificially split files (PART1, PART2)
- [ ] Natural topic boundaries respected

**Check sizes:**
```bash
wc -l references/*.md | sort -n
# Look for outliers > 1000 lines
```

### Structure and Formatting

- [ ] Each file has clear title matching filename
- [ ] "**Reference for:**" purpose statement present
- [ ] Cross-references to related files included
- [ ] Consistent heading hierarchy (##, ###, ####)
- [ ] Code blocks properly formatted
- [ ] No raw HTML unless necessary

### Organization

- [ ] Each file has single, clear purpose
- [ ] No "MISC.md" or catch-all files
- [ ] File names descriptive and specific
- [ ] Related files use consistent prefixing
- [ ] No duplicate content across files
- [ ] Clear which file covers which topic

**Verify:**
```
✅ Good organization:
├── NETWORKING.md (basics)
├── NETWORKING_ADVANCED.md (advanced)
├── SECURITY.md (all security)

❌ Poor organization:
├── STUFF.md (what stuff?)
├── NETWORKING_1.md (artificial split)
├── MISC.md (everything else)
```

## Assets and Examples

### Assets Directory

- [ ] All files in assets/ are actually used
- [ ] Assets referenced from SKILL.md or references/
- [ ] File formats appropriate (PNG/SVG for images)
- [ ] No redundant or outdated assets
- [ ] Asset files have descriptive names

### Examples Directory

- [ ] Examples are complete and working
- [ ] Each example has clear purpose
- [ ] Examples match current skill version
- [ ] README in examples/ if needed
- [ ] No broken or incomplete examples

## Link and Reference Validation

### Internal Links

- [ ] All relative paths correct
- [ ] Markdown anchor links work (#section-name)
- [ ] No links to removed or renamed files
- [ ] Cross-references between files accurate
- [ ] No circular or redundant references

**Test:**
```bash
# Check all internal references exist
grep -r "](references/" SKILL.md
# Verify each file exists

grep -r "](#" . 
# Check anchor links are valid
```

### External Links

- [ ] Documentation URLs accessible (return 200)
- [ ] GitHub repos public and exist
- [ ] API documentation links work
- [ ] No links to localhost or internal IPs
- [ ] Link text describes destination

**Note:** External links can break over time - document in CHANGELOG when updating.

## Git and Distribution

### File Structure

- [ ] No VALIDATION.md in repository
- [ ] No build artifacts (build/, dist/, .tmp/)
- [ ] No OS-specific files (.DS_Store, Thumbs.db)
- [ ] No editor configs unless needed (.vscode/, .idea/)
- [ ] No empty directories
- [ ] .gitignore excludes all artifacts

**Check:**
```bash
git status
# Should show only intended files

ls -la
# Look for .DS_Store, *.tmp, etc.
```

### Required Files

- [ ] SKILL.md exists
- [ ] README.md exists with clear instructions
- [ ] LICENSE exists with complete license text
- [ ] CHANGELOG.md exists (recommended)
- [ ] .gitignore exists (recommended)

## Version Control

### Git Best Practices

- [ ] Clean commit history (no "fix typo" spam)
- [ ] Descriptive commit messages
- [ ] Version tagged if releasing
- [ ] No sensitive data in commits
- [ ] No large binary files unless necessary

**Tag format:**
```bash
git tag v1.2.0
# Matches version in SKILL.md and CHANGELOG.md
```

## Final Validation

### Automated Checks

```bash
# Run official validation
skills-ref validate path/to/skill

# Check SKILL.md size
wc -l SKILL.md
# Should be < 500 lines

# Check for artifacts
git status --ignored
# Look for unexpected files
```

### Manual Review

- [ ] Read SKILL.md as if new to skill
- [ ] Follow instructions literally
- [ ] Try examples and verify outputs
- [ ] Check cross-references work
- [ ] Verify consistent terminology
- [ ] Confirm no broken links

### Pre-Commit Checklist

Just before committing:

```markdown
## Pre-Commit Validation

Essential:
- [ ] `skills-ref validate` passes
- [ ] No VALIDATION.md or artifacts present
- [ ] All referenced files exist
- [ ] SKILL.md under 500 lines (or justified)
- [ ] Version numbers match across files
- [ ] Clean git status (no unwanted files)

Quality:
- [ ] Terminology consistent throughout
- [ ] Code examples have language tags
- [ ] Cross-references work
- [ ] No duplicate content
- [ ] CHANGELOG.md updated

Distribution:
- [ ] README.md instructions accurate
- [ ] LICENSE complete and accurate
- [ ] .gitignore excludes artifacts
- [ ] Version tagged if releasing
```

## Compliance Overview Pattern

When checking compliance, present complete overview to user:

```
📊 Compliance Overview:

SKILL.md:
  ✅ 447 lines (under 500-line guideline)

Reference Files:
  ✅ AUTHENTICATION.md: 234 lines
  ✅ API_REFERENCE.md: 456 lines
  ⚠️ EXAMPLES.md: 1,103 lines (103 over recommendation)
  
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
C) Review specific sections
```

## Resources

- Official validation: `skills-ref validate path/to/skill`
- [SPECIFICATION.md](./SPECIFICATION.md) - Full Agent Skills specification
- [BEST_PRACTICES.md](./BEST_PRACTICES.md) - Writing guidelines
- [REFACTORING_GUIDE.md](./REFACTORING_GUIDE.md) - Refactoring patterns
