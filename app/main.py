from flask import Flask, jsonify
import os
import sys

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "GitOps demo app",
        "version": os.getenv("APP_VERSION", "v1.0.0"),
        "environment": os.getenv("ENVIRONMENT", "dev")
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    print("App starting...", flush=True)
    sys.exit(1)       # ← This causes the container to crash immediately on startup