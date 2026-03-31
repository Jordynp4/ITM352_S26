# read in a CSV file and create a dataframe
# pivot the dataframe, aggregate sales by region, columns defined by order type and totals.
# add in sub-columns showing the average sales by state and by sale type (retail or wholesale)

import pandas as pd
import numpy as np
import pyarrow

filename = 'Sales_data.csv'

pd.set_option('display.max_columns', None) #show all columns in the output
pd.set_option('display.float_format', '{:,.2f}'.format) #format floats to 2 decimal places

df = pd.read_csv(filename, engine='pyarrow')
df['order_date'] = pd.to_datetime(df['order_date'], format='%m/%d/%y', errors='coerce')

#coerce quantity and unit_price to numeric, setting errors to null
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')
df['sales'] = df['quantity'] * df['unit_price'] # Calculate sales as quantity multiplied by unit price

state_col = 'customer_state'

pivot_table = pd.pivot_table(df,
                             index= 'sales_region',
                             values= 'sales',
                             columns= ['order_type', state_col],
                             aggfunc= [np.sum, np.mean],
                             margins= True,
                             margins_name= 'Total_Sales')
print(pivot_table)