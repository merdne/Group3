import requests  # can be installed using: pip install requests
import os
from datetime import datetime

user_api = "2e50246423800adc73eaa3eb25da29b0"
location = input("Enter the city name: ")
# pasted from website: api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

complete_api_link = "http://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

api_link = requests.get(complete_api_link)
api_data = api_link.json()


if api_data['cod'] == '404':
    print("Invalid city: {}, Please check your city name".format(location))
else:
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print("____________________________________________________________")
    print("Weather Stats for - {} || {}".format(location.upper(), date_time))
    print("____________________________________________________________")

    print("Current temperature is: {:.2f} deg C".format(temp_city))
    print("Current weather desc  :",weather_desc)
    print("Current humidity      :",hmdt, '%')
    print("Current wind speed    :",wind_spd ,'kmph')