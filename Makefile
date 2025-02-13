.PHONY: install generate open lint format

install:
	poetry install

generate:
	poetry run python -m sbgs.generate

open:
	open ./dist/index.html

lint:
	poetry run pysen run lint

format:
	poetry run pysen run format
