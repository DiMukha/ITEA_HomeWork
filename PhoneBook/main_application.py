from ITEA_HomeWork.PhoneBook.file_app import config
from ITEA_HomeWork.PhoneBook.functions import print_start_text, enter_phone, enter_name, enter_email, PhoneBook
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

phone_book = PhoneBook(load())

functions = {
    'R': phone_book.read,
    'D': phone_book.delete,
    'U': phone_book.update,
}

choose_menu = f'{GREETINGS}{OPTIONS}'

while True:
    menu = print_start_text(choose_menu)
    choose_menu = OPTIONS

    if menu not in ['C', 'R', 'U', 'D']:
        save(phone_book.data)
        break

    name = enter_name()
    if menu == 'C':
        phone = enter_phone()
        email = enter_email()
        phone_book.create(name, phone=phone, email=email)
        continue
    try:
        functions.get(menu)(name)
    except KeyError:
        print(f"Name '{name}' not found\n")
