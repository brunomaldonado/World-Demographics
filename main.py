import src.read_csv as read_csv
from src.utils import get_population, population_by_country
from src.charts import generate_bar_chart, generate_pie_chart, generate_barh_chart, generate_plot_chart, generate_line_chart
from shutil import get_terminal_size

def run():
    data = read_csv.read_csv('./db/data.csv')
       
    territory = []
    continents = []
    for idx, i in enumerate(data):
      country = i['Country/Territory']
      territory.append(country)
      continent_ = i['Continent']
      continents.append(continent_)
    print()

    continent = list(set(continents))

    num_columns = 6
    num_rows_country = len(territory) // num_columns + (len(territory) % num_columns > 0)
    num_rows_continent = len(continent) // num_columns + (len(continent) % num_columns > 0)

    for i in range(num_rows_continent):
       for j in range(num_columns):
          index = i * num_columns + j
          if index < len(continent):
             print(f'{index + 1:<4}{continent[index]:<25}', end=' ')
       print()

    continent_ = input("\nType the continent: ").strip().title()

    option_chart = int(input("\noption: [1]. line chart [2]. pie chart \noption: "))
    if option_chart == 1:
      generate_line_chart(data, continent_)
    if option_chart == 2:
      generate_pie_chart(data, continent_)

    for i in range(num_rows_country):
       for j in range(num_columns):
          index = i * num_columns + j
          if index < len(territory):
             print(f'{index + 1:<4}{territory[index]:<25}', end=' ')
       print()

    country = input("\nEnter the country: ").strip().title()
    country = country.replace('And', 'and')
    country = country.replace("The", "the")
    country = country.replace("Of", "of")
    country = country.replace("Dr", "DR")
    
    result = population_by_country(data, country)
   
    if len(result) > 0:
      country = result[0]
      key, value = get_population(country)
      labels = key
      values = list(map(int, value))
      print()

      for i in result:
        country = i['Country/Territory']
        capital = i['Capital']
        continent = i['Continent']
        
      option_chart = int(input("option : [1]. vertical bars [2]. horizontal bars [3]. plot dashes \noption: "))
      if option_chart == 1:
        generate_bar_chart(labels, values, country, capital, continent)
      if option_chart == 2:
        generate_barh_chart(labels, values, country, capital, continent)
      if option_chart == 3:
         generate_plot_chart(labels, values, country, capital, continent)
      if option_chart == 4:
         pass
         
if __name__ == '__main__':
    run()

    # 33139445