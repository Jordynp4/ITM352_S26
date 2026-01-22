# an example of creating and use your own function
# Name: Jordyn Pendergrass
# Date: Jan 23, 2026

from os import name


def greet(name):
    """This function greets the person whose name is passed in. in addition we want to print a welcome message that includes the day of the week."""
    message = "Hello" + " " + name + "! " 
    return message

user_name = input("Please enter your name: ")
greeting_message = greet(user_name)
print(greeting_message)