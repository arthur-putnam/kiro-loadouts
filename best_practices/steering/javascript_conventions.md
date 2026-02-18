---
inclusion: fileMatch
fileMatchPattern: ["**/*.js", "**/*.jsx", "**/*.ts", "**/*.tsx", "**/*.mjs", "**/*.cjs", "**/package.json", "**/tsconfig*.json", "**/.eslintrc*", "**/.prettierrc*", "**/vite.config.*", "**/next.config.*", "**/webpack.config.*"]
---

# JavaScript and TypeScript steering for this workspace

## Goal
Help Kiro write and modify JS and TS code that matches this workspace’s standards: consistent style, safe by default, maintainable architecture, and predictable runtime behavior.

## Core rules
1. Prefer clarity over cleverness.
2. Keep modules small and single purpose.
3. Follow existing patterns in this repo. Do not introduce new frameworks or patterns unless asked.
4. Avoid breaking public APIs unless explicitly requested.
5. Avoid unnecessary dependencies.

## Language choices
1. If TypeScript is present in the repo, prefer TypeScript for new code and use types in edits.
2. If the file is JavaScript, do not convert it to TypeScript unless requested.
3. Prefer modern ECMAScript features already supported by the project toolchain.

## Formatting and linting
1. Use the project’s existing ESLint and Prettier configuration.
2. Do not fight formatting. Write code that formats cleanly.
3. Keep line length and quote style consistent with repo conventions.

## Imports and modules
1. Keep imports at the top of the file.
2. Prefer ESM imports and exports if the repo is ESM, otherwise follow existing CommonJS style.
3. Avoid circular dependencies.
4. Remove unused imports and dead code when touched.
5. Use path aliases only if already configured.

## Naming and structure
1. Use consistent naming:
   1. camelCase for variables and functions
   2. PascalCase for components and classes
   3. UPPER_SNAKE_CASE for constants when that is already used
2. Prefer named exports for reusable modules unless the repo standard prefers default exports.
3. Keep public APIs intentional:
   1. export only what is needed
   2. keep internal helpers private to the module

## Types and interfaces (TypeScript)
1. Prefer explicit public types for exported functions and components.
2. Use `type` for unions and simple shapes, and `interface` where extension or merging is beneficial, but follow repo convention.
3. Avoid `any`. Use `unknown` with narrowing when necessary.
4. Keep types close to usage, but extract shared types into a dedicated module when reused.
5. Narrow types early, and avoid overly complex generic types unless needed.

## Error handling
1. Handle errors at boundaries:
   1. API handlers
   2. user input parsing
   3. network calls
   4. file operations
2. Throw `Error` objects, not strings.
3. Include actionable context in error messages, but never include secrets or tokens.
4. For async flows, ensure rejected promises are handled.

## Async and performance
1. Prefer async and await for readability.
2. Avoid sequential awaits when operations can be parallel:
   1. use `Promise.all` thoughtfully
   2. preserve ordering only when required
3. Avoid blocking the main thread with heavy computation in frontend apps.
4. For large lists, avoid repeated work inside render paths.

## React guidance (if applicable)
1. Follow existing component patterns, state management, and file organization.
2. Prefer function components and hooks unless the repo uses classes.
3. Keep hooks rules:
   1. do not call hooks conditionally
   2. keep dependencies correct
4. Prefer controlled components when forms need validation, otherwise follow existing patterns.
5. Avoid premature memoization. Use `useMemo` and `useCallback` only when there is a measured need.

## API and networking
1. Use the repo’s existing HTTP client, for example fetch, axios, ky, or a custom client.
2. Use timeouts and cancellation where the repo supports it.
3. Validate server responses when practical, especially in TypeScript.
4. Keep request code centralized if that is the existing architecture.

## Security
1. Never hardcode secrets. Do not log tokens, cookies, or credentials.
2. Sanitize and validate untrusted inputs.
3. Prevent injection:
   1. never build SQL with string concatenation
   2. avoid `eval` and `new Function`
4. In frontend:
   1. avoid unsafe `dangerouslySetInnerHTML` unless necessary and sanitized
   2. follow CSP and escaping patterns in the repo

## Tests
1. Follow the existing test framework, for example Jest, Vitest, Mocha, Cypress, Playwright.
2. Write tests for new behavior and bug fixes:
   1. happy path
   2. key edge cases
   3. error cases
3. Keep tests deterministic:
   1. mock network
   2. control time
   3. seed randomness
4. Prefer testing behavior over implementation details.

## Documentation expectations
1. Use JSDoc or TSDoc only if the repo uses it.
2. Add docs when behavior is not obvious, public APIs change, or there are important constraints.

Example JSDoc style (fallback):
```js
/**
 * Normalize a user provided slug to a safe URL segment.
 * @param {string} input
 * @returns {string}
 * @throws {Error} If the input cannot be normalized.
 */
export function normalizeSlug(input) {
  // ...
}
