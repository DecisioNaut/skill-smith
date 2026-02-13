# API Reference

This document provides detailed technical reference for common REST API patterns and endpoints.

## Standard HTTP Methods

### GET

**Purpose:** Retrieve resources

**Characteristics:**
- Safe (no side effects)
- Idempotent (multiple identical requests have same effect)
- Cacheable
- Should not include request body

**Examples:**
```
GET /users              - List all users
GET /users/123          - Get specific user
GET /users?role=admin   - Filter users by role
```

### POST

**Purpose:** Create new resources

**Characteristics:**
- Not safe (has side effects)
- Not idempotent (multiple requests create multiple resources)
- Response may be cached with explicit headers

**Examples:**
```
POST /users             - Create new user
POST /users/123/posts   - Create post for user 123
```

### PUT

**Purpose:** Update/replace existing resource

**Characteristics:**
- Not safe (has side effects)
- Idempotent (multiple identical requests have same effect)
- Replaces entire resource

**Examples:**
```
PUT /users/123          - Replace user 123 entirely
```

### PATCH

**Purpose:** Partial update of resource

**Characteristics:**
- Not safe (has side effects)
- Should be idempotent
- Updates only specified fields

**Examples:**
```
PATCH /users/123        - Update specific fields of user 123
```

### DELETE

**Purpose:** Remove resource

**Characteristics:**
- Not safe (has side effects)
- Idempotent (deleting multiple times has same effect)

**Examples:**
```
DELETE /users/123       - Delete user 123
```

## Common Headers

### Request Headers

**Authorization:**
```
Authorization: Bearer ACCESS_TOKEN
Authorization: Basic base64(username:password)
Authorization: ApiKey YOUR_API_KEY
```

**Content-Type:**
```
Content-Type: application/json
Content-Type: application/x-www-form-urlencoded
Content-Type: multipart/form-data
```

**Accept:**
```
Accept: application/json
Accept: application/xml
Accept: */*
```

**Custom Headers:**
```
X-API-Version: v1
X-Request-ID: unique-request-id
X-Client-Version: 2.0.1
```

### Response Headers

**Rate Limiting:**
```
X-RateLimit-Limit: 1000          # Total requests allowed
X-RateLimit-Remaining: 987        # Remaining requests
X-RateLimit-Reset: 1643875200     # Unix timestamp when limit resets
Retry-After: 3600                 # Seconds to wait (for 429 errors)
```

**Pagination:**
```
Link: <https://api.example.com/users?page=2>; rel="next"
X-Total-Count: 2543
X-Page: 1
X-Per-Page: 100
```

**Caching:**
```
Cache-Control: max-age=3600
ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"
Last-Modified: Wed, 21 Oct 2015 07:28:00 GMT
```

## Response Formats

### Success Response (200 OK)

```json
{
  "status": "success",
  "data": {
    "id": 123,
    "name": "Alice Smith",
    "email": "alice@example.com"
  }
}
```

### Created Response (201 Created)

```json
{
  "status": "success",
  "data": {
    "id": 124,
    "name": "Bob Jones",
    "created_at": "2026-02-13T15:30:00Z"
  },
  "message": "User created successfully"
}
```

**With Location Header:**
```
HTTP/1.1 201 Created
Location: https://api.example.com/users/124
Content-Type: application/json

{...}
```

### Error Response (4xx/5xx)

```json
{
  "status": "error",
  "error": {
    "code": "INVALID_INPUT",
    "message": "Email address is required",
    "field": "email",
    "details": {
      "provided": null,
      "expected": "valid email address"
    }
  }
}
```

### Paginated Response

**Offset-Based:**
```json
{
  "status": "success",
  "data": [
    {"id": 1, "name": "User 1"},
    {"id": 2, "name": "User 2"}
  ],
  "pagination": {
    "offset": 0,
    "limit": 100,
    "total": 2543,
    "has_more": true
  }
}
```

**Cursor-Based:**
```json
{
  "status": "success",
  "data": [...],
  "pagination": {
    "next_cursor": "eyJpZCI6MTAwfQ==",
    "has_more": true
  }
}
```

## Query Parameters

### Filtering

```
GET /users?status=active
GET /users?role=admin&status=active
GET /posts?author_id=123
GET /products?price[gte]=100&price[lte]=500
```

### Sorting

```
GET /users?sort=name              # Ascending
GET /users?sort=-created_at       # Descending (- prefix)
GET /users?sort=name,-created_at  # Multiple fields
```

### Pagination

```
GET /users?page=2&per_page=50
GET /users?offset=100&limit=50
GET /users?cursor=abc123&limit=50
```

### Field Selection

```
GET /users?fields=id,name,email
GET /users/123?fields=profile.bio,profile.avatar
```

### Search

```
GET /users?q=alice
GET /posts?search=api+integration
GET /products?query=laptop&category=electronics
```

## Authentication Methods

### API Key (Header)

**Header:**
```
Authorization: Bearer sk-abc123xyz789
```

**Request:**
```bash
curl -H "Authorization: Bearer sk-abc123xyz789" \
     https://api.example.com/users
```

