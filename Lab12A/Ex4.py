# Get public liscense data from the city of Chicago's data portal

import pandas as pd
from sodapy import Socrata

# Create a sodapy client to access the data portal
client = Socrata("data.cityofchicago.org", None)

# Specify the JSON file for liscense data
json_file = "rr23-ymwb"

results = client.get(json_file, limit=500)
# Convert the results to a pandas DataFrame
df = pd.DataFrame.from_records(results)

#print(df.head())

vehicles_and_fuel_sources = df[["public_vehicle_number", "vehicle_fuel_source"]]
print("Public Vehicle Number and their Fuel Sources:")
#print(vehicles_and_fuel_sources.head())

vehicles_by_fuel_source = vehicles_and_fuel_sources.groupby("vehicle_fuel_source").count()
print("Number of Public Vehicles by Fuel Source:")
print(vehicles_by_fuel_source)