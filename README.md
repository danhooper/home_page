# Home Page

[![Build Status](https://travis-ci.org/danhooper/home_page.svg?branch=master)](https://travis-ci.org/danhooper/home_page)

## Configuring

Create a file named `application.yml` in the `config/` directory.

A sample configuration file is in `config/sample-application.yml`. For now the ID must be unique.

## Running Production

`docker-compose up -d`

## Developing

### Using Docker

`docker-compose -f dev.docker-compose.yml up --build`

### Frontend

`ng serve`

### Backend

`./gradle build --continuous`
`./gradlew bootRun`

#### Swagger JSON

`/v2/api-docs`

## TODOs

- Generate feed IDs
- Hook up to DB
- CRUD for RSS feeds
- Versioning
