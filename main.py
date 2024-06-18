import requests
from twilio.rest import Client
import os

account_sid = "AC16393cf2ee7001fc9c755ec206f6d5db"
auth_token = os.environ.get("AUTH_TOKEN")
api_key = os.environ.get("OWN_API_KEY")
params = {
    "lat": 32.0853,
    "lon": 34.7818,
    "appid": api_key,
    "cnt": 4,
}
weather_data = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=params)
weather_data.raise_for_status()
if weather_data.status_code == 200:
    weather_json = weather_data.json()
weather_id = [weather_json["list"][i]["weather"][0]["id"] for i in range(4)]
will_rain = False
for id_status in weather_id:
    if int(id) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+12093950294',
        body='Its going to rain today take an umbrella',
        to='whatsapp:+972546736261'
    )

    print(message.status)
