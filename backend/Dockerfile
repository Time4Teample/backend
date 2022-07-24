FROM python:3.8.3-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /backend
COPY requirements.txt /backend/

RUN apk update
RUN apk add build-base

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /backend/