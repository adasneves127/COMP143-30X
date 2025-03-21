# Student Grade Manager Application

# 1. Data Initialization
student_data = []

# 2. Adding Students
student_data.append(("Alex", 85))
student_data.append(("Thomas", 69))
student_data.append(("James", 91))

# 3. Displaying Students
for student in student_data:
    print(f"{student[0]} - {student[1]}")

# 4. Calculate Average Grade

# Method 1:
if len(student_data) != 0:
    total = 0
    for student in student_data:
        total += student[1]
    print(f"Average: {total / len(student_data)}")


# Method 2:
if student_data:
    print(f"Average: {sum([student[1] for student in student_data]) / len(student_data)}")

# 5. Finding highest and lowest grades.

# Part A. Use max() and min()
max_a = max([student[1] for student in student_data])
min_a = min([student[1] for student in student_data])

# Part B. Do not use min, max, or sort.
max_b = student_data[0][1]
min_b = student_data[0][1]
for student in student_data:
    if max_b < student[1]:
        max_b = student[1]
    elif min_b > student[1]:
        min_b = student[1]

print(f"Part A: Max: {max_a}, Min: {min_a}")
print(f"Part B: Max: {max_b}, Min: {min_b}")

# 6. Filter Students above a threshold.
threshold = 85
for student in student_data:
    if student[1] > threshold:
        print(f"{student[0]} has exceeded the threshold grade of {threshold}, with a grade of {student[1]}")

a = 15
while a != 1: # This loop exits if and only if a == 1
    a = a // 2
    print(a)

user_input = input("What is your name? [Type 'q' to quit!] ")
while user_input != 'q':
    print(f"Nice to meet you, {user_input}")
    user_input = input("What is your name? [Type 'q' to quit!] ")


print("Menu System:")
print("1. Clear List")
print("2. Add Student")
print("3. Display Students")
print("4. Calculate Average")
print("5. Find max and min of grades")
print("6. Filter with Threshold")
print("7. Quit")
menu_option = input("Please choose an option from the list above. ")
while menu_option != '7':
    if menu_option == '1':
        student_data.clear()
    elif menu_option == '2':
        student_name = input("Student Name: ")
        student_grade = input("Student Grade: ")
        if student_grade.isdigit():
            student_grade = int(student_grade)
        else:
            print("Invalid Input.")
            exit(1)
        student_data.append((student_name, student_grade))
    elif menu_option == '3':
        for student in student_data:
            print(f"{student[0]} - {student[1]}")
    elif menu_option == '4':
        if student_data:
            print(f"Average: {sum([student[1] for student in student_data]) / len(student_data)}")
    elif menu_option == '5':
        max_a = max([student[1] for student in student_data])
        min_a = min([student[1] for student in student_data])
        print(f"Max Grade: {max_a}, Min Grade: {min_a}")
    elif menu_option == '6':
        threshold = input("Enter a grade to filter by: ")
        if threshold.isdigit():
            threshold = int(threshold)
        else:
            print("Invalid Input.")
            exit(1)
        for student in student_data:
            if student[1] > threshold:
                print(f"{student[0]} has exceeded the threshold grade of {threshold}, with a grade of {student[1]}")
    else:
        print("Invalid Input. Please choose a valid option.")
    menu_option = input("Please choose an option from the list above. ")
