#pylint: disable=line-too-long
from src.controllers.interfaces.pet_deleter_controller_interface import PetDeleterControllerInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface

class PetDeleterView(ViewInterface):
  def __init__(self, controller: PetDeleterControllerInterface) -> None:
    self.__controller = controller

  def handle(self, http_request: HttpRequest) -> HttpResponse:
    name = http_request.param["name"]
    self.__controller.detele(name)

    return HttpResponse(status_code=204)
