from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError('Invalid phone number')
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        return phone

    def remove_phone(self, phone: str):
        for i in self.phones:
            if i.value == phone:
                return self.phones.remove(i)

    def edit_phone(self, phone: str, new_phone: str):
        for i in self.phones:
            if i.value == phone:
                i.value = new_phone
                return i.value
            else:
                raise ValueError('Phone is not in list')

    def find_phone(self, phone: str):
        for n, i in enumerate(self.phones):
            if str(i) == phone:
                return self.phones[n]


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
        return self.data

    def find(self, name):
        for key, value in self.data.items():
            if key == name:
                return value

    def delete(self, name):
        for i in self.data.keys():
            if i == name:
                return self.data.pop(i)


if __name__ == '__main__':
    address_book = AddressBook()
