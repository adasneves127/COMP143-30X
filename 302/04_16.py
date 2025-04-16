
# What is a file?
#   Persistent Storage (Retains Data)
#   We can use them to store and recall data about our program's variables.
# What are some examples of files?
#   pdf, png, exe, dll, elf, py, txt, csv
# There are really only 2 types of files. Binary Files and Text-Based Files
# Binary Files: pdf, png, exe, dll, elf
# Text-Based: py, txt, csv

file = open("test.txt", "w")
file.write("My name is Alex.\n")
file.write("32")
file.close()

file_2 = open("test.txt", "r")
print(file_2.readline())
print(int(file_2.readline()))
file_2.close()

# Reading data from JSON (Preserves Types)
import json
with open("data.json", 'r') as file:
    print(json.load(file)['data'][0]['attributes']['bearing'])

my_dictionary = {
    "name": "Alex Dasneves",
    "advisor": "Dr. Black",
    "classes": [
        "COMP151", "COMP250", "COMP206"
    ],
    "bannerID": 4123456
}

with open("out.json", 'w') as file:
    json.dump(my_dictionary, file, indent=4)



file_2 = open("test.txt", "r")
for line in file_2:
    print(line.strip())
file_2.close()

