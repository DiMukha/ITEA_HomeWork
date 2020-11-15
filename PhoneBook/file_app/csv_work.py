import csv

def load():
    try:
        with open(f'data.csv', 'r') as f:
            reader = csv.reader(f)
            data = {rows[0]:rows[1] for rows in reader}
    except FileNotFoundError:
        data = {}
    return data


def save(data):
    with open(f'data.csv', 'w') as f:
        for key in data.keys():
            f.write(f"{key},{data[key]}")
