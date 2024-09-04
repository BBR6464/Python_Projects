import requests
from datetime import datetime

MY_LAT = 8.485400
MY_LONG = 76.957510
# responce = requests.get(url="http://api.open-notify.org/iss-now.json")
# responce.raise_for_status()
#
# data = responce.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# print(longitude)
# print(latitude)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

responce =requests.get("https://api.sunrise-sunset.org/json", params=parameters)
responce.raise_for_status()
data = responce.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()

# print(time_now.hour)
