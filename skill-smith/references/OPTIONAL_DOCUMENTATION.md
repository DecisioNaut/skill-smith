# Optional Documentation Files

**Reference for:** When and how to create optional repository documentation files like GENESIS.md, .gitignore, and other supplementary documentation

> **Cross-references:** See [REPOSITORY_README_GUIDE.md](./REPOSITORY_README_GUIDE.md) for README.md structure | See [BEST_PRACTICES.md](./BEST_PRACTICES.md) for file structure guidelines

## Table of Contents

- [GENESIS.md - Project History & Retrospective](#genesismd---project-history--retrospective)
- [.gitignore - Artifact Exclusion](#gitignore---artifact-exclusion)
- [Quick Decision Checklist](#quick-decision-checklist)
- [When NOT to Create Added Files](#when-not-to-create-added-files)

## GENESIS.md - Project History & Retrospective

### Purpose

GENESIS.md documents the **creation journey** of the skill:
- Why the skill was created
- Key discoveries during development
- Major decisions made
- Lessons learned and design rationale
- Evolution and pivots that occurred

**Who reads it:** Maintainers, contributors looking to understand design context, future developers maintaining the skill

### When to Create GENESIS.md

**Recommended for:**
- ✅ Skills created through significant research or resource gathering
- ✅ Skills that involved major architectural or design decisions
- ✅ Skills where the "why" behind choices isn't obvious from SKILL.md
- ✅ Team-maintained skills (helps new contributors understand context)
- ✅ Complex skills where rationale matters for future modifications

**Optional for:**
- Simple, straightforward skills with minimal design choices
- Single-developer side projects
- Skills that will never be modified

**Not needed:**
- ❌ Temporary or throwaway skills
- ❌ Direct ports of existing skills without meaningful changes

### GENESIS.md Template

```markdown
# Project Genesis: [Skill Name]

**Created:** [Date]  
**Creator(s):** [Names]  
**Purpose:** [One-line statement of why this skill exists]

## Origin Story

[Narrative: What problem prompted creating this skill? What need does it address?]

## Research Phase

### Resources Analyzed
- **[Resource Type]**: [Specific source or documentation]
  - Key insights: [What was learned]
  - Links: [URLs if applicable]

- **[Resource Type]**: [Another source]
  - Key insights: [What was learned]
  - Limitations: [What wasn't covered]

### Key Findings
1. **Discovery 1**: [What was discovered during research]
   - Impact: How this shaped the skill design

2. **Discovery 2**: [Another finding]
   - Impact: How this affected decisions

## Design Decisions

### Decision 1: [Major Design Choice]
- **Question**: [What choice needed to be made?]
- **Options Considered**: [What alternatives existed?]
- **Choice Made**: [What was decided and why]
- **Rationale**: [The reasoning behind this choice]
- **Trade-offs**: [What was sacrificed, if anything]

### Decision 2: [Another Significant Decision]
- **Question**: [What choice needed to be made?]
- **Options Considered**: [Alternative approaches]
- **Choice Made**: [Final decision]
- **Rationale**: [Why this approach was best]
- **Trade-offs**: [Costs/limitations of this choice]

## Architecture & Structure

### Overall Approach
[Describe the high-level structure and philosophy]

### File Organization
- **SKILL.md**: [What it covers and why organized this way]
- **references/**: [Which files and their organization rationale]
- **scripts/**: [If applicable; what utilities are included and why]
- **assets/**: [If applicable; what resources are needed and why]

## Lessons Learned

### What Worked Well
1. [Successful approach or decision]
   - Why it worked: [Reason]

2. [Another successful element]
   - Benefit: [What value it provided]

### What We'd Do Differently
1. [Mistake or suboptimal choice made]
   - Better approach: [How to improve it next time]

2. [Another area for improvement]
   - Lesson: [General principle learned]

## Pivots & Evolution

### Pivot 1: [If significant direction change occurred]
- **Original plan**: [What was initially intended]
- **What changed**: [How the approach shifted]
- **Reason**: [Why the pivot was necessary]
- **Result**: [What happened after the pivot]

[Continue for other major pivots if applicable]

## Current Status & Future

### Scope
- **In scope**: [What this skill covers]
- **Out of scope**: [What it intentionally doesn't cover]
- **Why**: [Reasoning for scope boundaries]

### Known Limitations
1. [Limitation 1]: [Description and why]
2. [Limitation 2]: [Description and why]

### Future Enhancements
- [ ] Enhancement idea 1: [What and why]
- [ ] Enhancement idea 2: [What and why]

## Acknowledgments

[Optional: Credit any sources, inspiration, or contributors who influenced the design]

---

**For current documentation**, see [SKILL.md](./[skill-name]/SKILL.md) and the referen files.
```

### Example GENESIS.md

```markdown
# Project Genesis: TM1py Expert Skill

**Created:** February 14, 2026  
**Creator(s):** [Your Name]  
**Purpose:** Teach agents to work effectively with IBM Planning Analytics using TM1py

## Origin Story

This skill was created because TM1py documentation is rich but scattered across multiple sources (PyPI, GitHub, IBM docs), making it hard for agents to quickly learn effective patterns. The goal was to create a curated, agent-friendly guide showing the most practical patterns for real-world TM1 work.

## Research Phase

### Resources Analyzed
- **PyPI**: Official TM1py package and release notes
  - Key insights: Version 2.0+ introduced significant API improvements
  - Discovered: Async patterns, connection pooling features

- **GitHub Repository**: https://github.com/cubewise-code/tm1py
   - Key insights: Samples show real-world patterns
   - Limitations: Samples focused on advanced use cases; missing basics

- **IBM Planning Analytics Documentation**: Official IBM reference
  - Key insights: MDX and TurboIntegrator integration details
  - Limitations: Not TM1py-specific; somewhat dated

### Key Findings
1. **Connection Patterns Matter**: Most beginner mistakes involve incorrect connection setup. SSL/TLS handling was a major learning curve.
   - Impact: Prioritized connection guidance early in the skill

2. **Two Distinct User Patterns**: Users either need sync (one-off scripts) or async (long-running processes). Cannot optimize for both equally.
   - Impact: Created separate sections for sync and async patterns

3. **MDX Expertise Gap**: Agents understand SQL but MDX dimensions/hierarchies often cause errors.
   - Impact: Added dedicated MDX primer in references

## Design Decisions

### Decision 1: Sync vs. Async Patterns
- **Question**: Should the skill cover both sync and async TM1py patterns?
- **Options Considered**: 
  - A) Only sync (simpler, covers 80% of use cases)
  - B) Only async (better for production systems)
  - C) Both sync and async (comprehensive but complex)
- **Choice Made**: Both sync and async patterns
- **Rationale**: Real production systems need both; excluding one would limit skill utility
- **Trade-offs**: SKILL.md became longer (~520 lines); had to move detailed patterns to references/

### Decision 2: File Organization by Feature vs. By Complexity
- **Question**: How to organize reference files?
- **Options Considered**:
  - A) By complexity (BASICS.md + ADVANCED.md) - Artificial splits
  - B) By feature area (CONNECTIONS.md, METADATA.md, DATA_OPS.md) - User mental model
- **Choice Made**: By feature area
- **Rationale**: Users think "I need to work with connections" or "I need data operations," not "I need basic vs. advanced"
- **Trade-offs**: More files to navigate, but clearer mental model

## Architecture & Structure

### Overall Approach
The skill uses progressive disclosure: SKILL.md covers essential sync patterns plus async overview; references/ contains detailed async patterns, MDX primer, and troubleshooting specific to TM1py.

### File Organization
- **SKILL.md** (520 lines): Core sync patterns + async overview + quick samples
- **references/CONNECTION_GUIDE.md**: SSL, authentication, pooling patterns
- **references/MDX_PRIMER.md**: MDX syntax for agents unfamiliar with it
- **references/ASYNC_PATTERNS.md**: Complete async/await patterns for production
- **references/DATA_OPERATIONS.md**: CRUD operations, views, subsets
- **scripts/test_connection.py**: Quick validation utility

## Lessons Learned

### What Worked Well
1. **Organizing by feature area**: Users quickly found what they needed
2. **Including test scripts**: Validation script helped users debug connection issues
3. **Async samples**: Showing both sync and async prevented confusion about which to use

### What We'd Do Differently
1. **SIZE MANAGEMENT**: File sizes got away from us - ASYNC_PATTERNS.md hit 1,150 lines before we split it
   - Better approach: Split proactively at 800 lines, not at 1,000
   
2. **VERSION SPECIFICITY**: We assumed TM1py 2.0+ but should have documented version-specific differences
   - Lesson: Always note minimum version requirements upfront

3. **LESS COPY-PASTE**: Some scripts are too generic
   - Lesson: Samples should be more concrete and realistic, not generalized code

## Current Status & Future

### Scope
- **In scope**: Using TM1py to work with cube data, dimensions, hierarchies, subsets
- **Out of scope**: TurboIntegrator scripting, MDX optimization beyond basics, IBM Cloud specifics
- **Why**: TM1py covers client-side operations; TI and cloud require separate expertise

### Known Limitations
1. **Performance optimization**: The skill covers basic operations but doesn't deep-dive into query optimization or caching strategies
2. **Error handling**: Real systems need enterprise error recovery patterns not fully documented here
3. **Security**: Only covers basic SSL; enterprise security policies were out of scope

### Future Enhancements
- [ ] Add performance optimization guide based on real-world patterns
- [ ] Create troubleshooting guide for common TM1py errors
- [ ] Add samples for TI orchestration from TM1py

---

**For current documentation**, see [SKILL.md](./tm1py/SKILL.md)
```

### Key Points for Writing GENESIS.md

**Do:**
- ✅ Focus on **why** decisions were made, not just what was decided
- ✅ Document **evolutionary thinking** - how understanding changed during creation
- ✅ Record **discoveries** that shaped design
- ✅ Explain **known limitations** and why they exist
- ✅ Be **honest** about mistakes and lessons learned
- ✅ Keep it **pragmatic** - this is for future maintainers, not marketing

**Don't:**
- ❌ Make it a lengthy personal journal
- ❌ Repeat information from SKILL.md
- ❌ Create marketing copy
- ❌ Document every small change (focus on *major* decisions)

## .gitignore - Artifact Exclusion

### Purpose

.gitignore tells Git which files to ignore when committing. This keeps repositories clean by excluding:
- Temporary build artifacts
- OS-specific files
- Editor configurations
- Cache/compiled files

### When to Create .gitignore

**Always create .gitignore for:**
- ✅ ANY skill repository (even simple ones)
- ✅ Projects that might generate build artifacts
- ✅ Multi-contributor projects (ensures consistency)

**Especially important for:**
- Repositories with Python scripts
- Repositories with multiple languages/tools
- Projects that use editors with config files

### Recommended .gitignore Template

```gitignore
# Build artifacts & validation
VALIDATION.md
.validation-cache/
*.tmp
build/
dist/

# OS files
.DS_Store
Thumbs.db
*.swp
*~

# Editor configurations (adjust by team preference)
.vscode/
.idea/
*.sublime-project
*.sublime-workspace

# Python artifacts
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
*.egg-info/
venv/
.venv/
*.virtualenv

# Node artifacts (if applicable)
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Logs
*.log

# IDE
.env.local
.env.*.local
```

### Important: Files to COMMIT

Always commit these (don't add to .gitignore):
- ✅ .gitignore itself
- ✅ LICENSE
- ✅ README.md
- ✅ CHANGELOG.md
- ✅ GENESIS.md (project history should be preserved)
- ✅ SKILL.md
- ✅ All reference files
- ✅ All scripts and assets (if they're source, not generated)

## Quick Decision Checklist

### Should I create GENESIS.md?

Answer these questions:
- Is this skill complex with non-obvious design choices? → YES = Create GENESIS.md
- Was there significant research or resource gathering? → YES = Create GENESIS.md
- Will this skill be maintained long-term or by a team? → YES = Create GENESIS.md
- Do future maintainers need to understand the "why"? → YES = Create GENESIS.md
- Is this a simple, straightforward skill? → YES = Skip GENESIS.md (optional)

### Should I create .gitignore?

Answer these questions:
- Does my repository have any potential artifacts? → YES = Create .gitignore
- Are multiple people contributing? → YES = Create .gitignore
- Could builds generate temporary files? → YES = Create .gitignore

**ANSWER: Always create .gitignore** (it's just good practice)

## When NOT to Create Added Files

**Skip GENESIS.md if:**
- ❌ Skill is very simple (< 10 lines of logic)
- ❌ Skill is purely instructional with no design decisions
- ❌ Skill is temporary or experimental
- ❌ You're in a rush and can add it later

**Never skip .gitignore** - even 5-minute skills should have one

## File Maintenance

### Keeping GENESIS.md Updated

When significant versions are released:
- Add **Future Enhancements** section updates
- Note if major **limitations were resolved**
- Document **new discoveries** if major changes occur
- Create a **v2.0 Genesis** if architecture radically changes

**Example update:**
```markdown
## Version 2.0 Evolution (August 2026)

After 100+ users and 50+ issues, we discovered:
- [New learning that changed design]
- [Major request that reshaped scope]

### v2.0 Changes
- [What changed from v1.0]
- [Why this evolution was needed]
```

### Maintaining .gitignore

Review .gitignore whenever:
- New build tools are added
- Team changes development environments
- New artifact types appear in repository

## Validation

Before publishing repository, confirm:

- [ ] .gitignore exists at repository root
- [ ] .gitignore excludes all artifacts (VALIDATION.md, .tmp, etc.)
- [ ] GENESIS.md (if created) explains major design decisions
- [ ] LICENSE file exists with current year
- [ ] README.md explains how to install the skill
- [ ] CHANGELOG.md documents version history
- [ ] No build artifacts committed to Git
- [ ] No .gitignore entries are causing needed files to be ignored

---

**Next Steps:**
- Create .gitignore immediately
- Create GENESIS.md if your skill has meaningful design decisions
- Add to repository documentation checklist before publishing
