import configparser
import json
import pickle

from ITEA_HomeWork.PhoneBook.functions import print_start_text

config = configparser.ConfigParser()
config['file'] = {
    'format': 'pickle'
}

with open('config.ini', 'w') as configfile:
    config.write(configfile)

config.read('config.ini')
file_format = config['file']['format']

try:
    with open(f'data.{file_format}', 'rb') as f:
        if file_format == 'json':
            phone_book = json.load(f)
        else:
            phone_book = pickle.load(f)
except FileNotFoundError:
        phone_book = {}


hi_text = "Hi! I`m your PhoneBook\n"
choose_text = """Select option:
'C'-to create
'R'-to read
'U'-to update
'D'-to delete
any key - to exit"""

file_action = {'json': 'w', 'pickle': 'wb'}


def saving_data(data):
    with open(f'data.{file_format}', f'{file_action[file_format]}') as f:
        if file_format == 'json':
            json.dump(data, f)
        else:
            pickle.dump(data, f)


def enter_name():
    return input("Enter Name: ")


def enter_number():
    return input("Enter Number: ")


def name_in_phonebook(f):
    def check(contact_name, contact_number, dct):
        if contact_name in dct:
            yes_no = input(f"Name '{contact_name}' exist in PhoneBook\n\
would you like to change the number?(y/n)\n")
            if yes_no.upper() == 'Y':
                dct[contact_name] = contact_number
                saving_data(dct)
        f(contact_name, contact_number, dct)
    return check


@name_in_phonebook
def create_contact(contact_name, contact_number, dct):
    dct[contact_name] = contact_number
    saving_data(dct)
    print(f"{contact_name} - {contact_number} saved\n")


def read_contact(contact_name, dct):
    print(f"{contact_name}: {dct[contact_name]}\n")


def update_contact(contact_name, dct):
    contact_number = enter_number()
    dct[contact_name] = contact_number
    saving_data(dct)
    print(f"{contact_name} - {contact_number} saved\n")


def delete_contact(contact_name, dct):
    del dct[contact_name]
    saving_data(dct)
    print(f"Name '{contact_name}' deleted\n")


func_dict = {
    'R': read_contact,
    'D': delete_contact,
    'U': update_contact,
}

choose_menu = f'{hi_text}{choose_text}'

while True:
    menu = print_start_text(choose_menu)
    choose_menu = choose_text

    if menu not in ['C', 'R', 'U', 'D']:
        break

    name = enter_name()
    if menu == 'C':
        number = enter_number()
        create_contact(name, number, phone_book)
        continue
    try:
        func_dict.get(menu)(name, phone_book)
    except KeyError:
        print(f"Name '{name}' not found\n")
