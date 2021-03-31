install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl.

publish:
	poetry publish -r testpypi -u entropax --dry-run

run:
	poetry run brain-games

lint:
	poetry run flake8 brain_games
