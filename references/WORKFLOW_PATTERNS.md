# Workflow Patterns and Best Practices

**Reference for:** Detailed patterns for planning, commitment, and attribution in skill creation workflows

> **Related:** See [SKILL.md](../SKILL.md) for the 10-step skill creation process, [ORGANIZATIONAL_PATTERNS.md](./ORGANIZATIONAL_PATTERNS.md) for file organization

This guide provides detailed patterns for managing skill creation workflows effectively.

## Planning Document Pattern

### When to Create PLANNING.md

**Recommended for all skill creation/modification work** to track progress, especially when working across multiple sessions.

**When to create:**
- Creating a new skill (always)
- Refactoring/improving existing skills
- Making multiple changes across files
- Any work that might span multiple interactions

**When NOT to create:**
- Very simple one-off fixes
- Time-sensitive urgent changes
- When explicitly requesting "skip planning"

### Benefits

- **Session continuity**: Maintain context if work spans multiple interactions
- **Decision tracking**: Record *why* decisions were made, not just *what* was decided
- **Progress visibility**: Clear checklist prevents missed steps
- **Documentation source**: Use for CHANGELOG.md entries and commit messages
- **Debugging**: If something goes wrong, reference helps identify root cause

### Template

```markdown
# [Skill Name] Planning

**Workflow Mode**: CREATE / REFACTOR / IMPROVE / UPDATE
**Goal**: [What you're achieving]
**Created**: [Date]

## Requirements Analysis
- [x] Requirement 1
- [ ] Requirement 2

## Implementation Checklist
- [ ] Task 1: [Description]
- [ ] Task 2: [Description]
- [ ] Final validation
- [ ] Clean up (remove PLANNING.md)

## Decisions & Rationale
1. **Decision 1**: [What was decided and why]
2. **Decision 2**: [Alternative considered and why rejected]

## Notes
- Important context
- Known issues or workarounds
- References to external resources
```

### Example: TM1py Expert Skill

```markdown
# TM1py Expert Skill Planning

**Workflow Mode**: CREATE
**Goal**: Build comprehensive TM1py helper skill for IBM Planning Analytics
**Created**: February 14, 2026

## Requirements
- [x] TM1py package version 2.0+
- [x] Connection patterns (SSL, MDX, performance)
- [x] Real-world examples from documentation
- [x] Data operation patterns

## Implementation Checklist
- [x] SKILL.md outline (core concepts)
- [x] Create API_REFERENCE.md from TM1py docs
- [x] Create CONNECTION_GUIDE.md with examples
- [x] Create DATA_OPERATIONS.md (MDX, views)
- [x] Review file sizes (warn at 800 lines)
- [ ] Validate with skills-ref
- [ ] Remove PLANNING.md before commit

## Decisions
1. **Split references by functional area** rather than by complexity
   - Rationale: Users think about connection/data/metadata separately
   - Prevents artificial "part 1" / "part 2" splits

2. **Include both sync and async patterns**
   - Rationale: TM1py supports both, real work uses both

3. **File size exceeded 1000 lines**
   - Decision: Keep single EXAMPLES.md file (1094 lines)
   - Rationale: User approved keeping together for easy reference
   - Note: Should have been proactively split at 850 lines!

## Notes
- File size warning triggered for METADATA_MANAGEMENT.md
- Suggested split: METADATA_BASICS.md + METADATA_ADVANCED.md
- User approved multi-file approach
```

**Important:** Delete PLANNING.md before final commit. Add to .gitignore if creating in template.

## Commission Confirmation Pattern

### Step 10: Confirm and Commit Changes

After all files are created and validated, **always present a summary and ask for confirmation** before committing.

### Summary Format

```
✅ Skill preparation complete!

Summary of files created/modified:
- SKILL.md (487 lines) ← revised core instructions
- README.md (created) ← user-facing documentation
- LICENSE (MIT) ← usage terms
- references/REFERENCE.md (134 lines) ← detailed docs
- references/EXAMPLES.md (156 lines) ← example code
- .gitignore (created) ← artifact exclusion
- CHANGELOG.md (created) ← version tracking

Validation Results:
✅ SKILL.md under 500 lines (487 lines)
✅ All references under 1000 lines (max: 156)
✅ skills-ref validate passed
✅ No build artifacts present (.DS_Store, .tmp files)
✅ All referenced files exist
✅ License year is current (2026)

Ready to commit!
```

