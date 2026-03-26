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

## Rendering workflow

After generating a `.puml` file, always attempt to render it immediately:

```bash
java -jar plantuml.jar diagram.puml          # PNG output
java -jar plantuml.jar -tsvg diagram.puml    # SVG output
```

If the render command fails (missing JAR, Java not found, etc.), run the bundled install script to set up PlantUML automatically:

```bash
python .kiro/skills/plantuml/scripts/install_plantuml.py
```

Optional: specify a custom JAR destination:

```bash
python .kiro/skills/plantuml/scripts/install_plantuml.py --dest /path/to/plantuml.jar
```

The script checks for Java, downloads the JAR if missing, verifies the checksum, and confirms everything works. It exits with code 0 when PlantUML is ready. After a successful install, retry the render command.

If the install script also fails, inform the user that PlantUML dependencies need to be installed manually. PlantUML requires Java 8 or later. Point them to:

- **Java**: <https://adoptium.net/> or their OS package manager (`brew install openjdk`, `apt install default-jdk`, etc.)
- **PlantUML JAR**: <https://plantuml.com/download>

### Alternative render methods

#### Docker (no Java required)

```bash
docker run --rm -v "$(pwd):/data" plantuml/plantuml diagram.puml
```

#### npm (Node.js projects)

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
