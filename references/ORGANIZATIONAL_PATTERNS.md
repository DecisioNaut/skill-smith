# Agent Skills Organizational Patterns

**Reference for:** File organization, reference file management, and proactive agent behavior patterns for Agent Skills

> **Related:** See [BEST_PRACTICES.md](./BEST_PRACTICES.md) for writing guidance and core principles

This guide covers how to organize skill files systematically and implement proactive agent behavior patterns.

## Reference File Organization

When skills grow complex, organize reference files systematically based on real-world patterns.

### Naming Conventions

**Standard Format:** `TOPIC.md` or `TOPIC_SUBTOPIC.md`

**Rules:**
- ALL_CAPS with underscores separating words
- Descriptive and specific (not generic)
- Related files use same prefix

**Examples:**
- ✅ AUTHENTICATION.md - Clear single topic
- ✅ DOCKER_COMPOSE.md - Specific feature
- ✅ NETWORKING.md + NETWORKING_ADVANCED.md - Progressive complexity
- ❌ MISC.md - Too generic
- ❌ authentication.md - Wrong case

### Size Guidelines

**Target Range:** 200-800 lines (optimal for readability)
**Warning Threshold:** 800 lines (proactively consider splitting)
**Hard Limit:** 1000 lines (must split or justify)

**Proactive Management:**
- ✅ **At 700-800 lines**: Evaluate if content can be logically split
- ⚠️  **At 800-900 lines**: Actively plan split before reaching 1000
- 🚫 **At 1000+ lines**: Must split immediately or provide strong justification

**Real-world data from production skills:**
- devcontainer-expert: 9 files, 365-574 lines each (all well under limit)
- uv-expert: 11 files, 155-1026 lines (1 at 1026 should have been split earlier)

**Agent Behavior During Creation:**
- Check file size after each major content addition
- Warn user when approaching 800 lines
- Proactively suggest split strategies at 850+ lines
- Do not create files over 1000 lines without explicit user approval

**When NOT to split:**
- Topic is cohesive and splitting would fragment understanding
- Content needs to be referenced together as a unit
- User explicitly approves keeping larger file with justification

### Splitting Strategies

**By Complexity Level:**
- Pattern: `TOPIC.md` + `TOPIC_ADVANCED.md`
- Example: NETWORKING.md (basics) + NETWORKING_ADVANCED.md (advanced patterns)
- Benefits: Clear learning path, beginners not overwhelmed

**By Functional Area:**
- Pattern: `TOPIC_AREA1.md` + `TOPIC_AREA2.md`
- Example: CONFIGURATION_BASICS.md + CONFIGURATION_ADVANCED.md
- Benefits: Clear separation of concerns

**By Feature Category:**
- Pattern: Distinct files for distinct features
- Example: PROJECTS.md, SCRIPTS_TOOLS.md, PYTHON_MANAGEMENT.md
- Benefits: Each file has clear, single purpose

### Reference File Structure

**Standard Template:**
```markdown
# Descriptive Title

**Reference for:** One-sentence description of content

> **Cross-references:** Links to related files

## Table of Contents (for files > 400 lines)
- [Section 1](#section-1)
- [Section 2](#section-2)

## Main Content

Clear hierarchical organization with examples...
```

**Key Elements:**
1. **Title** - Matches file name (proper case)
2. **Purpose Statement** - "**Reference for:** [what this covers]"
3. **Cross-References** - Link prerequisites and related files
4. **Table of Contents** - For files > 400 lines
5. **Content** - Clear hierarchy, code examples with language tags

### Cross-Referencing

**Link Prerequisites:**
```markdown
> **Prerequisites:** Read [BASICS.md](./BASICS.md) for fundamentals.
```

**Link to Advanced Content:**
```markdown
> **For advanced topics**, see [ADVANCED.md](./ADVANCED.md).
```

**Use Relative Paths:**
- `[FILE.md](./FILE.md)` from same directory
- `[FILE.md](../references/FILE.md)` from SKILL.md

### Organizational Anti-Patterns

**❌ Avoid:**
- Catch-all files (MISC.md, OTHER.md)
- Overly generic names (DOCUMENTATION.md - documentation about what?)
- Feature mixing (DOCKER_AND_KUBERNETES.md)
- Artificial splitting (SECURITY_PART1.md, SECURITY_PART2.md)

