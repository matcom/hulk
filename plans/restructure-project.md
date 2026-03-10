# Execution Plan: Unified HULK/Banner Repository Consolidation

This plan outlines the consolidation of separate `frontend/` and `backend/` directories into a single root-level project structure.

## 1. Objective
Merge the repository into a unified structure where Python source resides in `src/hulk/` and Rust source resides in `src/banner/`, with configuration files at the root.

## 2. Implementation
- Created `src/hulk/` and `src/banner/` directories.
- Migrated Python source to `src/hulk/` and Rust source to `src/banner/`.
- Moved Python tests to root `tests/`.
- Merged `frontend/pyproject.toml` into root `pyproject.toml`.
- Moved and updated `backend/Cargo.toml` to root as `banner` package.
- Updated `makefile` to run all commands from the root.
- Performed bulk replacement of `export` paths in all `pages/*.qmd` files.
- Updated `.gitignore` for the new `src/` layout.
- Implemented `src/hulk/cli.py` for the `hulk` entry point.

## 3. Cleanup
- Removed obsolete `frontend/` and `backend/` directories.
- Removed old `requirements.txt`.
