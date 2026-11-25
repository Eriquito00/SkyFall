from fastapi import APIRouter, Query, status
from typing import Optional

from src.api.schemas.meteorite_schema import MeteoriteCreate
from src.core.container.meteorite_container import get_controller

router = APIRouter(tags=["Meteorites"])

@router.get("/meteorites", status_code=status.HTTP_200_OK)
def get_meteorites(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=1000),
    search: Optional[str] = Query(None),
    fall: Optional[str] = Query(None),
    min_mass: Optional[float] = Query(None, ge=0)
):
    return get_controller().get_meteorites(
        page=page,
        limit=limit,
        search=search,
        fall=fall,
        min_mass=min_mass,
    )

@router.get("/meteorites/{id}", status_code=status.HTTP_200_OK)
def get_meteorite_by_id(id: int):
    return get_controller().get_meteorite_by_id(id)

@router.post("/meteorites", status_code=status.HTTP_201_CREATED)
def create_meteorite(meteorite_data: MeteoriteCreate):
    return get_controller().create_meteorite(
        meteorite_data.model_dump(by_alias=True)
    )

@router.delete("/meteorites/{id}", status_code=status.HTTP_200_OK)
def delete_meteorite(id: int):
    return get_controller().delete_meteorite(id)
