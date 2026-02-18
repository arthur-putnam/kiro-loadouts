# Rapid Prototyping Steering

## Goal
Move fast and demonstrate ideas quickly. Prioritize visible progress, working demos, and iteration speed over polish, scalability, and long term maintainability.

This mode is for proofs of concept, hack sessions, and demos. Not production.

## Core principles
1. Optimize for speed of delivery.
2. Prefer simple solutions over correct architecture.
3. Skip non essential abstractions.
4. Favor working demos over clean design.
5. Assume the code may be thrown away later.

## Testing
1. Do not write tests unless explicitly requested.
2. Manual verification is sufficient.
3. Focus on demo behavior, not edge cases.

## Code quality tradeoffs
1. Accept duplication if it saves time.
2. Use hardcoded values when convenient.
3. Ignore minor linting and formatting issues.
4. Prefer fewer files and less structure.
5. Skip refactoring unless it blocks progress.

## UI prototyping shortcuts
1. You may use hardcoded data instead of building a backend.
2. Mock API responses directly in the frontend.
3. Use static JSON fixtures to simulate real data.
4. Skip authentication flows for UI demos.
5. Focus on visual behavior, not infrastructure.

## Data and persistence
1. In memory storage is acceptable.
2. Temporary files are fine.
3. Mock data is encouraged.
4. Fake APIs and stub services are acceptable.
5. Data resets are acceptable between runs.

## Error handling
1. Handle only errors that break the demo.
2. Use simple error messages.
3. Avoid complex retry logic.

## Security tradeoffs
1. Use fake credentials and dummy secrets.
2. Do not design production auth flows.
3. Clearly label unsafe shortcuts.

## Performance
1. Ignore scalability concerns.
2. Accept inefficient implementations.
3. Optimize only if the demo becomes slow.

## Documentation
1. Add brief comments explaining shortcuts.
2. Document what must change before production.

Example comment:

```text
// Rapid prototype: hardcoded data for UI demo. Replace with real backend before release.
```