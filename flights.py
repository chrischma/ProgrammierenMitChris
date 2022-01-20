# a simple webscraper example that allows to see all upcoming departures from a certain airport.

import requests
from time import localtime
from bs4 import BeautifulSoup


def main():
	airport_input = input('Enter airport: \n')

	if not airport_input: 
		airport_input = 'BER'

	flight_data = get_flight_data(airport_input)
	flights = extract_flights_from_data(flight_data)

	for flight in flights:
		print(flight)


# takes any ATA airport code (like 'BER' for Berlin Airport) 
# and makes a request to flightsfrom.com.
def get_flight_data(airport_input):

	current_time = localtime()
	current_hour = current_time.tm_hour
	current_minute = current_time.tm_min
	formatted_time_string = current_hour * 60 + current_minute

	url = f'https://www.flightsfrom.com/{airport_input}/departures?timeFrom={formatted_time_string}&timeTo=1440'
	request = requests.get(url)

	if request.status_code != 200:
		print(f'No results for {airport_input}.')
		exit()

	return request


# takes the data that was returned by flightsfrom.com 
# and returns a list of flights.
def extract_flights_from_data(data):
	soup = BeautifulSoup(data.text, 'html.parser')
	departure_list = soup.find('ul', {'id':'airport-departure-list'})

	flight_list_items = departure_list.find_all('li')
	flight_list_items = flight_list_items[:-1]

	flight_results = list()
	for item in flight_list_items:
		flight_string = item.text
		flight_string = flight_string.replace('\n', ' ') 
		flight_string = flight_string.replace('\t', ' ')
		flight_string = flight_string.replace('  ', '')

		flight_results.append(flight_string)

	return flight_results


if __name__ == '__main__':
	main()