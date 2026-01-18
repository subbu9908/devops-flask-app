from flask import Flask, jsonify
import os

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

@app.route("/")
def home():
    return jsonify({
        "message": "DevOps CI/CD Demo Application",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "UP"}), 200

@app.route("/version")
def version():
    return jsonify({"version": APP_VERSION})

@app.route("/fail")
def fail():
    raise Exception("Simulated application failure")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
