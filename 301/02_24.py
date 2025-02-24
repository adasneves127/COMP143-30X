
my_list = ["Apple", "Banana", "Cherry", "Tomato", "Pineapple", "Avocado"]

for item in my_list:
    print(item)

# List Assignment does not make a copy of the list,
# it makes a reference to the existing list.
list_2 = my_list
list_2[2] = "Cucumber"
print(my_list)

# Booleans (bool) are special.
# They have only 2 values. True, and False.
number_1 = 10
number_2 = 20

# is number_1 greater than number 2?
print(number_1 > number_2)

# is number 2 greater than number 1?
print(number_1 < number_2)

number_10 = "bear"
number_7 = "deer"
# is bear less than deer?
print(number_10 < number_7)

# Python Comparisons:
# Greater Than (>)
# Less Than (<)
# Greater Than or Equal To (>=)
# Less Than or Equal to (<=)
# Equal To (==) [Not to be confused with assignment operator (=)]
# Not Equal To (!=)
string_1 = "Hello"
string_2 = "HELLO"
print(string_1 == string_2)

# Logical Connectives
# Python has 3 Logical Connectives:
# and -- Both sides must be true for the result to be true.
# or  -- Either side must be true for the result to be true.
# not -- Inverts the conditional following.
a = True
b = False
c = True

print(a or b)
print(a and b)
print(a and (b or c))
print(a and not b)