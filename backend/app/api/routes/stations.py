from fastapi import APIRouter

from backend.app.core.flows.stations import fetch_station_departures
from backend.app.models import Station, StationDeparture

router = APIRouter(prefix="/stations", tags=["stations"])


@router.post("/")
def get_station_departures(station_departure: StationDeparture):
    departures = fetch_station_departures(station_departure)

    return departures
