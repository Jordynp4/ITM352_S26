country_capitals = {
    "Germany": "Berlin",
    "canada": "Ottawa",
    "Endland": "London",}

print(country_capitals)

print(country_capitals["canada"])
print(country_capitals["Endland"])

country_capitals["Italy"] = "Rome"
print(country_capitals)

print("Germany" in country_capitals)
print("Spain" not in country_capitals)