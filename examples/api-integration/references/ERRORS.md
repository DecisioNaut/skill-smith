# API Error Reference

Complete reference for handling API errors and troubleshooting common issues.

## Error Response Format

Standard error response structure:

```json
{
  "status": "error",
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message",
    "field": "field_name",
    "details": {}
  }
}
```

## HTTP Status Codes and Meanings

### 400 Bad Request

**Meaning:** The request is malformed or contains invalid parameters.

**Common Causes:**
- Invalid JSON syntax
- Missing required parameters
- Invalid parameter values
- Incorrectly formatted data

**Example Response:**
```json
{
  "status": "error",
  "error": {
    "code": "INVALID_JSON",
    "message": "Request body contains invalid JSON",
    "details": {
      "line": 2,
      "column": 15,
      "syntax_error": "Unexpected token }"
    }
  }
}
```

**How to Fix:**
1. Validate JSON syntax using a linter
2. Check all required fields are present
3. Verify parameter types match expectations
4. Review API documentation for correct format

### 401 Unauthorized

**Meaning:** Authentication credentials are missing or invalid.

**Common Causes:**
- Missing Authorization header
- Expired API key or token
- Invalid API key format
- Typos in credentials

**Example Response:**
```json
{
  "status": "error",
  "error": {
    "code": "INVALID_AUTH",
    "message": "Authentication failed. Invalid or missing API key.",
    "details": {
      "header": "Authorization",
      "expected_format": "Bearer YOUR_API_KEY"
    }
  }
}
```

**How to Fix:**
1. Verify API key is correct (check for typos, trailing spaces)
2. Ensure Authorization header is present
3. Check header format: `Authorization: Bearer YOUR_KEY`
4. Generate new API key if expired
5. Verify key has proper permissions

### 403 Forbidden

**Meaning:** Authentication succeeded but you don't have permission for this resource.

**Common Causes:**
- Insufficient permissions
- Resource belongs to different user
- Account/API key lacks required scope
- Account suspended or limited

**Example Response:**
```json
{
  "status": "error",
  "error": {
    "code": "INSUFFICIENT_PERMISSIONS",
    "message": "Your API key does not have permission to access this resource",
    "details": {
      "required_permission": "users:write",
      "your_permissions": ["users:read"]
    }
  }
}
```

**How to Fix:**
1. Check API key has required scopes/permissions
2. Verify you own the resource you're trying to access
3. Contact support to upgrade permissions
4. Use different API key with proper access

### 404 Not Found

**Meaning:** The requested resource doesn't exist.

**Common Causes:**
- Incorrect resource ID
- Resource has been deleted
- Typo in endpoint URL
- Resource not yet created

**Example Response:**
```json
{
  "status": "error",
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "User with ID 12345 not found",
    "details": {
      "resource_type": "user",
      "resource_id": 12345
    }
  }
}
```

**How to Fix:**
1. Verify resource ID is correct
2. Check resource wasn't deleted
3. Verify endpoint URL spelling
4. Try listing resources to find correct ID

### 409 Conflict

**Meaning:** Request conflicts with current state (often duplicate creation).

**Common Causes:**
- Duplicate resource (unique constraint violation)
- Resource in wrong state for operation
- Concurrent modification conflict

**Example Response:**
```json
{
  "status": "error",
  "error": {
    "code": "DUPLICATE_EMAIL",
    "message": "A user with email alice@example.com already exists",
    "details": {
      "field": "email",
      "value": "alice@example.com",
      "existing_id": 789
    }
  }
}
```

**How to Fix:**
1. Check if resource already exists (GET before POST)
2. Use unique identifiers
3. Implement idempotency keys for retries
4. Update existing resource instead of creating

### 422 Unprocessable Entity

**Meaning:** Request is well-formed but contains semantic errors (validation failures).

**Common Causes:**
- Field value doesn't meet validation rules
- Business logic constraints violated
- Invalid data format
- Missing dependent fields

**Example Response:**
```json
{
  "status": "error",
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Request validation failed",
    "errors": [
      {
        "field": "email",
        "message": "Email address is invalid",
        "value": "not-an-email"
      },
      {
        "field": "age",
        "message": "Age must be between 0 and 150",
        "value": -5
      }
    ]
  }
}
```

**How to Fix:**
1. Read validation error messages carefully
2. Check field formats match requirements
3. Verify all business rules are satisfied
4. Review API documentation for field constraints

