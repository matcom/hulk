.PHONY: all tangle test lint format docs vscode syntax

all: tangle lint test

syntax:
	python3 syntax/generate.py

tangle:
	illiterate pages/*.qmd --dir .

vscode: syntax
	cd vscode && npx @vscode/vsce package -o ../hulk-vscode.vsix

test: tangle
	cd frontend && uv run pytest
	cd backend && cargo test

lint: tangle
	cd frontend && uv run ruff check .
	cd backend && cargo clippy

format: tangle
	cd frontend && uv run ruff format .
	cd backend && cargo fmt

docs: syntax
	quarto publish gh-pages --no-prompt --no-browser pages/

preview:
	quarto preview pages/

dev:
	find pages | grep qmd$ | entr make test
