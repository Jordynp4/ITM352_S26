# Append a new name at the end of the file.

with open("names.txt") as file_object:
    contents_list = file_object.readlines()
    print(contents_list)
    

with open("names.txt", "a") as file_object:
    print("appending new name to the file...")
    file_object.write("Williams, Venus\n") 
    contents_list.append("Williams, Venus\n")
    print(f"Number of names: {len(contents_list)}")
