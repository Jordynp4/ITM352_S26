# Create a chart of trip payment type

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Read in the data from the JSON file
trip_df = pd.read_json('Trips from area 8.json')

# Extract the trips and payment type data
trips_df = trip_df[['tips', 'payment_type']]

# Clean up the data
trips_df = trips_df.dropna()
trips_df = trips_df.astype({'tips': float})
trips_df = trips_df.set_index('payment_type')

# Sum tthe tis by payment type
tips_by_payment = trips_df.groupby('payment_type').sum()

x_labels = pd.Series(tips_by_payment.index.values)
y_values = pd.Series(tips_by_payment['tips'].values)

bars = np.array(range(len(x_labels)))
plt.xticks(bars, x_labels, color='red', fontweight='bold')

# Create a bar chart of the tips by payment type
plt.bar(bars, y_values)
plt.title('TaxiTips by Payment Type')
plt.xlabel('Payment Type')
plt.ylabel('Total $ in Tips')

plt.show()