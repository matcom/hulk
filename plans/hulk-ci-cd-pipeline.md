# Plan: HULK CI/CD Pipeline

## Objective
Establish a GitHub Actions workflow to automate the generation and deployment of project artifacts (HTML/PDF documentation and VS Code extension) upon a new GitHub Release.

## 1. Workflow Architecture
Create a new GitHub Actions workflow file:
- **Location:** `.github/workflows/release.yml`
- **Trigger:** `on: release: types: [published]`
- **Permissions:** `contents: write` (to upload assets and push to `gh-pages`).

## 2. Environment Configuration
The workflow will run on `ubuntu-latest` and set up the following environments:
- **Checkout:** Use `actions/checkout@v4`.
- **Python:** Setup Python and install `PyYAML` (required by `syntax/generate.py`).
- **Node.js:** Setup Node.js (required for `vsce package`).
- **Quarto:** Setup Quarto and install `TinyTeX` (required for PDF generation).

## 3. Build and Package Steps
- **Syntax Generation:** Run `make syntax` to ensure grammars are up to date.
- **VS Code Extension:** Run `make vscode` to package `hulk-vscode.vsix`.
- **Documentation (HTML):** Render Quarto documentation as HTML.
- **Documentation (PDF):** Render Quarto documentation as PDF.

## 4. Deployment and Asset Attachment
- **GitHub Pages:** Deploy the generated HTML (from `pages/_book/`) to the `gh-pages` branch.
- **Release Assets:** Attach the generated `hulk-docs.pdf` and `hulk-vscode.vsix` to the GitHub Release.

## 5. Workflow Implementation (YAML)
```yaml
name: Release Pipeline

on:
  release:
    types: [published]

permissions:
  contents: write

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      - name: Install Python dependencies
        run: pip install PyYAML

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Set up Quarto
        uses: quarto-dev/quarto-actions/setup@v2
        
      - name: Install TinyTeX
        run: |
          quarto install tinytex --no-prompt

      - name: Build Syntax and VS Code Extension
        run: |
          make syntax
          make vscode

      - name: Render Documentation
        run: |
          quarto render pages/ --to html
          quarto render pages/ --to pdf

      - name: Deploy HTML to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: pages/_book
          exclude_assets: '*.pdf'

      - name: Prepare Release Assets
        run: |
          cp pages/_book/*.pdf hulk-docs.pdf

      - name: Upload Release Assets
        uses: softprops/action-gh-release@v2
        with:
          files: |
            hulk-docs.pdf
            hulk-vscode.vsix
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## 6. Testing and Validation
- **Release Verification:** Manually trigger a release on GitHub and monitor the workflow logs.
- **Asset Verification:** Ensure the `gh-pages` branch is updated and the `hulk-docs.pdf` and `hulk-vscode.vsix` are attached to the release.
- **PDF Check:** Verify that the PDF is correctly formatted and includes all chapters.
