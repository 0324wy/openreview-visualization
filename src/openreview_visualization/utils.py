import orjson
import json


def save_json(data, filename):
    with open(filename, "wb") as f:
        f.write(orjson.dumps(data))


def save_jsonl(data, filename):
    with open(filename, "w") as f:
        for item in data:
            f.write(orjson.dumps(item) + "\n")

def open_json(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data