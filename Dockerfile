FROM python:3.10.2 as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.10.2

WORKDIR /begemotic

COPY --from=requirements-stage /tmp/requirements.txt /begemotic/requirements.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /begemotic/requirements.txt

COPY . .
