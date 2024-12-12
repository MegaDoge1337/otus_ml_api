.PHONY: lint, format, import-sort


lint:
	ruff check

format:
	black .

import-sort:
	isort .
