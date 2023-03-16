FROM python:3.10

WORKDIR /chatapp

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python3", "chatapp.py" ]
