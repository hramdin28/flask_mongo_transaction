define USAGE
Commands:
	init      Install Python dev dependencies
	init-prod      Install Python prod-only dependencies
	test      Run linters, test db migrations and tests.
	mongodb   launch a docker-compose to launch a 3 nodes mongo cluster
endef

export USAGE

help:
	@echo "$$USAGE"

init:
	pip install -r resources/requirements/dev.txt

init_prod:
	pip install -r resources/requirements/common.txt

test:
	pytest -v -o junit_family=xunit1 --cov=. --cov-report xml:coverage.xml --junitxml=nosetests.xml
