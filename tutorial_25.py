import requests

api_key = "PASTE YOUR API CODE HERE"
city = input("Hallo! Bitte gib eine Stadt ein.")

# creating a https request
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
data = requests.get(url).json()

# saving parts the received data in variables
temp = data['main']['temp']
humidity = data['main']['humidity']

# printing them out
print(f'In {city} beträgt die Temperatur {temp}. Die Luftfeuchtigkeit beträgt {humidity}')
