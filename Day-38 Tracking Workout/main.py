# Here we accessed nutritionix api which calculates calories burnt on the exercise you did and fetched the output.
# Then we gave this output as input to sheety api which stores our data on the Google sheet

import requests
import os
from datetime import datetime

GENDER = "Male"
WEIGHT_KG = "60"
HEIGHT_CM = "175"
AGE = "28"

"""
Q. Why to set Environment variables?
Ans: To hide the sensitive information like username, password, api key, token etc. from the code
so that no other users can use it when we upload that code somewhere online.

Q.How to manually set user environment variable in pycharm?
Ans: 
Step-1) Edit_Configurations > + > Python
Step-2) Then in "script" select file path
Step-3) Then add variables manually in "Environment variables"
e.g - we added APP_ID as a variable name in the "Name" column and in "Value" column we added the actual ID

Q.How to use these added environment variables?
Ans: print(os.environ.get("APP_ID")

"""
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercise you did:")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=params, headers=headers)
dict_data = response.json()["exercises"][0]
exercise = dict_data["user_input"]
duration = dict_data["duration_min"]
calories = dict_data["nf_calories"]

sheet_endpoint = os.environ.get("Link")

date_today = datetime.now()
format_date = date_today.strftime("%d/%m/%Y")
format_time = date_today.strftime("%X")

parameters = {
    "workout": {
        "date": format_date,
        "time": format_time,
        "exercise": exercise.title(),
        "duration": duration,
        "calories": calories
    }
}

auth_username = os.environ.get("Username")
auth_pwd = os.environ.get("Pwd")

# OR ALTERNATE FOR ABOVE username AND pwd
# headers = {
#     "Authorization": os.environ.get("Authorization")
# }

workout_response = requests.post(url=sheet_endpoint, json=parameters, auth=(auth_username, auth_pwd))
print(workout_response.text)

# In above request I have used Basic authentication by using username and pwd
# We can also use Authorisation Header for the same.
# Or we can create a Bearer Token for the authorisation.
