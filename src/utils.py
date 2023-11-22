def get_population(country):
  population = {
    '1970': country['1970 Population'],
    '1980': country['1980 Population'],
    '1990': country['1990 Population'],
    '2000': country['2000 Population'],
    '2010': country['2010 Population'],
    '2015': country['2015 Population'],
    '2020': country['2020 Population'],
    '2022': country['2022 Population']

  }

  labels = list(population.keys())
  values = list(population.values())

  return labels, values

def population_by_country(data, country):
  # return [i for i in data if i['Country/Territory'] == country]
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result