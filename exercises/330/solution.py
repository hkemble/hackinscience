import json


def load_json(path):
    json_data = open(path)
    data = json.load(json_data)
    decoded = json.JSONDecoder(data)
    return decoded
