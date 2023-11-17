install:
	poetry install
docker-mdb:
	docker-compose up -d
start-server:
	poetry run flask --app api --debug run --port 8000
test:
	poetry run pytest api/test.py



