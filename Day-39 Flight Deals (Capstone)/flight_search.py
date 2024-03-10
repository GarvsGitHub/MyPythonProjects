import os

TEQUILA_API = os.environ.get("Flight_API_KEY")
TEQUILA_endpoint = "https://api.tequila.kiwi.com/"


# This class is responsible for talking to the Flight Search API.
class FlightSearch:

    def get_destination_code(self, city_name):
        code = "Testing"
        return code
