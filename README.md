[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/DESIFpxz)
# CS_2025_project

## Description

Simple Flask server and a client script to check. In future (to next deadline) planning to realize beneficial habit tracker. You can track how many pages have you read in a day or how many days you are not smoking or anything. 

## Setup

To run the project locally:

```
docker compose up --build -d # to launch

docker compose logs backend # to get logs

docker compose run --rm client # to watch check if everything is OK


```

## Requirements

Python 3.11

Flask

requests

Docker & Docker Compose

## Features

Backend: Flask server with at least one route (/)

Client: Python script to test server routes

Deployment: Dockerized setup for CI/CD on GitHub Actions and Railway

## Git

The main branch stores the latest stable version of the application.

## Success Criteria

Backend runs successfully, responds to requests
Client can check if server is OK
on Github Actions it passes test
Railway deployment is accessible on cs-project-2025-matveidetonator-production.up.railway.app
