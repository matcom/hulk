.PHONY: all tangle test lint format docs

all: tangle lint test

tangle:
	illiterate pages/*.qmd --dir .

test: tangle
	cd frontend && uv run pytest
	cd backend && cargo test

lint: tangle
	cd frontend && uv run ruff check .
	cd backend && cargo clippy

format: tangle
	cd frontend && uv run ruff format .
	cd backend && cargo fmt

docs:
	quarto publish gh-pages --no-prompt --no-browser pages/
