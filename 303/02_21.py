# this is used to generate a random list. We will explore this at a later date.
import random

student_list = ["John", "Adam", "James", "Kyle", "Tyler"]
student_majors = ["CS", "Bio", "Music Ed", "Math", "Criminal Justice"]

# print(list(zip(student_list, student_majors)))

for student in zip(student_list, student_majors):
    print(f"{student[0]} has a major of {student[1]}")

print(sorted(student_list))
# print(student_list.sort())
print(student_list)

number_list = [10, 20, 30, 40, 50]
print(sum(number_list))

total = 0
for number in number_list:
    total = total + number
print(total)

x = 0
y = 1
z = 1
for i in range(10):
    z = y + x
    print(x)
    x, y = y, z

fib = [0, 1]
for i in range(10):
    x = fib[-2]
    y = fib[-1]
    z = x + y
    fib.append(z)
print(fib)



# generate a random list of 100 numbers:
random_list = [random.randint(0, 100) for x in range(100)]
print(random_list)
sorted_random_list = sorted(random_list)
print(sorted_random_list)

target = 15
is_found = False
lp = 0
rp = len(sorted_random_list)-1
while(lp <= rp and not is_found):
    mid = (lp + rp)//2
    if sorted_random_list[mid] == target:
        print("Found!")
        is_found = True
    elif sorted_random_list[mid] < target:
        lp = mid + 1
    else:
        rp = mid - 1

if(not is_found):
    print("I couldn't find it.")
