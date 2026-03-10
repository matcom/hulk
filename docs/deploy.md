# Deployment & Setup

This guide covers the prerequisites and steps required to build, test, and deploy the HULK ecosystem.

## Prerequisites

Ensure the following tools are installed on your system:

- **Python 3.13+:** We use [uv](https://github.com/astral-sh/uv) for fast and reliable dependency management.
- **Rust (Stable):** Managed via [rustup](https://rustup.rs/).
- **Quarto:** For rendering the book and documentation.
- **Illiterate:** A tool for literate programming (`pip install illiterate`).
- **Node.js & npm:** Required for building the VS Code extension.

## Building the Project

The root `makefile` manages the entire build lifecycle.

### 1. Tangle Source Code
Extract the Python and Rust code from the Quarto pages:
```bash
make tangle
```

### 2. Generate Syntax Definitions
Update VS Code and Quarto highlighting from `syntax/hulk.yaml`:
```bash
make syntax
```

### 3. Run All Tests
Tangle, lint, and run both Python and Rust tests:
```bash
make all
```

### 4. Build VS Code Extension
Package the extension into a `.vsix` file:
```bash
make vscode
```

## Deployment

Documentation is automatically published to GitHub Pages via CI/CD when a release is created. To manually publish:
```bash
make docs
```
