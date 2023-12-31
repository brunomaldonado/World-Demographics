import matplotlib.ticker as mticker
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import numpy as np
from src.utils import get_population

# global function and variables 
palette = ['blue', 'red', 'green', 'grey', 'maroon', 'pink', 'orange', 'purple']

def format_population(value, _):
      if value >= 1e6:
          return f'{value / 1e6:.1f}M'
      elif value >= 1e3:
          return f'{value / 1e3:.0f}K'
      else:
          return f'{value:.0f}'

def generate_bar_chart(labels, values, country, capital, continet): 
  fig, ax = plt.subplots(figsize=(9, 6))
  bars = ax.bar(labels, values, width=0.87, color=palette)
  ax.spines['right'].set_visible(False)
  ax.spines['top'].set_visible(False)
  ax.spines['left'].set_visible(False)
  ax.spines['bottom'].set_visible(False)

  plt.tick_params(left = False, bottom = False)
  ax.tick_params(axis='both')
  plt.xticks(fontsize='8.5', weight='bold', color='#7e807e')
  plt.yticks(fontsize='8.5', weight='bold', color='#7e807e')

  ax.set_xlabel("Years in census", labelpad=18, size=10, fontfamily="sans", weight="bold")
  ax.xaxis.set_label_coords(x=0.51, y=-0.087, transform=ax.transAxes)
  ax.set_ylabel("Populations in (K - thousands & M - millions)", labelpad=18, size=10, fontfamily="sans", weight="bold")
  ax.yaxis.set_label_coords(x=-0.1, y=0.51, transform=ax.transAxes)
  
  plt.title("Population of " + country + " - " + capital + " - " + continet, size=12, weight="bold", fontfamily="sans", color="#080404", horizontalalignment = "left", x=0.12, y=0.96, transform = fig.transFigure)
  plt.suptitle("From the year 1970 to the year 2022", size=10, weight="bold", fontfamily="sans", color="#080808", horizontalalignment = "left", x=0.12, y=0.94, transform = fig.transFigure)
  plt.grid(color='grey', linestyle='-.', linewidth=0.5, alpha=0.4)

  for bar in bars:
    height = bar.get_height()
    num = height/1e6
    # formatter 'y' axis K-thousands & M-millions
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_population))
    # text formatter
    if height >= 1000000:
      text_values = "{:.3f}M".format(num)
    else:
      text_values = "{:.3f}k".format(num * 1000)

    ax.text(bar.get_x() + bar.get_width() / 2, height, text_values, ha='center', va='bottom', fontsize=8, fontweight='bold')

  plt.savefig(f'./images/{country}.png')
  plt.close()


def generate_pie_chart(data, continent):
  fig, ax = plt.subplots(figsize=(10, 6))

  continent_and_countries = list(filter(lambda i: i['Continent'] == str(continent), data))
  countries = list(map(lambda i: i['Country/Territory'], continent_and_countries))
  population_percentage = list(map(lambda i: i['World Population Percentage'], continent_and_countries))
  percentages = list(map(float, population_percentage))

  percentage_continent_countries = {'Asia': 10, 'Europe': 12, 'Africa': 19, 'South America': 10, 'North America': 8, 'Oceania': 5}

  for key, value in percentage_continent_countries.items():
    if key == str(continent):
      top_countries = value
      explode_2d = [0.05] + [0] * (top_countries - 1)

  sorted_data = sorted(zip(percentages, countries), reverse=True)
  # print("sorted_data ===> ", sorted_data)
  values, labels = zip(*sorted_data[:top_countries])
  # print("values labels ==> ", values, labels)
  ax.pie(values, labels=labels, autopct='%1.1f%%', explode=explode_2d)
  ax.axis('equal')

  continent = continent.replace('Europe', 'European')
  continent = continent.replace('South America', 'South American')
  continent = continent.replace('North America', 'North American')
  continent = continent.replace('Asia', 'Asian')
  continent = continent.replace('Africa', 'African')
  plt.title(f"Percentage of population of the countries of the \n{continent} continent", size=12, weight="bold", fontfamily="sans", color="#080404", horizontalalignment = "left", x=0.12, y=.9, transform = fig.transFigure)

  plt.legend(bbox_to_anchor=(.85, 1.0), loc='upper left')
  plt.savefig(f'./images/{continent}.png')
  plt.close()


def generate_barh_chart(objects, performance, country, capital, continent):
  fig, ax = plt.subplots(figsize=(9, 6))

  y_pos = np.arange(len(objects))

  ax.barh(y_pos, performance, color=palette)
  plt.yticks(y_pos, objects)

  ax.spines['right'].set_visible(False)
  ax.spines['top'].set_visible(False)
  ax.spines['left'].set_visible(False)
  ax.spines['bottom'].set_visible(False)

  plt.xticks(fontsize='8.5', weight='bold', color='#7e807e')
  plt.yticks(fontsize='8.5', weight='bold', color='#7e807e')
  # Remove x, y Ticks
  ax.xaxis.set_ticks_position('none')
  ax.yaxis.set_ticks_position('none')

  plt.title("Population of " + country + " - " + capital + " - " + continent, size=12, weight="bold", fontfamily="sans", color="#080404", horizontalalignment = "left", x=0.12, y=0.96, transform = fig.transFigure)
  plt.suptitle("From the year 1970 to the year 2022", size=10, weight="bold", fontfamily="sans", color="#080808", horizontalalignment = "left", x=0.12, y=0.94, transform = fig.transFigure)

  plt.xlabel('Populations in (K - thousands & M - millions)', labelpad=8, size=10, fontfamily="sans", weight="bold")
  plt.ylabel('Years census', labelpad=8, size=10, fontfamily="sans", weight="bold")

  plt.grid(color='grey', linestyle='-.', linewidth=0.5, alpha=0.4)

  for i in ax.patches:
    width = i.get_width()
    num = width/1e6
    # formatter 'x' axis K-thousands & M-millions
    plt.gca().xaxis.set_major_formatter(FuncFormatter(format_population))
    # text formatter
    if width >=1000000:
      text_values = "{:.3f}M".format(num)
    else:
      text_values = "{:.3f}k".format(num * 1000)

    plt.text(i.get_width()+0.2, i.get_y()+0.27, text_values, fontsize=8, fontweight='bold', color='grey')

  plt.savefig(f'./images/{country}.png')
  plt.close()

