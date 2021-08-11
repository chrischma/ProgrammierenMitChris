import requests
import os

API_KEY = os.environ.get('wetter_api_key')

city = input("Hallo! Bitte gib eine Stadt ein.")
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

data = requests.get(url).json()
temp = data['main']['temp']
humidity = data['main']['humidity']

print(f'In {city} beträgt die Temperatur {temp}. Die Luftfeuchtigkeit beträgt {humidity}%.')
