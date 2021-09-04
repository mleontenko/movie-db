FROM python:3.9.6

WORKDIR /code

RUN pip install requests && pip install psycopg2 && pip install nltk

# Copy project
COPY . /code/