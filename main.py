import src.read_csv as read_csv
from src.utils import get_population, population_by_country
from src.charts import generate_bar_chart, generate_barh_chart, generate_plotdashed_chart, generate_plot_line_chart
from shutil import get_terminal_size

def run():
    data = read_csv.read_csv('./db/data.csv')

    continents = ['North America', 'South America', 'Asia', 'Europe', 'Oceania', 'Africa']
    num_columns = 6
    num_rows = len(continents) // num_columns + (len(continents) % num_columns > 0)
    print()
    for i in range(num_rows):
      for j in range(num_columns):
          index = i * num_columns + j
          if index < len(continents):
            print(f'{index + 1:<4}{continents[index]:<25}', end='')
    print()
    
    continent_ = input("\nType the continent: ").strip().title()
    generate_plot_line_chart(data, continent_)

    territory = []
    for idx, country_ in enumerate(data):
       country = country_['Country/Territory']
       territory.append(country)
    
    num_columns = 6
    num_rows = len(territory) // num_columns + (len(territory) % num_columns > 0)

    for i in range(num_rows):
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
      objects = key
      performance = list(map(int, value))

      for country_ in result:
        country = country_['Country/Territory']
        capital = country_['Capital']
        continent = country_['Continent']
        
      option_bars = int(input("option bars: [1]. vertical bars [2]. horizontal bars [3]. plot dashes \noption: "))
      if option_bars == 1:
        generate_bar_chart(labels, values, country, capital, continent)
      if option_bars == 2:
        generate_barh_chart(objects, performance, country, capital, continent)
      if option_bars == 3:
         generate_plotdashed_chart(labels, values, country, capital, continent)
      if option_bars == 4:
         pass
         
if __name__ == '__main__':
    run()

    # 18507907