---
name: api-integration
description: Integrates with REST APIs including authentication, request handling, response parsing, and error management. Use when connecting to web services, APIs, webhooks, or when the user mentions REST, HTTP requests, API calls, or web service integration.
---

# API Integration Skill

This skill helps you integrate with REST APIs by handling authentication, making requests, parsing responses, and managing errors gracefully.

## When to Use This Skill

Use this skill when:
- Connecting to REST APIs or web services
- Building integrations with third-party services
- Fetching or sending data via HTTP/HTTPS
- User mentions API, REST, HTTP requests, webhooks, or web services

## Prerequisites

- HTTP client library (curl, requests, fetch, axios, etc.)
- API credentials if required (API key, OAuth token, etc.)
- API documentation URL
- Network connectivity

## Core Concepts

**REST API**: Representational State Transfer API that uses HTTP methods (GET, POST, PUT, DELETE) to interact with resources

**Endpoint**: A specific URL path that provides access to a resource (e.g., `/users`, `/posts/123`)

**Authentication**: Process of verifying identity (API keys, OAuth, JWT)

**Status Codes**: HTTP response codes indicating success (2xx), client errors (4xx), or server errors (5xx)

## Step-by-Step Integration Process

### Step 1: Understand the API

Before writing any code:

1. **Review API documentation** (endpoints, authentication, rate limits)
2. **Identify required endpoints** for your use case
3. **Note authentication method** (API key, OAuth, Basic Auth, etc.)
4. **Check rate limits** and usage constraints
5. **Find code examples** in the documentation

### Step 2: Set Up Authentication

Choose the appropriate authentication method:

**API Key (Header):**
```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
     https://api.example.com/resource
```

**API Key (Query Parameter):**
```bash
curl "https://api.example.com/resource?api_key=YOUR_API_KEY"
```

**Basic Authentication:**
```bash
curl -u username:password \
     https://api.example.com/resource
```

**OAuth 2.0 (with token):**
```bash
# First, obtain token
curl -X POST https://auth.example.com/oauth/token \
     -d "client_id=YOUR_ID" \
     -d "client_secret=YOUR_SECRET" \
     -d "grant_type=client_credentials"

# Then use token
curl -H "Authorization: Bearer ACCESS_TOKEN" \
     https://api.example.com/resource
```

**Best Practice:** Store credentials in environment variables, never hardcode them.

```bash
export API_KEY="your-key-here"
curl -H "Authorization: Bearer $API_KEY" https://api.example.com/resource
```

### Step 3: Make API Requests

**GET Request (Fetch Data):**
```bash
# Simple GET
curl https://api.example.com/users

# GET with query parameters
curl "https://api.example.com/users?page=2&limit=10"

# GET with authentication
curl -H "Authorization: Bearer $API_KEY" \
     https://api.example.com/users
```

**POST Request (Create Data):**
```bash
# POST with JSON body
curl -X POST https://api.example.com/users \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer $API_KEY" \
     -d '{"name":"Alice","email":"alice@example.com"}'
```

**PUT Request (Update Data):**
```bash
# PUT to update resource
curl -X PUT https://api.example.com/users/123 \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer $API_KEY" \
     -d '{"name":"Alice Smith","email":"alice@example.com"}'
```

**DELETE Request (Delete Data):**
```bash
# DELETE resource
curl -X DELETE https://api.example.com/users/123 \
     -H "Authorization: Bearer $API_KEY"
```

### Step 4: Parse Responses

**Check Status Code:**
```bash
# Save status code
STATUS=$(curl -s -o response.json -w "%{http_code}" https://api.example.com/users)

if [ "$STATUS" -eq 200 ]; then
    echo "Success!"
    cat response.json
else
    echo "Error: HTTP $STATUS"
fi
```

**Parse JSON Response:**
```bash
# Using jq
curl https://api.example.com/users | jq '.data[] | {id: .id, name: .name}'

# Extract specific field
USER_NAME=$(curl https://api.example.com/users/123 | jq -r '.name')
echo "User name: $USER_NAME"
```

