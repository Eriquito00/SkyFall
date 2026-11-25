from fastapi import APIRouter, Request, status

from src.core.container.meteorite_container import get_controller

router = APIRouter(tags=["SkyFall API"])

@router.get("/", status_code=status.HTTP_200_OK)
def main(request: Request):
    docs_url = f"{request.base_url}docs"
    registers_count = get_controller().get_total_meteorites()
    return {
        "status": 200,
        "message": "Welcome to the SkyFall API! This API provides access to meteorite data and related information.",
        "data": {
            "registers_count": registers_count,
            "api_documentation": docs_url,
        }
    }