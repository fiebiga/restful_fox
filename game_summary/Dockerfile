FROM python:3.8.3-slim-buster

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /service
WORKDIR /service

EXPOSE 8080

ENTRYPOINT cd service && python ./load_data.py && gunicorn main:app -w 2 --threads 2 -b 0.0.0.0:8080
