FROM python:3.12-slim-bookworm

ENV PATH="/root/.local/bin:$PATH"

ENV YOUR_ENV=${YOUR_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # Poetry's configuration:
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=true \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local' \
  POETRY_VERSION=1.7.1

RUN apt-get update && apt-get install -y curl && apt-get clean

RUN curl -sSL https://install.python-poetry.org | python3 -

RUN #export PATH="/root/.local/bin:$PATH"

WORKDIR /mistapp

COPY . /mistapp/

RUN poetry install

CMD ["poetry","run", "uvicorn", "--host", "0.0.0.0", "--port", "8080", "mistapp.main:app", "--reload"]

EXPOSE 8080