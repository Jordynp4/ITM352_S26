emotions = ("sad", "angry", "fear", "surprise", "happy")

# Write code that uses a conditional expression (do not use an if-statement or ternary expression) to print “true” if the last element is “happy” and there are more than 3 elements, or “false” if it is not

result = emotions[-1] == "happy" and len(emotions) > 3
#print(result)

# rewrite the above code using an if-statement instead of a conditional expression
if(result == True):
    print("true")
else:
    print("false")
