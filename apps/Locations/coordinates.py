import requests
from requests.models import PreparedRequest
from django.conf import settings

from rest_framework.utils import json


def find_coordinates(user_address):
    global geometry
    key = settings.API_KEY
    json_address = json.dumps(user_address)

    url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    address = 'address=' + json_address
    key = '&key=' + key

    req = PreparedRequest()
    req.prepare_url(url, address)

    final_url = req.url + key
    data = requests.get(final_url).json()

    for i in data['results']:
        address = i['formatted_address']
        geometry = i['geometry']
        geometry = str(geometry)
    response = {"address": address, "coordinates": geometry}

    return response
