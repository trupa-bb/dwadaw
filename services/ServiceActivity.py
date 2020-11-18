from domain.ActivityEntity import Activity, ActivityValidator
from repository.RepoActivity import RepoActivity
from repository.RepoPerson import RepoPerson
import random
from datetime import date, time


class ServiceActivity:

    def __init__(self, repo_activity: RepoActivity, repo_person: RepoPerson, activity_validator: ActivityValidator):
        self.repo_activity = repo_activity
        self.repo_person = repo_person
        self.activity_validator = activity_validator

    def list_init_activity(self):
        list_description = [
            "football", "homework", "shop", "read", "write", "exercise", "relax", "eat", "sing", "draw"]

        d = random.randrange(1, 28)
        m = random.randrange(1, 12)
        y = random.randrange(1980, 2020)
        data = date(y, m, d)
        h = random.randrange(0, 23)
        minutes = random.randrange(0, 60)
        timm = time(h, minutes)

        list_id = []
        for i in range(0, random.randrange(2, 6)):
            j = random.randrange(1, len(self.repo_person.person_list))
            list_id.append(self.repo_person.person_list[j].get_person_id)
        activity = Activity(random.randrange(1, 100), list_id,
                            data, timm, random.choice(list_description))
        self.repo_activity.add_activity_repo(activity)

        k = 1
        while k < 10:
            d = random.randrange(1, 28)
            m = random.randrange(1, 12)
            y = random.randrange(1980, 2020)
            data = date(y, m, d)
            h = random.randrange(0, 23)
            minutes = random.randrange(0, 60)
            timm = time(h, minutes)

            list_id = []
            for i in range(0, random.randrange(2, 5)):
                j = random.randrange(1, len(self.repo_person.person_list))
                while j in list_id:
                    j = random.randrange(1, len(self.repo_person.person_list))
                list_id.append(str(self.repo_person.person_list[j].get_person_id))

            x = random.randrange(1, 100)
            if self.repo_activity.find_by_id_activity(x) == None:
                activity = Activity(x, list_id,
                                    data, timm, random.choice(list_description))
                if self.repo_activity.find_by_id_activity(activity) is None:
                    self.repo_activity.add_activity_repo(activity)
                    k = k + 1

    def check_for_unique_datetime(self, date, time):
        for i in range(0, len(self.repo_activity.activity_list)):
            if self.repo_activity.activity_list[i].get_date() == date and self.repo_activity.activity_list[i].get_time() == time:
                return False
        return True

    def add_activity(self, activity_id, person_id, activity_date, activity_time, activity_description):
        """
        This function add an activity and checks if it is correct.
        :param activity_id: The activity id we want to add
        :param person_id: The persons who have those activities
        :param activity_date: The date of the activity
        :param activity_time: The time of the activity
        :param activity_description: The description of the activity
        """
        activity = Activity(activity_id, person_id, activity_date, activity_time, activity_description)
        self.activity_validator.validate(activity)
        activity_id = int(activity_id)
        if self.check_for_unique_datetime(activity.get_date(), activity.get_time()) == False:
            raise ActivityServiceException("Date and time are already used by another activity!")
        if self.repo_activity.find_by_id_activity(int(activity_id)) != None:
            raise ActivityServiceException("This id already exist!")
        self.repo_activity.add_activity_repo(activity)

    def remove_activity(self, activity_id):
        activity = self.repo_activity.find_by_id_activity(activity_id)
        self.repo_activity.remove_activity_repo(activity)

    def update_activity(self, activity_id, person_id, activity_date, activity_time, activity_description):
        activity = self.repo_activity.find_by_id_activity(activity_id)
        self.repo_activity.remove_activity_repo(activity)
        activity = Activity(activity_id, person_id, activity_date, activity_time, activity_description)
        self.activity_validator.validate(activity)
        self.repo_activity.add_activity_repo(activity)

    def list_activity(self):
        return self.repo_activity.list_activity_repo()


class ActivityServiceException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
