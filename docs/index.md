# HULK Developer Documentation

Welcome to the internal documentation for the HULK language implementation. This documentation is intended for maintainers and contributors.

## Project Overview

HULK is a dual-component project designed to demonstrate the full compiler pipeline:

1.  **HULK Frontend:** A Python-based implementation that handles source code analysis and lowering to an intermediate representation.
2.  **Banner IR:** A Rust-based backend that executes the intermediate representation in a stack-based virtual machine.

## Core Principles

- **Literate Programming:** The source code and the pedagogical book are one and the same.
- **Single Source of Truth:** Syntax highlighting definitions for VS Code and Quarto are generated from a single YAML specification.
- **Modern Tooling:** We leverage `uv` for Python dependency management and `cargo` for Rust.

## Navigation

- [Deployment & Setup](deploy.md): How to build and run the project from scratch.
- [Architectural Design](design.md): Deep dive into the project's structure and data flow.
- [Development Workflow](develop.md): Coding standards, testing strategies, and CI/CD integration.
