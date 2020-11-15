import csv

class SerializerSCV:
    def __init__(self, data):
        self.data = data

    def load(self):
        try:
            with open(f'data.csv', 'r') as f:
                reader = csv.reader(f)
                data = {rows[0]: rows[1] for rows in reader}
        except FileNotFoundError:
            data = {}
        return data

    def save(self):
        with open(f'data.csv', 'w') as f:
            for key in self.data.keys():
                f.write(f"{key},{self.data[key]}")