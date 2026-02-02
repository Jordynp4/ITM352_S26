# string manipulation examples

first = input("Enter your first name:  ")
MiddleIn = input("Enter your middle initial:  ")
last = input("Enter your last name:  ")

#full_name = (f'{first} {MiddleIn}. {last}')
#print("Your full name is:  ", full_name)

#full_name_2 = "first: %s, middle initial: %s, last: %s" % (first, MiddleIn, last)
#print("Your full name is:  ", full_name_2)

#full_name_3 = "first: {}, middle initial: {}, last: {}".format(first, MiddleIn, last)
#print("Your full name is:  ", full_name_3)

#full_name_4 = " ".join([first, MiddleIn + ".", last])
#print("Your full name is:  ", full_name_4)

#unpaking the list as the argument usinf the format method
full_name_5 = "first: {0}, middle initial: {1}, last: {2}".format(*[first, MiddleIn, last])
print("Your full name is:  ", full_name_5)
