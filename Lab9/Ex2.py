import csv
import os

filename = "Employee_data.csv"
salaries = []

if os.path.exists(filename):

    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Skip the header row
        salary_index = header.index("Annual_Salary")   
        
        print(header)  # Print the header row
        for row in reader:
            print(row)
            salaries.append(float(row[salary_index]))

    print(salaries)
    if (salaries):
        average_salary = sum(salaries) / len(salaries)
        print(f"Average Salary: ${average_salary:.2f}")
        max_salary = max(salaries)
        print(f"Maximum Salary: ${max_salary:.2f}")
        min_salary = min(salaries)
        print(f"Minimum Salary: ${min_salary:.2f}")
    else:
        print("No salary data found.")
else:
    print("Error: File does not exist.")