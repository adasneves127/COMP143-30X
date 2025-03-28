# 3/28/25

# Dictionary Review
# Problems:
#   Get from a dictionary
#   Insert into a dictionary
#   Update a dictionary

my_dictionary = {
    "name": "Alex",
    "grade": 95
}

print(my_dictionary)

my_dictionary['advisor'] = "Margaret Black"
print(my_dictionary)
my_dictionary['advisor'] = "John Santore"
print(my_dictionary)

print(my_dictionary['name'])
print(my_dictionary.get('major', 'Undeclared'))

# print(list(my_dictionary.keys()))
# print(list(my_dictionary.values()))
# print(list(my_dictionary.items()))

for key in my_dictionary.keys():
    print(f"{key}: {my_dictionary[key]}")

for value in my_dictionary.values():
    print(value)

for key, value in my_dictionary.items():
    print(f"{key}: {value}")

# Functions (Quick Introduction)
# Questions:
#   What is a Function?
#       It is a thing that does a thing. Programmer definable.
#       Can take in arguments or parameters, and give back a value based on that data.
#   Do we know of any functions that we use?
#       len, print, max, min, all methods (string.upper(), list.sort()).
#   Functions are anything that have the parenthesis after it "()"

def my_function():
    print("Hello!")

my_function()

def my_function_with_args(x):
    return 2 * x + 5

for i in range(10):
    data = my_function_with_args(i)
    print(data)

# Do not uncomment. The code will crash.
# def crashing_function():
#     crashing_function()
#
# crashing_function()
