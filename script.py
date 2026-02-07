from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__, static_folder=".")
CORS(app)


# Page principale
@app.route("/")
def index():
    return send_from_directory(".", "login.html")


@app.route("/login.html")
def login():
    return send_from_directory(".", "login.html")


@app.route("/success.html")
def success():
    return send_from_directory(".", "success.html")


# Endpoint formulaire
@app.route("/auth", methods=["POST"])
def auth():

    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "no data"}), 400

    name = data.get("name", "")
    message = data.get("message", "")

    line = f"{datetime.now().isoformat()} | {name} | {message}\n"

    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(line)

    print(line.strip(), flush=True)

    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
