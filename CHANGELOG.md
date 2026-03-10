# Changelog

All notable changes to this project will be documented in this file.

## [0.8.0] - 2026-03-10
### Added
- **Project Structure:** Consolidated `frontend/` and `backend/` into a single, unified root-level architecture with `src/hulk/` and `src/banner/`.
- **CLI:** Added `hulk` CLI entry point to the root package.

### Changed
- **Build:** Unified `pyproject.toml` and `Cargo.toml` at the root.
- **Literate Programming:** Updated all Quarto chapters to export to the new root-level structure.
- **Build System:** Refactored `makefile` for simplified root-level command execution.

### Fixed
- **Syntax:** Corrected inheritance declaration for the `PolarPoint` type in syntax examples.
- **Syntax Generator:** Fixed a linting error (E701) in the grammar generation script.

## [0.7.0] - 2026-03-10
### Added
- **Syntax:** Full syntax highlighting for Banner IR (standalone files and Quarto code block injection).
- **VS Code Extension:** HULK icon support for Banner files.
- **Documentation:** New "BANNER Intermediate Representation" appendix with formal design details.
- **Documentation:** New "Tooling" appendix describing the HULK ecosystem.

### Changed
- **Documentation:** Restructured the book into "Part 1: The Frontend" and "Part 2: The Backend" for a clearer curriculum.
- **Build:** Updated project structure and dependencies for better literate programming support.
- **Build:** Explicitly defined `hatch` build targets for the `frontend` package to resolve build errors.

### Removed
- Redundant `requirements.txt` (redundant with `uv`).

## [0.6.2] - 2026-03-10
### Fixed
- **Documentation:** Enabled HULK syntax highlighting in the rendered PDF output by adding `syntax-definitions` to the Quarto PDF configuration.

## [0.6.1] - 2026-03-10
### Fixed
- **CI/CD:** Repaired the release pipeline by switching to the official `install-tinytex` action and explicitly naming the PDF output.
- **Quarto:** Fixed PDF rendering issues by configuring a predictable output filename (`hulk.pdf`) in `_quarto.yml`.
- **VS Code Extension:** Improved Quarto syntax highlighting by adding the `text.html.quarto` scope to the injection grammar.

## [0.6.0] - 2026-03-10
### Added
- **Project Structure:** Scaffolding for a split-brain architecture (Python frontend, Rust backend) using a literate programming approach (`illiterate`).
- **Documentation:** Migrated and refactored the entire project into a 14-week Quarto book format.
- **VS Code Extension:** Initial release of the `hulk-vscode` extension providing full syntax highlighting (including macros, protocols, and types).
- **Quarto Syntax:** Implemented a single source of truth (`syntax/hulk.yaml`) that generates both VS Code TextMate JSON and Quarto KDE XML highlighting definitions.
- **CI/CD:** Automated GitHub Actions pipeline to publish HTML/PDF documentation and the `.vsix` extension upon GitHub Release.

## [Unreleased]
- Integrated Gemini CLI framework.
