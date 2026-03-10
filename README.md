# HULK (Havana University Language for Kompilers)

[![Release Pipeline](https://github.com/matcom/hulk/actions/workflows/release.yml/badge.svg)](https://github.com/matcom/hulk/actions/workflows/release.yml)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by-sa/4.0/)
[![Python 3.13+](https://img.shields.io/badge/python-3.13%2B-blue.svg)](https://www.python.org/)
[![Rust 2021](https://img.shields.io/badge/rust-2021-orange.svg)](https://www.rust-lang.org/)
[![Docs: GitHub Pages](https://img.shields.io/badge/docs-gh--pages-blueviolet)](https://matcom.github.io/hulk)

HULK is a didactic, type-safe, object-oriented, and incremental programming language designed for teaching compiler construction at the university level.

## Project Architecture

The project follows a **literate programming** approach, where the implementation is embedded within the documentation itself.

- **Frontend (HULK):** Implemented in Python 3.13+, focusing on lexing, parsing, and semantic analysis.
- **Backend (Banner IR):** A stack-based virtual machine implemented in Rust for high performance and safety.
- **Literate Engine:** Uses `illiterate` to tangle code from Quarto (`.qmd`) files in `pages/` into the `src/` directory.

## Getting Started

To set up the development environment, ensure you have the following installed:
- Python 3.13+ (and `uv`)
- Rust (and `cargo`)
- Quarto
- Node.js (for VS Code extension development)

Run the full build and test suite:
```bash
make all
```

## Documentation

- **[Student-Facing Book](https://matcom.github.io/hulk):** The primary pedagogical resource for the language.
- **[Developer Documentation](docs/index.md):** Technical guides on architecture, deployment, and development workflows.

## License

HULK is licensed under [CC BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/).
