FROM docker.io/python:3.13.1-alpine
WORKDIR /app

COPY ./poetry.lock .

COPY ./pyproject.toml .

RUN pip install poetry==1.8.5

RUN poetry install

COPY . .

CMD ["python", "-m", "poetry", "run", "fastapi", "dev", "./api/main.py", "--port", "8000", "--host", "0.0.0.0", "--reload"]