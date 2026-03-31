


import pandas as pd
import numpy as np

filename = 'Sales_data.csv'

pd.set_option('display.max_columns', None) #show all columns in the output

df = pd.read_csv(filename, engine='pyarrow')

print(df.info())
print(df.describe())
print(df.head(5))