.PHONY: install generate open

install:
	poetry install

generate:
	poetry run python -m sbgs.generate

open:
	open ./dist/index.html
