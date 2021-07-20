install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

test:
	poetry run python -m pytest tests

linter:
	poetry run pre-commit run --all

package-install:
	python3 -m pip install --user dist/*.whl
