# Data Types:
# Strings   -- Str
# Integers  -- Int
# Floats    -- Float
# Lists     -- List
# Tuples    -- Tuple
# Booleans  -- Bool
# Dictionaries- Dict

# Dictionaries... What are they?
my_dict = {
    "name": "Alex",
    "grade": 96,
    "courses": {}
}

# Getting from the dictionary
# print(my_dict['advisor']) # Since there is no advisor, this crashes.
print(my_dict.get('advisor', 'No Advisor.'))

# Update the dictionary
my_dict['grade'] = 81
print(my_dict)

# Insert into the dictionary
my_dict['GPA'] = 3.5
print(my_dict)

# Deleting from the dictionary
my_dict.pop('GPA')
print(my_dict)

del my_dict['grade']
print(my_dict)

copy_dictionary = my_dict.copy()

# What is a function?
#   A set of instructions
#   Re-usable
#   Typically accomplishes one end-goal


def my_function():

    print("Menu:")
    print("1. Clear List")
    print("2. Add Student")
    print("3. Display Students")
    print("4. Calculate Average")
    print("5. Find max and min of grades")
    print("6. Filter with Threshold")
    print("7. Quit")
    return input("Please choose an option from above: ")


choice = my_function()
print(choice)


choice = my_function()
print(choice)
