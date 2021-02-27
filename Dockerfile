FROM python:3.7-alpine

WORKDIR /work

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY config config
COPY app app

CMD ["python", "app/app.py"]