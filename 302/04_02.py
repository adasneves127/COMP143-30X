my_dictionary = {}

my_dictionary['key'] = 'value'


# Functions
#   Blocks of code that can be reused.
#   Examples: print(), sum(), len(), max(), min(), input()
#   Functions have parenthesis after their name.

# We can create a function using the following syntax:
# def <function-name>():
#    <function-body>

# Example:
def my_function():
    print("This is called from my_function! Now I added some extra text!")

# my_function()
# my_function()
# my_function()

# We can add parameters to our function using variables inside our parenthesis.
# These variables are to be defined when we "call" or "invoke" our function.
def my_function_with_params(name, age):
    print(f"Nice to meet you, {name}! You are {age} years old!")
    test_list = [1,2,3,4,5]
    print(test_list)
#
# my_function_with_params("Alex", 21)
# my_function_with_params("Tyler", 30)

# Random Library
# Randomness. What is it?

import random
# random.seed(100)
print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.random())
print(random.randrange(0, 101, 2))
print(random.uniform(1, 100))

import datetime
print(datetime.datetime.now() + datetime.timedelta(hours=4))
print(datetime.datetime.now().strftime("%m/%d/%Y %H:%M %I"))
print(datetime.datetime.now().strftime("%s"))


