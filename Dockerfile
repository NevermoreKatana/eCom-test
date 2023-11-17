FROM python:3.11.0-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3-pip

RUN pip install poetry

WORKDIR /app
COPY . /app

RUN poetry install
CMD ["poetry", "run", "python", "api/bd.py"]