**Python Example:**
```python
import requests

response = requests.get('https://api.example.com/users')
response.raise_for_status()  # Raises exception for 4xx/5xx

data = response.json()
for user in data['users']:
    print(f"{user['id']}: {user['name']}")
```

### Step 5: Handle Errors

**Common HTTP Status Codes:**
- **200 OK**: Success
- **201 Created**: Resource created successfully
- **400 Bad Request**: Invalid request data
- **401 Unauthorized**: Missing or invalid authentication
- **403 Forbidden**: Authenticated but not authorized
- **404 Not Found**: Resource doesn't exist
- **429 Too Many Requests**: Rate limit exceeded
- **500 Internal Server Error**: Server-side error
- **503 Service Unavailable**: Service temporarily down

**Error Handling Pattern:**
```python
import requests
import time

def make_request_with_retry(url, max_retries=3):
    """Make API request with retry logic for transient errors."""
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            
            # Handle different status codes
            if response.status_code == 200:
                return response.json()
            
            elif response.status_code == 401:
                raise ValueError("Authentication failed. Check API key.")
            
            elif response.status_code == 404:
                raise ValueError(f"Resource not found: {url}")
            
            elif response.status_code == 429:
                # Rate limited - wait and retry
                retry_after = int(response.headers.get('Retry-After', 60))
                print(f"Rate limited. Waiting {retry_after} seconds...")
                time.sleep(retry_after)
                continue
            
            elif response.status_code >= 500:
                # Server error - retry with exponential backoff
                wait_time = 2 ** attempt
                print(f"Server error. Retrying in {wait_time}s...")
                time.sleep(wait_time)
                continue
            
            else:
                raise ValueError(f"Unexpected status: {response.status_code}")
        
        except requests.exceptions.Timeout:
            print(f"Request timeout. Retry {attempt + 1}/{max_retries}")
            if attempt == max_retries - 1:
                raise
        
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            raise
    
    raise ValueError(f"Failed after {max_retries} retries")
```

### Step 6: Handle Pagination

Many APIs paginate results. Common patterns:

**Offset-Based Pagination:**
```bash
# Page 1
curl "https://api.example.com/users?offset=0&limit=10"

# Page 2
curl "https://api.example.com/users?offset=10&limit=10"
```

**Cursor-Based Pagination:**
```bash
# First page
curl "https://api.example.com/users?limit=10"
# Response includes: {"data": [...], "next_cursor": "abc123"}

# Next page using cursor
curl "https://api.example.com/users?limit=10&cursor=abc123"
```

**Page-Based Pagination:**
```bash
# Page 1
curl "https://api.example.com/users?page=1&per_page=10"

# Page 2
curl "https://api.example.com/users?page=2&per_page=10"
```

**Fetching All Pages (Python):**
```python
def fetch_all_pages(base_url):
    """Fetch all pages from a paginated API."""
    all_data = []
    page = 1
    
    while True:
        response = requests.get(f"{base_url}?page={page}&per_page=100")
        response.raise_for_status()
        
        data = response.json()
        all_data.extend(data['items'])
        
        # Check if there are more pages
        if not data.get('has_more', False):
            break
        
        page += 1
    
    return all_data
```

### Step 7: Respect Rate Limits

**Check rate limit headers:**
```python
response = requests.get(url)

remaining = response.headers.get('X-RateLimit-Remaining')
reset_time = response.headers.get('X-RateLimit-Reset')

print(f"Requests remaining: {remaining}")
print(f"Rate limit resets at: {reset_time}")
```

**Implement rate limiting:**
```python
import time

class RateLimiter:
    def __init__(self, calls_per_second):
        self.calls_per_second = calls_per_second
        self.last_call = 0
    
    def wait_if_needed(self):
        """Wait if necessary to respect rate limit."""
        current_time = time.time()
        time_since_last = current_time - self.last_call
        min_interval = 1.0 / self.calls_per_second
        
        if time_since_last < min_interval:
            time.sleep(min_interval - time_since_last)
        
        self.last_call = time.time()

# Usage
limiter = RateLimiter(calls_per_second=2)  # Max 2 calls per second

for url in urls:
    limiter.wait_if_needed()
    response = requests.get(url)
```

