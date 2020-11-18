

class RepoActivity:

    def __init__(self):
        self.activity_list = []


    def find_by_id_activity(self, id):
        for i in self.activity_list:
            if i.get_activity_id == id:
                return i
        return None

    def add_activity_repo(self, activity):
        self.activity_list.append(activity)

    def remove_activity_repo(self, activity):
        self.activity_list.remove(activity)

    def list_activity_repo(self):
        return self.activity_list

