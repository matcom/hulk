# Root Cause Analysis: HULK Syntax Highlighting Failure in Quarto (.qmd) Files

## Symptom
HULK syntax highlighting in ` ```hulk ` code blocks inside `.qmd` (Quarto) files is not working in VS Code, even though an injection grammar is configured.

## Root Causes

### 1. Missing Target Scope
The Quarto VS Code extension uses `source.qmd` as the primary scope for Quarto files. The current `hulk-vscode` extension only targets `text.html.markdown`, `text.quarto`, and `source.quarto`. Since the active scope in a `.qmd` file is often `source.qmd`, the injection grammar is never activated.

### 2. Broken End-of-Block Regex
The `end` pattern for the fenced code block in `hulk-markdown.tmLanguage.json` was defined as:
`"end": "(^|\\G)(\\s*)(\\3)\\b"`

The `\\b` (word boundary) at the end of the backticks (matched by `\\3`) is problematic. Because a backtick (`` ` ``) is a non-word character, `\\b` will only match if the *next* character is a word character (a-z, 0-9, etc.). However, code blocks usually end with a newline. This causes the regex to fail to match the closing fence, potentially breaking the highlighting for the rest of the document.

## Impact
- No syntax highlighting for HULK in Quarto documents.
- Potential highlighting "leak" or breakage in Markdown files due to the invalid `end` regex.

## Proposed Resolution
1.  Update `syntax/generate.py` to:
    - Add `source.qmd` to the `injectionSelector` in `generate_markdown_injection`.
    - Fix the `end` regex to `(^|\\G)(\\s*)(\\3)\\s*$` to correctly match the closing fence regardless of word boundaries.
2.  Update `vscode/package.json` to include `source.qmd` in the `injectTo` list.
3.  Regenerate the syntax files using `python3 syntax/generate.py`.
4.  Re-package the extension using `make vscode`.
