#!/bin/bash

# navigate to the docker-created 
# django project root directory
cd /app/

# migrate a docker container as needed
/opt/venv/bin/python manage.py migrate