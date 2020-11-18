from ITEA_HomeWork.PhoneBook.comunication import InputOutput

class PhoneBook(InputOutput):
    CONTACT_NAME = 'name'
    FIELDS = ['phone', 'email']

    def __init__(self, data):
        self.data = data

    def create(self):
        name = self.input_item(self.CONTACT_NAME)
        if name in self.data:
            self.output_message(self.EXIST_IN_PHONEBOOK)
            yes_no = self.input_item('Y/N')
            if yes_no.upper() == 'N':
                return
        self.data[name] = {field: self.input_item(field) for field in self.FIELDS}
        self.output_message(self.SAVE)

    def read(self):
        name = self.input_item(self.CONTACT_NAME)
        for field in self.data[name]:
            self.output_message(f"\t{field} - {self.data[name][field]}")

    def update(self):
        name = self.input_item(self.CONTACT_NAME)
        self.data[name] = {field: self.input_item(field) for field in self.FIELDS}
        self.output_message(self.SAVE)

    def delete(self):
        name = self.input_item(self.CONTACT_NAME)
        del self.data[name]
        self.output_message(self.DELETE)
