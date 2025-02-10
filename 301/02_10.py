my_greeting = "Hello, World!"
my_greeting = my_greeting + " Here is some other text!"
print(my_greeting)

# Must not:
#   * Start with a number
#   * Contain any "special character", other than _
#   * Cannot be a python keyword.


# Should be: (Guidelines)
#   * All lowercase
#   * Underscores separating words


# Variable Names:
# my_name         # Is valid.  Also follows the "guidelines" for a name.
# 2ndName         # Not Valid. Starts with a number
# student-list    # Not Valid. Contains a -
# AdvisorName     # Is valid.  Does not follow the "guidelines"

student_name = "JoHn SmItH"

print(student_name)
print(student_name.upper(), student_name.lower(), student_name.title())
print(student_name)

# This is a list.
student_list = ["John", "Adam", "James", "Kyle", "Tyler"]
print(student_list[0])

# Insert into a list
student_list.insert(0, "Zach")
student_list.append("Katie")

student_list.pop()
student_list.remove("John")
del student_list[2]

# While string methods do not modify the sting, list methods do modify the list
print(student_list)
student_list.sort(reverse=True)
# Preview into next week:
for name in student_list:
    print(name)