def generate_plot_chart(x_points, y_points, country, capital, continent):
  fig, ax = plt.subplots(figsize=(9,6))
  ax.plot(x_points, y_points, linestyle='dashed', color='green', linewidth=1.5, marker='o', markerfacecolor="blue", markersize=3.5)

  ax.spines['right'].set_visible(False)
  ax.spines['top'].set_visible(False)
  ax.spines['left'].set_visible(False)
  ax.spines['bottom'].set_visible(False)

  plt.xticks(fontsize='8.5', weight='bold', color='#7e807e')
  plt.yticks(fontsize='8.5', weight='bold', color='#7e807e')
  # Remove x, y Ticks
  ax.xaxis.set_ticks_position('none')
  ax.yaxis.set_ticks_position('none')

  plt.title("Population of " + country + " - " + capital + " - " + continent, size=12, weight="bold", fontfamily="sans", color="#080404", horizontalalignment = "left", x=0.12, y=0.96, transform = fig.transFigure)
  plt.suptitle("From the year 1970 to the year 2022", size=10, weight="bold", fontfamily="sans", color="#080808", horizontalalignment = "left", x=0.12, y=0.94, transform = fig.transFigure)

  plt.xlabel('Years census', labelpad=8, size=10, fontfamily="sans", weight="bold")
  plt.ylabel('Populations in (K - thousands & M - millions)', labelpad=8, size=10, fontfamily="sans", weight="bold")

  plt.grid(color='grey', linestyle='-.', linewidth=0.5, alpha=0.4)

  for (xi, yi) in zip(x_points, y_points):
    num = yi/1e6
    # formatter 'x' axis K-thousands & M-millions
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_population))
    # text formatter
    if yi >= 1000000:
      text_values = "{:.3f}M".format(num)
      plt.text(xi, yi, text_values, ha='right', va='bottom', color='grey')
    else:
      text_values = "{:.3f}K".format(num * 1000)
      plt.text(xi, yi, text_values, ha='right', va='bottom', color='grey')
  
  plt.savefig(f'./images/{country}.png')
  plt.close()

def generate_line_chart(data, continent):
  fig, ax = plt.subplots(figsize=(15,8))
  
  countries_to_look_at = []
  for i in data:
    if i['Continent'] == str(continent): #'Europe'
      key, value = get_population(i)
      x_points = key
      y_points = list(map(int, value))

      if list(filter(lambda num: num > 10000000, y_points)):
        country = i['Country/Territory']
        countries_to_look_at.append(country)

        for (xi, yi) in zip(x_points, y_points):
          num = yi/1e6
          upper_yaxis = (lambda x, pos: '{0:g}M'.format(x/1e6))
          ax.yaxis.set_major_formatter(mticker.FuncFormatter(upper_yaxis))
          # text formatter
          upper_populations = {'Asia': 200000000, 'Europe': 65000000, 'Africa': 45000000, 'South America': 32000000, 'North America': 20000000, 'Oceania': 2000000}
          for key, value in upper_populations.items():
            if key == continent:
              if yi >= value:
                text_values = "{:.3f}M".format(num)
                plt.text(xi, yi, text_values, ha='right', va='bottom', color='grey')

        plt.plot(x_points, y_points, linestyle='dashed', linewidth=1.5, marker='o', markerfacecolor="blue", markersize=2.5)
      else:
        pass

  ax.spines['right'].set_visible(False)
  ax.spines['top'].set_visible(False)
  ax.spines['left'].set_visible(False)
  ax.spines['bottom'].set_visible(False)

  plt.xticks(fontsize='8.5', weight='bold', color='#7e807e')
  plt.yticks(fontsize='8.5', weight='bold', color='#7e807e')
  # Remove x, y Ticks
  ax.xaxis.set_ticks_position('none')
  ax.yaxis.set_ticks_position('none')

  continent = continent.replace('Europe', 'European')
  continent = continent.replace("Asia", "Asian")
  continent = continent.replace("Africa", "African")
  continent = continent.replace("North America", "North American")
  continent = continent.replace("South America", "South American")

  plt.title(f"Top of the countries with the most rapidly growing population of the {continent} continent ", size=12, weight="bold", fontfamily="sans", color="#080404", horizontalalignment = "left", x=0.12, y=0.96, transform = fig.transFigure)
  plt.suptitle("From the year 1970 to the year 2022", size=10, weight="bold", fontfamily="sans", color="#080808", horizontalalignment = "left", x=0.12, y=0.94, transform = fig.transFigure)

  plt.xlabel('Years census', labelpad=8, size=10, fontfamily="sans", weight="bold")
  plt.ylabel('Populations in (M - millions)', labelpad=8, size=10, fontfamily="sans", weight="bold")

  plt.grid(color='grey', linestyle='-.', linewidth=0.5, alpha=0.4)
  plt.legend(countries_to_look_at, bbox_to_anchor=(.96, 1.0), loc='upper left')
  plt.savefig(f'./images/{continent}.png')
  plt.close()

if __name__ == '__main__':
  pass

# 69343657