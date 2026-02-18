---
inclusion: fileMatch
fileMatchPattern: ["**/*.py", "**/pyproject.toml", "**/requirements*.txt", "**/poetry.lock", "**/uv.lock", "**/Pipfile", "**/setup.cfg", "**/tox.ini"]
---

# Python steering for this workspace

## Goal
Help Kiro write and modify Python code that matches this workspace’s standards: readable, testable, type aware, secure by default, and easy to maintain.

## Core rules
1. Prefer clarity over cleverness. Optimize only with evidence.
2. Keep functions small and single purpose.
3. Use standard library features first, then third party libraries already in the repo.
4. Match existing project patterns. If a pattern exists, follow it even if alternatives are possible.
5. Avoid breaking public interfaces unless explicitly requested.

## Style and formatting
1. Follow PEP 8 and PEP 257 unless this repo clearly deviates.
2. Use type hints for new or modified code, especially public functions and complex data flows.
3. Use docstrings only when they add value, for example non obvious behavior, constraints, or tricky edge cases.
4. Prefer f strings for formatting.
5. Prefer pathlib over os.path for new code.
6. Prefer dataclasses for simple data containers.
7. Prefer named constants over magic numbers.

## Imports
1. Keep imports at the top of the file.
2. Group imports in this order:
   1. Standard library
   2. Third party
   3. Local application imports
3. Avoid wildcard imports.
4. Avoid importing heavy modules inside tight loops.

## Types and interfaces
1. Use typing thoughtfully:
   1. Use `list[str]`, `dict[str, Any]`, and `tuple[...]` on Python 3.9 plus.
   2. Use `Protocol` for structural interfaces when appropriate.
   3. Use `TypedDict` for dict shaped records when it improves clarity.
2. Keep function signatures stable and explicit.
3. Prefer returning structured objects over loosely typed dicts when the shape is stable.

## Error handling
1. Raise specific exceptions, not bare `Exception`.
2. Add context to errors, but do not swallow exceptions silently.
3. Use `from e` when re raising to preserve tracebacks.
4. Validate inputs at boundaries:
   1. API handlers
   2. CLI entrypoints
   3. File parsing
   4. External service calls

## Logging and observability
1. Use the project’s existing logging approach. If unclear, use the standard `logging` module.
2. Prefer structured logging style if the repo already uses it.
3. Do not log secrets, tokens, passwords, private keys, or full payloads containing PII.
4. Log actionable context:
   1. identifiers
   2. counts
   3. durations
   4. safe metadata

## Performance guidance
1. Avoid obvious anti patterns:
   1. repeated work inside loops that can be hoisted
   2. N plus 1 calls to databases or APIs
   3. reading large files into memory when streaming works
2. Use profiling or measurements before major optimizations.
3. Prefer generator based pipelines for large data flows when appropriate.

## Concurrency and async
1. Do not introduce async unless the surrounding code already uses it.
2. If using async:
   1. avoid blocking calls inside async functions
   2. use timeouts for network calls
   3. propagate cancellation correctly

## Tests
1. Follow existing test framework patterns. If the repo uses pytest, prefer pytest style.
2. Write tests for new behavior and bug fixes:
   1. happy path
   2. key edge cases
   3. error cases
3. Keep tests deterministic:
   1. avoid real network calls
   2. freeze time when needed
   3. seed randomness
4. Prefer fixtures and factories over repeated setup boilerplate.

## Security
1. Never introduce or hardcode secrets.
2. Validate and sanitize untrusted inputs.
3. Use safe file handling:
   1. avoid path traversal
   2. avoid shell injection
   3. use parameterized queries for SQL
4. Prefer vetted libraries already in the repo for crypto, auth, and HTTP.

## Documentation expectations
1. Add or update docstrings when:
   1. behavior is non obvious
   2. there are constraints, invariants, or side effects
   3. public APIs are introduced or changed
2. Keep docstrings consistent with the repo’s style. If none is obvious, use Google style.

Example docstring style (fallback):
```python
def parse_event(raw: str) -> dict[str, object]:
    """Parse a raw event string into a structured event dict.

    Args:
        raw: Raw event payload string.

    Returns:
        A dict containing normalized event fields.

    Raises:
        ValueError: If the payload is malformed.
    """
