from flask import Flask, jsonify
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import os
import time

app = Flask(__name__)

# ─── PROMETHEUS METRICS ───────────────────────────────────────────────────────
REQUEST_COUNT = Counter(
    'app_requests_total',
    'Total request count',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'app_request_latency_seconds',
    'Request latency in seconds',
    ['endpoint']
)

@app.route("/")
def home():
    start = time.time()
    response = jsonify({
        "message": "GitOps demo app",
        "version": os.getenv("APP_VERSION", "v1.0.0"),
        "environment": os.getenv("ENVIRONMENT", "dev")
    })
    REQUEST_COUNT.labels(method='GET', endpoint='/', status=200).inc()
    REQUEST_LATENCY.labels(endpoint='/').observe(time.time() - start)
    return response

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)