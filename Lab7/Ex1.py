# Name: Jordyn Pendergrass
# Date: Feb 17, 2026

# Create a code that uses a for-statement to create a list of elements that are the odd numbers between 1 and 50

nums = []

# All odd numbers between 1 and 50
for num in range(1, 51):
    if num % 2 == 1:
        nums.append(num)

print(nums)
