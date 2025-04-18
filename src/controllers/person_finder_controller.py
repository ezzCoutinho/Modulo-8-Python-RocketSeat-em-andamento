#pylint: disable=line-too-long
from typing import Dict
from src.models.sqlite.interfaces.people_repository_interface import PeopleRepositoryInterface
from src.models.sqlite.entities.people import PeopleTable
from src.controllers.interfaces.person_finder_controller_interface import PersonFinderControllerInterface
from src.errors.error_types.http_not_found import HtttpNotFound

class PersonFinderController(PersonFinderControllerInterface):
  def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
    self.__person_repository = people_repository

  def find(self, person_id: int) -> Dict:
    person = self.__find_person_id_db(person_id)
    response = self.__format_response(person)

    return response

  def __find_person_id_db(self, person_id: int) -> PeopleTable:
    person = self.__person_repository.get_person(person_id)
    if not person:
      raise HtttpNotFound("Pessoa não encontrada")

    return person

  def __format_response(self, person: PeopleTable) -> Dict:
    return {
      "data": {
        "type": "Person",
        "count": 1,
        "attributes": {
          "first_name": person.first_name,
          "last_name": person.last_name,
          "pet_name": person.pet_name,
          "pet_type": person.pet_type
        }
      }
    }
