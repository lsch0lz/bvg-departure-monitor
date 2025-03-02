from datetime import datetime
import requests

from prefect import flow, task

from backend.app.models import StationDeparture, DepartureMonitor, Departure, Station

HAFAS_BASE_URL: str = "https://v6.bvg.transport.rest/stops"


@flow(log_prints=True)
def fetch_station_departures(station_departure: StationDeparture) -> DepartureMonitor:
    hafas_response: dict = _get_hafas_information(station_departure)
    departures: list[Departure] = _convert_hafas_information_to_departures(hafas_response)

    return DepartureMonitor(
        departures_station=station_departure.station,
        departures=departures
    )


@task()
def _get_hafas_information(station_departure: StationDeparture):
    request_url: str = HAFAS_BASE_URL + f"/{station_departure.station.id}/departures"
    duration: int = None if station_departure.duration is None else station_departure.duration
    request = requests.get(request_url, params={
        "duration": duration,
        "pretty": True
    })
    return request.json()


@task()
def _convert_hafas_information_to_departures(hafas_information: dict) -> list[Departure]:
    departure_list: list[dict] = hafas_information["departures"]
    departures: list[Departure] = [Departure(
        product=departure["line"]["productName"],
        departure=datetime.fromisoformat(departure["when"]),
        direction=departure["direction"],
        destination=Station(id=int(departure["destination"]["id"]), name=departure["destination"]["name"]),
        line=departure["line"]["name"],
        occupacie=departure["occupancy"]
    ) for departure in departure_list]

    return departures