## Examples

### Example 1: Fetch User Data

**Task:** Get information about a user

**Request:**
```bash
curl -H "Authorization: Bearer sk-test-abc123" \
     https://api.example.com/v1/users/12345
```

**Response:**
```json
{
  "id": 12345,
  "name": "Alice Smith",
  "email": "alice@example.com",
  "created_at": "2026-01-15T10:30:00Z",
  "active": true
}
```

**Parsing:**
```bash
# Extract just the name
curl -H "Authorization: Bearer sk-test-abc123" \
     https://api.example.com/v1/users/12345 | jq -r '.name'
# Output: Alice Smith
```

### Example 2: Create a New Resource

**Task:** Create a new user

**Request:**
```python
import requests

url = "https://api.example.com/v1/users"
headers = {
    "Authorization": "Bearer sk-test-abc123",
    "Content-Type": "application/json"
}
data = {
    "name": "Bob Jones",
    "email": "bob@example.com",
    "role": "user"
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
    user = response.json()
    print(f"Created user with ID: {user['id']}")
else:
    print(f"Error: {response.status_code} - {response.text}")
```

**Expected Response:**
```json
{
  "id": 12346,
  "name": "Bob Jones",
  "email": "bob@example.com",
  "role": "user",
  "created_at": "2026-02-13T14:22:00Z"
}
```

### Example 3: Handle Pagination

**Task:** Fetch all users (paginated)

```python
import requests

def fetch_all_users(api_key):
    """Fetch all users handling pagination."""
    base_url = "https://api.example.com/v1/users"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    all_users = []
    page = 1
    
    while True:
        response = requests.get(
            base_url,
            headers=headers,
            params={"page": page, "per_page": 100}
        )
        response.raise_for_status()
        
        data = response.json()
        users = data.get('users', [])
        all_users.extend(users)
        
        # Check if there are more pages
        total_pages = data.get('total_pages', 1)
        if page >= total_pages:
            break
        
        page += 1
    
    return all_users

# Usage
users = fetch_all_users("sk-test-abc123")
print(f"Fetched {len(users)} users")
```

## Troubleshooting

**Error: 401 Unauthorized**
- **Cause**: Invalid or missing API key
- **Solution**: 
  1. Verify API key is correct
  2. Check for trailing spaces or newlines
  3. Ensure key is in correct header/parameter
  4. Verify key hasn't expired

**Error: 429 Too Many Requests**
- **Cause**: Exceeded rate limit
- **Solution**:
  1. Check `Retry-After` header for wait time
  2. Implement exponential backoff
  3. Reduce request frequency
  4. Consider caching responses

**Error: Connection Timeout**
- **Cause**: Network issues or slow API
- **Solution**:
  1. Check internet connection
  2. Increase timeout value
  3. Check API status page
  4. Try alternative endpoint if available

**Error: SSL Certificate Verification Failed**
- **Cause**: SSL/TLS certificate issues
- **Solution**:
  1. Update CA certificates: `pip install --upgrade certifi`
  2. Check system time is correct
  3. Only as last resort: disable verification (not recommended for production)

## Best Practices

1. **Store credentials securely**: Use environment variables or secret managers
2. **Validate responses**: Always check status codes before parsing
3. **Handle errors gracefully**: Implement retry logic with exponential backoff
4. **Respect rate limits**: Monitor and throttle your requests
5. **Log API calls**: Track requests for debugging and monitoring
6. **Use timeouts**: Prevent hanging on slow responses
7. **Parse carefully**: Validate JSON structure before accessing fields
8. **Cache when possible**: Reduce unnecessary API calls
9. **Use appropriate HTTP methods**: GET for reading, POST for creating, etc.
10. **Version your API usage**: Use versioned endpoints (e.g., `/v1/`) when available

## Additional Resources

For detailed API reference information, see:
- [API Reference Documentation](references/API_REFERENCE.md) - Complete endpoint documentation
- [Authentication Guide](references/AUTH.md) - Detailed authentication methods
- [Error Codes](references/ERRORS.md) - Complete error code reference

---

**Need help?** If you encounter issues not covered here, check the API's documentation or status page.
