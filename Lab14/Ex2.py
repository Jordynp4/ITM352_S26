# Create a histogram from the trip miles data

import matplotlib.pyplot as plt
import pandas as pd

# Read in the data from the JSON file
trip_df = pd.read_json('Trips from area 8.json')
# Ectract the trip miles data
trip_miles_series = trip_df['trip_miles']

fig = plt.figure()

# Create a histogram of the trip miles data
plt.hist(trip_miles_series)
plt.title('Distribution of Taxi Trip Miles')
plt.xlabel('Trip Miles')
plt.ylabel('Frequency')
plt.show()