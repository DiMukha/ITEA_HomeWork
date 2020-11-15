class PhoneBook:

    def __init__(self, data):
        self.data = data

    def read(self, name):
        print(f"{name}: {self.data[name]}\n")

    def update(self, name):
        number = input("Enter Name: ")
        self.data[name] = number
        print(f"{name} - {number} saved\n")

    def delete(self, name):
        del self.data[name]
        print(f"Name '{name}' deleted\n")

    def create(self, name, number):
        self.data[name] = number
        print(f"{name} - {number} saved\n")


def print_start_text(*messages):
    for message in messages:
        print(message)
    return input().upper()


def enter_name():
    return input("Enter Name: ")


def enter_number():
    return input("Enter Number: ")


# def name_in_phonebook(f):
#     def check(name, number, dct):
#         if name in dct:
#             yes_no = input(f"Name '{name}' exist in PhoneBook\n\
# would you like to change the number?(y/n)\n")
#             if yes_no.upper() == 'Y':
#                 dct[name] = number
#             else:
#                 return
#         f(name, number, dct)
#     return check


# @name_in_phonebook
# def create_contact(name, number, dct):
#     dct[name] = number
#     print(f"{name} - {number} saved\n")
