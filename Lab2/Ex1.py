# ask the user for a number between 1 and 100. Square the number and its square.
# Name: Jordyn Pendergrass
# Date: Jan 20, 2026

print("Welcome to the Program!")
value_entered = input("please enter a number between 1 and 100: ")
print("You entered:", value_entered)

value_as_interger = int(value_entered)
squared_value = value_as_interger ** 2
#print("The square of", value_as_interger, "is", squared_value)
print(f"The square of {value_as_interger} is {squared_value}")