import json

filename = "quiz_data.json"

with open(filename, 'r') as jsonfile:
    quiz_data = json.load(jsonfile)
    
    
print("Quiz Data:")
for question, answers in quiz_data.items():
    print(f"\nQuestion: {question}")
    for option in answers:
        print(f"- {option}")