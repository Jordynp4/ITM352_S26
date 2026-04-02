# read in a CSV file and save a local CSV file with the first 10 rows.
# 

import pandas as pd
import numpy as np
import pyarrow

filename = 'Sales_data.csv'

df = pd.read_csv(filename, engine='pyarrow')

out_file = "sales_data_test.csv"
df.head(10).to_csv(out_file, index=False)