from flask import Flask, request
import json
import numpy as np
from datetime import date

server = Flask(__name__)

@server.route("/")
def hello():
    return "Hello World"

@server.route("/identity")
def identity():
    a = int(request.args.get("aSize", 2))
    b = int(request.args.get("bSize", 2))

    c = np.eye(a, b, dtype=int)

    response = json.dumps(
        {
        "response": c.tolist()
        }
    )

    with open(f"./logs/{date.today().isoformat("T", "seconds")}", "wb") as f:
        f.write(response)

    return response

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000)