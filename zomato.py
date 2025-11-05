import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataframe = pd.read_csv("Zomato-data-.csv")
print(dataframe.head())

def handlerate(value):
    value=str(value).split("/")
    value=value[0]
    return float(value)

dataframe["rate"] = dataframe["rate"].apply(handlerate)
print(dataframe.head())

sns.countplot(x=dataframe['listed_in(type)'])
plt.show()

#4
grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data}) 
plt.plot(result, c='green', marker='o') 
plt.xlabel('Type of restaurant') 
plt.ylabel('Votes')
plt.show()

#5
restaurant_rate = dataframe['votes'].max()
restaurant = dataframe.loc[dataframe['votes'] == restaurant_rate, 'name']
print(restaurant)

#6 Online Order Availability
sns.countplot(x=dataframe['online_order'])
plt.show()

#7 analyze ratings
sns.histplot(dataframe['rate'], bins=20)
plt.show()

#8 approximate cost for couples 
sns.histplot(dataframe['approx_cost(for two people)'], bins=20)
plt.show()

#9 online vs offline orders
pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
print(type(pivot_table))
