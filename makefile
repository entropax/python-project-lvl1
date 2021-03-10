install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl.

build:
	poetry build

publish:
	poetry publish

run:
	poetry run brain-games