**✅ Instead:**
- Specific, focused files
- Clear topic per file
- Natural boundaries (basics vs. advanced)
- Topic-based organization

## Proactive Agent Behavior

When skill-smith is active, agents should automatically check best practices and offer recommendations. Don't wait for users to ask - be proactive!

### Automatic Checking Pattern

**Workflow:**
```
Agent automatically checks → Identifies issues → Presents recommendations → Asks for user input
```

**Core Principle:** Agents should be helpful collaborators, not passive executors.

### When to Check Automatically

**After file modifications:**
- ✅ Check SKILL.md line count
- ✅ Verify file structure (no artifacts)
- ✅ Check all file references still valid
- ✅ Verify .gitignore covers artifacts

**After refactoring:**
- ✅ Run skills-ref validate
- ✅ Check consistency across files
- ✅ Verify reference organization follows patterns
- ✅ Check for duplicate content

**After content additions:**
- ✅ Check if SKILL.md approaching/exceeding 500 lines
- ✅ Check if ANY reference file approaching 800 lines (warn at 800, require split at 1000)
- ✅ Suggest where new content should go
- ✅ Check version number needs update
- ✅ Remind about CHANGELOG.md entry

**File Size Thresholds:**
- SKILL.md: Warn at 450 lines, recommend split at 500+
- Reference files: Warn at 800 lines, require split/justification at 1000+

**Before committing:**
- ✅ Full compliance check
- ✅ File structure validation
- ✅ Verify no artifacts present
- ✅ Check consistency across files

### Example Interactions

**After modifying SKILL.md:**
```
User: "I've updated the SKILL.md with new authentication section"

Agent: 
✅ Checking best practices...

Issues found:
1. SKILL.md is now 571 lines (71 over 500-line guideline)
2. New authentication content is 85 lines

Recommendations:
• Move authentication details to references/AUTHENTICATION.md
• Keep only quick start auth in SKILL.md (est. 15-20 lines)
• This would bring SKILL.md to ~506 lines (still slightly over)
• Consider moving another section to stay under 500

Would you like me to:
A) Create references/AUTHENTICATION.md and move the content
B) Suggest additional sections to move
C) Keep as-is (572 lines is acceptable for this complexity)
D) You have another approach in mind

What do you prefer?
```

**During refactoring:**
```
User: "Let's refactor this skill"

Agent:
✅ Analyzing current state...

Current Structure:
- SKILL.md: 687 lines
- No reference files
- VALIDATION.md present (should remove)

Refactoring Recommendations:
1. Move API documentation (230 lines) → references/API_REFERENCE.md
2. Move examples (120 lines) → references/EXAMPLES.md
3. Remove VALIDATION.md artifact
4. Add .gitignore to exclude artifacts

This would bring SKILL.md to ~337 lines.

Shall I proceed with these changes?
```

**During skill creation (LICENSE validation):**
```
User: "Create LICENSE file"

Agent:
✅ Creating MIT License...

Current date: February 14, 2026

Generated LICENSE:
- Copyright (c) 2026 [Your Project Name] Contributors
- Full MIT License text from official source

✅ Verification:
- [ ] Year is CURRENT year (2026, not 2024 or other past year)
- [ ] Author name specified
- [ ] Complete MIT text present

LICENSE created successfully with correct current year.
```

**During content creation (proactive file size check):**
```
User: "Add data validation examples to API_REFERENCE.md"

Agent:
✅ Adding examples...

⚠️ File Size Check:
- API_REFERENCE.md was 687 lines
- After additions: 843 lines
- Status: Approaching warning threshold (800 lines)

Recommendation:
This file is getting large. Consider splitting before reaching 1000 lines:
• Option A: Split now (API_BASICS.md + API_ADVANCED.md)
• Option B: Continue but monitor (57 lines until warning at 900)
• Option C: Keep unified (acceptable if content is cohesive)

What's your preference?
```

### Compliance Overview Pattern

When checking compliance, present complete picture:

