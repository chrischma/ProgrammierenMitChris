# original 'worldcities.csv'-file can be downloaded here: https://simplemaps.com/data/world-cities

import csv

with open('worldcities.csv', newline='') as csvfile:              
    csv_reader = csv.DictReader(csvfile, delimiter=',')           

    for item in csv_reader:
        print(item["country"], item["population"])
