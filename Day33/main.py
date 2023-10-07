import time

import requests
import datetime as dt
import smtplib

MY_LAT = -34.6075682
MY_LONG = -58.4370894


def close_enough():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 3
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) - 3

    time_now = dt.datetime.now().hour

    return sunset < time_now or time_now < sunrise

while True:
    if close_enough() and is_night():
        mail = 'chris.code.testing@gmail.com'
        password = input('Enter the password: ')

        with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
            conn.starttls()
            conn.login(user=mail, password=password)
            conn.sendmail(from_addr=mail, to_addrs=mail, msg='Subject: Look up in Tokio\n\n')
        break
    print('Working...')
    time.sleep(60)
