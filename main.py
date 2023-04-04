import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "e9ec2c1f010668be07db60a53fb70ad0"
lat = 44.020401
lon = 144.268188
# part = "current,minutely,hourly"
weather_parameters = {
    "lat": lat,
    "lon": lon,
    # "exclude": part,
    "appid": api_key
}


# response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude="
#                               f"{part}&appid={api_key}")


response = requests.get(OWM_Endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
weather_list = [n for n in weather_data["list"]]

weather_list_for3hour = []

for n in range(len(weather_list)):
    weather_list_for3hour.append(weather_list[n]["weather"][0]["id"])
# weather_list_for3hour = [n for n["weather"] in weather_list]
print(weather_list_for3hour)