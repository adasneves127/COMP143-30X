list_of_numbers = [1,2,3,4,5,6,7,8,9,10]
target_number = 15

# we want to know if target_number is in the list_of_numbers.
if target_number in list_of_numbers:
    print("Target is in the list!")
else:
    print("Target is not in the list!")

is_found = False
for element in list_of_numbers:
    if target_number == element:
        is_found = True

if is_found:
    print("Target is in the list!")
else:
    print("Target is not in the list!")


current_grade = 96
if current_grade >= 93:
    print("A")
elif current_grade >= 90:
    print("A-")
elif current_grade >= 87:
    print("B+")
elif current_grade >= 83:
    print("B")
elif current_grade >= 80:
    print("B-")
elif current_grade >= 77:
    print("C+")
elif current_grade >= 73:
    print("C")
elif current_grade >= 70:
    print("C-")
elif current_grade >= 65:
    print("D")
else:
    print("F")

name = input("What is your name? ")
print(f"Nice to meet you, {name}")