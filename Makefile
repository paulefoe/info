PROJECT_NAME=info

# Common

all: run

run:
	@docker-compose up

stop:
	@docker-compose stop

down:
	@docker-compose down

migrations:
	@docker exec -it info alembic -n alembic:dev revision --autogenerate;

migrate:
	@docker exec -it info alembic -n alembic:dev upgrade head;

psql:
	@docker exec -it info_postgres psql -U postgres
