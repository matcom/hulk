.PHONY: all tangle test lint format docs vscode syntax

all: tangle lint test

syntax:
	python3 syntax/generate.py

tangle:
	rm -rf src/hulk/*
	rm -rf src/banner/*
	illiterate pages/*.qmd --dir .

vscode: syntax
	cd vscode && npx @vscode/vsce package -o ../hulk-vscode.vsix

test: tangle
	uv run pytest
	cargo test

lint: tangle
	uv run ruff check .
	cargo clippy

format: tangle
	uv run ruff format .
	cargo fmt

docs: syntax
	quarto publish gh-pages --no-prompt --no-browser pages/

preview:
	quarto preview pages/

dev:
	find pages | grep qmd$ | entr make test
