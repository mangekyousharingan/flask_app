.PHONY:
	test

deps:
	pip install -r requirements.txt;
	pip install -r test_requirements.txt

lint:
	flake8 hello_world test

run:
	python main.py

test:
	python -m pytest

docker_build:
	docker build -t hello-world-printer .

docker_run:
	sudo docker run --name flask_app -p 5000:5000 -d hello-world-printer
