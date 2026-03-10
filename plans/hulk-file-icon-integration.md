# Plan: HULK File Icon Integration

## Objective
Add a distinctive file icon for `.hulk` files in the VS Code extension and refine project metadata.

## 1. Extension Assets
Create a new directory `vscode/images/` and place the generated HULK icon inside:
- **Location:** `vscode/images/hulk.png`
- **Specification:** A single 128x128 PNG file (provided by user).

## 2. Manifest Updates (`vscode/package.json`)
Update the extension manifest to include:
- **Icon:** Association of the language ID `hulk` with the new icon.
- **Metadata Enhancement:**
    - `icon`: Add the extension icon (can use the same `hulk.png`).
    - `repository`: Ensure the URL is correct (`https://github.com/matcom/hulk.git`).
    - `homepage`: Point to the GitHub repository.
    - `bugs`: Link to the GitHub issues page.

## 3. Implementation Details
The `package.json` needs to be updated with the `icon` and `language` association:
```json
{
    "icon": "images/hulk.png",
    "contributes": {
        "languages": [
            {
                "id": "hulk",
                "aliases": ["HULK", "hulk"],
                "extensions": [".hulk"],
                "configuration": "./language-configuration.json",
                "icon": {
                    "light": "./images/hulk.png",
                    "dark": "./images/hulk.png"
                }
            }
        ]
    }
}
```

## 4. Metadata Alignment
- **`frontend/pyproject.toml`**: Ensure the author is consistently set to `Alejandro Piad Morffis <apiad@apiad.net>`.
- **`README.md`**: Update the root documentation to mention the new icon and extension status.

## 5. Workflow Integration
- **`makefile`**: No changes required (the `vsce package` command will include all files in the `vscode/` folder).
- **`.vscodeignore`**: Ensure `images/` is NOT ignored.

## 6. Testing and Validation
- **Package Verification:** Run `make vscode` and ensure the `.vsix` contains the `images/hulk.png` file.
- **Visual Check:** Install the extension and verify that `.hulk` files in the VS Code Explorer show the new icon.
