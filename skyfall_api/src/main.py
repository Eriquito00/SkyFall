from fastapi import FastAPI
from src.api.routers.api_router import router as api_router
from src.api.routers.meteorite_router import router as meteorite_router

app = FastAPI(title="SkyFall API")

app.include_router(api_router)
app.include_router(meteorite_router)
