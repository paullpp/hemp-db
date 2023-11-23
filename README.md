# hemp-db

This repository will hosts all code and documentation for the Hemp DB Capstone, CS46X at Oregon State University

## Local Setup

1. Clone repository
2. run docker-compose up
3. Open localhost:8000

## Local Development

1. Checkout new branch
2. Develop Features
3. Test by running docker-compose up

For migrations, run
1. `docker exec -it <container_id> bash`
2. `python manage.py makemigrations`
3. `python manage.py migrate`

4. Open PR when done

Make sure to add any new dependencies to requirements.txt