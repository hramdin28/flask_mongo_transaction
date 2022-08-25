define USAGE
Commands:
	init		Install Python dev dependencies
	init-prod	Install Python prod-only dependencies
	run 		Run the application
	test		Run test and generate html coverage
	test-xml	Run test and generate xml coverage
	mongo		Launch a 3 node mongo cluster with replicaset
	clean		Clean cache and .py file command for macos
	network		Create a shared docker network
	build		Build a docker image
	run-docker	Run the docker container app
	kill 		kill docker container
endef

export USAGE

app_name = flask-prod-app

help:
	@echo "$$USAGE"

init:
	pip install -r resources/requirements/dev.txt

init-prod:
	pip install -r resources/requirements/common.txt

run:
	python3 main.py

test:
	mkdir -p coverage
	pytest --cov-report html:coverage/ --cov=.

test-xml:
	pytest -v -o junit_family=xunit1 --cov=. --cov-report xml:coverage.xml --junitxml=nosetests.xml

clean:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

network:
	docker network create netApplication

mongo:
	docker-compose -f resources/docker/docker-compose.yml up -d

build:
	docker build --tag $(app_name) .

run-docker:
	docker run --name $(app_name) --detach --network=netApplication -e PROFILE='prod' -e FLASK_RUN_PORT=8081 -p 8081:8081 $(app_name)

kill:
	docker stop $(app_name)
	docker container prune -f
	docker rmi -f $(app_name)