```
Agent: "Running comprehensive compliance check...

📊 Compliance Overview:

SKILL.md:
  ✅ 447 lines (under 500-line guideline)

Reference Files:
  ✅ AUTHENTICATION.md: 234 lines
  ✅ API_REFERENCE.md: 456 lines
  ⚠️ EXAMPLES.md: 1,103 lines (103 over 1000-line recommendation)
  
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
C) Review specific sections to decide"
```

**Why This Works:**
- Shows ALL files, not just problems
- Visual organization (SKILL.md, references, assets)
- Clear status indicators (✅ ⚠️ ❌)
- Context for decisions ("slightly over" vs "way over")
- User empowerment (present options, let user decide)
- Acknowledges trade-offs (sometimes slightly over is fine)

### Behavior by Workflow Mode

**During CREATE mode:**
- Check SKILL.md size at Step 4 (after writing)
- Suggest splits if approaching 500 lines
- Validate before Step 9
- Final check before commit

**During REFACTOR mode:**
- Automatically check after each change
- Present issues with specific recommendations
- Suggest reorganization patterns
- Validate when refactoring complete

**During IMPROVE mode:**
- Check impact before adding content
- Alert if additions will exceed 500 lines
- Suggest placement (SKILL.md vs references/)
- Validate after additions

**During UPDATE mode:**
- Check what has changed in resources
- Identify content that needs updating
- Suggest versioning strategy
- Validate after updates

**During VALIDATE mode:**
- Run full compliance check immediately
- Present comprehensive findings
- Prioritize issues by severity
- Suggest specific fixes with examples

### Key Principles

1. **Automatic Checking** - Don't wait for user to ask "is this compliant?"
2. **Clear Communication** - Present findings in structured format
3. **Actionable Recommendations** - Offer specific solutions, not just problems
4. **User Choice** - Always give options (A/B/C/D) including "other ideas"
5. **Collaborative** - Agent recommends, user decides
6. **Complete Picture** - Show all files when checking compliance
7. **Context Matters** - "Slightly over" is different from "way over"

### What to Check After Modifications

```markdown
After any skill file modification:
- [ ] SKILL.md line count (warn if >450, alert if >500)
- [ ] File structure (check for artifacts)
- [ ] File references (verify all exist)
- [ ] .gitignore covers artifacts
- [ ] Frontmatter valid
- [ ] Version number appropriate for changes

Present findings like:
✅ SKILL.md: 447 lines (under limit)
✅ No artifacts found
⚠️ Found reference to 'references/MISSING.md' that doesn't exist
❌ .gitignore missing VALIDATION.md pattern

Recommendations:
1. Create references/MISSING.md or remove reference
2. Add 'VALIDATION.md' to .gitignore

Would you like me to fix these issues?
```

### Error Handling

**If unclear which approach is best:**
```
Agent: "I notice SKILL.md is 571 lines. I see several sections that could 
potentially move to references:

1. Authentication (85 lines) - Detailed, good candidate
2. Configuration (120 lines) - Mix of essential + details
3. Troubleshooting (95 lines) - Could split into references

I'm not sure which approach is best for this skill. What's your preference?
- Move all three to references/
- Move just authentication?
- Move authentication + troubleshooting?
- Different sections entirely?

Let me know and I'll make the changes."
```

**When presenting options:**
- Always include "other ideas" or "different approach"
- Be humble about recommendations
- Explain trade-offs
- Let user make final decision

## Summary: Quick Wins

To improve any skill instantly:

1. **Add concrete examples** with actual inputs/outputs
2. **Break complex instructions** into numbered steps
3. **Handle errors explicitly** (don't assume success)
4. **Keep SKILL.md focused** (< 500 lines)
5. **Use progressive disclosure** (move details to references/)
6. **Write for literal interpretation** (no vague language)
7. **Include specific keywords** in description
8. **Keep file references flat** (one level deep)
9. **Validate with skills-ref** before sharing
10. **Test by following literally** (don't assume steps)

## Resources

- [Agent Skills Specification](https://agentskills.io/specification)
- [Integration Guide](https://agentskills.io/integrate-skills)
- [Example Skills](https://github.com/anthropics/skills)
- [skills-ref Library](https://github.com/agentskills/agentskills/tree/main/skills-ref)
