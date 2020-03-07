SRCS = $(shell find egauge/ -name \*.py)

all:
	python3 setup.py sdist

release: all
	twine upload dist/*

lint:
	pylint $(SRCS)
