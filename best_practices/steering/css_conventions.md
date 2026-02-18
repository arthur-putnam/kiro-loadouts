---
inclusion: fileMatch
fileMatchPattern: ["**/*.css", "**/*.scss", "**/*.sass", "**/*.less", "**/*.module.css", "**/*.module.scss"]
---

# CSS steering for this workspace

## Goal
Help Kiro write and modify CSS that is consistent with this repo’s styling system, accessible, maintainable, and predictable. Emphasize readability, low specificity, and reusable patterns.

## Core rules
1. Follow the repo’s existing styling approach:
   1. plain CSS, CSS Modules, Sass, Less, Tailwind, styled components, etc.
2. Keep selectors simple and low specificity.
3. Prefer reusable utilities and components over one off rules.
4. Do not introduce new frameworks or preprocessors unless asked.
5. Accessibility and responsive behavior are required.

## Organization
1. Keep styles near the component or feature when that is the repo pattern.
2. Prefer a consistent structure within files:
   1. layout
   2. spacing
   3. typography
   4. color
   5. interaction states
3. Keep related rules grouped.
4. Avoid giant monolithic stylesheets unless the repo uses them.

## Naming conventions
1. Follow the repo’s naming scheme:
   1. BEM
   2. CSS Modules local class names
   3. utility class conventions
2. Use clear, descriptive names.
3. Avoid names tied to specific colors or pixels when intent based naming is possible.

## Specificity and selectors
1. Prefer class selectors.
2. Avoid id selectors for styling.
3. Avoid deep descendant selectors.
4. Avoid !important unless the repo uses it intentionally and there is no better option.
5. Avoid styling by element type globally unless part of a reset or typography system.

## Reusability
1. Prefer design tokens or variables if the repo has them:
   1. CSS custom properties
   2. Sass variables
   3. theme objects
2. Reuse spacing and typography scales instead of raw numbers.
3. Prefer shared utility classes when appropriate.

## Responsiveness
1. Use mobile first styles when possible.
2. Follow the repo’s breakpoint conventions.
3. Avoid fixed widths that break on small screens.
4. Prefer fluid layouts:
   1. flex
   2. grid
   3. clamp where appropriate

## Accessibility
1. Maintain sufficient color contrast.
2. Ensure focus states are visible:
   1. do not remove outlines without providing a replacement
3. Provide hover, focus, and active states for interactive elements.
4. Respect reduced motion preferences:
   1. use prefers-reduced-motion for animations
5. Avoid relying on color alone to convey meaning.

Example reduced motion pattern:

```css
@media (prefers-reduced-motion: reduce) {
  .animated {
    transition: none;
    animation: none;
  }
}
```

## Layout guidance
1. Prefer modern layout primitives:
   1. flexbox
   2. CSS grid
2. Avoid clearfix and legacy layout hacks unless required by existing code.
3. Keep layout rules separated from component appearance when feasible.

## Typography
1. Follow the repo’s typography scale.
2. Use consistent font stacks and line heights.
3. Avoid hardcoded font sizes where tokens exist.

## Colors and theming
1. Use tokens or CSS variables for colors when available.
2. Do not hardcode colors repeatedly.
3. Support dark mode if the repo supports it:
   1. class based theme switching
   2. prefers-color-scheme patterns

## Animations
1. Keep animations subtle and purposeful.
2. Avoid layout thrashing animations:
   1. prefer transform and opacity
3. Keep durations consistent with repo conventions.
4. Respect prefers-reduced-motion.

## Performance
1. Avoid expensive selectors.
2. Avoid large paint areas where possible.
3. Prefer composited animations.
4. Minimize unused CSS:
   1. remove dead rules when touched
   2. avoid copy paste blocks

## Cross browser concerns
1. Follow the repo’s browser support targets.
2. Use autoprefixer if the repo uses it.
3. Avoid unsupported features unless guarded by fallbacks.

## Security and content
1. Avoid loading remote assets unless the repo already does.
2. Do not embed secrets in CSS URLs.

## Documentation expectations
1. Comments should explain intent, not restate obvious rules.
2. Add comments only when a rule is non obvious or a workaround is required.

Example:

```css
/* Workaround for Safari flexbox min-height behavior in this layout */
```

## When unsure
1. Inspect nearby components and reuse existing patterns.
2. Prefer low specificity and reusable tokens.
3. Keep changes minimal and consistent.
4. Choose the simplest solution that meets accessibility and responsiveness requirements.
