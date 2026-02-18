---
inclusion: auto
name: api-design
description: REST API design patterns and conventions. Use when creating or modifying API endpoints.
---

# API design steering for this workspace

## Goal
When creating or modifying API endpoints, follow consistent REST design, predictable resource modeling, safe defaults, and the conventions already present in this codebase.

## Core rules
1. Follow existing API patterns in this repo first.
2. Prefer resource oriented URLs and standard HTTP methods.
3. Be consistent across endpoints: naming, status codes, error shape, pagination, auth, and versioning.
4. Validate input at the boundary and return actionable errors.
5. Do not introduce breaking changes without explicit instruction.

## Resource modeling and URLs
1. Use nouns, not verbs, in paths.
2. Prefer plural resource collections:
   1. /users
   2. /orders
3. Use hierarchical paths for containment when it reflects ownership:
   1. /users/{userId}/orders
4. Avoid deeply nested paths. If nesting exceeds two levels, consider alternative modeling.
5. Use consistent casing:
   1. prefer kebab case or snake case based on repo convention
   2. avoid mixed styles

## HTTP methods
1. GET retrieves resources and must not mutate state.
2. POST creates new resources or triggers well scoped actions when unavoidable.
3. PUT replaces a resource when full replacement is intended.
4. PATCH partially updates a resource.
5. DELETE removes a resource or marks it deleted based on repo behavior.
6. Use idempotency where expected:
   1. PUT is idempotent
   2. DELETE is idempotent
   3. POST may be idempotent only if the repo supports idempotency keys

## Status codes
1. Use consistent status codes:
   1. 200 OK for successful reads and updates with response body
   2. 201 Created for successful creation, include Location when appropriate
   3. 204 No Content for successful operations with no body
   4. 400 Bad Request for validation and parsing errors
   5. 401 Unauthorized when auth is missing or invalid
   6. 403 Forbidden when auth is valid but access is denied
   7. 404 Not Found when the resource does not exist or is not visible
   8. 409 Conflict for versioning conflicts or constraint conflicts
   9. 422 Unprocessable Entity when the repo uses it for semantic validation
   10. 429 Too Many Requests for rate limiting
   11. 500 and 503 only for server side failures
2. Prefer consistent error mapping. Do not leak internal exception messages.

## Request and response shapes
1. Use consistent JSON structure across endpoints.
2. Prefer stable, explicit field names.
3. Do not include internal database identifiers unless they are part of the public contract.
4. Use ISO 8601 timestamps in UTC unless repo conventions differ.
5. For booleans, use true or false, not strings or integers.

## Error response format
Use the repo’s existing error envelope. If none exists, default to:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Human readable summary",
    "details": [
      { "field": "email", "issue": "must be a valid email address" }
    ],
    "requestId": "optional-correlation-id"
  }
}
```

Rules:
1. error.code is stable and machine readable.
2. error.message is safe for end users.
3. details is optional and used for validation issues.
4. Include a requestId or correlation id if available.

## Validation
1. Validate at the API boundary:
   1. required fields
   2. types and formats
   3. min and max constraints
   4. enum membership
2. Reject unknown fields if the repo does this, otherwise ignore safely.
3. Return field specific errors where possible.

## Pagination, filtering, and sorting
1. Follow repo conventions for pagination. If none exists:
   1. prefer cursor pagination for large datasets
   2. otherwise use limit and offset for smaller datasets
2. Provide defaults and enforce reasonable maximum limits.
3. Use consistent query parameters:
   1. limit
   2. cursor or offset
   3. sort
   4. order
4. Filters should be explicit and documented. Avoid ad hoc parameter names.

Example cursor response pattern:

```json
{
  "items": [ ... ],
  "nextCursor": "opaque-token"
}
```

## Versioning and compatibility
1. Follow existing versioning strategy:
   1. path versioning like /v1
   2. header based versioning
2. Avoid breaking changes:
   1. do not rename fields
   2. do not change types
   3. do not change semantics
3. Use additive changes:
   1. add optional fields
   2. add new endpoints
4. Deprecate with a clear plan:
   1. add deprecation notice
   2. provide migration guidance
   3. preserve backward compatibility for an agreed window

## Authentication and authorization
1. Use the repo’s established auth mechanism:
   1. JWT
   2. session cookies
   3. API keys
   4. OAuth
2. Authorization must be enforced server side on every request.
3. Avoid leaking existence of resources across tenants. Use consistent 404 versus 403 behavior per repo convention.
4. Do not return secrets, tokens, or sensitive fields.

## Idempotency and retries
1. For create endpoints that may be retried, support idempotency keys if the repo uses them.
2. Ensure safe retries for:
   1. timeouts
   2. 502 and 503
3. Avoid double writes and duplicate resources.

## Observability
1. Include correlation ids in logs and responses when available.
2. Log:
   1. request path and method
   2. status code
   3. duration
   4. safe identifiers
3. Do not log request bodies that may contain PII unless explicitly required and redacted.

## Documentation
1. Update API docs when changing endpoints:
   1. OpenAPI or Swagger if present
   2. README or docs site if present
2. Provide examples:
   1. request
   2. response
   3. error cases
3. Keep naming and descriptions consistent.

## Testing
1. Add or update tests for:
   1. success path
   2. validation failures
   3. auth failures
   4. not found and forbidden cases
2. Include contract tests if the repo uses them.

## When unsure
1. Look at existing endpoints and copy the established patterns.
2. Choose consistent semantics over personal preference.
3. Prefer additive, backward compatible changes.
4. Ask for clarification only if a breaking change is unavoidable.

## Useful live references (optional)
1. #[[file:api/openapi.yaml]]
2. #[[file:api/openapi.json]]
3. #[[file:docs/api/]]
4. #[[file:src/server/routes/]]
5. #[[file:src/server/controllers/]]
