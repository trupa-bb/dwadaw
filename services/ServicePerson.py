from domain.PersonEntity import Person, PersonValidator
from repository.RepoPerson import RepoPerson
import random


class ServicePerson:

    def __init__(self, repository: RepoPerson, person_validator: PersonValidator):
        self.repo = repository
        self.person_validator = person_validator

    def list_init_person(self):
        list_names = [
            "Oliver", "Jake", "Noah", "John", "Charlie", "William", "Bella", "Sofia", "Lauren", "Karen"
        ]
        person = Person(random.randrange(1, 100), random.choice(list_names), random.randrange(1000000000, 9999999999))
        self.repo.add_person_repo(person)
        i = 1
        while i < 10:
            person = Person(random.randrange(1, 100), random.choice(list_names),
                            random.randrange(1000000000, 9999999999))
            if self.repo.find_by_id_person(person) is None:
                self.repo.add_person_repo(person)
                i = i + 1

    def add_person(self, person_id, name, phone_number):
        person = Person(person_id, name, phone_number)
        self.person_validator.validate(person)
        person_id = int(person_id)
        phone_number = int(phone_number)
        for x in self.repo.person_list:
            if int(person.get_person_id) == x.get_person_id:
                raise PersonServiceException("This id already exist!")
        self.repo.add_person_repo(person)

    def remove_person(self, person_id):
        person = self.repo.find_person_by_id(person_id)
        ok = False
        for x in self.repo.person_list:
            if person_id == int(x.get_person_id):
                ok = True
        if not ok:
            raise PersonServiceException("This id does not exist!")
        self.repo.remove_person_repo(person)

    def update_person(self, person_id, name, phone_number):
        person = self.repo.find_by_id_person(person_id)
        ok = False
        for x in self.repo.person_list:
            if int(person.get_person_id) == x.get_person_id:
                ok = True
        if not ok:
            raise PersonServiceException("This id does not exist!")
        self.repo.remove_person_repo(person)
        person = Person(person_id, name, phone_number)
        self.repo.add_person_repo(person)

    def list_person(self):
        return self.repo.list_person_repo()


class PersonServiceException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
