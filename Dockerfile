FROM python:3.9.2-slim-buster
RUN apt update && apt install -y sqlite3 gcc libpq-dev
RUN pip install flask flask-sqlalchemy psycopg2-binary psycopg2
WORKDIR /app
ADD src/app.py /app
CMD ["python", "app.py"]