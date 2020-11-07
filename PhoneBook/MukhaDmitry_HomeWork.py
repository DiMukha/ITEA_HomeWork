from ITEA_HomeWork.PhoneBook.file_app import config, json_work, pickle_work
from ITEA_HomeWork.PhoneBook.functions import print_start_text, enter_number, enter_name, read_contact, delete_contact, \
    update_contact, create_contact

config.create_config(format='pickle')
file_format = config.read_config()

if file_format == 'json':
    load, save = json_work.load_json, json_work.save_json
elif file_format == 'pickle':
    load, save = pickle_work.load_pickle, pickle_work.save_pickle

phone_book = load()

hi_text = "Hi! I`m your PhoneBook\n"
choose_text = """Select option:
'C'-to create
'R'-to read
'U'-to update
'D'-to delete
any key - to exit"""

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
        save(phone_book)
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
