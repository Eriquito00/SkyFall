from threading import Lock

from src.persistence.dao.meteorite_dao import MeteoriteDAO

class MeteoriteRepository:
    def __init__(self, dao: MeteoriteDAO):
        self.dao = dao
        self.data = self.dao.load_all()
        self._mutation_lock = Lock()

    def count_all(self) -> int:
        return len(self.data)

    def find_all(
        self,
        page: int = 1,
        limit: int = 10,
        search: str | None = None,
        fall: str | None = None,
        min_mass: float | None = None,
    ) -> tuple[list[dict], int]:
        meteorites = self.data

        if search:
            search_term = search.casefold()
            meteorites = [
                item for item in meteorites
                if search_term in item.get("name", "").casefold()
            ]
        if fall:
            fall_type = fall.casefold()
            meteorites = [
                item for item in meteorites
                if item.get("fall", "").casefold() == fall_type
            ]
        if min_mass is not None:
            meteorites = [
                item for item in meteorites
                if item.get("mass (g)") is not None
                and item["mass (g)"] >= min_mass
            ]

        total = len(meteorites)
        offset = (page - 1) * limit
        return meteorites[offset:offset + limit], total

    def find_by_id(self, meteorite_id: int) -> dict | None:
        for item in self.data:
            if item.get("id") == meteorite_id:
                return item
        return None

    def create(self, meteorite: dict) -> dict:
        with self._mutation_lock:
            meteorite_id = max(
                (item["id"] for item in self.data),
                default=0,
            ) + 1
            created_meteorite = {"id": meteorite_id, **meteorite}
            updated_data = [*self.data, created_meteorite]
            self.dao.save_all(updated_data)
            self.data = updated_data
            return created_meteorite

    def delete_by_id(self, meteorite_id: int) -> dict | None:
        with self._mutation_lock:
            for index, meteorite in enumerate(self.data):
                if meteorite.get("id") == meteorite_id:
                    updated_data = self.data[:index] + self.data[index + 1:]
                    self.dao.save_all(updated_data)
                    self.data = updated_data
                    return meteorite
            return None
