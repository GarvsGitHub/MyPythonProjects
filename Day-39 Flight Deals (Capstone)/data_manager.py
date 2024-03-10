import requests
import os
# from pprint import pprint

SHEET_PRICES_ENDPOINT = os.environ.get("Sheet_Link")  # Url/API of Sheet


# This class is responsible for talking to the Google Sheet.
class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEET_PRICES_ENDPOINT)
        data = response.json()
        # pprint(data)
        # In case if you are trying to figure out how this name(prices) even occurred in the dictionary data, "prices"
        # is the name of Google sheet(refer bottom left corner of sheet)
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {  # This is not sheet name here it is a format for storing data on sheety API
                    # i.e. if sheet name is plural then we should use singular(ex: Prices = Price, Workouts = workout)
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEET_PRICES_ENDPOINT}/{city['id']}",  # Fetching sheet cell by city id(refer the output in main)
                json=new_data
            )  # See the "new_data" format and learn how to update value of dictionary data
            print(response.text)
