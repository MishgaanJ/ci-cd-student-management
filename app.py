from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():  # <-- Missing colon added
    return jsonify({"status": "ok"})  # <-- Fixed dictionary syntax

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
