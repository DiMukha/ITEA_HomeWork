import csv
from ITEA_HomeWork.PhoneBook.phone_book import PhoneBook


def load():
    fields = PhoneBook.FIELDS
    data = {}
    try:
        with open(f'data.csv', 'r') as f:
            reader = csv.reader(f)
            for rows in reader:
                data[rows[0]] = {fields[r]: rows[r+1] for r in range(len(fields))}
    except FileNotFoundError:
        return data
    return data


def save(data):
    with open(f'data.csv', 'w') as f:
        for key, value in data.items():
            f.write(f"{key},{','.join(value.values())}\n")
