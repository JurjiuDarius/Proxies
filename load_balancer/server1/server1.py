from flask import Flask
import json

app1 = Flask(__name__)


@app1.route("/")
def get_method():
    return "Responding from server 1"


if __name__ == "__main__":
    app1.run(debug=True, host="0.0.0.0", port=5001)
