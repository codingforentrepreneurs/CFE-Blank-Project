[![Create a Blank Django Project Logo](https://cfe2-static.s3-us-west-2.amazonaws.com/media/cfe-blog/create-a-blank-django-project/BlankDjangoProject.jpg)](https://www.codingforentrepreneurs.com/blog/create-a-blank-django-project/)

# CFE Blank Project

This is a blank Django project that can be used as a starting point for any Django project. It includes related Docker and Docker Compose configuration for local development with Postgres and Redis.

We'll continue to refine this project based on requests from people like you. If you have any suggestions or want to submit ideas, please do so on [github discussions](https://github.com/codingforentrepreneurs/CFE-Blank-Project/discussions).

_Reference blog post coming soon_.

## Get Started


### Clone project
```
mkdir -p ~/Dev/your-project
cd ~/Dev/your-project
git clone https://github.com/codingforentrepreneurs/CFE-Blank-Project .
```

### Create a Python Virtual Environment
Using Python 3.11, create a virtual environment using the built-in `venv` module:

_macOS/Linux_:
```
python3.11 -m venv venv
source venv/bin/activate
$(venv) python --version
```

_Windows_:
```
c:\>Python311\python -m venv venv
.\venv\Scripts\activate
(venv) > python --version
```
If you're on Windows, consider install Python using [this guide](https://www.codingforentrepreneurs.com/guides/install-python-on-windows/) or [this blog post](https://www.codingforentrepreneurs.com/blog/install-python-django-on-windows/).


### Install requirements
```
$(venv) python -m pip install -r src/requirements.txt
```


### Configure Environment Variables

In `src/.env` add:
```
DJANGO_DEBUG=True
DJANGO_SECRET_KEY=your-secret-key
ALLOWED_HOSTS=.codingforentrepreneurs.com,.cfe.sh,localhost,127.0.0.1
```

You can generate a Django Secret Key with ([reference post](https://www.codingforentrepreneurs.com/blog/create-a-one-off-django-secret-key/)) the following:

```bash
$(venv) python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### Various Django Commands

Below are a few commands that will work for this configuration both before and after using the database configuration and the _docker-compose_-based configuration below.
```
$(venv) python manage.py makemigrations
$(venv) python manage.py migrate
$(venv) python manage.py createsuperuser
```


### Configuring for Postgres Database

In `src/cfehome/db.py` you will see a Postgres database configuration based on available environment variables. Do _not_ change the variable names _without_ changing several other configurations (at least `src/cfehome/db.py`, `docker-compose.yaml`).

Update `.env` or your environment variables to include the following configuration
```
POSTGRES_USER=...
POSTGRES_PASSWORD=...
POSTGRES_DB=...
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```
You can also set `POSTGRES_DB_REQUIRE_SSL=True` if you want to require SSL connections to the database.


### Using Docker Compose for Postgres and Redis
Assuming you have the POSTGRES environment variables set, you can use Docker Compose to create development Postgres database for your project. 

To start the Postgres database and Redis, run:
```
docker compose -f docker-compose.dev.yaml up -d
```
This sets our Postgres database to be available at `localhost:5432` and Redis at `localhost:6379`.

To stop and remove your Postgres database and Redis, run:
```
docker compose -f docker-compose.dev.yaml down
```
Use `docker compose -f docker-compose.dev.yaml down -v` to remove the volumes as well.

_If you need to learn about how to use Docker & Docker Compose, consider [this course](https://www.codingforentrepreneurs.com/courses/docker-and-docker-compose/)._


### Docker Image for Django Local Development

To build the Docker image, run:
```
docker build -t cfe-blank-project .
```

Update `POSTGRES_HOST` in `.env` to use `host.docker.internal` if you are using the local `docker-compose` Postgres database.

To run the Docker image locally, run:
```
docker run --network cfe_blank_network -p 8000:8000 -e  -e PORT=8000 --env-file src/.env cfe-blank-project --name cfe-blank-project 
```

To stop the Docker container, run:
```
docker stop cfe-blank-project
```
In this case `cfe-blank-project` is the name of the container we set in the previous command with `--name cfe-blank-project`.



### Production Configuration
Would you like this project to be augmented for a minimal production environment as well? If so, please start a [discussion](https://github.com/codingforentrepreneurs/CFE-Blank-Project/discussions) requesting so.
