# File IO

# What is a file?
#   "Persistent" storage
# What are different types of files?
#   .txt, .exe, .rar, .bin, .webp, .png, .jpg/.jpeg, .dll, .zip, .py, .c, .cpp, .cs, .ini, .cfg
#   Text-Based Files - .txt, .py, .c, .cpp, .cs, .ini, .cfg
#   Data/Binary Files- .exe, .rar, .bin, .webp, .png, .jpg, .dll, .zip

file = open("./test.txt")

for line in file:
    print(line.rstrip())
file.close()

# second_file = open("./name.txt", "w")
# user_name = input("What is your name? ")
# second_file.write(user_name)
# second_file.close()


import json
with open("data.json") as file:
    data = json.load(file)

print(type(data))

with open("data2.json", 'w') as file:
    json.dump(data, file, indent=4)
