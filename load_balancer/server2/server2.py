from flask import Flask
import json

app2 = Flask(__name__)


@app2.route("/")
def get_method():
    return "Responding from server 2"


if __name__ == "__main__":
    app2.run(debug=True, host="0.0.0.0", port=5002)
