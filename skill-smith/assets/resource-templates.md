# Resource Gathering Templates

Templates for systematically collecting information when building Agent Skills.

## Table of Contents

- [GitHub Repository Analysis Template](#github-repository-analysis-template)
- [Documentation Website Analysis Template](#documentation-website-analysis-template)
- [API Service Analysis Template](#api-service-analysis-template)
- [Tool/CLI Documentation Analysis Template](#toolcli-documentation-analysis-template)
- [Library/Package Analysis Template](#librarypackage-analysis-template)
- [Specification/Standard Analysis Template](#specificationstandard-analysis-template)
- [Resource Collection Checklist](#resource-collection-checklist)
- [Common Resource Gathering Mistakes](#common-resource-gathering-mistakes)
- [Quick Reference: fetch_webpage Flow](#quick-reference-fetch_webpage-flow)
- [Example: Complete Resource Gathering](#example-complete-resource-gathering)
- [Resources](#resources)

## GitHub Repository Analysis Template

When analyzing a GitHub repository to build a skill:

### Initial Exploration

1. **Fetch main README**:
   ```
   https://github.com/owner/repo
   ```
   Look for: Overview, features, installation, usage samples, links to docs

2. **Fetch repository structure**:
   ```
   https://github.com/owner/repo/tree/main
   ```
   Identify: Main source directories, sample folders, documentation folders

3. **Fetch documentation index** (if exists):
   ```
   https://github.com/owner/repo/tree/main/docs
   ```
   Look for: Index.md, README.md, navigation structure

### Deep Dive Areas

4. **Installation/setup documentation**:
   ```
   https://github.com/owner/repo/blob/main/docs/installation.md
   https://github.com/owner/repo/blob/main/docs/getting-started.md
   ```
   Extract: Prerequisites, installation commands, initial setup steps

5. **API/usage documentation**:
   ```
   https://github.com/owner/repo/blob/main/docs/api.md
   https://github.com/owner/repo/blob/main/docs/usage.md
   https://github.com/owner/repo/blob/main/docs/reference.md
   ```
   Extract: Core functions, parameters, return values, samples

6. **Samples directory**:
   ```
   https://github.com/owner/repo/tree/main/samples
   ```
   Look for complete samples showing typical usage patterns

7. **Source code samples** (if needed):
   ```
   https://github.com/owner/repo/blob/main/src/main.py
   https://github.com/owner/repo/blob/main/lib/core.js
   ```
   Use for: Understanding implementation patterns when docs are sparse

### Quality Checks

- [ ] README fetched and reviewed
- [ ] Installation instructions extracted
- [ ] Core API/usage patterns identified
- [ ] At least 2-3 samples found
- [ ] Error handling patterns noted
- [ ] Dependencies/prerequisites listed
- [ ] Common troubleshooting documented

## Documentation Website Analysis Template

When analyzing a documentation site to build a skill:

### Navigation Mapping

1. **Fetch homepage**:
   ```
   https://docs.example.com/
   ```
   Look for: Navigation structure, key sections, getting started links

2. **Identify main navigation sections**:
   ```
   https://docs.example.com/overview
   https://docs.example.com/guides
   https://docs.example.com/reference
   https://docs.example.com/samples
   ```
   Map out complete structure - **don't stop at homepage!**

### Systematic Page Fetching

3. **Fetch "Getting Started" section** (typically multiple pages):
   ```
   https://docs.example.com/getting-started
   https://docs.example.com/getting-started/installation
   https://docs.example.com/getting-started/quick-start
   https://docs.example.com/getting-started/first-steps
   ```
   Extract: Installation, setup, basic configuration

4. **Fetch core guides/tutorials** (follow navigation links):
   ```
   https://docs.example.com/guides/authentication
   https://docs.example.com/guides/data-operations
   https://docs.example.com/guides/error-handling
   https://docs.example.com/guides/best-practices
   ```
   Extract: Step-by-step processes, common patterns

5. **Fetch API reference** (comprehensive):
   ```
   https://docs.example.com/reference/api
   https://docs.example.com/reference/classes
   https://docs.example.com/reference/functions
   https://docs.example.com/reference/methods
   ```
   Extract: Function signatures, parameters, return types

6. **Fetch guides/recipes**:
   ```
   https://docs.example.com/guides
   https://docs.example.com/guides/basic
   https://docs.example.com/guides/advanced
   https://docs.example.com/recipes
   ```
   Extract: Complete working code samples

7. **Fetch troubleshooting/FAQ**:
   ```
   https://docs.example.com/troubleshooting
   https://docs.example.com/faq
   https://docs.example.com/common-issues
   ```
   Extract: Common problems and solutions

### Multi-Page Exploration Strategy

**Key principle**: Documentation sites have nested pages. Always explore navigation links!

**Pattern to follow**:
```
1. Fetch homepage → Find navigation structure
2. For each major section in navigation:
   a. Fetch section index
   b. Identify sub-pages from navigation/links
   c. Fetch each sub-page systematically
3. Continue until all relevant pages fetched
```

**Example navigation flow**:
```
Homepage
  ├─ Getting Started (INDEX)
  │   ├─ Installation (FETCH)
  │   ├─ Configuration (FETCH)
  │   └─ Quick Start (FETCH)
  ├─ Guides (INDEX)
  │   ├─ Authentication (FETCH)
  │   ├─ Data Processing (FETCH)
  │   ├─ Error Handling (FETCH)
  │   └─ Advanced Topics (FETCH)
  └─ Reference (INDEX)
      ├─ API Methods (FETCH)
      ├─ Configuration (FETCH)
      └─ CLI Commands (FETCH)
```

**Don't stop at the index page - fetch each linked page!**

### Quality Checks

- [ ] Homepage and navigation structure fetched
- [ ] All major sections identified
- [ ] Installation/setup pages fetched (not just overview)
- [ ] Core guides/tutorials fetched (multiple pages)
- [ ] API reference fetched (comprehensive)
- [ ] Samples/recipes fetched
- [ ] Troubleshooting/FAQ fetched
- [ ] Followed links at least 2 levels deep

## API Service Analysis Template

When analyzing an API service to build an integration skill:

### API Documentation

1. **Fetch API overview**:
   ```
   https://api-docs.example.com/
   https://api-docs.example.com/introduction
   ```
   Look for: Base URL, authentication methods, rate limits

2. **Fetch authentication documentation**:
   ```
   https://api-docs.example.com/authentication
   https://api-docs.example.com/auth/api-keys
   https://api-docs.example.com/auth/oauth
   ```
   Extract: How to authenticate, where to get credentials, sample requests

3. **Fetch endpoint documentation** (each major resource):
   ```
   https://api-docs.example.com/endpoints/users
   https://api-docs.example.com/endpoints/projects
   https://api-docs.example.com/endpoints/data
   ```
   Extract: HTTP methods, paths, parameters, request/response samples

4. **Fetch error documentation**:
   ```
   https://api-docs.example.com/errors
   https://api-docs.example.com/error-codes
   ```
   Extract: Error codes, meanings, how to handle

5. **Fetch rate limits/quotas**:
   ```
   https://api-docs.example.com/rate-limits
   https://api-docs.example.com/quotas
   ```
   Extract: Request limits, how to check remaining quota, backoff strategies

### SDK/Client Libraries (if available)

6. **Fetch SDK documentation**:
   ```
   https://api-docs.example.com/sdks
   https://api-docs.example.com/libraries/python
   https://api-docs.example.com/libraries/javascript
   ```
   Look for: Installation, initialization, sample usage

7. **Fetch code samples**:
   ```
   https://api-docs.example.com/samples
   https://api-docs.example.com/code-samples
   https://api-docs.example.com/tutorials
   ```
   Extract: Complete working samples in target language

### Quality Checks

- [ ] Base URL and API version identified
- [ ] Authentication method documented with samples
- [ ] Core endpoints documented (at least 3-5)
- [ ] Request/response formats shown
- [ ] Error codes and handling documented
- [ ] Rate limits documented
- [ ] Code samples in at least one language
- [ ] SDK/library information (if available)

## Tool/CLI Documentation Analysis Template

When analyzing a command-line tool to build a skill:

### Core Documentation

1. **Fetch README/overview**:
   ```
   https://tool-docs.example.com/
   ```
   Look for: What the tool does, installation, basic usage

2. **Fetch installation instructions**:
   ```
   https://tool-docs.example.com/installation
   https://tool-docs.example.com/getting-started
   ```
   Extract: How to install (package managers, binary, source)

3. **Fetch command reference** (comprehensive):
   ```
   https://tool-docs.example.com/commands
   https://tool-docs.example.com/cli-reference
   https://tool-docs.example.com/reference/commands
   ```
   Extract: All commands, flags, arguments, descriptions

4. **Fetch configuration documentation**:
   ```
   https://tool-docs.example.com/configuration
   https://tool-docs.example.com/config-file
   ```
   Extract: Config file format, environment variables, precedence

5. **Fetch usage samples** (multiple pages):
   ```
   https://tool-docs.example.com/samples
   https://tool-docs.example.com/tutorials
   https://tool-docs.example.com/guides
   ```
   Extract: Common workflows, typical use cases

### Quality Checks

- [ ] Installation methods documented
- [ ] All major commands listed with flags
- [ ] Configuration options documented
- [ ] At least 3 usage samples extracted
- [ ] Error messages and troubleshooting noted
- [ ] Prerequisites and dependencies listed

## Library/Package Analysis Template

When analyzing a library/package to build a skill:

### Package Information

1. **Fetch package page**:
   ```
   https://pypi.org/project/package-name/
   https://www.npmjs.com/package/package-name
   https://crates.io/crates/package-name
   ```
   Look for: Current version, installation command, description

2. **Fetch official documentation**:
   ```
   https://package-name.readthedocs.io/
   https://docs.package-name.org/
   ```
   Navigate through all major sections

3. **Fetch quickstart/tutorial**:
   ```
   https://docs.package-name.org/quickstart
   https://docs.package-name.org/tutorial
   https://docs.package-name.org/getting-started
   ```
   Extract: Minimal working example, first steps

4. **Fetch API documentation** (all classes/functions):
   ```
   https://docs.package-name.org/api
   https://docs.package-name.org/reference
   ```
   Note: May span multiple pages - fetch them all!

5. **Fetch usage guides** (all topics):
   ```
   https://docs.package-name.org/guides/topic1
   https://docs.package-name.org/guides/topic2
   https://docs.package-name.org/how-to
   ```
   Extract: Common patterns, best practices

### Quality Checks

- [ ] Installation command extracted
- [ ] Import/initialization documented
- [ ] Core classes/functions documented
- [ ] Working samples fetched (3+ scenarios)
- [ ] Configuration options noted
- [ ] Common usage patterns extracted
- [ ] Error handling patterns noted

## Specification/Standard Analysis Template

When analyzing a specification or standard to build a skill:

### Specification Gathering

1. **Fetch specification overview**:
   ```
   https://spec.example.org/
   https://spec.example.org/intro
   ```
   Look for: Purpose, scope, version, structure

2. **Fetch each section systematically**:
   ```
   https://spec.example.org/section-1
   https://spec.example.org/section-2
   https://spec.example.org/section-3
   ```
   Read through entire specification

3. **Fetch samples**:
   ```
   https://spec.example.org/samples
   https://spec.example.org/quickstart
   ```
   Extract: Valid samples, common patterns

4. **Fetch validation rules**:
   ```
   https://spec.example.org/validation
   https://spec.example.org/conformance
   ```
   Extract: Rules that implementations must follow

5. **Fetch implementation notes**:
   ```
   https://spec.example.org/implementation
   https://spec.example.org/notes
   ```
   Extract: Practical guidance for implementers

### Quality Checks

- [ ] Complete specification read
- [ ] Key concepts extracted
- [ ] Validation rules documented
- [ ] Samples collected
- [ ] Implementation guidance noted
- [ ] Edge cases identified

## Resource Collection Checklist

After gathering resources for a skill, verify:

### Coverage
- [ ] Installation/setup process clear
- [ ] Core functionality documented
- [ ] Common use cases covered (3-5 samples minimum)
- [ ] Error handling documented
- [ ] Prerequisites/dependencies listed

### Multi-Page Exploration
- [ ] Didn't stop at just the homepage
- [ ] Followed navigation links to sub-pages
- [ ] Fetched at least 5-10 distinct pages
- [ ] Explored guides/tutorials section completely
- [ ] Fetched reference/API documentation thoroughly

### Quality
- [ ] Instructions are concrete and actionable
- [ ] Code samples are complete and runnable
- [ ] Configuration options are explained
- [ ] Troubleshooting guidance available
- [ ] Version/compatibility noted

### Synthesis Readiness
- [ ] Enough info to write SKILL.md without guessing
- [ ] Can write concrete samples from gathered info
- [ ] Can create troubleshooting section
- [ ] Can list prerequisites accurately
- [ ] Can explain when to use the skill

## Common Resource Gathering Mistakes

### ❌ Stopping Too Early

**Mistake**: Fetching only the homepage
```
✗ Fetch https://docs.example.com/ only
✗ Read README only
✗ Check homepage and stop
```

**Fix**: Follow navigation systematically
```
✓ Fetch homepage
✓ Identify navigation sections
✓ Fetch each section's pages
✓ Continue until comprehensive
```

### ❌ Missing Critical Pages

**Mistake**: Skipping important sections
```
✗ Skip installation docs (assume obvious)
✗ Skip error handling docs (will figure out)
✗ Skip samples (can make them up)
```

**Fix**: Be exhaustive
```
✓ Fetch installation (all methods)
✓ Fetch error docs (all codes)
✓ Fetch samples (all scenarios)
```

### ❌ Shallow Navigation

**Mistake**: Not exploring links
```
✗ See "Guides" section → don't click
✗ See "API Reference" → assume simple
✗ See "Samples" → skip it
```

**Fix**: Click through systematically
```
✓ Guides → Fetch all guide pages
✓ API Reference → Fetch all endpoint docs
✓ Samples → Collect all samples
```

### ❌ Incomplete API Coverage

**Mistake**: Documenting only one endpoint
```
✗ Focus on /users endpoint only
✗ Ignore other resources
✗ Miss authentication variations
```

**Fix**: Cover all major operations
```
✓ Document all CRUD operations
✓ Cover all major resources
✓ Include auth variations
```

## Quick Reference: fetch_webpage Flow

For documentation sites with good navigation:

```
1. fetch_webpage(homepage)
   ↓
2. Identify navigation structure
   ↓
3. For each major section:
   fetch_webpage(section_index)
   ↓
4. For each sub-page in section:
   fetch_webpage(sub_page)
   ↓
5. Continue until comprehensive
   ↓
6. Verify coverage against checklist
```

## Sample: Complete Resource Gathering

**Task**: Build skill for "SampleAPI" service

**Execution**:
```
1. fetch_webpage("https://docs.exampleapi.com/")
   → Found sections: Intro, Auth, Endpoints, Errors, Samples

2. fetch_webpage("https://docs.exampleapi.com/introduction")
   → Extracted: Base URL, version, overview

3. fetch_webpage("https://docs.exampleapi.com/authentication")
   → Found sub-pages: API Keys, OAuth, JWT
   
4. fetch_webpage("https://docs.exampleapi.com/authentication/api-keys")
   → Extracted: How to get key, where to add it in requests

5. fetch_webpage("https://docs.exampleapi.com/authentication/oauth")
   → Extracted: OAuth flow, redirect URLs, token refresh

6. fetch_webpage("https://docs.exampleapi.com/endpoints")
   → Found: /users, /projects, /data endpoints

7. fetch_webpage("https://docs.exampleapi.com/endpoints/users")
   → Extracted: GET /users, POST /users, PUT /users/:id, DELETE /users/:id

8. fetch_webpage("https://docs.exampleapi.com/endpoints/projects")
   → Extracted: Project CRUD operations

9. fetch_webpage("https://docs.exampleapi.com/errors")
   → Extracted: Error codes 400, 401, 403, 404, 429, 500

10. fetch_webpage("https://docs.exampleapi.com/samples")
   → Found samples: Basic auth, Create user, List projects

11. Verify coverage:
    ✓ Auth methods: 3 pages fetched
    ✓ Endpoints: 2 resources documented
    ✓ Errors: All codes documented
   ✓ Samples: 3+ scenarios collected
    
12. Proceed to writing SKILL.md with comprehensive understanding
```

**Key**: Fetched 10+ pages, not just 1-2. This ensures the skill has solid foundation.

## Resources

- Use `fetch_webpage` tool to retrieve documentation pages
- Follow links systematically - don't stop at homepage
- Verify coverage with checklists above
- When in doubt, fetch more pages rather than fewer