### API Key (Query Parameter)

**URL:**
```
https://api.example.com/users?api_key=sk-abc123xyz789
```

**Security Note:** Less secure; keys visible in logs and browser history.

### Basic Authentication

**Header:**
```
Authorization: Basic base64(username:password)
```

**Request:**
```bash
curl -u username:password \
     https://api.example.com/users
```

### OAuth 2.0

**Step 1: Obtain Access Token**
```bash
curl -X POST https://auth.example.com/oauth/token \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials" \
     -d "client_id=YOUR_CLIENT_ID" \
     -d "client_secret=YOUR_CLIENT_SECRET"
```

**Response:**
```json
{
  "access_token": "ya29.xxx",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

**Step 2: Use Access Token**
```bash
curl -H "Authorization: Bearer ya29.xxx" \
     https://api.example.com/users
```

### JWT (JSON Web Token)

**Header:**
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Token Structure:**
- Header (algorithm and token type)
- Payload (claims/data)
- Signature (verification)

## Status Codes Reference

### 2xx Success

| Code | Name | Meaning |
|------|------|----------|
| 200 | OK | Request succeeded |
| 201 | Created | Resource created successfully |
| 202 | Accepted | Request accepted but processing not complete |
| 204 | No Content | Request succeeded but no content to return |

### 3xx Redirection

| Code | Name | Meaning |
|------|------|----------|
| 301 | Moved Permanently | Resource permanently moved to new URL |
| 302 | Found | Temporary redirect |
| 304 | Not Modified | Cached version is still valid |

### 4xx Client Errors

| Code | Name | Meaning |
|------|------|----------|
| 400 | Bad Request | Invalid request syntax or parameters |
| 401 | Unauthorized | Missing or invalid authentication |
| 403 | Forbidden | Authenticated but not authorized |
| 404 | Not Found | Resource doesn't exist |
| 405 | Method Not Allowed | HTTP method not supported for this endpoint |
| 409 | Conflict | Request conflicts with current state (e.g., duplicate) |
| 422 | Unprocessable Entity | Validation errors |
| 429 | Too Many Requests | Rate limit exceeded |

### 5xx Server Errors

| Code | Name | Meaning |
|------|------|----------|
| 500 | Internal Server Error | Unexpected server error |
| 502 | Bad Gateway | Invalid response from upstream server |
| 503 | Service Unavailable | Server temporarily unavailable |
| 504 | Gateway Timeout | Upstream server timeout |

## Best Practices

### Versioning

**URL Path:**
```
https://api.example.com/v1/users
https://api.example.com/v2/users
```

**Header:**
```
Accept: application/vnd.example.v1+json
```

### Resource Naming

**Use nouns for resources:**
```
GET /users          ✅
GET /getUsers       ❌
```

**Use plural for collections:**
```
GET /users          ✅
GET /user           ❌
```

**Nested resources:**
```
GET /users/123/posts         ✅
GET /posts?user_id=123       ✅ (alternative)
```

### Request/Response Format

**Consistent structure:**
```json
{
  "status": "success|error",
  "data": {},
  "error": {},
  "meta": {}
}
```

**ISO 8601 timestamps:**
```json
{
  "created_at": "2026-02-13T15:30:00Z",
  "updated_at": "2026-02-13T15:35:00Z"
}
```

**Snake_case for JSON:**
```json
{
  "user_id": 123,
  "first_name": "Alice",
  "last_login": "2026-02-13T15:30:00Z"
}
```

### Rate Limiting

**Communicate limits:**
```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 987
X-RateLimit-Reset: 1643875200
```

**Return 429 when exceeded:**
```
HTTP/1.1 429 Too Many Requests
Retry-After: 3600
```

### Error Messages

**Be specific and actionable:**
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Email address is invalid",
    "field": "email",
    "value": "not-an-email",
    "suggestion": "Provide a valid email address (e.g., user@example.com)"
  }
}
```

## Common Patterns

### Batch Operations

**Request:**
```json
POST /users/batch
{
  "operations": [
    {"action": "create", "data": {"name": "Alice"}},
    {"action": "update", "id": 123, "data": {"status": "active"}},
    {"action": "delete", "id": 456}
  ]
}
```

### Webhooks

**Register webhook:**
```json
POST /webhooks
{
  "url": "https://your-server.com/webhook",
  "events": ["user.created", "user.updated"]
}
```

**Webhook payload:**
```json
{
  "event": "user.created",
  "timestamp": "2026-02-13T15:30:00Z",
  "data": {
    "id": 123,
    "name": "Alice Smith"
  }
}
```

### Long-Running Operations

**Initial request:**
```
POST /jobs
HTTP/1.1 202 Accepted
Location: /jobs/abc123
```

**Check status:**
```
GET /jobs/abc123
{
  "status": "processing",
  "progress": 45,
  "estimated_completion": "2026-02-13T16:00:00Z"
}
```

**Get result:**
```
GET /jobs/abc123/result
HTTP/1.1 303 See Other
Location: /results/xyz789
```