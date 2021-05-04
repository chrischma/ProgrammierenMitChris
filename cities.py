# original 'worldcities.csv'-file can be downloaded here: https://simplemaps.com/data/world-cities

import csv

f = open('worldcities.csv', newline='')
cities_csv = csv.DictReader(f, delimiter=',')

for item in cities_csv:
    print(item['city'], item['population'])
