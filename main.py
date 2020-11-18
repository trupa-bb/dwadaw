from repository.RepoPerson import RepoPerson
from repository.RepoActivity import RepoActivity
from services.ServicePerson import ServicePerson
from services.ServiceActivity import ServiceActivity
from UI.console import UI
from domain.ActivityEntity import ActivityValidator
from domain.PersonEntity import PersonValidator

person_repo = RepoPerson()
person_validator = PersonValidator()
person_service = ServicePerson(person_repo, person_validator)
activity_repo = RepoActivity()
activity_validator = ActivityValidator()
activity_service = ServiceActivity(activity_repo, person_repo, activity_validator)
console = UI(person_service, activity_service)

console.run_console()
