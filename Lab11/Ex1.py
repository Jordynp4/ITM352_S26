# read in a CSV file with sales data, called sales_data.csv into a dataframe
# print the first 5 rows and show the data types of the columns

import pandas as pd
import numpy as np
import pyarrow

filename = 'Sales_data.csv'

pd.set_option('display.max_columns', None) #show all columns in the output

df = pd.read_csv(filename, engine='pyarrow')
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

print(df.info())
print(df.describe())
print(df.head(5))