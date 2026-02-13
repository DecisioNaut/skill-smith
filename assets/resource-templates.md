# Resource Gathering Templates

Use these templates to systematically collect information when building a new Agent Skill.

## Template 1: GitHub Repository Analysis

Use this when analyzing an open-source repository as a resource for building a skill.

### Repository Information

**Repository URL:** _________________

**Primary Language(s):** _________________

**Purpose/Domain:** _________________

### Key Files to Examine

- [ ] **README.md** - Overview, installation, usage
- [ ] **CONTRIBUTING.md** - Development guidelines
- [ ] **docs/** - Documentation directory
- [ ] **examples/** - Example code and use cases
- [ ] **tests/** - Test files (show edge cases and error handling)
- [ ] **LICENSE** - Licensing information

### Questions to Answer

1. **What problem does this tool/library solve?**
   
   Answer: _________________

2. **What are the 3-5 most common use cases?**
   
   - _________________
   - _________________
   - _________________
   - _________________
   - _________________

3. **What are the prerequisites? (dependencies, tools, access)**
   
   Requirements: _________________

4. **What are the key concepts or terminology to understand?**
   
   - _________________
   - _________________
   - _________________

5. **What does the typical workflow look like? (step-by-step)**
   
   1. _________________
   2. _________________
   3. _________________
   4. _________________

6. **What are common errors or failure modes?**
   
   - _________________
   - _________________
   - _________________

7. **Are there good code examples to reference?**
   
   Location: _________________

8. **What authentication or configuration is needed?**
   
   Details: _________________

### Files/Sections to Reference in Skill

| Source File | Content Type | Include in Skill Where? |
|-------------|--------------|-------------------------|
| Example: README.md#Installation | Setup steps | SKILL.md Prerequisites |
| | | |
| | | |

---

## Template 2: Documentation Website Analysis

Use this when analyzing a documentation website as a resource.

### Website Information

**Website URL:** _________________

**Product/Service Name:** _________________

**Documentation Type:** (API Reference / Tutorial / User Guide / Mixed) _________________

### Site Structure Analysis

**Main Navigation Sections:**
- _________________
- _________________
- _________________
- _________________

**Quick Start / Getting Started URL:** _________________

**API Reference URL:** _________________

**Examples/Tutorials URL:** _________________

### Content Extraction

1. **Core Concepts (what users need to understand first)**
   
   - Concept 1: _________________
   - Concept 2: _________________
   - Concept 3: _________________

2. **Authentication/Authorization (if applicable)**
   
   Method: _________________
   
   Steps: _________________

3. **Most Common Operations (top 5)**
   
   - Operation 1: _________________
   - Operation 2: _________________
   - Operation 3: _________________
   - Operation 4: _________________
   - Operation 5: _________________

4. **Code Examples Available?**
   
   - [ ] Yes, in multiple languages
   - [ ] Yes, single language: _________________
   - [ ] No code examples
   - [ ] Interactive playground/sandbox available

5. **Error Codes / Troubleshooting Section?**
   
   URL: _________________
   
   Key errors: _________________

6. **Rate Limits / Quotas / Constraints?**
   
   Details: _________________

7. **Best Practices Section?**
   
   URL: _________________
   
   Key practices: _________________

### Pages to Deep-Link in Skill

| Topic | URL | Use in Skill For |
|-------|-----|------------------|
| Example: Authentication | https://... | Setup instructions |
| | | |
| | | |

---

## Template 3: API Reference Analysis

Use this when the resource is primarily an API (REST, GraphQL, etc.).

### API Information

**Base URL:** _________________

**API Type:** (REST / GraphQL / SOAP / gRPC / Other) _________________

**Documentation URL:** _________________

**API Version:** _________________

### Authentication

**Method:** (API Key / OAuth / JWT / Basic Auth / Other) _________________

**How to obtain credentials:**

1. _________________
2. _________________
3. _________________

**How credentials are used:**

```
Example: Authorization: Bearer YOUR_TOKEN
```

### Core Endpoints/Operations

| Endpoint/Operation | Method | Purpose | Example |
|-------------------|--------|---------|---------|
| Example: /api/users | GET | Fetch users | `curl https://api.../users` |
| | | | |
| | | | |
| | | | |
| | | | |

### Request/Response Formats

**Common Request Structure:**
```json
{
  "field1": "type",
  "field2": "type"
}
```

**Common Response Structure:**
```json
{
  "status": "...",
  "data": {},
  "errors": []
}
```

### Error Handling

| Error Code | Meaning | How to Handle |
|------------|---------|---------------|
| 401 | Unauthorized | Check API key |
| 429 | Rate limited | Wait and retry |
| | | |
| | | |

### Special Considerations

- **Rate Limits:** _________________
- **Pagination:** _________________
- **Filtering/Sorting:** _________________
- **Webhooks/Callbacks:** _________________
- **Batch Operations:** _________________

---

## Template 4: Comprehensive Resource Checklist

Use this holistic checklist to ensure you have all necessary context before building the skill.

### ✅ Scope Definition

- [ ] I clearly understand what the skill should do
- [ ] I have identified 3-5 concrete use cases
- [ ] I know what success looks like
- [ ] I understand the target user's expertise level

### ✅ Resources Gathered

- [ ] Official documentation reviewed
- [ ] Example repositories examined
- [ ] Code samples collected
- [ ] API/technical specs obtained
- [ ] Existing similar skills reviewed (if any)

### ✅ Prerequisites Identified

- [ ] Required tools/software listed
- [ ] Dependencies documented
- [ ] Authentication/access requirements clear
- [ ] System/environment requirements noted
- [ ] Estimated setup time: _________

### ✅ Core Knowledge Extracted

- [ ] Key terminology defined
- [ ] Core concepts understood
- [ ] Common workflow mapped out
- [ ] Edge cases identified
- [ ] Error handling patterns noted

### ✅ Examples Prepared

- [ ] At least 2 complete, working examples ready
- [ ] Examples cover common use case
- [ ] Examples show expected input and output
- [ ] Edge case example available
- [ ] All examples have been tested

### ✅ Structure Planned

- [ ] Skill complexity level decided (simple/medium/full)
- [ ] SKILL.md outline drafted
- [ ] Need for scripts/ directory determined
- [ ] Need for references/ directory determined
- [ ] Need for assets/ directory determined

### ✅ Validation Ready

- [ ] Skill name follows rules (lowercase, kebab-case, 1-64 chars)
- [ ] Description written (includes what + when + keywords)
- [ ] Description is 1-1024 characters
- [ ] Instructions are actionable and clear
- [ ] No assumed knowledge remains undefined

---

## Template 5: Interactive Resource Request

Use this template when you need to ask the user for more resources or clarification.

### Initial Understanding

Based on what I know so far, here's my understanding of the skill:

**Purpose:** [What you understand the skill should do]

**Target Users:** [Who would use this]

**Complexity:** [Simple/Medium/Complex based on initial impression]

### Gaps in Knowledge

To build an effective skill, I need more information about:

1. **[Topic/Area where you need more info]**
   
   Specifically: [What exactly you need to know]
   
   Why: [How this will be used in the skill]

2. **[Another topic/area]**
   
   Specifically: [What you need]
   
   Why: [How this helps]

### Requested Resources

Can you provide:

- [ ] **Documentation Links**
  - [ ] Official docs: [URL]
  - [ ] API reference: [URL]
  - [ ] Tutorials: [URL]

- [ ] **Example Repositories**
  - [ ] Repository 1: [URL] - [What it demonstrates]
  - [ ] Repository 2: [URL] - [What it demonstrates]

- [ ] **Specific Information**
  - [ ] How authentication works: [Details]
  - [ ] Common error scenarios: [Details]
  - [ ] Performance considerations: [Details]

- [ ] **Validation**
  - [ ] Can you provide a real example task I can test against?
  - [ ] What does successful output look like?
  - [ ] Are there any dealbreakers or must-haves?

### Alternative Approach

If some resources aren't available, I can:

- [ ] Build a basic version and iterate
- [ ] Focus on a subset of functionality
- [ ] Make reasonable assumptions and document them
- [ ] Other: _________________

---

## Template 6: Example-Driven Resource Gathering

Use this when you want to build the skill based on concrete examples provided by the user.

### Example Request Template

To build this skill effectively, please provide 2-3 real examples:

#### Example 1: [Common/Basic Case]

**Task Description:** What needs to be accomplished?

**Context:** What information is available at the start?

**Steps Taken:** What actions are performed?
1. 
2. 
3. 

**Result:** What's the end state or output?

**Common Issues:** Were there any challenges or errors?

---

#### Example 2: [More Complex Case]

**Task Description:** 

**Context:** 

**Steps Taken:**
1. 
2. 
3. 

**Result:** 

**Common Issues:** 

---

#### Example 3: [Edge Case or Variation]

**Task Description:** 

**Context:** 

**Steps Taken:**
1. 
2. 
3. 

**Result:** 

**Common Issues:** 

---

### Analysis After Examples

After receiving examples:

1. **Common patterns identified:**
   - _________________
   - _________________

2. **Variations to handle:**
   - _________________
   - _________________

3. **Error handling needs:**
   - _________________
   - _________________

4. **Additional resources needed:**
   - _________________
   - _________________

---

## Template 7: Quick Resource Assessment

Use this for a rapid initial assessment of whether you have enough information to proceed.

### Quick Checklist (5-Minute Assessment)

Answer YES/NO/PARTIAL:

- [ ] I know what problem this skill solves: _____
- [ ] I have at least one working example: _____
- [ ] I understand the main workflow: _____
- [ ] I know what tools/libraries are involved: _____
- [ ] I have access to documentation or code: _____
- [ ] I understand prerequisites and setup: _____
- [ ] I know what errors commonly occur: _____
- [ ] I have identified 3-5 keywords for the description: _____

### Decision Matrix

**Score:** (Count YES = 1, PARTIAL = 0.5, NO = 0) = _____ / 8

| Score | Decision | Action |
|-------|----------|--------|
| 6-8 | ✅ Sufficient | Proceed with building the skill |
| 4-5 | ⚠️ Gaps exist | Request specific resources (use Template 5) |
| 0-3 | ❌ Insufficient | Need substantial more information |

### Next Steps

Based on score: _________________

---

## Using These Templates

### When Building a Skill

1. **Start with Template 7** (Quick Assessment) to determine readiness
2. **Use Templates 1-3** based on resource type (repo/docs/API)
3. **Apply Template 4** (Comprehensive Checklist) before starting SKILL.md
4. **Use Template 5** (Interactive Request) if gaps remain
5. **Try Template 6** (Example-Driven) if resources are sparse but examples are available

### Template Selection Guide

| Resource Type | Recommended Template |
|---------------|---------------------|
| GitHub Repository | Template 1 |
| Documentation Site | Template 2 |
| API Reference | Template 3 |
| Mixed/Multiple | Template 4 |
| Incomplete Info | Template 5 |
| User Examples | Template 6 |
| Initial Assessment | Template 7 |

### Tips for Effective Resource Gathering

1. **Be systematic**: Work through templates methodically
2. **Take notes**: Document what you learn as you explore resources
3. **Test examples**: Try running code samples to verify they work
4. **Ask specific questions**: If requesting more info, be precise about what you need
5. **Focus on user needs**: Gather what will help users accomplish tasks, not just reference material
6. **Look for patterns**: Similar operations often follow similar patterns
7. **Document gaps**: Note what's missing so you can fill it later

### Customizing Templates

Feel free to adapt these templates based on:
- Domain-specific needs
- Organizational requirements
- Available resources
- Time constraints
- Complexity of the skill being built

---

**Remember:** The goal is to gather enough information to write clear, actionable instructions. It's better to spend time understanding the domain deeply than to rush into writing incomplete or unclear skill instructions.
