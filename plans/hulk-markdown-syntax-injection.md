# Plan: HULK Markdown Syntax Highlighting Injection

## Objective
Enable syntax highlighting for ` ```hulk ` code blocks in VS Code for both standard Markdown (`.md`) and Quarto (`.qmd`) files using a grammar injection.

## 1. Extension Structure
Add a new grammar file to the `vscode/` directory:
- `vscode/syntaxes/hulk-markdown.tmLanguage.json`: Grammar injection for HULK inside Markdown/Quarto.

## 2. Injection Grammar (`vscode/syntaxes/hulk-markdown.tmLanguage.json`)
Create a specialized grammar that:
- **Scope Name:** `markdown.hulk.codeblock`
- **Injection Selector:** `L:text.html.markdown, L:text.quarto`
- **Pattern:** Detects fenced code blocks starting with ` ```hulk ` (case-insensitive) and applies `source.hulk` inside the block.

## 3. Register the Injection Grammar (`vscode/package.json`)
Update the `contributes.grammars` section in `vscode/package.json` to include the new injection:
- `scopeName: markdown.hulk.codeblock`
- `path: ./syntaxes/hulk-markdown.tmLanguage.json`
- `injectTo: ["text.html.markdown", "text.quarto"]`

## 4. Workflow Integration (Makefile)
Ensure the `make vscode` command includes the new files in the resulting `.vsix` package.

## 5. Testing and Validation
- **Manual Verification:** Open a `.qmd` or `.md` file in VS Code and verify that ` ```hulk ` blocks are correctly highlighted.
- **Package Verification:** Run `make vscode` and ensure the `.vsix` contains the new `syntaxes/hulk-markdown.tmLanguage.json` file.
