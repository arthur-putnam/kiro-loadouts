---
inclusion: fileMatch
fileMatchPattern: [
  "**/templates/**/*.html",
  "**/*.j2",
  "**/*.jinja",
  "**/*.jinja2",
  "**/*.djhtml",
  "**/*.tmpl",
  "**/*.gotmpl",
  "**/*.gohtml"
]
---

# Server template steering for this workspace
Django templates, Jinja, Go templates

## Goal
Help Kiro write and modify server rendered templates that are secure, maintainable, accessible, and consistent with this workspace’s conventions. Emphasize safe output handling, clear separation of concerns, and predictable template structure.

## Core rules
1. Never trust template input. Assume all data may be untrusted.
2. Prefer simple templates. Keep business logic out of templates.
3. Match the existing template engine and project conventions.
4. Keep markup semantic and accessible.
5. Prefer reusable partials over copy paste.

## Template security
1. Do not disable auto escaping.
2. Do not mark content as safe unless it is sanitized and the repo already has a vetted pattern for doing so.
3. Avoid constructing HTML with string concatenation in template expressions.
4. Never render raw user provided HTML unless explicitly requested and sanitized.
5. Do not output secrets, tokens, or sensitive identifiers.

## Data shaping and logic boundaries
1. Templates render presentation only.
2. Complex logic belongs in:
   1. Django views or template tags and filters
   2. Jinja filters, macros, or view layer helpers
   3. Go handlers or helper functions and structs
3. If the template needs complex data transformation, request or implement that transformation in the server code rather than the template.

## Structure and reuse
1. Prefer layouts and inheritance if supported:
   1. Django `{% extends %}` and `{% block %}`
   2. Jinja `{% extends %}` and `{% block %}`
2. Use includes for shared sections:
   1. headers, footers, nav, forms, error banners, flash messages
3. Name partials consistently with repo conventions.
4. Keep block names stable and descriptive.

## Semantics and accessibility
1. Use semantic HTML elements where possible:
   1. header, nav, main, section, article, aside, footer
2. Use proper heading hierarchy.
3. Forms must have labels connected to inputs.
4. Error messages should be linked to inputs via aria-describedby when appropriate.
5. Ensure keyboard navigation works for interactive controls.

## Template readability
1. Keep indentation consistent.
2. Keep template tags readable and not overly nested.
3. Avoid deep nested if and for blocks. Prefer server side shaping of context.
4. Prefer early checks for empty states.

## Internationalization
1. Follow existing i18n patterns:
   1. Django `{% trans %}` and `{% blocktrans %}`
   2. Jinja translation functions if configured
2. Do not hardcode user visible strings if the repo uses translations.

## URL and routing helpers
1. Use the framework’s routing helpers:
   1. Django `{% url 'name' arg %}`
   2. Jinja route helpers provided by the app
   3. Go templates should receive fully formed URLs from handlers if there is no routing helper
2. Avoid hardcoding absolute URLs unless required.

## Forms and CSRF
1. Always include CSRF protection for POST forms:
   1. Django `{% csrf_token %}`
   2. Jinja and Go must follow the repo’s CSRF approach
2. Ensure method and action are correct and explicit.
3. Prefer server side validation and show field specific errors in the template.

## Go template specific guidance
1. Keep templates logic minimal:
   1. prefer `{{ if }}` and `{{ range }}` only for presentation
2. Avoid complex pipelines that become unreadable.
3. Prefer to compute booleans and derived values in Go code and pass them as fields.

Example patterns:

```gotemplate
{{ if .User }}
  <p>Welcome, {{ .User.Name }}</p>
{{ else }}
  <p>Please sign in.</p>
{{ end }}
```

```gotemplate
<ul>
  {{ range .Items }}
    <li>{{ .Title }}</li>
  {{ else }}
    <li>No items found.</li>
  {{ end }}
</ul>
```

## Django template specific guidance
1. Prefer built in filters and tags over custom logic.
2. Use `{% with %}` sparingly to improve readability, not to build logic.
3. Use `{% include %}` for reusable pieces.
4. Keep template tags consistent with repo conventions.

Example patterns:

```django
{% extends "base.html" %}

{% block content %}
  <h1>{{ page_title }}</h1>

  {% if items %}
    <ul>
      {% for item in items %}
        <li>{{ item.name }}</li>
      {% endfor %}
    </ul>
  {% else %}
    <p>No items found.</p>
  {% endif %}
{% endblock %}
```

## Jinja specific guidance
1. Prefer macros for reusable UI patterns when the repo uses them.
2. Keep filters and tests consistent.
3. Avoid heavy logic in templates.

Example macro pattern:

```jinja
{% macro field_error(errors) %}
  {% if errors %}
    <p class="error" role="alert">{{ errors[0] }}</p>
  {% endif %}
{% endmacro %}
```

## Asset and script loading
1. Follow the repo’s asset pipeline conventions:
   1. static file helpers
   2. hashed assets
   3. bundler generated manifests
2. Prefer deferred scripts where appropriate.
3. Avoid inline scripts unless the repo does this and has CSP allowances.

## Performance
1. Avoid expensive work in templates:
   1. do not loop over large collections without pagination
   2. do not call heavy helpers per item
2. Prefer server side pagination and precomputed fields.
3. Keep DOM size reasonable.

## Documentation expectations
1. Add comments only for non obvious template logic.
2. Document why a block exists, not what obvious HTML does.

Example comment:

```html
<!-- Renders flash messages from server session -->
```

## When unsure
1. Inspect nearby templates and match the style.
2. Keep templates dumb. Move logic to server code.
3. Default to safe escaping and simple rendering.
4. Prefer includes and inheritance over duplication.
