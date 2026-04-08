# Retrieve mortgage rate info 
# Find the rate table and extract each row
# Output the name of each bank and its current rates per row

import requests
from bs4 import BeautifulSoup

url = "https://www.hicentral.com/hawaii-mortgage-rates.php"

print("Opening URL: " + url)

response = requests.get(url)
results = BeautifulSoup(response.content, "html.parser")

# Extract and print each row of the mortgage rates table
rows = results.find_all("tr")
for row in rows:
    columns = row.find_all("td")
    if columns:
        bank = columns[0].text.strip()
        loan_type = columns[0].text.strip()
        rate = columns[1].text.strip()
        points = columns[2].text.strip()
        apr = columns[3].text.strip()
        
        print("Bank:", bank)
        print("Loan Type:", loan_type)
        print("Rate:", rate)
        print("Points:", points)
        print("APR:", apr)

for column in columns:
    results.append(column.text.strip())

print(results)



