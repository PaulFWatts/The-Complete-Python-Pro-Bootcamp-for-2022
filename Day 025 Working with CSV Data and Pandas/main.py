# import csv

# with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#   temperatures = []
#  for row in data:
#      if row[1] != "temp":
#           temperatures.append(int(row[1]))
#   print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)
print()

temp_list = data["temp"].to_list()
print(temp_list)
print()

# Calculate the average temperature
average_temp = sum(temp_list) / len(temp_list)
print(f'{average_temp:.2f}')
print()

# Use Pandas to calculate the average temperature
average_temp = data["temp"].mean()
print(f'{average_temp:.2f}')
print()

# Use Pandas to calculate the maximum temperature
max_temp = data["temp"].max()
print(max_temp)
print()

# Get data in columns
print(data["condition"])
print(data.condition)
print()

# Get data in rows
print(data[data.day == "Monday"])
print()
print(data[data.temp == data.temp.max()])
print()

monday = data[data.day == "Monday"]  # Get data for Monday
monday_temp = int(monday.temp)  # Get the temperature for Monday
monday_temp_F = monday_temp * 9 / 5 + 32  # Convert to Fahrenheit
print(monday_temp_F)
print()

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)  # Create a dataframe from the dictionary
data.to_csv("new_data.csv")  # Save the dataframe to a CSV file
print(data)
print()


