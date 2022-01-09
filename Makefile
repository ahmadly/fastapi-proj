docker: docker.down docker.up docker.log

.ONESHELL:
docker.up:
	docker-compose up -d

.ONESHELL:
docker.log:
	docker-compose logs  --follow

.ONESHELL:
docker.stop:
	docker-compose stop

.ONESHELL:
docker.down:
	docker-compose down --remove-orphans --rmi local --volumes

.ONESHELL:
flake8:
	flake8 --max-line-length=119 --exclude=*/migrations/* src | nl

.ONESHELL:
isort:
	./venv/bin/isort --use-parentheses --atomic src/

.ONESHELL:
black:
	python -m black --safe --skip-string-normalization src/
