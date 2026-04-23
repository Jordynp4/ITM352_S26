# Create a scatter plot of fares by trip miles based JSON file
# Save the plot to a file called FaresXmiles.png
# Filter out trips of 0 miles.
# Filter out trips less than 2 miles

import matplotlib.pyplot as plt
import pandas as pd
import json

# Read in the data from the JSON file
trip_df = pd.read_json('Trips from area 8.json')


miles = []
fares = []

with open('Trips from area 8.json', 'r') as f:
    data = json.load(f)

for trip in data:
    try:
        trip_miles = float(trip['trip_miles'])
        fare = float(trip['fare'])
 
        # Filter out trips of 0 miles and trips less than 2 miles
        if trip_miles >= 2:
            miles.append(trip_miles)
            fares.append(fare)
    except (ValueError, KeyError):
        pass
 
print(f"Total trips after filtering: {len(miles)}")

fig = plt.figure()

plt.plot(miles, fares, marker='.', linestyle='none')
plt.title('Fares by Taxi Trip Miles')
plt.xlabel('Trip Miles')
plt.ylabel('Fare in $')
plt.savefig('FaresXmiles.png')
plt.show()


