import csv
from ITEA_HomeWork.PhoneBook.functions import PhoneBook


def load():
    attributes = PhoneBook.FIELDS
    data = {}
    try:
        with open(f'data.csv', 'r') as f:
            reader = csv.reader(f)
            for rows in reader:
                name_attribute = {attributes[i+1]: rows[i+1] for i in range(len(attributes[1:]))}
                data[rows[0]] = name_attribute
    except FileNotFoundError:
        data = {}
    return data


def save(data):
    with open(f'data.csv', 'w') as f:
        for key, value in data.items():
            f.write(f"{key},{','.join(value.values())}\n")
