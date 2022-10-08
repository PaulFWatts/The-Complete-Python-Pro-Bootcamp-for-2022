# Central Park Squirrel Data Analysis
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(f'\nGrey Squirrels Count: {grey_squirrels_count}')
print(f'Red Squirrels Count: {red_squirrels_count}')
print(f'Black Squirrels Count: {black_squirrels_count}\n')

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
file_name = "squirrel_count.csv"
print(f'Creating File: {file_name}')
df.to_csv(file_name)
