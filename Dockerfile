FROM python:3.9

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./project ./project
COPY ./tests ./tests
COPY create_tables.py .
RUN python create_tables.py
COPY fixtures.json .
COPY load_fixtures.py .
RUN python load_fixtures.py

COPY run.py .
#COPY volumes/project.db .

CMD flask run -h 0.0.0.0 -p 80