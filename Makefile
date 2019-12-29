build: ## build the package
	python3 setup.py build

install: ## install the package
	pip3 install .

tests: ## Clean and Make unit tests
	python3 -m pytest -v ./aat/crypto/tests --cov=aat

lint: ## run linter
	python3 -m flake8 aat 

docs:  ## Build the sphinx docs
	make -C docs html

dist:  ## dist to pypi
	rm -rf dist build
	python3 setup.py sdist
	python3 setup.py bdist_wheel
	twine check dist/* && twine upload dist/*

clean: ## clean the repository
	find . -name "__pycache__" | xargs rm -rf
	find . -name "*.pyc" | xargs rm -rf
	rm -rf .coverage coverage cover htmlcov logs build dist *.egg-info
	find . -name "*.so"  | xargs rm -rf
	make -C ./docs clean

# Thanks to Francoise at marmelab.com for this
.DEFAULT_GOAL := help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

print-%:
	@echo '$*=$($*)'

.PHONY: clean tests help install docs data dist build
