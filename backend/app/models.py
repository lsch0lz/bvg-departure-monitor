import datetime

from pydantic import BaseModel


class JourneyInformation(BaseModel):
    start: int
    end: int
    departure: datetime.datetime
    arrival: datetime.datetime

class Station(BaseModel):
    id: int = None
    name: str = None

class StationDeparture(BaseModel):
    station: Station
    duration: int

class Departure(BaseModel):
    product: str
    departure: datetime.datetime
    direction: str
    destination: Station
    line: str
    occupacie: str
    remarks: str = None

class DepartureMonitor(BaseModel):
    departures_station: Station
    departures: list[Departure]