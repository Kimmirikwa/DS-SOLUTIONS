import pandas as pd

# dataframe of the input data
input_data = pd.read_csv('data/input.csv')

# the columns of the dataframe
print(input_data.columns) # MSISDN, Network, Date, Product, Amount

# first 5 rows of the data
print(input_data.head())

# check for missing values
print(input_data.isnull().values.any())  # False, this dataframe does not have any missing values