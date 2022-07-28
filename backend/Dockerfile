FROM python:3.8.3-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /backend
COPY requirements.txt /backend/

RUN echo 'http://dl-cdn.alpinelinux.org/alpine/v3.6/main' >> /etc/apk/repositories
RUN echo 'http://dl-cdn.alpinelinux.org/alpine/v3.6/community' >> /etc/apk/repositories
RUN apk update
RUN apk add build-base
RUN apk add libressl-dev libffi-dev musl-dev gcc python3-dev zlib-dev mongodb mongodb-tools

RUN mongo --version
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /backend/
