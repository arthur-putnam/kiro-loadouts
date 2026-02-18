---
inclusion: fileMatch
fileMatchPattern: ["**/*.jsx", "**/*.tsx"]
---

# React and JSX steering for this workspace

## Goal
Help Kiro write and modify React components that are consistent with this repo’s patterns, accessible, maintainable, and predictable. Prefer clear composition, good state boundaries, and minimal surprises.

## Core rules
1. Match existing patterns in this codebase before inventing new ones.
2. Prefer simple components with clear props over complex abstractions.
3. Accessibility is required.
4. Do not introduce new dependencies unless explicitly asked.
5. Do not change public component APIs without explicit instruction.

## Component style
1. Prefer function components and hooks unless the repo uses class components.
2. Use PascalCase for component names.
3. Keep components focused. Extract subcomponents when a file becomes hard to scan.
4. Prefer composition over inheritance.
5. Avoid deep prop drilling. If the repo uses context, state libraries, or hooks for shared state, follow that.

## JSX and semantics
1. Use semantic HTML elements where possible:
   1. header, nav, main, section, article, aside, footer
   2. button for actions
   3. a for navigation
2. Avoid div soup. Use meaningful structure.
3. Keep JSX readable:
   1. prefer early returns for empty and error states
   2. avoid nested ternaries
4. Prefer fragments only when they improve structure.

## Accessibility
1. All interactive controls must be keyboard accessible.
2. Images:
   1. meaningful images require alt text
   2. decorative images use alt=""
3. Forms:
   1. inputs must have labels
   2. use aria-describedby for help text and errors
4. Use ARIA only when semantic HTML is insufficient.
5. Ensure focus management for modals, dialogs, and routed views, following repo patterns.

## Props and TypeScript
1. If using TypeScript:
   1. type component props explicitly
   2. export prop types only if they are reused
2. Avoid `any`. Use `unknown` plus narrowing when needed.
3. Prefer optional props with defaults over complex unions unless required.
4. Keep props stable. Avoid adding props when composition would suffice.

Example TS props pattern:

```tsx
type ButtonProps = {
  label: string;
  onClick: () => void;
  disabled?: boolean;
};

export function Button({ label, onClick, disabled = false }: ButtonProps) {
  return (
    <button type="button" onClick={onClick} disabled={disabled}>
      {label}
    </button>
  );
}
```

## State and data flow
1. Keep state close to where it is used.
2. Prefer derived state over duplicated state.
3. Avoid syncing props to state unless necessary, and document why.
4. For async data:
   1. follow the repo’s pattern for fetching and caching
   2. handle loading, error, and empty states explicitly
5. Do not introduce new state management libraries unless asked.

## Hooks
1. Follow the Rules of Hooks:
   1. do not call hooks conditionally
   2. do not call hooks inside loops
2. Use custom hooks for reusable logic, not for hiding complexity.
3. Keep dependency arrays correct.
4. Avoid premature useMemo and useCallback. Use them only when there is a clear benefit.

## Effects
1. Prefer event driven logic over effects where possible.
2. Effects must:
   1. be idempotent
   2. clean up subscriptions and timers
   3. avoid stale closures by using correct dependencies
3. Avoid effects that run on every render unless intentional.

## Styling
1. Follow the repo’s styling approach:
   1. CSS modules, styled components, Tailwind, plain CSS, etc.
2. Keep class names consistent with existing conventions.
3. Avoid inline styles unless the repo commonly uses them.
4. Keep layout and spacing concerns in CSS, not in component logic.

## Performance
1. Avoid rendering large lists without virtualization if the repo has that pattern.
2. Keep render paths cheap:
   1. avoid creating new objects and functions in hot components unless needed
3. Avoid unnecessary re renders:
   1. lift state only when needed
   2. split components when a subtree changes often

## Error boundaries and resilience
1. Follow repo patterns for error boundaries, toasts, and user facing error states.
2. Fail gracefully:
   1. show actionable messages
   2. provide retry affordances where appropriate

## Testing
1. Follow the repo’s testing stack:
   1. React Testing Library, Jest, Vitest, Cypress, Playwright
2. Test behavior, not implementation details.
3. Prefer queries by role, label text, and accessible name.
4. Keep tests deterministic:
   1. mock network
   2. control timers when needed

## Security
1. Never render untrusted HTML. Avoid dangerouslySetInnerHTML unless required and sanitized.
2. Do not log secrets or tokens.
3. Validate and sanitize user inputs following repo patterns.

## Documentation expectations
1. Add comments only for non obvious behavior.
2. Prefer self documenting code through clear naming and small components.

## When unsure
1. Look at nearby components and match their patterns.
2. Choose the simplest accessible structure.
3. Prefer predictable data flow and explicit states.

