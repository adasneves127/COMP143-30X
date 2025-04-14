# Files

# What are files
#   Long-Term (Persistent) storage
#   What are some examples of file?
#       .py, .txt, .bin, .exe, .dll, .jpg, .webp, .png
#   Binary Files (Data Files) and Text Files

var_1 = "This is a test!"
var_2 = 15

file = open("test.txt", 'w')

file.write(var_1)
file.write('\n')
file.write(str(var_2))

file.close()


file_2 = open("test.txt", 'r')

print(file_2.readlines())
file_2.seek(0)
for line in file_2:
    print(line, end="")
print()

file_2.close()

import json

with open("data.json", 'r') as data_file:
    data = json.load(data_file)

my_dictionary = {
    "name": "Alex",
    "age": 21,
    "location": "Bridgewater",
    "siblings": ["Reagan", "Milly"],
    "courses": {
        "COMP151": "Margaret Black",
        "COMP250": "Sean Stanley"
    }
}

with open("my_data.json", 'w') as out_file:
    json.dump(my_dictionary, out_file, indent=4)
