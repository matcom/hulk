# Architectural Design

The HULK project is designed around a decoupled, split-brain architecture where the high-level frontend and low-level backend are connected by an Intermediate Representation (Banner IR).

## Literate Programming

The project uses a **Literate Programming** paradigm with [Illiterate](https://github.com/apiad/illiterate) and [Quarto](https://quarto.org/).

1.  **Source of Truth:** All semantic code (Python and Rust) is written inside Markdown code blocks within `.qmd` files in the `pages/` directory.
2.  **Tangling:** The `make tangle` command uses `illiterate` to scan these files for blocks marked with `{export=path/to/file}` and writes the content to the specified file path.
3.  **Rendering:** Quarto is used to render these same `.qmd` files into a high-quality, pedagogical book for students.

## HULK Frontend (Python)

The frontend is implemented in Python 3.13+. It follows a traditional compiler frontend structure:

- **Lexer/Parser:** Hand-rolled or generator-based components that translate HULK source code into an Abstract Syntax Tree (AST).
- **Semantic Analysis:** Performs type checking, scoping, and validation.
- **Lowering:** Translates the HULK AST into **Banner IR**, our stack-based intermediate language.

## Banner IR & Backend (Rust)

The backend is implemented in Rust for memory safety and execution speed.

- **Banner IR:** A low-level, stack-based bytecode designed to be easy for compilers to generate and simple for machines to execute.
- **Virtual Machine:** A stack machine that executes Banner IR instructions. It manages the runtime environment, memory (stack and heap), and built-in functions.

## Syntax Highlighting System

The project uses a unique "single source of truth" system for syntax highlighting:

- **Input:** `syntax/hulk.yaml` defines the language grammar in a custom format.
- **Output:** `syntax/generate.py` converts the YAML into:
    - **TextMate JSON:** For VS Code.
    - **KDE XML:** For Quarto/Pandoc (PDF and HTML rendering).
    - **Injection Grammars:** For highlighting HULK code blocks inside Markdown/Quarto files.