### 429 Too Many Requests

**Meaning:** You've exceeded the rate limit.

**Common Causes:**
- Making requests too quickly
- Exceeding daily/hourly quota
- Parallel requests exceeding limit
- Shared rate limit across team

**Example Response:**
```json
{
  "status": "error",
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Rate limit exceeded. Try again in 3600 seconds.",
    "details": {
      "limit": 1000,
      "remaining": 0,
      "reset_at": "2026-02-13T17:00:00Z"
    }
  }
}
```

**Response Headers:**
```
HTTP/1.1 429 Too Many Requests
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1643896800
Retry-After: 3600
```

**How to Fix:**
1. Check Retry-After header and wait that long
2. Implement exponential backoff
3. Reduce request frequency
4. Cache responses when possible
5. Use batch endpoints if available
6. Contact support to increase limits

**Implementation:**
```python
import time
import requests

def handle_rate_limit(response):
    if response.status_code == 429:
        retry_after = int(response.headers.get('Retry-After', 60))
        print(f"Rate limited. Waiting {retry_after} seconds...")
        time.sleep(retry_after)
        return True
    return False

# Usage
while True:
    response = requests.get(url)
    if handle_rate_limit(response):
        continue  # Retry after waiting
    break
```

### 500 Internal Server Error

**Meaning:** Unexpected error on the server.

**Common Causes:**
- Server bug or exception
- Database connection failure
- External service timeout
- Configuration error

**Example Response:**
```json
{
  "status": "error",
  "error": {
    "code": "INTERNAL_ERROR",
    "message": "An unexpected error occurred. Please try again.",
    "request_id": "req_abc123xyz"
  }
}
```

**How to Fix:**
1. Retry the request (might be transient)
2. Check API status page
3. Contact support with request_id
4. Try alternative endpoint if available

### 503 Service Unavailable

**Meaning:** Service is temporarily unavailable (maintenance, overload).

**Common Causes:**
- Scheduled maintenance
- Server overload
- Deployment in progress
- Infrastructure issues

**Example Response:**
```json
{
  "status": "error",
  "error": {
    "code": "SERVICE_UNAVAILABLE",
    "message": "Service temporarily unavailable. Please try again later.",
    "retry_after": 300
  }
}
```

**How to Fix:**
1. Wait and retry with exponential backoff
2. Check Retry-After header
3. Check API status page or Twitter
4. Implement circuit breaker pattern

## Common Error Codes

### Authentication Errors

| Code | Meaning | Solution |
|------|---------|----------|
| `INVALID_API_KEY` | API key is invalid | Check key, generate new one |
| `EXPIRED_TOKEN` | Access token expired | Refresh token |
| `MISSING_AUTH` | No authentication provided | Add Authorization header |
| `INVALID_SIGNATURE` | Request signature invalid | Verify signing algorithm |

### Validation Errors

| Code | Meaning | Solution |
|------|---------|----------|
| `REQUIRED_FIELD` | Required field missing | Add missing field |
| `INVALID_FORMAT` | Field format invalid | Check format requirements |
| `OUT_OF_RANGE` | Value outside allowed range | Use valid range |
| `INVALID_TYPE` | Wrong data type | Convert to correct type |

### Resource Errors

| Code | Meaning | Solution |
|------|---------|----------|
| `NOT_FOUND` | Resource doesn't exist | Verify ID, check if deleted |
| `ALREADY_EXISTS` | Duplicate resource | Use existing or update |
| `DELETED` | Resource was deleted | Cannot be recovered |

### Rate Limit Errors

| Code | Meaning | Solution |
|------|---------|----------|
| `RATE_LIMIT_EXCEEDED` | Too many requests | Wait and retry |
| `QUOTA_EXCEEDED` | Daily/monthly quota exceeded | Wait for reset or upgrade |

## Retry Strategies

### Exponential Backoff

```python
import time
import requests

def exponential_backoff(func, max_retries=5):
    \"\"\"Retry with exponential backoff.\"\"\"
    for attempt in range(max_retries):
        try:
            response = func()
            
            if response.status_code < 500:
                return response
            
            # Server error - retry with backoff
            wait_time = 2 ** attempt  # 1s, 2s, 4s, 8s, 16s
            print(f\"Server error. Retry {attempt+1}/{max_retries} in {wait_time}s\")
            time.sleep(wait_time)
        
        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                raise
            wait_time = 2 ** attempt
            time.sleep(wait_time)
    
    raise Exception(f\"Failed after {max_retries} retries\")

# Usage
response = exponential_backoff(lambda: requests.get(url))
```

