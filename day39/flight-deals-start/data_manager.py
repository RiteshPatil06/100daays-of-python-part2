import os
import pprint

from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
import requests

load_dotenv()

SHEETY_ENDPOINT = "https://api.sheety.co/fc8228e0a21f5dca311c6d0e486ce39e/flightDeals/prices"

class DataManager:
    def __init__(self):
        self._user = os.environ["SHEETY_USRERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data['prices']
        pprint.pprint(self.destination_data)
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"],
                }
            }

            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)