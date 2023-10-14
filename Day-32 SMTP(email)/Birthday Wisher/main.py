# ===== Welcome to the Birthday Wisher project ===== #
# This application will send the birthday wish email to your loved ones from 3 different format.
# So you don't have to worry about missing to wish someone on their birthday.
# To do it automatically you can upload this code on the cloud and set event to trigger it automatically to send email
# For example: pythonanywhere website will help you do this task

from datetime import datetime
import pandas
import random
import smtplib

my_email = "xxxxxxx@gmail.com"
password = "xxxxxxxxx"

data = pandas.read_csv("birthdays.csv")
name = data["name"].to_list()
email = data["email"].to_list()
month = data["month"].to_list()
day = data["day"].to_list()

now = datetime.now()
day_of_month = now.day
current_month = now.day

for i in range(len(name)):
    if day[i] == day_of_month and month[i] == current_month:
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter_format:
            letter_content = letter_format.read()
            letter_content = letter_content.replace("[NAME]", name[i])

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=email[i],
                                msg=f"Subject:Happy Birthday\n\n{letter_content}")
