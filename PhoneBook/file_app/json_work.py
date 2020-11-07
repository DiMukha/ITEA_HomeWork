import json


def load_json():
    try:
        with open(f'data.json', 'rt') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    return data


def save_json(data):
    with open(f'data.json', 'wt') as f:
        json.dump(data, f)
