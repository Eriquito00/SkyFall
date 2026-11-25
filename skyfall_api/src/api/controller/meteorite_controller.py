from fastapi import HTTPException, status
from src.domain.service.meteorite_service import MeteoriteNotFoundError, MeteoriteService

class MeteoriteController:
    def __init__(self, service: MeteoriteService):
        self.service = service

    def get_total_meteorites(self) -> int:
        return self.service.get_total_meteorites()

    def get_meteorites(
        self,
        page: int,
        limit: int,
        search: str | None,
        fall: str | None,
        min_mass: float | None,
    ) -> dict:
        meteorites, total = self.service.get_meteorites(
            page=page,
            limit=limit,
            search=search,
            fall=fall,
            min_mass=min_mass,
        )
        return {
            "status": 200,
            "message": "Meteorites retrieved successfully",
            "data": {
                "items": meteorites,
                "total": total,
                "total_pages": (total + limit - 1) // limit,
                "page": page,
                "limit": limit,
            },
        }

    def create_meteorite(self, meteorite_data: dict) -> dict:
        meteorite = self.service.create_meteorite(meteorite_data)
        return {
            "status": 201,
            "message": "Meteorite created successfully",
            "data": meteorite,
        }

    def get_meteorite_by_id(self, meteorite_id: int) -> dict:
        try:
            meteorite = self.service.get_meteorite_by_id(meteorite_id)
        except MeteoriteNotFoundError as error:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(error),
            ) from error
        return {
            "status": 200,
            "message": "Meteorite retrieved successfully",
            "data": meteorite,
        }

    def delete_meteorite(self, meteorite_id: int) -> dict:
        try:
            meteorite = self.service.delete_meteorite(meteorite_id)
        except MeteoriteNotFoundError as error:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(error),
            ) from error
        return {
            "status": 200,
            "message": "Meteorite deleted successfully",
            "data": meteorite,
        }
