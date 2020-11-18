

class RepoPerson:

    def __init__(self):
        self.person_list = []


    def find_by_id_person(self, id):
        for person in self.person_list:
            if person.get_person_id == id.get_person_id:
                return person
        return None

    def find_person_by_id(self, id):
        for person in self.person_list:
            if person.get_person_id == id:
                return person
        return None

    def add_person_repo(self, person):
        self.person_list.append(person)

    def remove_person_repo(self, person):
        self.person_list.remove(person)

    def list_person_repo(self):
        return self.person_list

