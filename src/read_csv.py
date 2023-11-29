import csv
from shutil import get_terminal_size


def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      # print('=' * get_terminal_size().columns)
      data.append(country_dict)
    return data
  
if __name__ == '__main__':
  pass
  # data = read_csv('../db/data.csv')
  # print(data)
