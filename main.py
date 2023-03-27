# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#
#
# print(temperature)
#
# import pandas as pd
#
# data = pd.read_csv('weather_data.csv')
#
# temp_list = data['temp'].to_list()
# # print(data['temp'].mean())
# # print(data['temp'].max())
# # print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == 'Monday']
# # printing fahrenheit from Celsius
# print((monday.temp * 1.8) + 32)

import pandas as pd

df = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
squirrel_count = df['Primary Fur Color'].groupby(df['Primary Fur Color']).count().to_dict()

val1 = []
val2 = []
for key, value in squirrel_count.items():
    val1.append(key)
    val2.append(value)

data = pd.DataFrame({'Fur Color': val1, 'Count':val2})
data.to_csv('squirrel_count.csv')