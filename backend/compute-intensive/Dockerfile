FROM python:latest
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["celery", "-A", "main.app", "worker", "--loglevel=info"]