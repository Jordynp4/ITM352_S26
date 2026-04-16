# Name: Jordyn Pendergrass
# Date: March 5, 2026

# Create a quiz application that asks the user 5 multiple-choice questions. Each question should have 4 options.
# Allow the user to select correct answer by a label. 
# At the end of the quiz, the application should calculate and display the user's final score as a percentage.

from string import ascii_lowercase

QUESTIONS = { 
    "What kind of magical creature is Shrek?": ["Ogre", "Giant", "Troll","Centaur"],
    "What is the name of the princess Shrek rescues?": ["Fiona", "Rapunzel", "Cinderella", "Snow White"],
    "What does Shrek turn into after drinking the Happily Ever After potion?": ["Human", "Fairy", "Horse", "Elf"],
    "Who is the main antagonist in the second Shrek movie?": ["Fairy Godmother", "Lord Farquaad", " King Harold", "Prince Charming"],
    "What is the name of the giant ginerbread man in Shrek 2?": ["Mongo", "Gingy", "gum drop", "cookie"]
}

score = 0
for num, (question, options) in enumerate(QUESTIONS.items(), start=1):
    print(f"Question {num}:")
    print(question)
    correct_answer = options[0]  # The first option is the correct answer
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(options)))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}. {alternative}")
    
    # input answer validation loop
    while True:
        answer_label = input("Enter answer here: ")
        if answer_label in labeled_alternatives:
            break
        print("Invalid input. Please enter a valid choice.")

    answer = labeled_alternatives.get(answer_label)
    if answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect!")

print(f"\nYour final score is {score}/{len(QUESTIONS)} ({score/len(QUESTIONS)*100:.1f}%)")


# Notify the user when they get a new high score.
high_score = 0
try:
    with open("quiz_scores.txt", "r") as file:
        for line in file:
            score_part = line.split("/")[0].replace("Score:", "").strip()
            previous_score = int(score_part)

            if previous_score > high_score:
                high_score = previous_score
except FileNotFoundError:
    high_score = 0

if score > high_score:
    print("New high score!")

# Write the history of scores out to a file
with open("quiz_scores.txt", "a") as score_file:
    score_file.write(f"Score: {score}/{len(QUESTIONS)} ({score/len(QUESTIONS)*100:.1f}%)\n")


