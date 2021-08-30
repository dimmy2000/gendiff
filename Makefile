install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

pytest:
	poetry run python -m pytest

lint:
	poetry run flake8 gendiff

package-install:
	pip install dist/*.whl

package-uninstall:
	pip uninstall hexlet-code -y
