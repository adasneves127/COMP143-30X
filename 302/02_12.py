student_name = "JoHn SmItH"

print(student_name)
print(student_name.upper())
print(student_name.lower())
print(student_name.title())

student_list = ["John", "Adam", "James", "Kyle", "Tyler"]
student_majors = ['CS', "Bio", "Music Ed", "Math", "Crim Justice"]
print(student_list[0])

student_list.insert(0, "Zach")
student_majors.insert(0, "Psych")
print(student_list)

student_list.append("Katie")
student_majors.append("Anthropology")
print(student_list)

student_list.pop()
student_majors.pop()
student_list.remove("John")
student_majors.remove("CS")
# del student_list[2]
student_list.pop(2)
student_majors.pop(2)
# print(popped_item)

# Naive Approach
# print(student_list[0])
# print(student_list[1])
# print(student_list[2])
# print(student_list[3])

# Iterating over two lists:
# Naive Approach (Unsafe)
# print(len(student_list))
for index in range(len(student_list)):
    print(f"{student_list[index]} - {student_majors[index]}")

print(list(zip(student_list, student_majors)))
# Improved Approach (Safe)
for name, major in zip(student_list, student_majors):
    print(f"{name} - {major}")


