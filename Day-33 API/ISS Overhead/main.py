# ===== Welcome to the ISS(International Space Station) Overhead project ===== #
# In this project we have fetched data from various api and make use of it to complete the project.
# We used ISS api to get to know the location of space station.
# And we used Sunrise-sunset api to get to know when sunrise and sunset happen at my location.
# For location, we have used longitude and latitude as per api requirement.
# Main function: 1) When the International Space Station is within the range of +5 or -5 of our longitude and latitude.
# 2) And it's dark up there in the sky i.e. after sunset and before sunrise.
# 3) This application will email us that the ISS is above us.
# It's hard to get output of this code as we have to wait whole not knowing when it will come overhead.
# Internet connection is required to run

import smtplib
import time
import requests
from datetime import datetime

MY_LAT = 18.521428  # Your latitude
MY_LONG = -3.8544541  # Your longitude
my_email = "jforreels@gmail.com"
password = "tkuzsqldoiluyfzb"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

# If the ISS is close to my current position, and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


# If you run this code the below code it will run every 60 sec as long as your computer is on.
# And at some point during the day it will email you about the ISS.
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject:Look Up\n\nThe ISS is above you in the sky."
        )
