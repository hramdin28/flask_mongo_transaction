define USAGE
Commands:
	init		Install Python dev dependencies
	init-prod	Install Python prod-only dependencies
	test		Run test and generate html coverage
	test-xml	Run test and generate xml coverage
	mongo		Launch a 3 node mongo cluster with replicaset
	clean		Clean cache and .py file command for macos
endef

export USAGE

help:
	@echo "$$USAGE"

init:
	pip install -r resources/requirements/dev.txt

init_prod:
	pip install -r resources/requirements/common.txt

test:
	mkdir -p coverage
	pytest --cov-report html:coverage/ --cov=.

test-xml:
	pytest -v -o junit_family=xunit1 --cov=. --cov-report xml:coverage.xml --junitxml=nosetests.xml

clean:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

mongo:
	docker-compose -f resources/docker/docker-compose.yml up -d