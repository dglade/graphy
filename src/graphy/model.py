import requests

from .settings import metra_auth, metra_base_url


def get(path):
    path = metra_base_url + path
    resp = requests.get(path, auth=metra_auth)
    resp.raise_for_status()
    return resp.json()


def get_alerts():
    return get('/gtfs/alerts')


def get_positions():
    return get('/gtfs/positions')


def get_trip_updates():
    return get('/gtfs/tripUpdates')

