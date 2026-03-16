# Read the 1,000 lines of taxi data from the taxi_1000.csv file
# Calculate the total of all fares, average fare, and the max
# Trip distance

import csv

filename = "taxi_1000.csv"
with open(filename) as csvfile:
    csv_reader = csv.reader(csvfile)

    total_fare = 0.0
    max_distance = 0.0
    average_fare = 0.0
    num_rows = 0

    for line in csv_reader:
        if (num_rows == 0):
            fare_index = line.index("Fare")
            distance_index = line.index("Trip Miles")
            num_rows += 1
            continue
        if (num_rows > 0):
            tripfare = float(line[fare_index])
            tripDistance = float(line[distance_index])
            total_fare += tripfare
            if tripDistance > max_distance:
                max_distance = tripDistance
        num_rows += 1

    if num_rows > 0:
        average_fare = total_fare / (num_rows - 1)  # Subtract 1 for the header row

print(f"We read {num_rows - 1} rows of data.")
print(f"Total Fare: ${total_fare:.2f}")
print(f"Average Fare: ${average_fare:.2f}")
print(f" Max Trip Distance: {max_distance:.2f} miles")
         
