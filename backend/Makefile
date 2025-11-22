.PHONY: build up down logs test lint format migrate load-data

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

test:
	docker-compose exec backend pytest

lint:
	ruff check .
	black --check .

format:
	black .
	ruff check . --fix

migrate:
	docker-compose exec backend python manage.py migrate

make-migrations:
	docker-compose exec backend python manage.py makemigrations