# Machine Learning Model Server

This repository provides an example implementation of a machine learning model server using FastAPI and PostgreSQL.
It allows you to deploy machine learning models as RESTful APIs, providing predictions and storing model data in a PostgreSQL database.

## Features

- Serve machine learning models as RESTful APIs using FastAPI.
- Store model data in a PostgreSQL database for persistence.
- Secure the APIs using API key authentication.
- Containerize the application using Docker for easy deployment.

## Prerequisites

- Python 3.10 or later
- PostgreSQL 9.5 or later
- Docker
- poetry (optional)

## Deployment with Docker compose

```shell
   docker-compose up --build
```

## Load Database with dummy data and models

1. Install Dependencies

```shell
poetry install
poetry shell
```

or

```shell
pip install -r requirements.txt
```

2. Load database

```shell
python load_db.py
```

## Got to FastAPI

1. Navigate to `localhost:8000\docs`
