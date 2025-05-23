# An Introduction to NLP in Python
<!-- An Easy Way To Unlocking Language Using Code -->

[![NLP-CI](https://github.com/a-mhamdi/nlp/actions/workflows/nlp.yml/badge.svg)](https://github.com/a-mhamdi/nlp/actions/workflows/nlp.yml)
[![Docker Version](https://img.shields.io/docker/v/abmhamdi/nlp?sort=semver)](https://hub.docker.com/r/abmhamdi/nlp)

This repository contains slides and code samples for using `Python` to implement some **NLP** related tasks. 

## Included Topics
The repository includes the implementation of the following parts:
>1. Regular Expressions (RegEx)
>1. Text Tokenization
>1. Text Processing and Visualization
>1. Gensim Text Processing
>1. Named Entity Recognition (NER)

## Prerequisites

> [!NOTE]
> You can either follow the steps below for local installation or use the provided Docker image for a containerized environment.

## Installation Steps
These commands will set up an isolated environment and install all required packages for this project.
```zsh
uv venv # creates a virtual environment: `.venv`
uv sync # installs all dependencies
```
## Docker Setup
Codes run on top of a `Docker` image, ensuring a consistent and reproducible environment. 

> [!IMPORTANT]
>
> You will need to have `Docker` installed on your machine. You can download it from the [Docker website](https://hub.docker.com).

To run the code, you will need to first pull the `Docker` image by running the following command:

```zsh
docker pull abmhamdi/nlp
```

This may take a while, as it will download and install all necessary dependencies.

## How to control the containers:

* ```docker-compose up -d``` starts the container in detached mode
* ```docker-compose down``` stops and destroys the container

Services can be run by typing the command `docker-compose up`. This will start the `Jupyter Lab` on [http://localhost:2468](http://localhost:2468), and you should be able to use `Python` from within the notebook by starting a new `Python` notebook. You can parallelly start `Marimo` on [http://localhost:1357](http://localhost:1357).

## License
This project is licensed under the MIT License - see the [LICENSE](https://raw.githubusercontent.com/a-mhamdi/nlp/refs/heads/main/LICENSE) file for details.
