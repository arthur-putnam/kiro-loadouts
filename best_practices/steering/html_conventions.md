---
inclusion: fileMatch
fileMatchPattern: ["**/*.html", "**/*.htm"]
---

# HTML steering for this workspace

## Goal
Help Kiro write and modify HTML that is semantic, accessible, maintainable, and consistent with this workspace’s frontend architecture. Emphasize clarity, accessibility, and predictable structure.

## Core rules
1. Prefer semantic HTML over div heavy layouts.
2. Accessibility is required, not optional.
3. Match existing project patterns before introducing new structure.
4. Keep markup simple and readable.
5. Avoid inline hacks when structured solutions exist.

## Semantics
1. Use semantic elements whenever possible:
   1. header
   2. nav
   3. main
   4. section
   5. article
   6. aside
   7. footer
2. Use proper heading hierarchy:
   1. one h1 per page unless the repo standard differs
   2. do not skip heading levels arbitrarily
3. Use lists for grouped content.
4. Use buttons for actions and links for navigation.

## Accessibility
1. All images must have meaningful alt text.
2. Decorative images must use empty alt attributes.
3. Form inputs must have associated labels.
4. Use ARIA only when semantic HTML is insufficient.
5. Ensure keyboard navigation works.
6. Avoid relying on color alone to convey meaning.

## Structure and readability
1. Use consistent indentation.
2. Keep nesting shallow when possible.
3. Avoid excessive wrapper divs.
4. Group related sections clearly.
5. Use meaningful class and id names.

## Attributes and validation
1. Use valid HTML5 markup.
2. Avoid deprecated elements.
3. Prefer data attributes for custom metadata.
4. Quote attribute values consistently.
5. Avoid inline JavaScript when possible.

## Performance
1. Avoid unnecessary DOM complexity.
2. Defer non critical scripts.
3. Use appropriate image formats and sizes.
4. Avoid blocking rendering with large inline assets.

## Forms
1. Use proper input types:
   1. email
   2. number
   3. date
   4. tel
2. Validate both client and server side.
3. Provide helpful error messages.
4. Preserve accessibility in validation flows.

## Security
1. Never inject untrusted HTML without sanitization.
2. Avoid inline event handlers.
3. Follow CSP rules defined by the project.
4. Escape dynamic content properly.

## Reusability
1. Prefer reusable components or templates if the project supports them.
2. Avoid copy paste markup duplication.
3. Follow existing partial or layout conventions.

## Documentation expectations
1. Add comments only when structure is non obvious.
2. Explain intent, not trivial markup.

Example:

```html
<!-- Primary navigation for authenticated users -->
<nav class="main-nav">
  ...
</nav>
```

## When unsure
1. Follow existing HTML patterns in nearby files.
2. Prefer accessibility over visual shortcuts.
3. Choose simpler markup over clever tricks.
4. Add structure that future developers can understand quickly.