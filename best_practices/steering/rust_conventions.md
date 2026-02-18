---
inclusion: fileMatch
fileMatchPattern: ["**/*.rs", "**/Cargo.toml", "**/Cargo.lock"]
---

# Rust steering for this workspace

## Goal
Help Kiro write and modify Rust code that is idiomatic, safe, maintainable, and aligned with this workspace’s architecture. Emphasize correctness, ownership clarity, and predictable behavior.

## Core rules
1. Prefer safe Rust over unsafe Rust.
2. Follow existing project patterns before introducing new abstractions.
3. Make ownership and lifetimes obvious from the API.
4. Optimize for readability first, performance second.
5. Do not change public APIs without explicit instruction.

## Style and formatting
1. Follow rustfmt defaults unless the repo overrides them.
2. Use `cargo fmt` style formatting.
3. Use descriptive names, avoid abbreviations unless conventional.
4. Prefer expression oriented style where it improves clarity.
5. Keep functions small and focused.

## Modules and organization
1. Match the repo’s existing module structure.
2. Avoid deep module nesting without a clear reason.
3. Keep public interfaces minimal.
4. Use `pub(crate)` instead of `pub` when possible.
5. Separate internal helpers from public APIs.

## Ownership and borrowing
1. Prefer borrowing over cloning when practical.
2. Avoid unnecessary allocations.
3. Make ownership explicit in function signatures.
4. Prefer references over Arc or Rc unless shared ownership is required.
5. Avoid lifetime complexity unless needed.

## Error handling
1. Prefer `Result<T, E>` over panics in library code.
2. Use `?` for propagation.
3. Create domain specific error types when appropriate.
4. Use `thiserror` or repo standard error tooling if present.
5. Panics are acceptable only for unrecoverable programmer errors.

Example:

```rust
fn parse_id(input: &str) -> Result<u64, ParseError> {
    input.parse().map_err(ParseError::InvalidId)
}
```

## Option and Result patterns
1. Prefer combinators when they improve clarity.
2. Avoid deeply nested match blocks.
3. Use early returns for error paths.
4. Use `expect` only with meaningful messages.

## Unsafe code
1. Avoid unsafe unless absolutely necessary.
2. Document why unsafe is required.
3. Minimize unsafe scope.
4. Encapsulate unsafe inside safe abstractions.
5. Add tests around unsafe boundaries.

## Concurrency
1. Prefer message passing over shared mutable state.
2. Use existing async runtime if the repo defines one.
3. Avoid blocking in async contexts.
4. Clearly document thread safety.
5. Prefer Send and Sync safe abstractions.

## Performance guidance
1. Measure before optimizing.
2. Prefer algorithmic improvements over micro optimizations.
3. Avoid premature inlining and specialization.
4. Minimize allocations in hot paths.
5. Use iterators and zero cost abstractions.

## Traits and generics
1. Prefer simple generic bounds.
2. Avoid overly clever trait hierarchies.
3. Use traits to express behavior, not clever type tricks.
4. Keep public generics ergonomic.

## Tests
1. Follow existing test style in the repo.
2. Write tests for:
   1. normal cases
   2. edge cases
   3. error cases
3. Prefer deterministic tests.
4. Use property testing only if already part of the repo.

## Documentation
1. Public APIs must have rustdoc comments.
2. Explain intent, not just mechanics.
3. Include examples when helpful.

Example:

```rust
/// Parses a user ID from a string.
///
/// Returns an error if the string is not a valid integer.
fn parse_user_id(s: &str) -> Result<u64, ParseError> { ... }
```

## Security
1. Validate all external inputs.
2. Avoid exposing secrets in logs.
3. Prefer safe parsing and bounds checks.
4. Avoid unchecked indexing.

## Dependencies
1. Prefer existing dependencies in the repo.
2. Avoid adding heavy crates without justification.
3. Favor well maintained crates.
4. Keep dependency surface minimal.

## When unsure
1. Search nearby code for precedent.
2. Prefer idiomatic Rust patterns.
3. Choose the simplest safe implementation.
4. Add comments explaining non obvious decisions.

