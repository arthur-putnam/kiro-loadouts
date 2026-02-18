---
inclusion: fileMatch
fileMatchPattern: ["**/*.c", "**/*.h", "**/CMakeLists.txt", "**/Makefile", "**/*.mk"]
---

# C steering for this workspace

## Goal
Help Kiro write and modify C code that is safe, readable, portable, and consistent with this workspace’s style. Emphasize correctness, memory safety, and predictable behavior.

## Core rules
1. Correctness and safety come before performance.
2. Prefer simple, explicit control flow.
3. Match existing project patterns before introducing new ones.
4. Avoid undefined behavior.
5. Do not silently change public interfaces unless asked.

## Style and formatting
1. Follow the repo’s existing formatting style. If unclear:
   1. 4 space indentation
   2. braces on the same line for functions and blocks
2. Keep functions short and focused.
3. Use descriptive names, avoid single letter variables except for loop indices.
4. Prefer explicit types over implicit assumptions.

## Headers and file organization
1. Each `.c` file should have a corresponding `.h` when exposing public functions.
2. Header files must:
   1. use include guards or `#pragma once`
   2. contain declarations, not implementations
3. Order includes:
   1. the file’s own header
   2. standard library headers
   3. third party headers
   4. local project headers
4. Avoid cyclic header dependencies.

Example include guard:

```c
#ifndef BUFFER_H
#define BUFFER_H

/* declarations */

#endif
```

## Memory management
1. Every allocation must have a clear owner.
2. Document ownership rules in comments when not obvious.
3. Pair allocations and frees in the same abstraction layer.
4. Check allocation results:
   1. handle NULL from malloc and calloc
5. Avoid leaks:
   1. free on all error paths
   2. use cleanup labels for complex functions

Example cleanup pattern:

```c
int do_work(void) {
    char *buf = malloc(1024);
    if (!buf) return -1;

    if (step1(buf) != 0) goto cleanup;
    if (step2(buf) != 0) goto cleanup;

cleanup:
    free(buf);
    return 0;
}
```

## Bounds and safety
1. Never trust external input.
2. Validate all sizes and indexes.
3. Prefer size_t for sizes and counts.
4. Avoid unsafe functions:
   1. do not use gets
   2. avoid strcpy and sprintf without bounds
5. Prefer safer alternatives:
   1. strncpy, snprintf
   2. explicit length tracking

## Error handling
1. Return explicit error codes.
2. Document return values in headers.
3. Do not ignore function results that can fail.
4. Use errno only if the project already relies on it.
5. Keep error handling consistent across modules.

## Pointers and ownership
1. Initialize pointers.
2. Set pointers to NULL after free when reused.
3. Avoid dangling pointers.
4. Clearly distinguish:
   1. borrowed pointers
   2. owned pointers
5. Avoid pointer arithmetic unless necessary and well documented.

## Concurrency (if applicable)
1. Follow existing synchronization primitives in the repo.
2. Protect shared state consistently.
3. Avoid hidden global mutable state.
4. Document thread safety of public functions.

## Globals and state
1. Avoid global variables unless explicitly required.
2. If globals exist:
   1. keep them static to the translation unit
   2. document their purpose
3. Prefer passing state explicitly.

## Macros and inline functions
1. Prefer inline functions over macros when possible.
2. If macros are required:
   1. wrap arguments in parentheses
   2. avoid side effect surprises
3. Use macros for constants only when enums or const are unsuitable.

## Performance guidance
1. Measure before optimizing.
2. Avoid premature micro optimizations.
3. Prefer algorithmic improvements over low level tricks.
4. Keep hot paths simple and branch predictable when possible.

## Portability
1. Avoid compiler specific extensions unless the project requires them.
2. Guard platform specific code with clear preprocessor checks.
3. Use fixed width integer types when size matters:
   1. uint32_t
   2. int64_t

## Tests
1. Follow the repo’s test framework or harness.
2. Write tests for new functionality:
   1. normal cases
   2. edge cases
   3. failure cases
3. Avoid flaky timing dependent tests.
4. Keep tests deterministic.

## Documentation expectations
1. Public functions must be documented in headers.
2. Document:
   1. parameters
   2. ownership rules
   3. return values
   4. error behavior

Example header doc:

```c
/*
 * Reads a file into memory.
 * path: null terminated path string (borrowed)
 * out_buf: receives allocated buffer (owned by caller)
 * out_len: receives buffer length
 * returns 0 on success, non zero on error
 */
int read_file(const char *path, char **out_buf, size_t *out_len);
```

## Security
1. Validate all external input.
2. Avoid buffer overflows and integer overflow.
3. Do not expose secrets in logs.
4. Zero sensitive memory before freeing if required by the domain.

## When unsure
1. Search nearby code and follow the established pattern.
2. Prefer the safest reasonable implementation.
3. Add comments explaining non obvious decisions.

