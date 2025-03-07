
students = [
    ("Alex", 95),
    ("Thomas", 80),
    ("Jane", 76)
]

threshold = 80
students_above_threshold = []

for student in students:
    if student[1] >= threshold:
        # print(f"{student[0]} has exceeded the grade threshold of {threshold} with a grade of {student[1]}")
        students_above_threshold.append(student)

print(students_above_threshold)

random_list = [20, 49, 29, 40, 1, 84, 92]

# Assume! The 0th element is both the max and the min!
maximum = random_list[0]
minimum = random_list[0]

# Check our assumptions!
for number in random_list:
    if number < minimum:
        minimum = number

    if number > maximum:
        maximum = number

print(maximum)
print(minimum)

average = 0

# Check if the list is empty. If not, calculate the average.
if len(random_list) > 0:
    average = sum(random_list) / len(random_list)

print(average)


