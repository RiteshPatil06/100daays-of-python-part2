import os
import pprint

from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
import requests

load_dotenv()


class DataManager:
    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)

        self._SHEETY_PRICES_ENDPOINT = os.environ["SHEETY_PRICES_ENDPOINT"]
        self._SHEETY_USERS_ENDPOINT = os.environ["SHEETY_USERS_ENDPOINT"]

        self.destination_data = {}
        self.customer_data = {}
    def get_destination_data(self):
        response = requests.get(url=self._SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data['prices']
        # pprint.pprint(self.destination_data)
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"],
                }
            }

            response = requests.put(url=f"{self._SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=self._SHEETY_USERS_ENDPOINT)
        data = response.json()
        # print(data)
        self.customer_data = data["users"]
        return self.customer_data

