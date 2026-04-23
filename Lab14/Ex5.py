# Create a scatterplot of trip miles vs fares
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Read in the data from the JSON file
trip_df = pd.read_json('Trips from area 8.json')

trip_miles_gt_0 = trip_df[['trip_miles', 'fare']].query('trip_miles > 0')
fare_series = trip_miles_gt_0['fare']
trip_series = trip_miles_gt_0['trip_miles']

fig = plt.figure()

plt.plot(fare_series, trip_series, marker='v', linestyle= 'none', color='c', alpha=0.2)
plt.title('Fares by Taxi Trip Miles')
plt.xlabel('Fare in $')
plt.ylabel('Trip Miles')
plt.show() 

