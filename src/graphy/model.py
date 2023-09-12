import requests

from graphy import settings


def get(path):
    path = settings.metra_base_url + path
    resp = requests.get(path, auth=settings.metra_auth)
    resp.raise_for_status()
    return resp.json()


def get_alerts():
    return get('/gtfs/alerts')


def get_positions():
    return get('/gtfs/positions')


def get_trip_updates():
    return get('/gtfs/tripUpdates')

