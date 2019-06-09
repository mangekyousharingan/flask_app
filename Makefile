SERVICE_NAME=hello-world-printer
MY_DOCKER_NAME=$(SERVICE_NAME)
USERNAME=mangekyou
TAG=$(USERNAME)/$(MY_DOCKER_NAME)

.PHONY:
	test
.DEFAULT_GOAL := test

deps:
	pip install -r web/requirements.txt;
	pip install -r web/test_requirements.txt

lint:
	flake8 hello_world test

run:
	python web/main.py

test:
	python -m pytest

docker_build:
	docker-compose build

docker_run:
	sudo docker run --name flask_app -p 5000:5000 -d $(MY_DOCKER_NAME)

docker_push: docker_build
	@docker login --username $(USERNAME) --password $${DOCKER_PASSWORD};
	docker tag $(MY_DOCKER_NAME) $(TAG);
	docker push $(TAG);
	docker logout;

test_smoke:
	curl --fail 127.0.0.1:5000
