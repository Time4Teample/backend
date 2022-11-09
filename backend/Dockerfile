FROM alpine:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /backend
COPY requirements.txt /backend/

RUN apk update
RUN apk add build-base
RUN apk add libressl-dev libffi-dev musl-dev gcc python3-dev py3-pip zlib-dev mongodb mongodb-tools

RUN mongo --version
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /backend/
