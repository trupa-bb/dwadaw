class Activity:
    def __init__(self, activity_id, person_id, date, time, description):
        self.__activity_id = activity_id
        self.__person_id = person_id
        self.__date = date
        self.__time = time
        self.__description = description

    def __str__(self):
        string = 'Activity id: ' + str(self.__activity_id).ljust(7) + 'Person id: '
        for i in range(0, len(self.__person_id) - 1):
            string += str(self.__person_id[i]) + ' '
        string += '\t\t Date: ' + str(self.__date).ljust(20) + ' Time: '
        string += str(self.__time).ljust(25) + ' Description: '
        string += self.__description
        return string

    def get_activity_id(self):
        return self.__activity_id

    def get_person_id_activity(self):
        return self.__person_id

    def get_date(self):
        return self.__date

    def get_time(self):
        return self.__time

    def get_description(self):
        return self.__description

    def set_activity_id(self, activity_id):
        self.__activity_id = activity_id

    def set_person_id(self, person_id):
        self.__person_id = person_id

    def set_date(self, date):
        self.__date = date

    def set_time(self, time):
        self.__time = time

    def set_description(self, description):
        self.__description = description


class ActivityValidator:
    def isdigit(self, x):
        for i in x:
            if i < '0' or i > '9':
                return False
        return True

    def validate(self, activity):
        if isinstance(activity.get_activity_id(), str):
            if not self.isdigit(activity.get_activity_id()):
               raise ActivityException("Id must be integer!")
        if activity.get_description() == '':
            raise ActivityException("An activity has have a descritpion")

    #data nu i corecta raise ActivityException("data nu e buna")

class ActivityException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

