import requests

limit = 500
days = 356

url = f'https://eonet.sci.gsfc.nasa.gov/api/v2.1/events?limit={limit}&days={days}'
r = requests.get(url)
events_data = r.json()
event_list = events_data['events']

for event in event_list:
    if 'fire' in str(event['categories']):
        print(event['title'])
      
