.DEFAULT_GOAL := help

.PHONY: test-install
test-install:  ## Install dependencies required for local test execution.
	@pip install -q -r requirements/test.txt

.PHONY: test
test: test-install  ## Run test suite.
	@py.test -v tests

.phony: help
help: ## Print Makefile usage.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
