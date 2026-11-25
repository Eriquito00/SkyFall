from src.persistence.dao.meteorite_dao import MeteoriteDAO
from src.persistence.repository.meteorite_repository import MeteoriteRepository
from src.domain.service.meteorite_service import MeteoriteService
from src.api.controller.meteorite_controller import MeteoriteController

class MeteoriteContainer:
    dao = MeteoriteDAO()
    repository = MeteoriteRepository(dao)
    service = MeteoriteService(repository)
    controller = MeteoriteController(service)

def get_controller():
    return MeteoriteContainer.controller