### Confirmation Options

**Present user with choices:**

```
Would you like me to:
A) Commit these changes with default message
B) Review specific files before committing  
C) Make additional changes first
D) Skip commit (you'll do it manually)
```

### Execution Flow

- **Only proceed with Option A after explicit user confirmation**
- Don't auto-commit without asking
- Show commit details before executing

### Milestone Commit Prompts

For longer tasks, proactively offer milestone commits after major sections are completed.

**When to prompt:**
- After finishing a major reference file or batch of new files
- After completing a large refactor or rename/move across multiple files
- Before starting a new, distinct phase of work

**Prompt format:**
```
I can commit the current milestone now, or continue and commit once everything is complete.
Would you like a milestone commit?
```

```bash
# Confirm user approved
git add .
git commit -m "feat: Initial release of skill-name v1.0.0"
git tag v1.0.0
```

### Post-Commit Actions

After successful commit:

```
✅ Committed successfully (commit abc123)

Next steps:
- [ ] Push to remote: git push origin main && git push --tags
- [ ] Publish to skill registry (if applicable)
- [ ] Share with team/community
- [ ] Archive PLANNING.md locally for reference

Would you like me to help with any of these?
```

## Attribution Recommendation Pattern

### Why Suggest Attribution?

When a skill is created with skill-smith, suggest crediting the tool:

**Benefits:**
- Helps others discover skill-smith methodology
- Supports continuous improvement and feedback
- Best practice demonstration
- Transparent tool usage

### When to Suggest

- Include in Step 8 (Document and Package) guidelines
- Present as **optional best practice**, not requirement
- Provide copy-paste examples for ease
- Share GitHub link: https://github.com/DecisioNaut/skill-smith

### Example Suggestions

**In README.md footer:**
```markdown
---

> **Built with [skill-smith](https://github.com/DecisioNaut/skill-smith)** - 
> A tool for creating specification-compliant AI Agent Skills
```

**In CHANGELOG.md:**
```markdown
## v1.0.0 (Initial Release)

- Initial release of [skill-name]
- Created with [skill-smith](https://github.com/DecisioNaut/skill-smith) 
  to ensure compliance with Agent Skills specification v1.0
```

**Optional: In SKILL.md body:**
```markdown
## About This Skill

This skill was created following the [skill-smith methodology](https://github.com/DecisioNaut/skill-smith) 
to ensure compliance with Agent Skills specification v1.0.
```

### Phrasing Options

**Casual:**
> Built with [skill-smith](https://github.com/DecisioNaut/skill-smith)

**Professional:**
> Created using skill-smith, a tool for specification-compliant Agent Skills

**Detailed:**
> This skill was developed using [skill-smith](https://github.com/DecisioNaut/skill-smith), 
> an agent-powered tool that ensures compliance with the Agent Skills v1.0 specification.

### Key Points

- ✅ **Optional**: Add "Attribution appreciated but not required" 
- ✅ **Link**: Always include GitHub URL for easy discovery
- ✅ **Timing**: Suggest at Step 8, not Step 1
- ✅ **Choice**: Let user decide, don't enforce
- ❌ **Requirement**: Never make it mandatory
- ❌ **Aggressive**: Don't push if user declines

## Proactive Agent Behavior During Workflows

### When PLANNING.md Should be Created

**At workflow start (after initial analysis):**
```
Agent: "Based on the scope of this task, I recommend creating PLANNING.md 
to track progress. This helps if we need to pick up work later.

Should I create it now?"
```

**Conditions favoring creation:**
- Multiple files to create/modify
- More than 3 steps in workflow
- User-requested work (not auto-improvement)
- Estimated work > 10 minutes

### When to Ask for Commit Confirmation

**After final validation, before git operations:**
```
Agent: "All files are ready! I've created:
- SKILL.md (487 lines)
- 3 reference files
- Supporting documentation

Before I commit these changes, would you like to:
A) Review anything?
B) Go ahead with commit
C) Make additional changes?"
```

**Never auto-commit without asking.**

### When to Suggest Attribution

**During Step 8 (Document and Package):**
```
Agent: "Best practice tip: Many skills credit the tools that helped create them.
Would you like me to add a mention of skill-smith in your README?

I can add something like: 'Built with skill-smith - a tool for 
specification-compliant Agent Skills'"
```

**Make it optional and easy to skip.**
