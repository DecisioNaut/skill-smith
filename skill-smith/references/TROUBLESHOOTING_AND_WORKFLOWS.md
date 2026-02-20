# Troubleshooting and Alternative Workflows

**Reference for:** Common skill creation scenarios, workflow modes for specific tasks, and troubleshooting common problems

> **Related:** See [SKILL.md](../SKILL.md) for the main 8-step skill creation process, [WORKFLOW_PATTERNS.md](./WORKFLOW_PATTERNS.md) for planning and commit patterns

This guide covers alternative workflows for different scenarios beyond basic skill creation, plus solutions for common problems.

## Table of Contents

- [Alternative Workflows](#alternative-workflows)
- [Troubleshooting Common Problems](#troubleshooting-common-problems)
- [Common Patterns and Anti-Patterns](#common-patterns-and-anti-patterns)

## Alternative Workflows

The 8-step process in SKILL.md is for **creating new skills**. Use these alternative workflows for other scenarios:

### Workflow Mode: Refactoring an Existing Skill

**When to use:** Improving structure/organization of an existing skill

**Process:**
1. **Analyze Current State** - Check SKILL.md line count, list all files, run `skills-ref validate`
2. **Identify Issues** - Is SKILL.md > 500 lines? Unwanted artifacts? Poorly organized references?
3. **Plan Improvements** - Decide what moves to references/, plan file names
4. **Execute Changes** - Create reference files, update SKILL.md links, remove artifacts
5. **Validate** - Verify SKILL.md under 500 lines, all references work, run validation
6. **Document** - Update CHANGELOG.md, increment version
7. **Commit** - Present summary and ask for confirmation before committing

**Example:** Splitting overgrown BEST_PRACTICES.md (970 lines) into BEST_PRACTICES.md (628 lines) + ORGANIZATIONAL_PATTERNS.md (361 lines)

### Workflow Mode: Adding Content to Existing Skill

**When to use:** Adding new features/documentation to existing skill

**Process:**
1. **Assess Impact** - Note current SKILL.md line count, estimate lines to add
2. **Decide Placement** - Core concepts → SKILL.md (if space), detailed docs → references/
3. **Add Content** - Maintain consistency with existing style
4. **Update References** - Add links, check cross-references
5. **Validate and Document** - Check size, run validation, update CHANGELOG.md
6. **File Size Check** - If SKILL.md approaching 450 lines or references approaching 800, plan split
7. **Commit** - Ask for confirmation before committing

**File size thresholds to monitor:**
- SKILL.md: Warn at 450 lines, recommend split at 500+
- Reference files: Warn at 800 lines, split/justify at 1000+

### Workflow Mode: Updating an Existing Skill

**When to use:** Source resources have changed or skill needs refreshing

**Process:**
1. **Identify Original Resources** - Check README.md, CHANGELOG.md for resource list
2. **Verify Resources Valid** - Check URLs work, repos exist, APIs current
3. **Check for Changes** - Re-fetch docs, check for new features/deprecations
4. **Identify Additional Resources** - Any new official resources?
5. **Plan Updates** - List content to add/update/remove, decide placement
6. **Execute Updates** - Update outdated content, add new, remove deprecated
7. **Update Documentation** - Update version, CHANGELOG.md, README.md
8. **Validate** - Run skills-ref validate, test samples, check links
9. **Commit** - Present summary and ask for confirmation

**Versioning for Updates:**
- **Patch (1.0.0 → 1.0.1)**: Minor fixes, updated samples
- **Minor (1.0.0 → 1.1.0)**: New features, expanded coverage
- **Major (1.0.0 → 2.0.0)**: Breaking changes, major restructuring

### Workflow Mode: Quick Validation Check

**When to use:** Verify existing skill compliance without modification

**Commands:**
```bash
# 1. Specification validation
skills-ref validate path/to/skill

# 2. Check SKILL.md size
wc -l path/to/skill/SKILL.md

# 3. Check for artifacts
ls -la path/to/skill/

# 4. Verify skill package contents (only these belong in installed skill)
# Required: SKILL.md only
# Optional: scripts/, references/, assets/ (only if they have content)
# Do NOT include: README.md, LICENSE, CHANGELOG.md, CONTRIBUTING.md (these are repository-level)
# Do NOT include: VALIDATION.md, .tmp files, .DS_Store
```

**Quick checklist:**
- [ ] SKILL.md is present and valid?
- [ ] SKILL.md under 500 lines?
- [ ] No README.md, LICENSE, CHANGELOG.md, or CONTRIBUTING.md in the skill package?
- [ ] No VALIDATION.md or build artifacts?
- [ ] All file references (scripts/, references/, assets/) exist and are valid?
- [ ] .gitignore excludes artifacts?
- [ ] Version matches CHANGELOG?

## Troubleshooting Common Problems

### Problem: Validation fails with "name doesn't match directory"

**Error:** Directory name doesn't match skill name in frontmatter

**Root cause:** Skill name and directory must match exactly (lowercase, hyphens only)

**Solution:**
```bash
# Check current directory name
ls -d pdf*

# Check frontmatter name
grep "^name:" SKILL.md

# If they don't match, rename directory
# Example: if SKILL.md says "name: pdf-processing"
# and dir is "PDFProcessing", rename:
mv PDFProcessing pdf-processing
```

### Problem: SKILL.md is too large (> 500 lines)

**Error:** File exceeds progressive disclosure target

**Root cause:** Too much detail kept in main SKILL.md instead of moving to references/

**Solution:**
1. **Identify large sections** (check line counts):
   ```bash
   grep -n "^## " SKILL.md | while read line; do
     num=$(echo $line | cut -d: -f1)
     echo $line
   done
   ```

2. **Move to references/**:
   - API documentation → `references/API_REFERENCE.md`
   - Long samples → `references/SAMPLES.md`
   - Technical details → `references/TECHNICAL.md`
   - Troubleshooting → `references/TROUBLESHOOTING.md`

3. **Keep in SKILL.md**:
   - Overview and when to use
   - Quick start / core concepts
   - Basic samples (1-3 short ones)
   - Links to references/ for details

4. **Verify**: Target is < 500 lines, optimal is < 400 lines

### Problem: Description too vague, agent doesn't activate skill

**Error:** Agents don't recognize when to use this skill

**Root cause:** Description lacks specific keywords or use-case context

**Bad example:**
```yaml
description: "Helps with PDFs"
```

**Good example:**
```yaml
description: "Extract text and tables from PDF files, fill forms, and merge documents. Use when working with PDF documents or when user mentions PDFs, forms, document extraction, or PDF processing."
```

**How to fix:**
1. **Identify action verbs**: extract, create, modify, analyze, validate
2. **Add domain keywords**: PDF, forms, documents, tables
3. **Add trigger phrases**: "when user mentions ...", "use when ..."
4. **Aim for 1-1024 characters** with both "what" and "when"

### Problem: Can't fetch GitHub repository content

**Error:** fetch_webpage fails on GitHub repository or returning incomplete content

**Root causes:**
- Repository is private (needs authentication)
- Page is behind JavaScript rendering
- URL structure incorrect

**Solutions:**
```bash
# Use raw.githubusercontent.com for direct file access
https://raw.githubusercontent.com/user/repo/main/README.md
https://raw.githubusercontent.com/user/repo/main/docs/guide.md

# For specific files in specific locations
https://raw.githubusercontent.com/user/repo/main/docs/api/reference.md

# Check if repo is public
curl -I https://github.com/user/repo
# Should return 200, not 404 or redirect to login
```

**Workaround:**
- If repo is private, ask user for documentation or link to published docs
- If specific files are behind authentication, request user provide the content

### Problem: Resources conflict or show different approaches

**Error:** Multiple resources present conflicting information or different code patterns

**Symptom:** "I found two different ways to do this, which should I use?"

**Solution:**
1. **Ask user for clarification**:
   ```
   I found two authentication approaches:
   A) Bearer token authentication (shown in latest docs)
   B) API key authentication (shown in samples)
   
   Which should this skill focus on?
   ```

2. **Check documentation recency**:
   ```
   - Latest docs (2026): Prefers newer approaches
   - Samples folder: Often outdated
   - README: Usually reflects current best practice
   ```

3. **Document the choice**:
   ```markdown
   > Note: This skill uses [Bearer Token authentication] 
   > as recommended in the official 2026 documentation.
   > For alternative approaches, see [ALTERNATIVE_AUTH.md](./ALTERNATIVE_AUTH.md)
   ```

### Problem: API documentation is incomplete or unclear

**Error:** Cannot write complete instructions due to missing information

**Solutions:**
1. **Check multiple sources**:
   - Official API docs
   - Blog posts / tutorials
   - GitHub samples
   - Community forums

2. **Note the gap**:
   ```markdown
   > **Note:** The official documentation doesn't cover this scenario.
   > Based on [community discussion], the recommended approach is:
   ```

3. **When uncertain**:
   - Provide most complete information found
   - Add disclaimer about potential gaps
   - Suggest user test thoroughly
   - Recommend checking official docs for latest

4. **Don't guess**: If genuinely unclear, better to say "This specific scenario isn't documented" than provide potentially wrong information

### Problem: License year is hardcoded instead of current

**Error:** Created skill has 2024 copyright year when it's 2026

**Root cause:** Template or agent using fixed year instead of current date

**Solution:**
1. **Update LICENSE file**:
   ```bash
   # Check current year
   date +%Y  # outputs 2026
   
   # Fix LICENSE
   sed -i 's/Copyright (c) 2024/Copyright (c) 2026/' LICENSE
   ```

2. **Update any templates** to use current year dynamically
3. **Verify before committing**:
   ```bash
   grep "Copyright" LICENSE
   # Should show: Copyright (c) 2026 [Author Name]
   ```

### Problem: Reference files exceed 1000 lines

**Error:** Individual reference file is too large for on-demand loading

**Symptom:** One file has 1094 lines while others are < 700

**Root cause:** Didn't proactively split when file reached 800 lines

**Solution:**
1. **Identify split point** by section structure:
   ```bash
   grep -n "^## " file.md
   ```

2. **Look for natural divide**:
   - Basic vs Advanced topics
   - Different features/modules
   - Different complexity levels

3. **Split into two files**:
   - `TOPIC.md` (basics, 400-600 lines)
   - `TOPIC_ADVANCED.md` (advanced, 400-600 lines)

4. **Add cross-references**:
   ```markdown
   > For advanced topics, see [TOPIC_ADVANCED.md](./TOPIC_ADVANCED.md)
   ```

## Common Patterns and Anti-Patterns

### ✅ Good Practices

- **Progressive disclosure**: Start with SKILL.md only, add complexity as needed
- **Concrete samples**: Show actual code/commands with expected output
- **Clear scope**: One skill = one well-defined capability
- **Validation-ready**: Follow naming rules and structure from the start
- **Self-documenting**: Someone should understand the skill by reading SKILL.md
- **Proactive file management**: Monitor file sizes, split before exceeding limits
- **Planning documents**: Use PLANNING.md to track decisions and progress
- **Attribution**: Credit tools that helped create the skill

### ❌ Anti-Patterns to Avoid

- **Vague descriptions**: "Helps with coding" instead of specific capabilities
- **Monolithic skills**: Trying to do too much in one skill (split into multiple)
- **Heavy SKILL.md**: 2000 lines of reference docs in SKILL.md (use references/)
- **Unclear structure**: Random mix of instructions, samples, and references
- **Missing validation**: Not checking naming rules and frontmatter
- **Implicit knowledge**: Assuming agents will "figure out" what to do
- **Passive file management**: Letting files grow to 1200+ lines before splitting
- **Auto-committing**: Not asking for user confirmation before git operations
- **Hardcoded years**: Using fixed years (2024) instead of current date
- **No attribution**: Never mentioning tools that helped create the skill
