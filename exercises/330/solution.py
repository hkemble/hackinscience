import json


def load_json(path):
    with open(path) as json_data:
        data = json.load(json_data)
    return data
