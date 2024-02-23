import os
import requests
from dotenv import load_dotenv

load_dotenv()

NASA_API_KEY = os.getenv("NASA_API_KEY")
TOMORROW_API_KEY = os.getenv("TOMORROW_API_KEY")

def get_apod(date, api_key):
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "date": date,
        "api_key": api_key
    }
    response = requests.get(url=url, params=params)
    return response.json()

def apod(date, api_key):
    apod = get_apod(date, api_key)
    return(apod['explanation'])

print(apod("2024-01-10", NASA_API_KEY))

def get_forecast(location):
    url = "https://api.tomorrow.io/v4/weather/forecast"
    params = {
        "apikey": "OB1TTpR3Y6ayzGjmZZGC8y67ym9PJthg",
        "location": location,
        "units": "imperial",
        "timesteps": "daily"
    }
    response = requests.get(url=url, params=params)
    return response.json()

def forecast(location):
    forecast = get_forecast(location)
    result = [] 
    for days in forecast['timelines']['daily']:
        result.append(days['values']['temperatureAvg'])
    return result

print(forecast("boston"))