from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/api/test")
def test():
    return jsonify(dict(message="hello"))


if __name__ == "__main__":
    app.run(debug=True)
