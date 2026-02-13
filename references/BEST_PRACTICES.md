# Agent Skills Best Practices

This guide provides best practices for writing effective Agent Skills that work reliably with AI agents.

## Core Principles

### 1. Progressive Disclosure

Skills should reveal information gradually:

- **First contact (name + description)**: ~50-100 tokens
- **Activation (full SKILL.md)**: ~500-5000 tokens recommended
- **Deep dive (references, scripts)**: Loaded only when needed

**Why this matters:**
- Agents start faster (don't load everything at once)
- Context is used efficiently (load only what's needed)
- Skills scale better (can have many skills without overhead)

**Implementation:**
```markdown
<!-- In SKILL.md: Keep main instructions focused -->
For detailed API reference, see `references/REFERENCE.md`

<!-- In references/REFERENCE.md: Put exhaustive details here -->
```

### 2. Clarity Over Cleverness

Write for an AI that follows instructions literally.

**❌ Avoid:**
```markdown
You might want to consider checking if the file exists before proceeding.
```

**✅ Prefer:**
```markdown
1. Check if the file exists using `test -f filename`
2. If the file doesn't exist, create it with `touch filename`
3. Then proceed with the next steps
```

**Why:** Agents execute instructions as written. Vague suggestions lead to inconsistent behavior.

### 3. Self-Documenting Structure

A skill should be understandable by reading SKILL.md alone.

**Good indicators:**
- Headings reveal the logical flow
- Examples show expected inputs and outputs
- Prerequisites are stated upfront
- Troubleshooting addresses common issues

**Bad indicators:**
- You need to read external docs to understand basics
- Instructions reference concepts without explaining them
- No examples of successful execution
- Error messages aren't mentioned

## Writing Effective Descriptions

The `description` field is critical for skill discovery.

### Formula for Good Descriptions

**Structure:** `[What it does] + [When to use it] + [Keywords]`

**Examples:**

```yaml
# API Integration
description: Connects to REST APIs, handles authentication, and processes JSON responses. Use when integrating with web services, APIs, or webhooks, or when the user mentions REST, HTTP requests, or API calls.

# Data Analysis
description: Analyzes CSV and Excel files with statistical summaries, correlations, and visualizations. Use when analyzing datasets, generating reports, or when the user mentions data analysis, statistics, or spreadsheets.

# Code Review
description: Reviews code for bugs, security issues, style violations, and best practices. Use when reviewing pull requests, auditing code quality, or when the user mentions code review, linting, or security scanning.
```

### Description Anti-Patterns

**Too vague:**
```yaml
description: Helps with files  # ❌ What kind of files? How?
```

**Too technical:**
```yaml
description: Implements file I/O operations using buffered streams  # ❌ Internal details, not user benefits
```

**Missing "when to use":**
```yaml
description: Processes PDF files  # ❌ Agents won't know when to activate
```

**Missing keywords:**
```yaml
description: Handles documents  # ❌ No specific terms (PDF, extract, form, etc.)
```

### Keyword Strategy

Include terms that:
- Users naturally say ("merge PDFs", "create slides", "analyze data")
- Describe the domain ("REST API", "OAuth", "JSON")
- Indicate the task type ("extract", "generate", "validate", "format")

## Structuring Instructions

### Use Action-Oriented Headings

**❌ Avoid:**
```markdown
## About Authentication
## Understanding the API
## Discussion of Error Handling
```

**✅ Prefer:**
```markdown
## Authenticate with API Key
## Make API Requests
## Handle API Errors
```

### Write Step-by-Step Instructions

Break complex tasks into sequential steps.

**❌ Avoid:**
```markdown
Use the API to fetch data and process it accordingly. Make sure to handle errors and log the results.
```

**✅ Prefer:**
```markdown
1. Set the API key in an environment variable:
   ```bash
   export API_KEY="your-key-here"
   ```

2. Make a GET request to fetch data:
   ```bash
   curl -H "Authorization: Bearer $API_KEY" https://api.example.com/data
   ```

3. Check the response status:
   - If 200 OK: Parse the JSON response (see example below)
   - If 401: API key is invalid, check the key and retry
   - If 429: Rate limited, wait 60 seconds and retry

4. Process the JSON data:
   ```python
   import json
   data = json.loads(response_text)
   for item in data['results']:
       print(f"ID: {item['id']}, Name: {item['name']}")
   ```

5. Log the result:
   ```bash
   echo "Processed $(echo $data | jq '.results | length') items" >> log.txt
   ```
```

### Include Concrete Examples

Show complete, working examples with real data.

**❌ Avoid:**
```markdown
Call the API endpoint with the appropriate parameters and parse the response.
```

**✅ Prefer:**
```markdown
### Example: Fetch User Data

**Request:**
```bash
curl -X GET "https://api.example.com/users/123" \
  -H "Authorization: Bearer abc123xyz"
```

**Expected Response:**
```json
{
  "id": 123,
  "name": "Alice Smith",
  "email": "alice@example.com",
  "created_at": "2026-01-15T10:30:00Z"
}
```

**Processing:**
```python
import requests
response = requests.get('https://api.example.com/users/123',
                       headers={'Authorization': 'Bearer abc123xyz'})
user = response.json()
print(f"User: {user['name']} ({user['email']})")
# Output: User: Alice Smith (alice@example.com)
```
```

### Address Edge Cases Explicitly

Don't assume agents will infer error handling.

**❌ Avoid:**
```markdown
Fetch the data from the API.
```

**✅ Prefer:**
```markdown
Fetch the data from the API:

1. Make the request (see example above)
2. If the response status is 404: The resource doesn't exist, inform the user
3. If the response status is 500: Server error, retry up to 3 times with exponential backoff
4. If the request times out: Check network connection and retry
5. If successful (200): Parse the JSON and continue
```

## Organizing Skill Content

### When to Use scripts/

**Use scripts/ when:**
- Logic is too complex for step-by-step instructions
- Multiple languages or tools are involved
- Reusable components exist (parsers, validators, formatters)
- Error handling requires sophisticated control flow

**Example:**
```
scripts/
├── extract_data.py      # Data extraction logic
├── validate_schema.py   # JSON schema validation
└── generate_report.sh   # Combines scripts into workflow
```

**In SKILL.md:**
```markdown
## Extract Data from API

Run the extraction script:
```bash
python scripts/extract_data.py --endpoint users --output users.json
```

This script handles authentication, pagination, and rate limiting automatically.
```

### When to Use references/

**Use references/ when:**
- Main SKILL.md is getting long (>500 lines)
- Detailed technical specs exist (API docs, schemas)
- Domain knowledge requires depth (glossary, domain concepts)
- Multiple related topics need organization

**Example structure:**
```
references/
├── REFERENCE.md    # Complete API documentation
├── FORMS.md        # JSON schemas, request/response templates
├── GLOSSARY.md     # Domain-specific terminology
└── ERRORS.md       # Complete error code reference
```

**In SKILL.md:**
```markdown
## API Reference

For the complete list of endpoints, see `references/REFERENCE.md`.

For request/response schemas, see `references/FORMS.md`.
```

### Keep File References Shallow (One Level Deep)

**Important rule from the specification**: File references should be "one level deep" from SKILL.md. Avoid nested reference chains.

**✅ Good (one level):**
```markdown
<!-- In SKILL.md -->
For API details, see `references/API.md`
For examples, see `references/EXAMPLES.md`
```

**❌ Bad (nested chain):**
```markdown
<!-- In SKILL.md -->
See `references/OVERVIEW.md`

<!-- In references/OVERVIEW.md -->
See `references/details/API.md`  ← Agents may not follow this

<!-- In references/details/API.md -->
See `references/details/auth/OAUTH.md`  ← Too deep!
```

**Why:** Nested references create cognitive load and may not be followed reliably. Keep it flat and direct.

### When to Use assets/

**Use assets/ when:**
- Template files are needed (config templates, document templates)
- Diagrams or images clarify complex concepts
- Sample data helps with testing or examples
- Lookup tables or reference data exist

**Example:**
```
assets/
├── templates/
│   ├── config.yaml.template
│   └── report.md.template
├── diagrams/
│   └── workflow.png
└── sample_data/
    └── test_dataset.json
```

### Keep Files Focused

**One file, one purpose:**

```
references/
├── api_auth.md          # ✅ Just authentication
├── api_endpoints.md     # ✅ Just endpoint docs
└── api_examples.md      # ✅ Just examples

# ❌ Avoid: mega_api_docs.md (3000 lines of everything)
```

## Agent-Friendly Language

### Be Direct and Specific

**❌ Avoid:**
```markdown
- You should probably validate the input
- Consider using error handling
- It might be a good idea to check permissions
```

**✅ Prefer:**
```markdown
- Validate the input using the schema in FORMS.md
- Wrap the API call in a try-except block
- Check file permissions with `test -r filename`
```

### Use Consistent Terminology

Pick one term and stick with it throughout the skill.

**❌ Inconsistent:**
```markdown
1. Fetch the data from the API
2. Retrieve the response and validate it
3. Get the results and process them
```
*(Using "fetch", "retrieve", "get" interchangeably is confusing)*

**✅ Consistent:**
```markdown
1. Fetch the data from the API
2. Fetch the response and validate it
3. Fetch the results and process them
```

### Avoid Ambiguous Pronouns

**❌ Avoid:**
```markdown
Parse the JSON response and extract the ID. If it is null, use the fallback value. Then process it accordingly.
```
*(What does "it" refer to? The ID? The response?)*

**✅ Prefer:**
```markdown
Parse the JSON response and extract the ID. If the ID is null, use the fallback value. Then process the ID accordingly.
```

## Examples and Testing

### Provide Complete Examples

An example should be self-contained and runnable.

**❌ Incomplete:**
```markdown
### Example
```python
result = process_data(data)
```
```

**✅ Complete:**
```markdown
### Example: Process User Data

Given this input file `users.json`:
```json
[
  {"id": 1, "name": "Alice", "active": true},
  {"id": 2, "name": "Bob", "active": false}
]
```

Run this script:
```python
import json

with open('users.json', 'r') as f:
    users = json.load(f)

active_users = [u for u in users if u['active']]
print(f"Found {len(active_users)} active users")
for user in active_users:
    print(f"  - {user['name']} (ID: {user['id']})")
```

Expected output:
```
Found 1 active users
  - Alice (ID: 1)
```
```

### Show Edge Cases

**Include examples for:**
- Empty inputs
- Invalid data
- Error conditions
- Boundary cases

**Example:**
```markdown
### Example: Empty Input

When the input file is empty:
```json
[]
```

The script should output:
```
Found 0 active users
(no users to display)
```

### Example: Invalid Data

When a user record is missing the 'active' field:
```json
[{"id": 1, "name": "Charlie"}]
```

The script treats missing 'active' as false and outputs:
```
Found 0 active users
```
```

### Test Your Instructions

**Before finalizing a skill:**

1. **Literal reading test**: Follow your own instructions exactly. Don't fill in gaps.
2. **Fresh eyes test**: Have someone unfamiliar with the domain try to use it.
3. **Agent test**: If possible, give your skill to an agent and observe behavior.
4. **Edge case test**: Try unusual inputs, empty data, error conditions.

## Common Mistakes and Fixes

### Mistake 1: Assuming Implicit Knowledge

**❌ Problem:**
```markdown
Use the standard authentication flow.
```

**✅ Fix:**
```markdown
Authenticate using OAuth 2.0:

1. Obtain client credentials from the API dashboard
2. Request an access token:
   ```bash
   curl -X POST https://auth.example.com/token \
     -d "client_id=YOUR_ID" \
     -d "client_secret=YOUR_SECRET" \
     -d "grant_type=client_credentials"
   ```
3. Use the token in API requests:
   ```bash
   curl -H "Authorization: Bearer YOUR_TOKEN" https://api.example.com/resource
   ```
```

### Mistake 2: Overloading One Skill

**❌ Problem:**
A single skill tries to do:
- API integration
- Data analysis
- Report generation
- Email sending
- Database storage

**✅ Fix:**
Split into focused skills:
- `api-data-fetcher` - Fetches data from APIs
- `data-analyzer` - Analyzes datasets
- `report-generator` - Creates reports
- `email-sender` - Sends emails
- `database-writer` - Writes to databases

### Mistake 3: Burying Important Info

**❌ Problem:**
```markdown
## Introduction
[500 words of background]

## History
[300 words of context]

## Prerequisites
You need Python 3.8 and an API key  # ← Important info buried
```

**✅ Fix:**
```markdown
## Prerequisites

- Python 3.8 or higher
- API key from https://example.com/keys

## Overview
[Brief intro]

[Rest of content...]
```

### Mistake 4: Vague Error Guidance

**❌ Problem:**
```markdown
If you encounter errors, check the logs and try again.
```

**✅ Fix:**
```markdown
## Troubleshooting

**Error: "Authentication failed (401)"**
- **Cause**: Invalid or expired API key
- **Solution**: 
  1. Verify your API key at https://example.com/dashboard
  2. Check for trailing spaces in the key
  3. Generate a new key if needed

**Error: "Rate limit exceeded (429)"**
- **Cause**: Too many requests in a short time
- **Solution**: Wait 60 seconds and retry. Consider implementing exponential backoff.

**Error: "Connection timeout"**
- **Cause**: Network issues or slow API
- **Solution**: 
  1. Check your internet connection
  2. Try increasing timeout: `timeout=30` in your request
  3. Check API status at https://status.example.com
```

### Mistake 5: Missing Context in Examples

**❌ Problem:**
```python
# Example
data = fetch_data()
result = process(data)
print(result)
```

**✅ Fix:**
```python
# Example: Fetch and process user activity data
#
# This example:
# 1. Fetches user activity from the API
# 2. Filters for active users
# 3. Formats output as a summary report

import requests

# Step 1: Fetch data
response = requests.get('https://api.example.com/users/activity',
                        headers={'Authorization': 'Bearer YOUR_KEY'})
data = response.json()

# Step 2: Filter for active users (last_activity within 7 days)
from datetime import datetime, timedelta
cutoff = datetime.now() - timedelta(days=7)
active_users = [
    user for user in data['users']
    if datetime.fromisoformat(user['last_activity']) > cutoff
]

# Step 3: Format and print summary
print(f"Active users (last 7 days): {len(active_users)}")
for user in active_users:
    print(f"  - {user['name']}: last seen {user['last_activity']}")

# Expected output:
# Active users (last 7 days): 3
#   - Alice Smith: last seen 2026-02-12T15:30:00Z
#   - Bob Jones: last seen 2026-02-13T09:15:00Z
#   - Carol White: last seen 2026-02-11T18:45:00Z
```

## Version Control and Maintenance

### Semantic Versioning

Use semantic versioning in metadata:

```yaml
metadata:
  version: "1.0.0"  # Major.Minor.Patch
```

**Increment:**
- **Major (1.x.x → 2.x.x)**: Breaking changes (changed interfaces, removed features)
- **Minor (1.0.x → 1.1.x)**: New features, backwards compatible
- **Patch (1.0.0 → 1.0.1)**: Bug fixes, documentation improvements

### Document Changes

Keep a CHANGELOG.md:

```markdown
# Changelog

## [1.1.0] - 2026-02-13
### Added
- Support for pagination in API requests
- New example for batch processing

### Fixed
- Authentication timeout error handling
- Typo in error message

## [1.0.0] - 2026-01-15
### Initial Release
- Basic API integration
- Authentication support
- Data extraction and processing
```

### Git Tagging

Tag releases in git:
```bash
git tag -a v1.0.0 -m "Initial release"
git push origin v1.0.0
```

## Performance Considerations

### Keep SKILL.md Concise

**Target:** Under 500 lines in SKILL.md

**Why:** Agents load the full SKILL.md into context. Shorter = faster activation.

**How:**
- Move detailed API docs to `references/REFERENCE.md`
- Move examples to `references/EXAMPLES.md`
- Link to external resources for background reading

### Optimize for Scanning

Agents scan for relevant sections using headings.

**Good structure:**
```markdown
# Skill Name
## When to Use
## Prerequisites
## Core Tasks
### Task 1: [Clear Name]
### Task 2: [Clear Name]
## Examples
## Troubleshooting
```

**Agents can quickly jump to:**
- "Task 2" if that's what's needed
- "Examples" to see working code
- "Troubleshooting" if errors occur

## Security Considerations

### Don't Hardcode Secrets

**❌ Never:**
```python
API_KEY = "sk-abc123xyz789"  # ❌ Hardcoded secret
```

**✅ Always:**
```python
import os
API_KEY = os.environ.get('API_KEY')
if not API_KEY:
    raise ValueError("API_KEY environment variable not set")
```

### Warn About Dangerous Operations

**Example:**
```markdown
## Delete Data (⚠️ Destructive Operation)

**Warning:** This permanently deletes data and cannot be undone. Always backup first.

To delete:
1. Create a backup: `cp data.json data.backup.json`
2. Verify the backup: `cat data.backup.json`
3. Run deletion: `python scripts/delete_data.py --confirm`
```

### Validate User Input

**Example:**
```markdown
## Process User Input

1. Validate input format:
   ```python
   import re
   if not re.match(r'^[a-zA-Z0-9_-]+$', user_input):
       raise ValueError("Invalid input: only alphanumeric, dash, underscore allowed")
   ```

2. Sanitize for shell commands:
   ```python
   import shlex
   safe_input = shlex.quote(user_input)
   ```

3. Then proceed with processing
```

## Accessibility and Internationalization

### Use Clear, Simple Language

- Avoid jargon unless defined
- Use common English words
- Define acronyms on first use: "REST (Representational State Transfer) API"

### Support International Characters

```yaml
# ✅ Skill names support Unicode
name: café-reviews
name: 日本語-skill
```

But remember: names must be lowercase after NFKC normalization.

### Provide Context for Code Examples

Don't assume users know the language:

```markdown
### Python Example

This Python script (requires Python 3.8+) demonstrates...
```

```markdown
### Bash Example

This bash command (works on Linux/macOS) will...
```

## Summary Checklist

When creating or reviewing a skill, verify:

### Content Quality
- [ ] Instructions are clear, direct, and actionable
- [ ] Examples are complete and runnable
- [ ] Edge cases are addressed explicitly
- [ ] Troubleshooting covers common errors
- [ ] No assumed knowledge or implicit steps

### Structure
- [ ] Description includes what + when + keywords
- [ ] SKILL.md is under 500 lines
- [ ] Headings are action-oriented
- [ ] Progressive disclosure is used (references/ for details)
- [ ] Files are organized and focused

### Agent-Friendliness
- [ ] Language is direct (no "might", "could", "consider")
- [ ] Terminology is consistent
- [ ] Pronouns are clear (avoid ambiguous "it", "this")
- [ ] Steps are numbered and sequential
- [ ] Examples show expected input and output

### Technical Quality
- [ ] Code examples are tested and work
- [ ] Commands are shown with full syntax
- [ ] Error handling is explicit
- [ ] Security best practices are followed
- [ ] Dependencies are documented

### Maintenance
- [ ] Version is tracked in metadata
- [ ] Changes are documented
- [ ] Git tags match versions
- [ ] README is up to date

## Further Reading

- [Agent Skills Specification](https://agentskills.io/specification)
- [Anthropic's Best Practices Guide](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Example Skills](https://github.com/anthropics/skills)
- [Integration Guide](https://agentskills.io/integrate-skills)
