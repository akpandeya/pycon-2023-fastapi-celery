FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11 as base

WORKDIR /app/
ENV PYTHONFAULTHANDLER=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.4.1 \
    PYTHONPATH="/app:/app/src"


RUN pip install poetry && \
    poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* /app/

COPY ./src ./src
COPY worker-start.sh /worker-start.sh
RUN chmod +x /worker-start.sh


FROM base as dev
COPY ./tests ./tests



RUN poetry install --no-interaction --no-ansi

FROM base as prod
RUN poetry install --no-interaction --no-ansi --no-dev
