install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl.

build:
	poetry build

publish:
	poetry publish -r testpypi -u entropax --dry-run

run:
	poetry run brain-even

lint:
	poetry run flake8 brain_games
