class InputOutput:
    GREETINGS = "Hi! I`m your PhoneBook\n"
    OPTIONS = """Select option:
'C'-to create
'R'-to read
'U'-to update
'D'-to delete
any key - to exit"""
    EXIST_IN_PHONEBOOK = f"This name exist in PhoneBook\n\
would you like to change the number?\n"
    SAVE = "Contact saved\n"
    DELETE = "Contact deleted\n"
    NOT_FOUND = f"Name not found\n"

    def output_message(self, message):
        print(message)

    def input_option(self, *messages):
        for message in messages:
            print(message)
        return input().upper()

    def input_item(self, item):
        return input(f"Enter {item}: ")
