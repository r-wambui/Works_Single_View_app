build:
	docker-compose build

migrate:
	docker-compose run web python manage.py migrate

seed:
	docker-compose run web python manage.py music_works

start:
	docker-compose up --remove-orphans web

down:
	docker-compose down -v

makemigrations:
	docker-compose run web python manage.py makemigrations
