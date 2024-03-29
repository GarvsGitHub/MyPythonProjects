#====== Welcome to the Habit Tracking project ======
# This project mainly focuses on HTTP requests like POST(Create), PUT(Update), Delete.
# Here we are using pixela website to track our habit by daily uploading data on it.

import requests
from datetime import datetime

USERNAME = "Your Username"
TOKEN = "Your Pwd/Token"

#====> How to create a user on Pixela?
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#====> How to create a graph on pixela?
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"  # url

graph_config = {
    "id": "graph1",
    "name": "Coding",
    "unit": "Hr",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#====> How to create a pixel on graph?
pixel_post_endpoint = f"{graph_endpoint}/graph1"

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),  # Here we wanted date in yyyymmdd format which was mandatory according to the site
    "quantity": "4",
}

# response = requests.post(url=pixel_post_endpoint, json=pixel_config, headers=headers)
# print(response.text)

#====> How to Update pixela graph?
Update_date = datetime(year=2024, month=2, day=29)
update_date_format = Update_date.strftime("%Y%m%d")

update_endpoint = f"{pixel_post_endpoint}/{update_date_format}"

update_param = {
    "quantity": "4"
}

# response = requests.put(url=update_endpoint, json=update_param, headers=headers)
# print(response.text)

#====> How to delete a pixel?
delete_date = update_date_format
delete_endpoint = f"{pixel_post_endpoint}/{delete_date}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