### Conditional Retry

```python
def should_retry(status_code):
    \"\"\"Determine if request should be retried.\"\"\"
    # Retry on server errors and rate limits
    return status_code in [429, 500, 502, 503, 504]

def make_request_with_retry(url, max_retries=3):
    for attempt in range(max_retries):
        response = requests.get(url)
        
        if not should_retry(response.status_code):
            return response
        
        if response.status_code == 429:
            # Honor Retry-After for rate limits
            retry_after = int(response.headers.get('Retry-After', 60))
            time.sleep(retry_after)
        else:
            # Exponential backoff for server errors
            time.sleep(2 ** attempt)
    
    return response
```

## Debugging Tips

### 1. Check Request Format

**Verify headers:**
```bash
curl -v https://api.example.com/users
```

Look for:
- Correct Content-Type
- Authorization header present
- Custom headers if required

### 2. Validate JSON

```python
import json

try:
    data = json.loads(response_text)
except json.JSONDecodeError as e:
    print(f\"Invalid JSON at line {e.lineno}, column {e.colno}\")
```

### 3. Log Full Request/Response

```python
import requests
import logging

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

response = requests.get(url)
print(f\"Status: {response.status_code}\")
print(f\"Headers: {response.headers}\")
print(f\"Body: {response.text}\")
```

### 4. Use Request ID

Most APIs return a request ID for tracking:

```json
{
  \"error\": {
    \"request_id\": \"req_abc123xyz\"
  }
}
```

Include this when contacting support.

### 5. Test in Isolation

```bash
# Minimal test case
curl -X GET \"https://api.example.com/users/123\" \\\n  -H \"Authorization: Bearer YOUR_KEY\"\n```

Remove all optional parameters to isolate the issue.

## Prevention Best Practices

1. **Validate before sending**: Check data locally first\n2. **Handle all status codes**: Don't assume success\n3. **Implement retries**: For transient failures\n4. **Log requests**: Track what was sent\n5. **Use timeouts**: Prevent hanging\n6. **Monitor rate limits**: Track usage\n7. **Cache responses**: Reduce unnecessary calls\n8. **Test error scenarios**: Don't just test happy path

## Common Pitfalls

### Pitfall 1: Ignoring Error Messages

❌ **Bad:**\n```python\ntry:\n    response = requests.get(url)\nexcept:\n    print(\"Failed\")\n```

✅ **Good:**\n```python\ntry:\n    response = requests.get(url)\n    response.raise_for_status()\nexcept requests.exceptions.HTTPError as e:\n    error_data = e.response.json()\n    print(f\"Error {e.response.status_code}: {error_data['error']['message']}\")\n```

### Pitfall 2: Not Respecting Rate Limits

❌ **Bad:**\n```python\nfor item in items:\n    requests.post(url, json=item)  # Rapid fire\n```

✅ **Good:**\n```python\nimport time\n\nfor item in items:\n    response = requests.post(url, json=item)\n    if response.status_code == 429:\n        time.sleep(60)\n        response = requests.post(url, json=item)\n    time.sleep(0.1)  # Be nice to the API\n```

### Pitfall 3: Hardcoded Credentials

❌ **Bad:**\n```python\nAPI_KEY = \"sk-abc123xyz\"\n```

✅ **Good:**\n```python\nimport os\nAPI_KEY = os.environ.get('API_KEY')\nif not API_KEY:\n    raise ValueError(\"API_KEY environment variable not set\")\n```

## Quick Reference

| Status | Retry? | Action |\n|--------|--------|--------|\n| 400 | No | Fix request |\n| 401 | No | Fix credentials |\n| 403 | No | Check permissions |\n| 404 | No | Verify resource exists |\n| 409 | No | Handle conflict |\n| 422 | No | Fix validation errors |\n| 429 | Yes | Wait and retry (honor Retry-After) |\n| 500 | Yes | Retry with backoff |\n| 502 | Yes | Retry with backoff |\n| 503 | Yes | Retry with backoff |\n| 504 | Yes | Retry with backoff |\n\n---\n\n**When in doubt:** Read the error message carefully, check API documentation, and look for a request_id to reference when asking for help.
