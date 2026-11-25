from src.persistence.repository.meteorite_repository import MeteoriteRepository


class MeteoriteNotFoundError(Exception):
    pass


class MeteoriteService:
    def __init__(self, repository: MeteoriteRepository):
        self.repository = repository

    def get_total_meteorites(self) -> int:
        return self.repository.count_all()

    def get_meteorites(
        self,
        page: int,
        limit: int,
        search: str | None,
        fall: str | None,
        min_mass: float | None,
    ) -> tuple[list[dict], int]:
        return self.repository.find_all(
            page=page,
            limit=limit,
            search=search,
            fall=fall,
            min_mass=min_mass,
        )

    def get_meteorite_by_id(self, meteorite_id: int) -> dict:
        meteorite = self.repository.find_by_id(meteorite_id)
        if meteorite is None:
            raise MeteoriteNotFoundError(
                f"Meteorite with id {meteorite_id} not found"
            )
        return meteorite

    def create_meteorite(self, meteorite: dict) -> dict:
        return self.repository.create(meteorite)

    def delete_meteorite(self, meteorite_id: int) -> dict:
        meteorite = self.repository.delete_by_id(meteorite_id)
        if meteorite is None:
            raise MeteoriteNotFoundError(
                f"Meteorite with id {meteorite_id} not found"
            )
        return meteorite
