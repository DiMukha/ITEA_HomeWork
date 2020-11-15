from ITEA_HomeWork.PhoneBook.file_app import config
from ITEA_HomeWork.PhoneBook.functions import print_start_text, enter_number, enter_name, read_contact,\
    delete_contact, update_contact, create_contact
from ITEA_HomeWork.PhoneBook.messages import GREETINGS, OPTIONS


config.create_config(format='csv')
file_format = config.read_config()

if file_format == 'json':
    from ITEA_HomeWork.PhoneBook.file_app import json_work as file_work
elif file_format == 'pickle':
    from ITEA_HomeWork.PhoneBook.file_app import pickle_work as file_work
elif file_format == 'csv':
    from ITEA_HomeWork.PhoneBook.file_app import csv_work as file_work

load, save = file_work.load, file_work.save

phone_book = load()

functions = {
    'R': read_contact,
    'D': delete_contact,
    'U': update_contact,
}

choose_menu = f'{GREETINGS}{OPTIONS}'

while True:
    menu = print_start_text(choose_menu)
    choose_menu = OPTIONS

    if menu not in ['C', 'R', 'U', 'D']:
        save(phone_book)
        break

    name = enter_name()
    if menu == 'C':
        number = enter_number()
        create_contact(name, number, phone_book)
        continue
    try:
        functions.get(menu)(name, phone_book)
    except KeyError:
        print(f"Name '{name}' not found\n")
