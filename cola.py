from bs4 import BeautifulSoup
import requests

city_1 = 'Berlin'
city_2 = 'Leipzig'

url = f'https://www.numbeo.com/cost-of-living/compare_cities.jsp?country1=Germany&country2=Germany&city1={city_1}&city2={city_2}&tracking=getDispatchComparison'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find('table',attrs={'class':'data_wide_table new_bar_table cost_comparison_table'})
rows = table.find_all('tr')

cola_data = rows[7].text.split()

price_1 = cola_data[4]
price_2 = cola_data[6]

print(f'Der Colapreis in {city_1} beträgt {price_1}')
print(f'Der Colapreis in {city_2} beträgt {price_2}')