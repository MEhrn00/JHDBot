# JHDBot

The bot of John Hammond discord using discord.py

## Setup

1. Clone the repo.
2. Ensure python3.6+ and pip3 are installed.
    ```python
    python --version
    pip3 --version
    ```
3. Install `pipenv` if you don't already have it
    ```python
    pip3 install pipenv
    ```
4. Install project dependencies
    ```python
    pipenv install
    ```
5. Run the virtual env
    ```python
    pipenv shell
    ```
6. Create a `.env` file following the format of `.env_example`
7. Run! `pipenv run python3 bot.py`

## Docker

1. Clone the repo.
2. Ensure docker is installed.
    ```bash
    docker -v
    ```
3. Build the docker image
    ```bash
    docker build -t jhd_bot .
    ```
4. Run the docker image
    ```bash
    docker run -d --rm --name jhd_bot --env-file .env jhd_bot
    ```
