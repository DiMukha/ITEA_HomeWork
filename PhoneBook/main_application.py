from ITEA_HomeWork.PhoneBook.settings import load, save
from ITEA_HomeWork.PhoneBook.phone_book import PhoneBook

phone_book = PhoneBook(load())

functions = {
    'C': phone_book.create,
    'R': phone_book.read,
    'U': phone_book.update,
    'D': phone_book.delete,
}

choose_menu = f'{phone_book.GREETINGS}{phone_book.OPTIONS}'

while True:
    menu = phone_book.input_option(choose_menu)
    choose_menu = phone_book.OPTIONS

    if menu not in ['C', 'R', 'U', 'D']:
        save(phone_book.data)
        break
    try:
        functions.get(menu)()
    except KeyError:
        phone_book.output_message(phone_book.NOT_FOUND)
