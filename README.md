# FastAPI Chat Microservice

## Install Poetry

`curl -sSL https://install.python-poetry.org | python3 -`

## Install project dependencies

`poetry install`

## Start the dev server with hot reloading in the poetry virtual env

`poetry run uvicorn app.main:app --reload`

The app should now be running at `localhost:8000`

## View documentation

Documentation should be visible at `localhost:8000/docs`

## Build the docker image

`docker build -t myimage .`

## Run the docker image

`docker run -d --name mycontainer -p 80:80 myimage`

