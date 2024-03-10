# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.
from data_manager import DataManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# print(sheet_data)
# Output:
# [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2},
#  {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3},
#  {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4},
#  {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5},
#  {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6},
#  {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7},
#  {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8},
#  {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9},
#  {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:  # for each
        row["iataCode"] = flight_search.get_destination_code(row["city"])  # Passing parameter city name to get city cod
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()
