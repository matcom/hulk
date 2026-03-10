# Execution Plan: Syntax Highlighting for Banner IR

This plan outlines the implementation of syntax highlighting for the 'Banner' Intermediate Representation (IR) across the VS Code extension and Quarto documentation.

## 1. Objective
Add full syntax highlighting support for the Banner IR, including standalone `.banner` files, Markdown/Quarto code block injections, and KDE XML generation for Quarto rendering.

## 2. Implementation
- Created `syntax/banner.yaml` as the source of truth for Banner grammar.
- Refactored `syntax/generate.py` to support multiple languages dynamically.
- Registered 'banner' in `vscode/package.json` (Language ID, extension `.banner`, grammars, and injection).
- Created `vscode/language-configuration-banner.json` for editor settings.
- Generated `vscode/syntaxes/banner.tmLanguage.json` and `vscode/syntaxes/banner-markdown.tmLanguage.json`.
- Generated `syntax/banner.xml` for Quarto/Pandoc rendering.
- Updated `pages/_quarto.yml` to include the new syntax definition.

## 3. Language Details
- **Language ID**: `banner`
- **Extensions**: `.banner`, `.cil`
- **Grammar Scope**: `source.banner`
- **Injection Scope**: `markdown.banner.codeblock`
