---
name: plantuml
description: Generate, render, and manage PlantUML diagrams. Use when creating architecture diagrams, sequence diagrams, class diagrams, ERDs, state machines, activity flows, or any UML diagram from code or descriptions.
license: MIT
compatibility: Requires Java 8+ and plantuml.jar, or Docker. Optional npm wrapper for Node.js projects.
metadata:
  author: kiro-loadouts
  version: 1.0.0
---

## Overview

This skill generates PlantUML diagram source files (`.puml`) and provides render commands so diagrams can be produced immediately. It covers all major diagram types and includes runtime setup guidance.

## Runtime

### Preferred: install script

Use the bundled installer — it checks for Java, downloads the JAR if missing, verifies the checksum, and confirms everything works:

```bash
python .kiro/scripts/install_plantuml.py
```

Optional: specify a custom JAR destination:

```bash
python scripts/install_plantuml.py --dest /path/to/plantuml.jar
```

The script exits with code 0 when PlantUML is ready. If Java is missing it prints install instructions and exits non-zero. Run it before attempting to render any diagram.

### Render after install

```bash
java -jar plantuml.jar diagram.puml          # PNG output
java -jar plantuml.jar -tsvg diagram.puml    # SVG output
```

### Alternative: Docker (no Java required)

```bash
docker run --rm -v "$(pwd):/data" plantuml/plantuml diagram.puml
```

### Alternative: npm (Node.js projects)

```bash
npm install -g node-plantuml
puml generate diagram.puml --output diagram.png
```

## Generating a diagram

1. Identify the right diagram type for the concept (see `references/diagram-types.md`)
2. Write a `.puml` file — always `@startuml` / `@enduml`, always include a `title`
3. Apply the standard skinparam block for consistent styling
4. Provide the render command alongside the file

## Standard skinparam block

Include this in every diagram for consistent styling:

```plantuml
skinparam defaultFontName Arial
skinparam defaultFontSize 12
skinparam backgroundColor #FAFAFA
skinparam shadowing false
skinparam roundcorner 8
skinparam ArrowColor #555555
skinparam BorderColor #AAAAAA
```

## File organization

- Store puml diagrams in `docs/diagrams/` and generated diagrams in `docs/diagrams/rendered`
- Name files descriptively in kebab-case: `auth-flow.puml`, `domain-model.puml`
- Commit `.puml` source files — rendered outputs can be gitignored if CI generates them
