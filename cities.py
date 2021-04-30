# original 'worldcities.csv'-file can be downloaded here: https://simplemaps.com/data/world-cities

import csv

with open('worldcities.csv', newline='') as csvfile:              
    csv_reader = csv.DictReader(csvfile, delimiter=',')           

    for city in csv_reader:
        print(city["country"], city["population"])
