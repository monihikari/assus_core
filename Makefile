.PHONY: docs fixtures
.PHONY: docs fixtures
.SILENT: clean
.PRECIOUS: lint

COMPOSE := docker-compose -f local.yml

ARG=


build:
	$(COMPOSE) build
	@echo "Building..."

up:
	@echo "Server up..."
	$(COMPOSE) up

run:
	$(COMPOSE) run --rm django $(ARG)

command:
	$(COMPOSE) run --rm django python manage.py $(ARG)

debug:
	@echo "Launchings Server for debbugging..."
	$(COMPOSE) run --service-ports django

loaddata:
	@echo "Loading fixtures..."
	$(COMPOSE) run --rm django python manage.py loaddata $(ARG)

fixtures:
	@echo "Loading fixtures..."
	$(COMPOSE) run --rm django python manage.py loaddata phone_numbers users tenants tenant_users tenant_classes class_teachers class_schedules class_payment_plans class_students

dumpdata:
	@echo "Getting fixtures..."
	$(COMPOSE) run --rm django python manage.py dumpdata $(ARG)

superuser:
	@echo "Creating superuser..."
	$(COMPOSE) run --rm django python manage.py createsuperuser

migrate:
	@echo "Applying migrations ..."
	$(COMPOSE) run --rm django python manage.py migrate $(ARG)

migrations:
	@echo "Creating migrations ..."
	$(COMPOSE) run --rm django python manage.py makemigrations $(ARG)

squashmigrations:
	@echo "Creating migrations ..."
	$(COMPOSE) run --rm django python manage.py squashmigrations $(APP)

settings:
	@echo "Opening django compiled settings ..."
	$(COMPOSE) run --rm django python manage.py diffsettings

flushdb:
	@echo "Flushing database ..."
	$(COMPOSE) run --rm django python manage.py flush

# Window version: docker ps -aq |  %{docker stop $_}
clean:
	@echo "Cleaning containers ..."
	docker ps -aq | xargs docker stop
	docker ps -aq | xargs docker rm

clean_volumes:
	@echo "Cleaning volumes ..."
	docker volume ls -q | grep assus | xargs docker volume rm
	docker images | grep "^<none>" | awk '{print $3}' | xargs docker rmi

shell:
	@echo "Opening django shell for testing and debbugging"
	$(COMPOSE) run --rm django python manage.py shell

terminal:
	@echo "Opening container bash session"
	$(COMPOSE) run --rm django bash

dbshell:
	@echo "Opening database shell"
	$(COMPOSE) run --rm django python manage.py dbshell

stop:
	@echo "Stopping containers"
	docker ps -qa | xargs docker stop

restart: stop up
	@echo "Containers restarted"
