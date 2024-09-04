# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
# print(len(data))
# temp_list = data["temp"].to_list()
# print(data["temp"].mean())
# print(data["temp"].max())

# print(data.condition)

# Get data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# create a dataFram from scratch
# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores" : [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}
df = pd.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")