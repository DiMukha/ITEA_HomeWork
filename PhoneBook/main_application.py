from ITEA_HomeWork.PhoneBook.settings import load, save
from ITEA_HomeWork.PhoneBook.phone_book import PhoneBook
from ITEA_HomeWork.PhoneBook.interface_collection import PhoneBookDictionary

data = PhoneBookDictionary(load())

phone_book = PhoneBook(data)

choose_menu = f'{phone_book.GREETINGS}{phone_book.MENU}'

while True:
    menu = phone_book.input_option(choose_menu)
    choose_menu = phone_book.MENU

    if menu not in phone_book.ACTIONS:
        save(phone_book.data)
        break
    try:
        phone_book.get_action(menu)
    except KeyError:
        phone_book.output_message(phone_book.NOT_FOUND)
