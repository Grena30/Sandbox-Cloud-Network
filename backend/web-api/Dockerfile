FROM python:latest
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir fastapi uvicorn celery python-dotenv sqlmodel psycopg2-binary
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]