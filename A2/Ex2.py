# read in a CSV file and save a local CSV file with the first 10 rows.
# 

import time

import pandas as pd
import numpy as np
import pyarrow

filename = 'Sales_data.csv'

def load_csv(filepath):
    print(f"Loading data from {filepath}...")
    start_time = time.time()
    try:
        df = pd.read_csv(filepath, engine='python')
        end_time = time.time()
        load_time = end_time - start_time
        print(f"CSV file loaded successfully in {load_time:.2f} seconds.")
        print(f"number of rows: {len(df)}")
        print(f"columns: {df.columns.tolist()}")

        required_columns = ['quantity', 'unit_price', 'order_date']
        # Check if all required columns are present
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            print(f"Warning: Missing required columns: {missing_columns}")
        else:
            print("All required columns are present.")

        
        return df
    
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None


# Call load_csv to load the data amd print the first 10 rows
filename = 'Sales_data.csv'
#filename = 'Sales_data_test.csv'
sales_data = load_csv(filename)

print(sales_data.head(10))