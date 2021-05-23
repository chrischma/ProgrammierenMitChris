import pandas

data = pandas.read_csv('worldcities.csv')
sorted_data = data.sort_values(by=['city'], ascending=True)
sorted_data.to_csv('worldcities_by_city.csv', quoting=1, index=False)
