def print_start_text(*messages):
    for message in messages:
        print(message)
    return input().upper()


def enter_name():
    return input("Enter Name: ")


def enter_number():
    return input("Enter Number: ")


def name_in_phonebook(f):
    def check(name, number, dct):
        if name in dct:
            yes_no = input(f"Name '{name}' exist in PhoneBook\n\
would you like to change the number?(y/n)\n")
            if yes_no.upper() == 'Y':
                dct[name] = number
        f(name, number, dct)
    return check


@name_in_phonebook
def create_contact(name, number, dct):
    dct[name] = number
    print(f"{name} - {number} saved\n")


def read_contact(name, dct):
    print(f"{name}: {dct[name]}\n")


def update_contact(name, dct):
    number = enter_number()
    dct[name] = number
    print(f"{name} - {number} saved\n")


def delete_contact(name, dct):
    del dct[name]
    print(f"Name '{name}' deleted\n")
