---
inclusion: fileMatch
fileMatchPattern: ["**/*.java", "**/pom.xml", "**/build.gradle", "**/build.gradle.kts", "**/settings.gradle*", "**/gradle.properties"]
---

# Java steering for this workspace

## Goal
Help Kiro write and modify Java code that matches this workspace’s standards: readable, testable, maintainable, and secure by default. Prefer clear design, strong typing, and consistent architecture.

## Core rules
1. Follow existing project conventions and frameworks.
2. Prefer readability and correctness over cleverness.
3. Keep classes and methods small and focused.
4. Do not change public APIs without explicit instruction.
5. Add tests for new behavior and bug fixes.

## Style and formatting
1. Follow the repo’s formatter and style rules. If unclear:
   1. 4 space indentation
   2. braces on the same line
2. Use descriptive names.
3. Avoid overly long methods. Extract helpers when needed.
4. Prefer immutability:
   1. final fields
   2. unmodifiable collections where appropriate

## Project structure
1. Follow the existing package layout.
2. Keep package names lowercase and meaningful.
3. One top level public class per file.
4. Keep interfaces close to implementations unless the repo uses layered packaging.

## OO design
1. Prefer composition over inheritance.
2. Use interfaces where substitution is intended.
3. Keep responsibilities clear:
   1. controllers handle IO boundaries
   2. services contain business logic
   3. repositories handle persistence
4. Avoid god classes and utility dumping grounds.

## Null handling
1. Avoid returning null from public methods when possible.
2. Prefer Optional for absent values where it improves clarity, but follow repo convention.
3. Validate inputs at boundaries:
   1. public methods
   2. API endpoints
   3. deserialization
4. Use Objects.requireNonNull when appropriate.

## Exceptions and error handling
1. Throw specific exceptions with actionable messages.
2. Avoid swallowing exceptions.
3. Preserve causes when wrapping:
   1. new CustomException(message, cause)
4. Use checked exceptions only if the repo pattern requires them.
5. Do not use exceptions for normal control flow.

## Logging
1. Use the repo’s logging framework:
   1. slf4j, logback, log4j2, etc.
2. Use parameterized logging, not string concatenation.
3. Do not log secrets or sensitive data.
4. Log actionable context:
   1. identifiers
   2. counts
   3. durations
   4. safe metadata

Example:

```java
logger.info("Processed {} records for userId={}", count, userId);
```

## Concurrency
1. Do not introduce concurrency unless the repo already uses it for similar tasks.
2. Prefer standard concurrency primitives:
   1. Executors
   2. CompletableFuture
3. Avoid shared mutable state.
4. Document thread safety when relevant.

## Collections and streams
1. Prefer straightforward loops when they are clearer than streams.
2. Use streams for simple transformations and filters, not complex logic.
3. Avoid nested streams that harm readability.
4. Avoid collecting into mutable shared structures in parallel streams.

## Performance guidance
1. Avoid premature optimization.
2. Do not allocate in hot loops unnecessarily.
3. Prefer algorithmic improvements over micro optimizations.
4. Use profiling before major changes.

## Data access and persistence
1. Use the repo’s established persistence approach:
   1. JDBC, JPA, Hibernate, jOOQ, etc.
2. Use parameterized queries, never string concatenation.
3. Avoid N plus 1 patterns in ORM usage.
4. Keep transactions explicit and consistent.

## Testing
1. Follow the repo’s testing stack:
   1. JUnit
   2. Mockito
   3. AssertJ
   4. Spring test utilities if used
2. Write tests for:
   1. happy path
   2. edge cases
   3. error handling
3. Keep tests deterministic:
   1. avoid real network calls
   2. control time
4. Prefer testing behavior over internal implementation details.

## Documentation and comments
1. Use Javadoc for public APIs when the repo expects it.
2. Keep comments focused on intent and constraints, not obvious code.
3. Document:
   1. invariants
   2. thread safety
   3. performance constraints
   4. security constraints

Example Javadoc:

```java
/**
 * Parses an input into a normalized identifier.
 *
 * @param input raw identifier string
 * @return normalized identifier
 * @throws IllegalArgumentException if input is invalid
 */
public String normalizeId(String input) { ... }
```

## Security
1. Never hardcode secrets.
2. Validate and sanitize untrusted input.
3. Avoid injection vulnerabilities:
   1. SQL injection
   2. command injection
   3. template injection
4. Use safe defaults for serialization and deserialization.
5. Prefer vetted libraries already in the repo for crypto and auth.

## When unsure
1. Look at similar code in the repo and follow that.
2. Choose the simplest maintainable solution.
3. Add tests for behavior changes.
4. Add small comments only where behavior is non obvious.

