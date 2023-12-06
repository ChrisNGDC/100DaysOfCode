import requests as rq
from twilio.rest import Client
import os
from env_var import define_env
define_env()

# Message setup #
account_sid = 'ACaed507ce48a78089b1eba61fba2f948b'
auth_token = os.getenv("TSM_AUTH_KEY")
client = Client(account_sid, auth_token)

# Rain Logic #
API_KEY = os.getenv("OWA_API_KEY")
LAT = -34.603683
LONG = -58.381557
URL = "https://api.openweathermap.org/data/2.8/onecall"

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}

response = rq.get(URL, params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
weather = [hour['weather'][0]['id'] for hour in data['hourly'][:12]]
for code in weather:
    if code < 800:
        will_rain = True

if will_rain:
    message = client.messages.create(
        from_='+12764092358',
        body="It's going to rain, bring an umbrella ☂",
        to=f'+54{os.getenv("phone")}'
    )
    print(message.status)
