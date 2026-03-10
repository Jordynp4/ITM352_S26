with open("names.txt") as file_object:
    while (line := file_object.readline()):
        print(line.strip())
    