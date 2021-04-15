import requests
import json
import numpy as np

URL = "http://app-A:5000/identity"

def main():
    data = np.genfromtxt("./data/data.csv", delimiter=",")

    for row in data:

        _a = int(row[0])
        _b = int(row[1])

        _params = {
            "aSize": _a,
            "bSize": _b
        }

        response = requests.post(URL, params=params)

        _c = response.json["response"]

        c = np.array(_c).reshape((_a, _b)) * 5.0

        print(f"Response: {c}")



if __name__ == "__main__":

