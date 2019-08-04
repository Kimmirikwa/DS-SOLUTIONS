import pandas as pd
import numpy as np

# dataframe of the input data
input_data = pd.read_csv('data/input.csv')

# the columns of the dataframe
print(input_data.columns) # MSISDN, Network, Date, Product, Amount

# first 5 rows of the data
print(input_data.head())

# check for missing values
print(input_data.isnull().values.any())  # False, this dataframe does not have any missing values

# we need to extract a Month from a given data as we do not have month data given
# will use this function below
def get_month(row):
	return row['Date'][4:-1]

# add the month column
input_data['Month'] =  input_data.apply(lambda row: get_month(row), axis=1)

# we no longer need 'Date' column in our data
input_data.drop(['Date', 'MSISDN'], axis=1, inplace=True)

# the columns of the dataframe after adding 'Month' and dropping 'Date'
print(input_data.columns) # MSISDN, Network, Product, Amount, Month

# Aggregation: group the data by Network and Product, assumed sum aggregation for amount
agg_data = input_data.groupby(['Network', 'Product', 'Month']).agg({"Amount": [np.sum, np.size]})

agg_data.to_csv("output/Output.csv")
