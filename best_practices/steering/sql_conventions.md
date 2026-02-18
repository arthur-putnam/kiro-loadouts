---
inclusion: fileMatch
fileMatchPattern: ["**/*.sql", "**/*.psql", "**/*.ddl", "**/*.dml"]
---

# SQL steering for this workspace

## Goal
Help Kiro write and modify SQL that is correct, readable, secure, and performant, while matching this repo’s conventions and the target database dialect.

## Core rules
1. Match the project’s SQL dialect and conventions:
   1. Postgres, MySQL, SQL Server, Snowflake, BigQuery, Redshift, etc.
2. Prefer correctness and clarity over cleverness.
3. Avoid breaking schema or query interfaces without explicit instruction.
4. Prevent injection risks by designing for parameterization.
5. Prefer set based operations over row by row logic.

## Dialect and compatibility
1. Do not assume a dialect. Infer it from repo context:
   1. connection code
   2. migration tools
   3. CI configuration
   4. existing SQL files
2. Use dialect specific features only when consistent with the codebase.
3. Keep functions and syntax consistent across files.

## Formatting and style
1. Use consistent capitalization:
   1. keywords uppercase if repo does, otherwise follow existing style
2. Put major clauses on new lines:
   1. SELECT
   2. FROM
   3. JOIN
   4. WHERE
   5. GROUP BY
   6. HAVING
   7. ORDER BY
3. Use explicit JOIN syntax, avoid implicit joins.
4. Prefer meaningful aliases:
   1. short but descriptive
   2. avoid single letter aliases unless common in the repo
5. Prefer trailing commas or leading commas based on repo pattern.

## Query design
1. Prefer explicit column lists. Avoid SELECT * in production queries.
2. Filter early where it improves performance.
3. Use CTEs for readability when helpful, but avoid excessive CTE layering in performance critical paths.
4. Prefer window functions for analytics patterns when appropriate.
5. Avoid correlated subqueries when joins or window functions are clearer or faster.

## Joins
1. Choose join type explicitly:
   1. INNER JOIN
   2. LEFT JOIN
   3. RIGHT JOIN only if necessary
   4. FULL OUTER JOIN only if necessary
2. Join on keys, not computed expressions when possible.
3. Avoid many to many explosions. Apply deduping and constraints where needed.
4. Use EXISTS for semi joins when appropriate.

## Aggregations
1. Ensure GROUP BY matches the intent.
2. Avoid mixing aggregated and non aggregated columns without explicit grouping.
3. Prefer COUNT(*) when counting rows, COUNT(column) when counting non null values.

## Null handling
1. Be explicit about null behavior:
   1. COALESCE
   2. NULLIF
2. Understand three valued logic in WHERE clauses.
3. Prefer IS DISTINCT FROM where supported for null safe comparisons.

## Performance guidance
1. Avoid anti patterns:
   1. functions on indexed columns in WHERE clauses when avoidable
   2. leading wildcard LIKE patterns on large tables
   3. OR chains that defeat indexes when alternatives exist
2. Prefer sargable predicates.
3. Use LIMIT thoughtfully and only when correct.
4. Use EXPLAIN or query plan evidence for major performance claims.
5. Prefer incremental filtering and smaller joins.

## Index awareness
1. Prefer queries that can use indexes:
   1. filter on indexed columns
   2. join on indexed keys
2. Suggest index changes only when justified:
   1. repeated slow query
   2. known access pattern
3. Avoid recommending indexes that cause high write overhead unless necessary.

## Transactions and locking
1. Keep transactions as short as possible.
2. Be explicit about isolation requirements when relevant.
3. Avoid lock escalation patterns.
4. Use SELECT FOR UPDATE only when necessary and consistent with repo patterns.

## Data changes and migrations
1. Follow the repo’s migration system:
   1. Flyway, Liquibase, Alembic, Django migrations, Rails migrations, etc.
2. DDL changes must consider:
   1. backward compatibility
   2. rollout and rollback
   3. production locking behavior
3. Prefer additive migrations when possible:
   1. add new column as nullable
   2. backfill
   3. enforce constraints later
4. Avoid destructive changes without explicit instruction.

## Security
1. Queries must be parameterized in application code. Do not build SQL by string concatenation.
2. Do not embed secrets.
3. Follow least privilege assumptions.
4. Avoid exposing PII in outputs unless necessary.

## Data quality
1. Prefer constraints when appropriate:
   1. NOT NULL
   2. CHECK
   3. FOREIGN KEY
   4. UNIQUE
2. Validate assumptions in queries with explicit filters and joins.

## Testing and validation
1. If the repo has SQL tests, add or update them.
2. For analytics queries, include sanity checks:
   1. row counts
   2. null rates
   3. duplicate detection
3. For migrations, include verification steps.

## Documentation expectations
1. Use comments for intent and constraints, not for restating obvious SQL.
2. Document:
   1. business meaning of key fields
   2. join assumptions
   3. important edge cases
3. For complex queries, include a short header comment.

Example header:

```sql
-- Purpose: Build daily active users by platform.
-- Notes: Excludes internal users and test accounts.
-- Inputs: events, users
-- Output: date, platform, dau
```

## When unsure
1. Inspect nearby SQL files and match formatting and patterns.
2. Confirm dialect before using dialect specific functions.
3. Prefer simpler, explicit SQL.
4. Suggest alternatives with tradeoffs only when needed.
