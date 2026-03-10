# Execution Plan: HULK Book Refactoring

This plan outlines the restructuring of the HULK book into a two-part educational guide focusing on a Python-based frontend and a Rust-based backend.

## 1. Objective
Refactor the HULK book to separate the Frontend (Python) and Backend (Rust) implementation into two distinct parts. The Frontend follows language features, while the Backend follows VM implementation phases.

## 2. Part 1: The Frontend (Python)
Implementing HULK parser, analyzer, and interpreter incrementally.
- **Chapter 01: Arithmetic Expressions** - Lexer, basic expressions, and math.
- **Chapter 02: Strings and Builtins** - String literals and built-in functions.
- **Chapter 03: Variables and Binding** - Scoping and `let` expressions.
- **Chapter 04: Control Flow** - Conditionals and loops.
- **Chapter 05: Functions and Recursion** - Global functions and recursion.
- **Chapter 06: Objects and Classes** - Object-oriented features and classes.
- **Chapter 07: Type Checking and Inference** - Semantic analysis and type inference.

## 3. Part 2: The Backend (Rust)
Implementing a Rust-powered VM for Banner IR.
- **Chapter 08: Lowering to Banner IR** - Transpilation to intermediate representation.
- **Chapter 09: The Metal Sandbox** - Setting up the Rust VM environment.
- **Chapter 10: Stack Machine** - Core VM instruction set and execution.
- **Chapter 11: Object Representation and Heap** - Memory layout and allocation.
- **Chapter 12: Virtual Method Calls** - Dynamic dispatch and vtables.
- **Chapter 13: Garbage Collector** - Automatic memory management.
- **Chapter 14: Final Polish** - CLI integration and refinements.

## 4. Implementation Details
- All chapters are `.qmd` files in the `pages/` directory.
- Literate programming via `illiterate` extracts code to `frontend/` and `backend/`.
- Updated `pages/_quarto.yml` for the new structure.
