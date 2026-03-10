# Scaffolding Plan: Principles of Programming Languages (Literate Edition)

This plan outlines the steps to restructure the 'hulk' repository into a 14-week book project using **Literate Programming**. All source code will reside in `.qmd` files and be "tangled" (extracted) using `illiterate`.

## Phase 1: Directory Restructuring (Monorepo)

1.  **Rename/Create Core Folders**:
    - `frontend/`: Target for Python-based compiler logic (Lexing, Parsing, Semantic Analysis).
    - `bridge/`: Target for BANNER IR specifications and emitters.
    - `backend/`: Target for Rust-based Virtual Machine and runtime logic.
2.  **Initialize Project Skeletons** (These will be populated by `illiterate`):
    - `uv init --lib frontend`
    - `cargo init backend --bin`

## Phase 2: Quarto & Literate Content (`pages/`)

1.  **Flatten `pages/` structure**:
    - Organize into 14 numbered chapters (e.g., `01-dual-ancestry.qmd`, `02-atomization.qmd`).
    - Migrate current `pages/principles/` and `pages/hulk/` content into this sequence.
2.  **Consolidate Reference**:
    - Move all existing technical syntax notes from `pages/hulk/*.md` into `pages/appendix-hulk-syntax.qmd`.
3.  **Update `pages/_quarto.yml`**:
    - Section I: Frontend (Chapters 1-6)
    - Section II: Bridge (Chapters 7-8)
    - Section III: Backend (Chapters 9-14)

## Phase 3: Literate Workflow & Tooling

1.  **Integrate `illiterate`**:
    - Ensure `illiterate` is accessible in the environment.
    - Add code blocks to `.qmd` files with appropriate file paths (e.g., `frontend/lexer.py`, `backend/src/main.rs`).
2.  **Global `makefile`**:
    - **`tangle` target**: Runs `illiterate pages/*.qmd` to generate code from documentation.
    - **`test` / `lint` targets**: Must depend on the `tangle` target to ensure tests run against the latest extracted code.
    - **`all` target**: `tangle` + `lint` + `test`.

## Phase 4: Execution & Verification

1.  **Direct Refactor**: Move and rename existing files.
2.  **Boilerplate Generation**: Create the 14 chapter placeholders with initial `illiterate` tags.
3.  **Verification**: Run `make all` and `quarto render pages/`.

---
**Literate Mandate:** Do not edit files in `frontend/`, `bridge/`, or `backend/` directly. All changes must be made in the corresponding `.qmd` files in `pages/`.
