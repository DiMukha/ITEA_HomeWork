class PhoneBook:
    attributes = ['name', 'phone', 'email']

    def __init__(self, data):
        self.data = data

    def create(self, name, **attributes):
        self.data[name] = {key: value for key, value in attributes.items()}
        print(f"{name} saved\n")

    def read(self, name):
        print(f"{name}:")
        for attribute in self.data[name]:
            print(f"\t{attribute} - {self.data[name][attribute]}")
        print("\n")

    def update(self, name):
        phone = enter_phone()
        email = enter_email()
        self.data[name]['phone'] = phone
        self.data[name]['email'] = email
        print(f"{name} saved\n")

    def delete(self, name):
        del self.data[name]
        print(f"Name '{name}' deleted\n")



def print_start_text(*messages):
    for message in messages:
        print(message)
    return input().upper()


def enter_name():
    return input("Enter Name: ")


def enter_phone():
    return input("Enter Number: ")


def enter_email():
    return input("Enter e-Mail: ")


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
