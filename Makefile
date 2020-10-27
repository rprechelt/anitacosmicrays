##
# anitacosmicrays
#
# @file
# @version 0.0.1

# our testing targets
.PHONY: tests flake black mypy all

all: mypy isort black flake tests

tests:
	python -m pytest --cov=anitacosmicrays tests

flake:
	python -m flake8 anitacosmicrays

black:
	python -m black -t py37 anitacosmicrays tests

mypy:
	python -m mypy anitacosmicrays

isort:
	python -m isort --atomic -rc anitacosmicrays tests

# end
