# FastAPI and MySql - Base Project Generator

![Python版本](https://img.shields.io/badge/Python-3.7+-brightgreen.svg "版本号")
![FastAPI版本](https://img.shields.io/badge/FastAPI-0.61.1-ff69b4.svg "版本号")

[中文说明](./README.md) | [English](./README-en.md)

## Intro
Web application generator. Using FastAPI, MySql as databas.I am referring to tianolo's full-stack-fastapi-postgresql

https://github.com/tiangolo/full-stack-fastapi-postgresql

I changed it to my favorite format.

![demo](images/demo1.png)


## Features
- JWT token authentication.
- SQLAlchemy models(MySql).
- Alembic migrations.
- Use redis demo.
- File upload demo.
- apscheduler cron task (:noqa)


## How to use it

Go to the directory where you want to create your project and run:

```
pip install cookiecutter
cookiecutter https://github.com/CoderCharm/fastapi-mysql-generator

cd your_project/
pip install -r requirements.txt
```

## Configure your database

In the `project/app/core/config/development_config.py` or `production_config.py` file.

MySql and Redis config info

## Migrate the database

```
cd your_project/

# Generate mapping
alembic revision --autogenerate -m "init commit"

# Generate tables
alembic upgrade head
```

## Create admin user

```
cd your_project/app
python create_user.py
```

## Run
```
cd your_project/app

python main.py

or 

uvicorn main:app --host=127.0.0.1 --port=8010 --reload
```

online doc address
```
http://127.0.0.1:8010/api/docs
```