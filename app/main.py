import logging

logging.basicConfig(level=logging.INFO)
from prometheus_client import start_http_server, Counter

REQUEST_COUNT = Counter('requests_total', 'Total requests')
@app.get("/")
def home():
    logging.info("Home endpoint hit")
    return {"message": "Running"}
    
@app.get("/health")
def health():
    return {"status": "ok"}
    
@app.get("/")
def home():
    REQUEST_COUNT.inc()
    return {"message": "Running"}
