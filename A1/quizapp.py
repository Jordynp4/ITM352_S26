# Name: Jordyn Pendergrass
# Date: March 5, 2026

# Create a quiz application that asks the user 5 multiple-choice questions. Each question should have 4 options, and the user should input their answer (A, B, C, or D). 
# At the end of the quiz, the application should calculate and display the user's final score as a percentage.

QUESTIONS = { 
    "What kind of magical creature is Shrek?": ["Ogre", "Giant", "Troll","Centaur"],
    "What is the name of the princess Shrek rescues?": ["Fiona", "Rapunzel", "Cinderella", "Snow White"],
    "What does Shrek turn into after drinking the Happily Ever After potion?": ["Human", "Fairy", "Horse", "Elf"],
    "Who is the main antagonist in the second Shrek movie?": ["Fairy Godmother", "Lord Farquaad", " King Harold", "Prince Charming"],
    "What is the name of the giant ginerbread man in Shrek 2?": ["Mongo", "Gingy", "gum drop", "cookie"]
}


for question, options in QUESTIONS.items():
    correct_answer = options[0]  # The first option is the correct answer
    for alternative in sorted(options):
        print(f"  - {alternative}")

    answer = input(question + ": ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is '{correct_answer}' not '{answer}'")