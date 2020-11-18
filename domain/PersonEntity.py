class Person:
    def __init__(self, person_id, name, phone_number):
        self.__person_id = person_id
        self.__name = name
        self.__phone_number = phone_number

    def __str__(self):
        return 'Person ID: \t' + str(self.__person_id) + '\t Name: \t' + self.__name + '\t Phone number: \t' + str(
            self.__phone_number)

    @property
    def get_person_id(self):
        return self.__person_id

    def get_name(self):
        return self.__name

    def get_phone_number(self):
        return self.__phone_number

    def set_person_id(self, person_id):
        self.__person_id = person_id

    def set_name(self, name):
        self.__name = name

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number


class PersonValidator:
    def isdigit(self, x):
        for i in x:
            if i < '0' or i > '9':
                return False
        return True

    def validate(self, person):
        if isinstance(person.get_person_id, str):
            if not self.isdigit(person.get_person_id):
                raise PersonException("Id must be integer!")
        if person.get_name() == '':
            raise PersonException("A person need to have a name!")
        if person.get_phone_number() == '':
            raise PersonException("Every person need to have a phone number!")
        if int(person.get_phone_number()) <= 99999999 or int(person.get_phone_number()) > 9999999999:
            raise PersonException("A phone number must contain 10 digits!")


class PersonException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
