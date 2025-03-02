from fastapi import APIRouter

from backend.app.api.routes import journey, stations

api_router = APIRouter()

api_router.include_router(journey.router)
api_router.include_router(stations.router)
