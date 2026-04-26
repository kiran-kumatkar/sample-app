from flask import Flask, jsonify
import os

app = Flask(__name__)
VERSION = os.getenv("APP_VERSION", "v1.0.0")

@app.route("/")
def home():
    return jsonify({"message": "GitOps demo", "version": VERSION , "env": "staging"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)