from fastapi import FastAPI
from fastapi.routing import APIRoute

from backend.app.api.main import api_router

app = FastAPI(
    title="BVG Departure Monitor",
    summary="Backend for the BVG Departure Monitor, handling all incoming requests from the frontend"
)

app.include_router(api_router)