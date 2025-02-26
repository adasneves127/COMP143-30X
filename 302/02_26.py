# # Project 1:
# # Step 1:
# customer_name = "Alex"
# cart_items = []
# cart_prices = []
#
# # Step 2:
# cart_items.append("apple")
# cart_items.append("banana")
# cart_items.append("bread")
#
# cart_prices.append(1.5)
# cart_prices.append(0.75)
# cart_prices.append(2.0)
#
# # Step 3
# cart_items.insert(1, "milk")
# cart_prices.insert(1, 2.5)
#
# # Step 4
# cart_items.remove("banana")
# cart_prices.remove(0.75)
#
# # Step 5
# cart_items.pop()
# cart_prices.pop()
#
# # Step 6
# cart_items.sort()
#
# # Step 7
# # Method 1:
# for index in range(len(cart_items)):
#     print(f"{cart_items[index]} - {cart_prices[index]}")
#
# # Method 2:
# for element in zip(cart_items, cart_prices):
#     print(f"{element[0]} - {element[1]}")
#
# total = 0
# for price in cart_prices:
#     total = total + price
#
# print(total)
#
# print(sum(cart_prices))
#

# Data Types:
# String - Text surrounded by quotes ("")
# Int - A number with no decimal point
# Float - A number with a decimal point
# List - A collection of items surrounded by [], and separated by ,
# Booleans - True or False.
#       - They can be seen as the answer to a question.

# Are these two things equal?
# Are these two things not equal?
# Is item 1 greater than item 2? Less than?
# Is this item contained in some list/sequence?

number_1 = 55
number_2 = 30

print(number_1 == number_2) # Are they equal?
print(number_1 != number_2) # Are they not equal?
print(number_1 > number_2)  # Is number 1 greater than number 2?
print(number_1 < number_2)  # Is number 1 less than number 2?
print(number_1 >= number_2) # Is number 1 greater than or equal to number 2?
print(number_1 <= number_2) # Is number 1 less than or equal to number 2?

# Is this data in a collection/sequence (list)
number_list = [10,20,30,40,50,60]
print(number_1 in number_list)

if number_1 != number_2:
    print("Number 1 is not equal to Number 2.")

# Search for an item in a list.
is_found = False
for item in number_list:
    if item == number_1:
        is_found = True

if is_found:
    print("I found number 1!")
else:
    print("I didn't find number 1!")

number_grade = 60
if number_grade >= 93:
    print("You got an A!")
elif number_grade >= 90:
    print("You got an A-!")
elif number_grade >= 87:
    print("You got a B+!")
elif number_grade >= 83:
    print("You got a B!")
elif number_grade >= 80:
    print("You got a B-!")
elif number_grade >= 77:
    print("You got a C+!")
elif number_grade >= 73:
    print("You got a C!")
elif number_grade >= 70:
    print("You got a C!")
elif number_grade >= 65:
    print("You got a D...")
else:
    print("You got an F.")
