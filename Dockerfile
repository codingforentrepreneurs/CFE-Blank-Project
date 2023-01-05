FROM python:3.11.1-slim as builder

# copy project
COPY ./src /app
WORKDIR  /app

# Update system environment
ENV PYTHON_VERSION=3.10
ENV DEBIAN_FRONTEND noninteractive
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Update system defaults
RUN apt-get update && \
    apt-get install -y \ 
    locales \
    libmemcached-dev \ 
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    build-essential \
    python3-dev \
    python3-setuptools \
    gcc \
    make && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Update Locales
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && locale-gen &&  dpkg-reconfigure locales


# Install Python deps
RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/python -m pip install pip --upgrade && \
    /opt/venv/bin/python -m pip install -r /app/requirements.txt

# Purge unused
RUN apt-get remove -y --purge make gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Make local files executable
RUN chmod +x config/migrate.sh && \
    chmod +x config/entrypoint.sh

CMD [ "./config/entrypoint.sh" ]