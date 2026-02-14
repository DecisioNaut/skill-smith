# Refactoring Guide

**Reference for:** Patterns and strategies for refactoring existing Agent Skills

> **Related:** See [ORGANIZATIONAL_PATTERNS.md](./ORGANIZATIONAL_PATTERNS.md) for file organization patterns and [CONSISTENCY_CHECKLIST.md](./CONSISTENCY_CHECKLIST.md) for validation

## When to Refactor

Refactor when you notice:
- SKILL.md exceeds 500 lines
- Multiple related skills could share common references
- File structure has artifacts or unnecessary files
- References are poorly organized
- Inconsistencies across files

## Splitting Oversized SKILL.md

### Step 1: Identify Moveable Sections

Look for sections that:
- Are detailed reference material (not core workflow)
- Could stand alone
- Are > 50-100 lines
- Have clear boundaries

**Common candidates:**
- Complete API documentation
- Extended code examples
- Detailed error codes
- Glossaries or terminology
- Configuration references

### Step 2: Choose Reference File Names

Use ALL_CAPS.md format:
- **Specific**: `AUTHENTICATION.md` not `AUTH.md`
- **Clear purpose**: `ERROR_CODES.md` not `ERRORS.md`
- **Related prefix**: `NETWORKING.md` + `NETWORKING_ADVANCED.md`

### Step 3: Move Content with Cross-References

**In SKILL.md,** replace detailed section with brief overview + reference:

```markdown
## Authentication

Basic authentication uses API keys:

```bash
curl -H "Authorization: Bearer YOUR_KEY" https://api.example.com
```

For detailed authentication patterns, OAuth flows, and token management, 
see [references/AUTHENTICATION.md](references/AUTHENTICATION.md).
```

**In references/AUTHENTICATION.md**, add full details:

```markdown
# Authentication Patterns

**Reference for:** Complete authentication methods including API keys, OAuth, and token management

> **Prerequisites:** Read main SKILL.md for basic authentication setup

## API Key Authentication

[Full detailed content...]

## OAuth 2.0 Flow

[Complete OAuth guide...]
```

### Step 4: Update Internal Links

Check for:
- Section anchor links that moved
- Cross-references between sections
- Table of contents if present

### Step 5: Validate

- [ ] SKILL.md now under 500 lines
- [ ] All references in SKILL.md point to correct files
- [ ] Reference files are well-structured
- [ ] Run `skills-ref validate`

## Reorganizing References

### Patterns to Apply

#### 1. Group by Topic

Keep related content together:
```
references/
├── NETWORKING.md
├── NETWORKING_ADVANCED.md
├── SECURITY.md
├── KUBERNETES.md
```

#### 2. Split by Complexity

Separate basics from advanced:
```
references/
├── CONFIGURATION.md           (basics)
├── CONFIGURATION_ADVANCED.md  (advanced)
```

#### 3. Keep Files Focused

Each file should have one clear purpose:
- ✅ AUTHENTICATION.md - All auth methods
- ✅ ERROR_CODES.md - All error codes
- ❌ MISC.md - Random topics (avoid!)

### Example Refactoring

**Before:**
```
my-skill/
├── SKILL.md (850 lines)
└── README.md
```

**After:**
```
my-skill/
├── SKILL.md (420 lines)
├── README.md
└── references/
    ├── API_REFERENCE.md (280 lines)
    ├── EXAMPLES.md (150 lines)
    └── ERROR_CODES.md (120 lines)
```

**SKILL.md went from 850 → 420 lines**
**Total content preserved, better organized**

## Removing Artifacts

### Common Artifacts to Remove

**Build artifacts:**
```bash
rm VALIDATION.md
rm -rf .validation-cache/
rm -rf build/ dist/
```

**OS-specific files:**
```bash
rm .DS_Store
rm Thumbs.db
find . -name "*.swp" -delete
find . -name "*~" -delete
```

**Empty directories:**
```bash
# Remove only if empty
rmdir scripts/    # if no scripts needed
rmdir assets/     # if no assets
rmdir examples/   # if no examples
```

### Update .gitignore

```gitignore
# Build artifacts
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

# Editor configurations
.vscode/
.idea/
*.sublime-*
```

## Consistency Checking

After refactoring, verify consistency across files:

### Cross-File Checks

- [ ] Skill name matches in SKILL.md, README.md, directory name
- [ ] Version number same in SKILL.md frontmatter and CHANGELOG.md
- [ ] All file references in SKILL.md actually exist
- [ ] Terminology used consistently (e.g., "API key" not sometimes "api-key")
- [ ] Code examples use consistent style

### Reference File Checks

- [ ] Each file has clear title and purpose
- [ ] Files > 400 lines have table of contents
- [ ] Cross-references use relative paths correctly
- [ ] No duplicate content across files
- [ ] All code blocks have language tags

See [CONSISTENCY_CHECKLIST.md](./CONSISTENCY_CHECKLIST.md) for complete checklist.

## Before and After Examples

### Example 1: API Skill Refactoring

**Before (720-line SKILL.md):**
- Authentication (80 lines)
- Endpoints (300 lines)
- Request/Response formats (150 lines)
- Error codes (120 lines)
- Examples (70 lines)

**After:**
- SKILL.md (380 lines): Core instructions + quick start
- references/AUTHENTICATION.md (95 lines): Full auth patterns
- references/API_REFERENCE.md (320 lines): Complete endpoint docs
- references/ERROR_CODES.md (130 lines): All error codes

**Benefits:**
- SKILL.md loads faster (380 vs 720 lines)
- Easier to find specific information
- Can update error codes without changing main skill
- Progressive disclosure works as intended

### Example 2: Docker Skill Split

**Before:**
- SKILL.md (650 lines): Everything about networking

**After:**
- SKILL.md (430 lines): Core Docker instructions
- references/NETWORKING.md (320 lines): Basic networking concepts
- references/NETWORKING_ADVANCED.md (280 lines): Advanced patterns (VPN, security, mesh)

**Why this works:**
- Clear progression: basic → advanced
- Users can find relevant content quickly
- Advanced topics don't overwhelm beginners

## Tips for Successful Refactoring

1. **One change at a time** - Don't reorganize everything simultaneously
2. **Test after each change** - Run validation, check links work
3. **Use Planning Document** - Track changes in PLANNING.md (delete before commit)
4. **Update CHANGELOG.md** - Document structural improvements
5. **Increment version** - Patch for structure-only, minor if adding content
6. **Keep total content similar** - Refactoring reorganizes, doesn't add/remove much
7. **Preserve user value** - Don't remove useful content during cleanup

## Resources

- [ORGANIZATIONAL_PATTERNS.md](./ORGANIZATIONAL_PATTERNS.md) - File organization patterns
- [BEST_PRACTICES.md](./BEST_PRACTICES.md) - Writing guidance and structure patterns
- [CONSISTENCY_CHECKLIST.md](./CONSISTENCY_CHECKLIST.md) - Validation checklist
- [SPECIFICATION.md](./SPECIFICATION.md) - Agent Skills specification
