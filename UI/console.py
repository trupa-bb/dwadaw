from services.ServicePerson import ServicePerson, PersonServiceException
from services.ServiceActivity import ServiceActivity, ActivityServiceException
from domain.ActivityEntity import ActivityException
from domain.PersonEntity import PersonException
from datetime import date, time


class UI:
    def __init__(self, person_service: ServicePerson, activity_service: ServiceActivity):
        self.__operations = [
            "1. Add \n"
            "2. Remove \n"
            "3. Update \n"
            "4. List \n"
            "5. Exit\n"
        ]
        self.__command_dict = {
            1: self.add_ui,
            2: self.remove_ui,
            3: self.update_ui,
            4: self.list_ui
        }
        self.person_service = person_service

        self.activity_service = activity_service

    def run_console(self):
        self.person_service.list_init_person()
        self.activity_service.list_init_activity()
        while True:
            try:
                print(' ')
                print(*self.__operations)
                print(' ')
                command = int(input("Pick an operation from 1 to 5: "))
                print(' ')
                if command in self.__command_dict:
                    self.__command_dict[command]()
                elif int(command) == 5:
                    print("Bye bye!")
                    return
            except ActivityException as AE:
                print(AE)
            except PersonException as PE:
                print(PE)
            except ActivityServiceException as ASE:
                print(ASE)
            except PersonServiceException as PSE:
                print(PSE)
            # except exception:
            # print("you must enter a valid option")

    def add_ui(self):
        print("Press 1 for add a person. \n")
        print("Press 2 for add an activity \n")
        x = input("What do you want to add? : ")
        if int(x) == 1:
            person_id = input("Person id: ")
            person_name = input("Person name: ")
            person_phone_number = input("Phone number: ")
            self.person_service.add_person(person_id, person_name, person_phone_number)
        else:
            activity_id = input("Activity id: ")
            x = int(input("How many persons?: "))
            list_person_id = []
            for i in range (0, x):
                y = input("Person id: ")
                list_person_id.append(y)
            try:
                year = int(input("Year: "))
                month = int(input("Month: "))
                day = int(input("Day: "))
                hour = int(input("Hour: "))
                minute = int(input("Minute: "))
                activity_date = date(year, month, day)
                activity_time = time(hour, minute, 0)
            except Exception:
                  print("Please introduce valid data!")
            activity_description = input("Activity description: ")
            self.activity_service.add_activity(activity_id, list_person_id, activity_date, activity_time,
                                               activity_description)


    def remove_ui(self):
        print("Press 1 for remove a person. \n")
        print("Press 2 for remove an activity. \n")
        x = int(input("What do you want to remove? : "))
        if int(x) == 1:
            person_id = input("The ID of the person you want to remove is: ")
            self.person_service.remove_person(person_id)
        else:
            activity_id = input("The ID of the activity you want to remove is: ")
            self.activity_service.remove_activity(activity_id)

    def update_ui(self):
        print("Press 1 for update a person. \n")
        print("Press 2 for update an activity. \n")
        x = input("What do you want to update? : ")
        if int(x) == 1:
            person_id = int(input("The ID of the person you want to update is: "))
            person_name = input("Person name: ")
            person_phone_number = input("Phone number: ")
            self.person_service.update_person(person_id, person_name, person_phone_number)
        else:
            activity_id = input("The ID of the activity you want to update is: ")
            activity_date = input("Activity date: ")
            activity_time = input("Activity time: ")
            activity_description = input("Activity description: ")
            self.activity_service.update_activity(activity_id, activity_date, activity_time, activity_description)

    def list_ui(self):
        print("Press 1 for list the persons. \n")
        print("Press 2 for list the activities. \n")
        x = input("What do you want to list? : ")
        if int(x) == 1:
            for person in self.person_service.list_person():
                print(person)
        else:
            for activity in self.activity_service.repo_activity.activity_list:
                print(str(activity))


class ConsoleException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
