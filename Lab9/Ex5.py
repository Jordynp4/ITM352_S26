import json

QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles/hr?": ["12", "24", "36", "48"],
    "What is the capital of Texas?": ["Austin", "Houston", "Dallas", "San Antonio"],
    "The Last Supper was painted by which artist?": ["Da Vinci", "Michelangelo", "Donatello", "Raphael"]
}

filename = "quiz_data.json"

with open(filename, 'w') as jsonfile:
     json.dump(QUESTIONS, jsonfile, indent=4)
print(f"Quiz data has been written to {filename}.")