# Get a JSON file from city of Chicago's data portal and analyze driver types

import pandas as pd
import requests

# Create a REST quary to get the JSON data for driver types

search_results = requests.get("https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count%28license%29&$group=driver_type")

results_json = search_results.json()
print("Driver Types and their Counts:")
print(results_json)

# Convert the JSON results to a pandas DataFrame
results_df = pd.DataFrame(results_json)
results_df.columns = ["Driver Type", "Count"]
results_df = results_df.set_index("Driver Type")

print("\nDriver Types and their Counts (DataFrame):")
print(results_df)