# Development Workflow

This document outlines the development discipline and standards for contributing to the HULK project.

## Local Development Loop

The most efficient way to develop is using the "dev" mode, which watches for changes in your Quarto files and automatically re-runs tests:
```bash
make dev
```

## Testing Strategy

Tests are mandatory for every feature. We maintain a split testing suite:

- **Python Tests:** Use `pytest` for the HULK frontend.
- **Rust Tests:** Use `cargo test` for the Banner VM.

Tests should be triggered via the makefile:
```bash
make test
```

## Coding Standards

### Python
- **Linter/Formatter:** We use [Ruff](https://github.com/astral-sh/ruff) for linting and formatting.
- **Type Safety:** Use Python's type hints (`typing` module) wherever possible.

### Rust
- **Linter:** Use `clippy` for idiomatic Rust code.
- **Formatter:** Use `cargo fmt` for consistent styling.

## VS Code Extension Development

The `vscode/` directory contains the HULK VS Code extension.

- **To Debug:** Open the `vscode` folder in VS Code, go to the "Run and Debug" side bar, and select "Extension". This launches a new VS Code instance with your local extension installed.
- **Icons:** File icons are located in `vscode/images/hulk.png`.

## CI/CD Pipeline

The project uses GitHub Actions for continuous integration.

- **On Push:** Runs the full build, linting, and testing suite.
- **On Release:**
    - Renders the student book (HTML and PDF).
    - Packages the VS Code extension.
    - Publishes the book to GitHub Pages.
    - Attaches the PDF and `.vsix` extension to the GitHub Release.
