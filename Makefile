SRCS = $(shell find egauge/ -name \*.py)

UIFILES = $(wildcard egauge/webapi/cloud/gui/*.ui)
UIPYFILES = $(UIFILES:.ui=.py)

%.py: %.ui
	pyside2-uic --from-imports $^ -o $@

all: $(UIPYFILES)
	python3 setup.py sdist

release: all
	twine upload dist/*

lint:
	pylint $(SRCS)
