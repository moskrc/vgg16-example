FROM python:3.8-slim

RUN apt-get update

WORKDIR /app
COPY requirements.txt .

RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

COPY ./backend /app/backend
COPY ./docker /app/docker

RUN mkdir -p /app/backend/server/static
