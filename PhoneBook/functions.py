def print_start_text(*messages):
    for message in messages:
        print(message)
    return input().upper()


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
        f(contact_name, contact_number, dct)
    return check


@name_in_phonebook
def create_contact(contact_name, contact_number, dct):
    dct[contact_name] = contact_number
    print(f"{contact_name} - {contact_number} saved\n")


def read_contact(contact_name, dct):
    print(f"{contact_name}: {dct[contact_name]}\n")


def update_contact(contact_name, dct):
    contact_number = enter_number()
    dct[contact_name] = contact_number
    print(f"{contact_name} - {contact_number} saved\n")


def delete_contact(contact_name, dct):
    del dct[contact_name]
    print(f"Name '{contact_name}' deleted\n")
