FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN pip install prometheus-client

CMD ["python", "app/main.py"]

HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1

