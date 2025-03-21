# Project 2:

# Step 1: Data Initialization:
student_data = []

# Step 2: Add Students
student_data.append(("Alex", 96))
student_data.append(("Thomas", 67))
student_data.append(("Caleb", 79))

# Step 3: Diplay Students
for student in student_data:
    print(f"{student[0]} - {student[1]}")

# Step 4: Calculating Average Grade
total = 0
for student in student_data:
    total += student[1]

if student_data:
    print(f"Average Grade: {total / len(student_data)}")

if student_data:
    print(f"Average Grade: {sum([student[1] for student in student_data]) / len(student_data)}")

# Step 5:
min_a = min([student[1] for student in student_data])
max_a = max([student[1] for student in student_data])

min_b = student_data[0][1]
max_b = student_data[0][1]
for student in student_data:
    if student[1] < min_b:
        min_b = student[1]

    if student[1] > max_b:
        max_b = student[1]

print(f"Min and Max gave a min of {min_a} and a max of {max_a}")
print(f"Searching gave a min of {min_b} and a max of {max_b}")

# Step 6:

threshold = 74
for student in student_data:
    if student[1] > threshold:
        print(f"Student {student[0]} has exceeded the grade threshold of {threshold} with a grade of {student[1]}")

filtered_students = [
    student for student in student_data if student[1] > threshold
]

for student in filtered_students:
    print(f"Student {student[0]} has exceeded the grade threshold of {threshold} with a grade of {student[1]}")


# Definite Loops. Python will always know how many times to iterate (even if the programmer doesn't)
for i in range(10):
    print(i)

# Indefinite loop. Python will not know how many times to iterate!
x = 65
while x > 1:
    x = x // 2

print(x)


# Project 2 -- Electric Boogaloo
print("1. Empty Student List")
print("2. Add Student to List")
print("3. Print Student List")
print("4. Calculate Average Grade")
print("5. Find Max and Min Grade")
print("6. Filter by Grade")
print("0. Quit")
user_input = input("Please choose an option: ")

while user_input != "0":
    if user_input == "1":
        student_data.clear()
    elif user_input == "2":
        student_name = input("Name: ")
        student_grade = int(input("Grade: "))
        student_data.append((student_name, student_grade))
    elif user_input == "3":
        for student in student_data:
            print(f"{student[0]} - {student[1]}")
    elif user_input == "4":
        if student_data:
            print(f"Average Grade: {sum([student[1] for student in student_data]) / len(student_data)}")
    elif user_input == "5":
        min_a = min([student[1] for student in student_data])
        max_a = max([student[1] for student in student_data])
        print(f"Min Grade: {min_a}, Max Grade: {max_a}")
    elif user_input == "6":
        threshold = int(input("Enter a threshold: "))
        for student in student_data:
            if student[1] > threshold:
                print(f"Student {student[0]} has exceeded the grade threshold of {threshold} with a grade of {student[1]}")
    else:
        print("Invalid Option")

    print("1. Empty Student List")
    print("2. Add Student to List")
    print("3. Print Student List")
    print("4. Calculate Average Grade")
    print("5. Find Max and Min Grade")
    print("6. Filter by Grade")
    print("0. Quit")
    user_input = input("Please choose an option: ")
