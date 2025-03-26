# Project 2:

# Step 1:

student_data = []

# Step 2:

student_data.append(("Alex", 95))
student_data.append(("Thomas", 67))
student_data.append(("Kyra", 75))

# Step 3:

for student in student_data:
    print(f"{student[0]} - {student[1]}")

# Step 4:
if student_data:
    total = 0
    for student in student_data:
        total = total + student[1]
    average = total/len(student_data)
    print(f"The average is: {average}")

    average = sum([student[1] for student in student_data])/len(student_data)

# Step 5:
max_a = max([student[1] for student in student_data])
min_a = min([student[1] for student in student_data])

max_b = student_data[0][1]
min_b = student_data[0][1]
for student in student_data:
    if student[1] > max_b:
        max_b = student[1]
    if student[1] < min_b:
        min_b = student[1]

print(f"Using max and min: Max: {max_a}, Min: {min_a}")
print(f"Without max and min: Max: {max_b}, Min: {min_b}")

# Step 6:
threshold = 70
for student in student_data:
    if student[1] > threshold:
        print(f"Student {student[0]} exceeded the threshold with a grade of {student[1]}")


# Dictionaries
my_dictionary = {
    "name": "Alex",
    "grade": 95,
    "major": "Computer Science"
}

print(my_dictionary)
my_dictionary['minor'] = "Mathematics"
my_dictionary['advisor'] = None
# del my_dictionary
# # print(my_dictionary['advisor'])
advisor = my_dictionary.get('advisor', "No Advisor")
# if advisor is None:
#     print("No Advisor")
# else:
#     print(advisor)

print(list(my_dictionary.keys()))
print(list(my_dictionary.values()))
print(list(my_dictionary.items()))
# print(list(zip(my_dictionary.keys(), my_dictionary.values())))

for key in my_dictionary.keys():
    print(f"{key} - {my_dictionary[key]}")

for value in my_dictionary.values():
    print(value)

for key, value in my_dictionary.items():
    print(f"{key} - {value}")
