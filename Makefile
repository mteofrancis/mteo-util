SHELL = /bin/bash

FIND	= $(shell type -P find)
RM	= $(shell type -P rm)
PIP	= $(shell type -P pip)
PYTHON	= $(shell type -P python)
TWINE	= $(shell type -P twine)
XARGS	= $(shell type -P xargs)

PACKAGE_NAME = mteo-util

.PHONY: all
all:
	@$(PYTHON) -m build

.PHONY: check
check: check-syntax run-testsuite

.PHONY: check-syntax
check-syntax:
	@if [[ $$(type -P find-python-syntax-errors) ]]; \
	then \
	  echo; \
	  echo "Checking source tree for syntax errors in Python files..."; \
	  echo; \
	  find-python-syntax-errors || exit 1; \
	fi

.PHONY: run-testsuite
run-testsuite:
	@echo "Running test suite..."
	@echo
	@$(PYTHON) setup.py nosetests

.PHONY: upload
upload:
	@$(TWINE) upload --repository $(PACKAGE_NAME) dist/*

.PHONY: install
install:
	@$(PIP) install .

.PHONY: uninstall
uninstall:
	@$(PIP) uninstall -y $(PACKAGE_NAME)

.PHONY: clean
clean:
	@$(FIND) . -type d -name __pycache__ -print0 |$(XARGS) -0 $(RM) -rf
	@$(RM) -rf src/$(PACKAGE_NAME).egg-info

.PHONY: distclean
distclean: clean
	@$(RM) -rf dist

##
# vim: ts=8 sw=8 tw=100 noet fdm=marker :
##
