import pandas as pd

# Loading dataset into dataframe
df = pd.read_csv("squirrel-data.csv")

# counting the number of suqirrels according to their colour
fur_grey_count = len(df[df["Primary Fur Color"] == "Gray"])
fur_black_count = len(df[df["Primary Fur Color"] == "Black"])
fur_cinnamon_count = len(df[df["Primary Fur Color"] == "Cinnamon"])
print(fur_grey_count)
print(fur_black_count)
print(fur_cinnamon_count)

# creating a dict of fur color
color_dict = {"fur_color":["Gray", "Black", "cinnamon"],
              "count" : [fur_grey_count, fur_black_count, fur_cinnamon_count]
              }

# creating dataframe from color dict
df_dict = pd.DataFrame(color_dict)

# exporting the df_dict dataframe to csv file
df_dict.to_csv("squirrel_color_count")

# printing the df_dict
print(df_dict)

