FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN pip install prometheus-client

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1

