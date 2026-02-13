---
name: code-review
description: Reviews code for bugs, security vulnerabilities, style violations, and adherence to best practices. Use when reviewing pull requests, performing code audits, or when the user mentions code review, code quality, linting, or security scanning.
---

# Code Review Skill

This skill helps you perform thorough code reviews by checking for common issues, security vulnerabilities, style problems, and best practices.

## When to Use This Skill

Use this skill when:
- Reviewing pull requests or code changes
- Performing security audits on code
- Checking code quality before deployment
- Teaching best practices to developers
- User mentions code review, audit, or quality checks

## Code Review Checklist

### 1. Security Review

Check for common security issues:

**Authentication & Authorization:**
- [ ] Are credentials stored securely (not hardcoded)?
- [ ] Is user input validated and sanitized?
- [ ] Are authentication tokens handled properly?
- [ ] Is access control enforced at all levels?

**Data Protection:**
- [ ] Is sensitive data encrypted in transit (HTTPS)?
- [ ] Is sensitive data encrypted at rest?
- [ ] Are database queries parameterized (no SQL injection)?
- [ ] Is PII (personally identifiable information) handled properly?

**Common Vulnerabilities:**
- [ ] No hardcoded secrets or API keys
- [ ] No obvious injection vulnerabilities (SQL, command, XSS)
- [ ] Proper error handling (don't leak sensitive info in errors)
- [ ] Dependencies are up to date (no known CVEs)

### 2. Bug Detection

Look for common bug patterns:

**Null/Undefined Handling:**
```python
# ❌ Bad: No null check
user = get_user(id)
print(user.name)  # Crashes if user is None

# ✅ Good: Proper null handling
user = get_user(id)
if user:
    print(user.name)
else:
    print("User not found")
```

**Error Handling:**
```python
# ❌ Bad: Silent failure
try:
    result = risky_operation()
except:
    pass  # Error swallowed

# ✅ Good: Explicit error handling
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    raise
```

**Resource Management:**
```python
# ❌ Bad: Resource leak
f = open('file.txt')
data = f.read()
# File never closed

# ✅ Good: Proper cleanup
with open('file.txt') as f:
    data = f.read()
# File automatically closed
```

### 3. Code Style & Readability

**Naming Conventions:**
- Functions: `snake_case` or `camelCase` (consistent with language)
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Variables: descriptive and meaningful

**Code Structure:**
- Functions are focused (single responsibility)
- No overly long functions (>50 lines should be rare)
- Proper indentation and formatting
- Comments explain "why", not "what"
- No commented-out code in production

**Complexity:**
- Cyclomatic complexity is reasonable
- Nested loops/conditions don't exceed 3-4 levels
- Code is DRY (Don't Repeat Yourself)

### 4. Performance Considerations

**Algorithms:**
- Appropriate algorithm choice (O(n) vs O(n²))
- No N+1 query problems (iterating with DB calls in loop)
- Proper indexing on database queries
- Caching used where appropriate

**Resource Usage:**
- Large files read in chunks, not all at once
- Database connections properly pooled
- Memory leaks avoided (proper cleanup)

### 5. Testing Quality

**Test Coverage:**
- New functionality has associated tests
- Edge cases are tested
- Error paths are tested
- Integration/unit tests are appropriate

**Test Quality:**
```python
# ❌ Bad: Vague test
def test_function():
    result = my_function()
    assert result  # What does this test?

# ✅ Good: Clear test
def test_user_creation_with_valid_email():
    user = create_user("test@example.com")
    assert user.email == "test@example.com"
    assert user.is_active == True
```

## Review Process

### Step 1: Initial Scan

1. Read the change description/commit message
2. Understand the purpose of the changes
3. Verify changes align with stated purpose
4. Note any files that seem out of scope

### Step 2: Detailed Review

For each modified file:

1. **Security:** Check the security checklist above
2. **Logic:** Understand the code flow and verify correctness
3. **Edge Cases:** Think about what could go wrong
4. **Style:** Check formatting and naming conventions
5. **Tests:** Verify adequate test coverage

### Step 3: Provide Feedback

**Format feedback clearly:**

```markdown
## Critical Issues (Must Fix Before Merge)
- [File:Line] Security: Hardcoded API key
- [File:Line] Bug: Null pointer when user is not found

## Suggestions (Should Fix)
- [File:Line] Style: Function name should be `calculate_total` not `calc_tot`
- [File:Line] Performance: This loops N times with DB query inside

## Nitpicks (Optional)
- [File:Line] Comment typo: "recieve" -> "receive"
- [File:Line] Could use list comprehension for clarity
```

## Language-Specific Checklists

### Python

**Common Issues:**
- Mutable default arguments: `def func(items=[]):`  ❌
- Catching bare `except:` without specifying exception type
- Not using context managers for file/resource handling
- Inefficient string concatenation in loops
- Using `==` for None instead of `is None`

**Best Practices:**
- Follow PEP 8 style guide
- Use type hints for function signatures
- Docstrings for public functions/classes
- Virtual environments for dependencies

### JavaScript/TypeScript

**Common Issues:**
- Using `var` instead of `let`/`const`
- Not handling Promise rejections
- Callback hell (deeply nested callbacks)
- Comparing with `==` instead of `===`
- Not validating user input

**Best Practices:**
- Use ESLint/TSLint
- Async/await for cleaner Promise handling
- Proper TypeScript types (no excessive `any`)
- Error boundaries in React components

### Java

**Common Issues:**
- Not closing resources (files, connections)
- Catching generic `Exception` instead of specific types
- Using raw types instead of generics
- Comparing strings with `==` instead of `.equals()`
- Not handling `null` properly

**Best Practices:**
- Try-with-resources for auto-cleanup
- Follow Java Code Conventions
- Use Optional for nullable values
- Proper exception handling hierarchy

## Examples

### Example 1: Security Issue

**Problem Code:**
```python
def authenticate_user(username, password):
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    result = db.execute(query)
    return result is not None
```

**Issues:**
- SQL injection vulnerability
- Passwords stored/compared in plaintext
- No password hashing

**Review Comment:**
```markdown
## Critical Security Issues

**Line 2: SQL Injection Vulnerability**
This query is vulnerable to SQL injection. An attacker could input:
username = "admin' --" to bypass authentication.

**Line 2: Plaintext Password Comparison**
Passwords should never be stored or compared in plaintext.

**Recommended Fix:**
```python
def authenticate_user(username, password):
    # Use parameterized query
    query = "SELECT password_hash FROM users WHERE username=?"
    result = db.execute(query, (username,))
    
    if result:
        # Verify hashed password
        return bcrypt.checkpw(password.encode(), result['password_hash'])
    return False
```
```

### Example 2: Bug Detection

**Problem Code:**
```javascript
function processUsers(users) {
    let results = [];
    for (let i = 0; i <= users.length; i++) {
        results.push(users[i].name);
    }
    return results;
}
```

**Issues:**
- Off-by-one error (`i <= users.length` should be `i < users.length`)
- Will crash on last iteration (undefined.name)
- No null checks

**Review Comment:**
```markdown
## Bug: Off-by-One Error

**Line 3:** Loop condition `i <= users.length` will cause array out of bounds.
Arrays are 0-indexed, so valid indices are 0 to length-1.

**Recommended Fix:**
```javascript
function processUsers(users) {
    if (!users || users.length === 0) {
        return [];
    }
    
    return users
        .filter(user => user && user.name)  // null safety
        .map(user => user.name);
}
```
```

### Example 3: Style Improvement

**Original Code:**
```python
def f(x, y, z):
    if x > 0:
        if y > 0:
            if z > 0:
                return x + y + z
            else:
                return 0
        else:
            return 0
    else:
        return 0
```

**Review Comment:**
```markdown
## Suggestion: Improve Readability

**Function `f`:** Name is not descriptive, and logic can be simplified.

**Recommended Refactoring:**
```python
def sum_positive_numbers(a, b, c):
    """
    Returns the sum of three numbers if all are positive, otherwise 0.
    
    Args:
        a, b, c: Numbers to sum
    
    Returns:
        Sum if all positive, otherwise 0
    """
    if a > 0 and b > 0 and c > 0:
        return a + b + c
    return 0
```

Benefits:
- Descriptive function name
- Clear docstring
- Simplified logic (early return)
- Descriptive parameter names
```
```

## Troubleshooting

**Issue:** Too many minor issues to report

**Solution:** Focus on critical issues first. Group similar style issues together rather than commenting on every instance.

---

**Issue:** Unsure if something is a real problem

**Solution:** If it could potentially cause issues, flag it as a suggestion and explain your concern. Let the author decide if it's applicable.

---

**Issue:** Code uses unfamiliar patterns or libraries

**Solution:** Research the pattern/library first. If it's a legitimate best practice, learn from it. If it seems problematic, ask for clarification.

## Review Etiquette

1. **Be constructive**: Suggest improvements, don't just criticize
2. **Explain why**: Help the author understand the reasoning
3. **Acknowledge good code**: Point out clever solutions or good practices
4. **Ask questions**: If something is unclear, ask rather than assume
5. **Prioritize**: Separate critical issues from nice-to-haves
6. **Be respectful**: Remember there's a human behind the code

## Quick Reference

| Severity | When to Use | Example |
|----------|-------------|---------|
| Critical | Security issues, data loss bugs, crashes | SQL injection, null pointer dereference |
| Major | Functionality bugs, performance issues | Wrong calculation, N+1 queries |
| Minor | Style issues, code clarity | Missing docstring, verbose code |
| Nitpick | Typos, formatting | Comment typo, extra whitespace |

---

**Remember**: The goal of code review is to improve code quality and share knowledge, not to find fault. Be thorough but also supportive.
