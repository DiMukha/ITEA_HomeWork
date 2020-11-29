from PhoneBook.settings import load, save
from PhoneBook.phone_book import PhoneBook
from PhoneBook.interface_collection import PhoneBookDictionary
import argparse


data = PhoneBookDictionary(load())

phone_book = PhoneBook(data)

parser = argparse.ArgumentParser(description="Work with PhoneBook")
parser.add_argument('-c', action='store', dest='contact', nargs='+',
                    help='Create contact')
args = parser.parse_args()
name, phone, email = args.contact
print(name, phone, email)