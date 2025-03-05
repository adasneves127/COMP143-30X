# Generate random numbers
import random


students = [
    ("Alex", 95),
    ("Thomas", 80),
    ("Jane", 76)
]

threshold = 79

for student in students:
    if student[1] > threshold:
        print(f"{student[0]} has exceeded the threshold of {threshold} with a grade of {student[1]}")

# List Comprehension
# Generate a list of 100 elements. Each element will be between 1 and 100.
# Then sort the list.
my_random_list = sorted([random.randint(1, 100) for i in range(100)])
lp = 0
rp = len(my_random_list) - 1
is_found = False
target = 30
while lp <= rp and not is_found:
    mid = (lp + rp) // 2
    if my_random_list[mid] == target:
        is_found = True
    elif my_random_list[mid] < target:
        lp = mid + 1
    else:
        rp = mid - 1

print(my_random_list)
if is_found:
    print("We found it!")
else:
    print("We didn't find it.")

my_other_list = [20, 49, 29, 40, 1, 84, 92]

# We assume that the first item is the biggest in the list.
max_num = my_other_list[0]
min_num = my_other_list[0]
for item in my_other_list:
    if item > max_num:
        max_num = item
    if item < min_num:
        min_num = item

print(f"Max Item: {max_num}")
print(f"Min Item: {min_num}")


