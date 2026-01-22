# ask the user to eneter a floating point number. square the number. 
# print out the original number and the squared result 
# Name: Jordyn Pendergrass
# Date: Jan 22, 2026

input_value = input("Please enter a floating point number: ")
float_value = float(input_value)
squared_value = float_value ** 2

# Round the number to 2 decimal places
squared_value = round(squared_value, 2)

print("You entered:", float_value)
print(f"The square value is: {squared_value}")