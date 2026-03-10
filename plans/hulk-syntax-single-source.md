# Plan: HULK Syntax Highlighting Single Source of Truth

## Objective
Establish a central, extensible grammar definition for the HULK programming language to ensure consistent syntax highlighting in both VS Code and Quarto/Pandoc rendered output.

## 1. Architecture: Single Source of Truth
Create a new directory `syntax/` in the project root to house the grammar definition and generator:
- `syntax/hulk.yaml`: The primary grammar definition (Single Source of Truth).
- `syntax/generate.py`: Python script to generate TextMate and KDE XML formats.
- `syntax/hulk.xml`: Generated KDE XML definition for Quarto/Pandoc.

## 2. Grammar Definition (`syntax/hulk.yaml`)
The YAML structure will define:
- **Metadata:** Name, scope name, file extensions.
- **Tokens:** Groups for keywords, built-ins, constants, operators, literals, and comments.
- **Macro-specific patterns:** Patterns for `*` (variable arguments), `@` (symbolic arguments), and `$` (variable placeholders).
- **Type patterns:** Support for `Number`, `String`, `Boolean`, `Object`, and complex types like `T*` and `T[]`.

## 3. Generator Script (`syntax/generate.py`)
A Python 3.12+ script will:
1.  **Parse `hulk.yaml`**: Load the central grammar definition.
2.  **Generate TextMate JSON**: Produce `vscode/syntaxes/hulk.tmLanguage.json` for VS Code.
3.  **Generate KDE XML**: Produce `syntax/hulk.xml` for Quarto/Pandoc.
4.  **Scope Mapping**: Map TextMate scopes (e.g., `keyword.control`) to KDE XML attributes (e.g., `dsControlFlow`) to ensure visual consistency.

## 4. Quarto Integration (`pages/_quarto.yml`)
Update `pages/_quarto.yml` to include the generated KDE XML file:
```yaml
format:
  html:
    syntax-definitions:
      - ../syntax/hulk.xml
```
This ensures that ```hulk blocks in `.qmd` files are correctly highlighted in the rendered HTML.

## 5. Workflow Integration (Makefile)
Update the root `makefile` to automate the generation process:
- **New target `syntax`**: Runs `python3 syntax/generate.py`.
- **Update `vscode` target**: Add `syntax` as a dependency.
- **Update `docs` target**: Add `syntax` as a dependency.

## 6. Testing and Validation
- **VS Code Verification**: Open a `.hulk` file and verify all new constructs (Protocols, Macros) are highlighted correctly.
- **Quarto Verification**: Run `make docs` and inspect the generated HTML to ensure ```hulk blocks have the same highlighting as in the editor.
- **Extension Verification**: Verify that adding a keyword to `hulk.yaml` and running `make syntax` updates both the VS Code extension and the rendered documentation.
