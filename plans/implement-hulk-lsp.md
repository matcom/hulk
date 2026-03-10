# Execution Plan: HULK Language Server Protocol (LSP) Implementation

This plan outlines the steps to implement a Language Server for the HULK language using Python (`pygls`) and integrate it with the existing VS Code extension.

## 1. Objective
Provide a rich development experience for HULK in VS Code, including real-time diagnostics, hover information, navigation (Go to Definition), and code completion, by wrapping the existing HULK `frontend` library in an LSP-compliant server.

## 2. Architectural Impact
- **Language Server:** A Python process running `pygls`. It will reside within the `frontend` package.
- **LSP Client:** The VS Code extension (`vscode/`) will be updated to launch and communicate with the Python server via JSON-RPC over Standard I/O.
- **Analysis Engine:** The `frontend` library will be used for parsing and semantic analysis. The server will transform the AST and symbol table information into LSP-standard formats.

## 3. File Operations

### Modified Files:
- `frontend/pyproject.toml`: Add `pygls >= 1.3.1` to dependencies.
- `vscode/package.json`: 
    - Add `vscode-languageclient` to `dependencies`.
    - Add `main` entry point (e.g., `"./out/extension.js"`).
    - Add `activationEvents` for `onLanguage:hulk`.
    - Define configuration settings for the Python path.

### New Files:
- `frontend/src/frontend/lsp/server.py`: Entry point for the LSP server.
- `frontend/src/frontend/lsp/handlers/`:
    - `diagnostics.py`: Logic for converting parser/semantic errors to LSP diagnostics.
    - `hover.py`: Logic for extracting type/doc info from the AST.
    - `navigation.py`: Logic for "Go to Definition" and "Document Symbols".
    - `completion.py`: Logic for keyword and scope-based completion.
- `vscode/src/extension.ts`: TypeScript code to locate the Python interpreter and launch the server.
- `vscode/tsconfig.json`: TypeScript configuration for the extension.

## 4. Step-by-Step Execution

### Phase 1: Server Infrastructure (Python)
1. **Dependency Update:** Add `pygls` to `frontend/pyproject.toml` and sync the environment.
2. **Server Boilerplate:** Implement `HulkLanguageServer` class in `server.py` and set up standard I/O communication.
3. **Internal API:** Create a bridge between the LSP server and the `frontend` library's `Parser` and `SemanticAnalyzer`.

### Phase 2: Core LSP Features
1. **Diagnostics:** Implement handlers for `textDocument/didOpen`, `textDocument/didChange`, and `textDocument/didSave`. Run the HULK compiler frontend on the text and report errors.
2. **Document Symbols:** Implement `textDocument/documentSymbol` by traversing the HULK AST to find class, function, and variable declarations.
3. **Hover & Definition:**
    - Implement a "node at position" utility for the AST.
    - Use the `SemanticAnalyzer`'s symbol table to resolve symbols at the cursor.
    - Implement `textDocument/hover` and `textDocument/definition`.
4. **Code Completion:** Implement `textDocument/completion` providing HULK keywords and symbols available in the current scope.

### Phase 3: VS Code Integration
1. **Client Implementation:** Create `vscode/src/extension.ts` using `vscode-languageclient`.
2. **Server Launcher:** Implement logic to find the appropriate Python interpreter (respecting VS Code's Python extension settings) and run `python -m frontend.lsp.server`.
3. **Packaging:** Update `makefile` or build scripts to compile the TypeScript extension and package the VSIX.

## 5. Testing Strategy
- **Unit Testing:** Use `pytest` along with `pygls.testing` to unit test individual LSP handlers without needing a full VS Code instance.
- **Integration Testing:** Use the VS Code Extension Development Host to verify end-to-end functionality.
- **Robustness Testing:** Test the server with syntactically incorrect and partially written HULK files to ensure the server doesn't crash and provides useful (if partial) diagnostics.
