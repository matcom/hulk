.PHONY: all
all: install docs

.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: docs
docs:
	mkdocs build

.PHONY: serve
serve:
	mkdocs serve

.PHONY: reqs
reqs:
	pip freeze > requirements.txt
