FROM python:alpine3.17

WORKDIR /chatapp

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY source dest