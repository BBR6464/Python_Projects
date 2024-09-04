import requests
from twilio 

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "c29cff3a782795952e6d88764fe77f56"

weather_params = {
    "lat": 8.485400,
    "lon": 76.957512,
    "appid": api_key,
    "cnt": 4,
}
+12564881638
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    print("Bring an Umbrella")