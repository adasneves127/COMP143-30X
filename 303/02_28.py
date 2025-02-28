# Project 1
# Step 1:
customer_name = "Alex"
cart_items = []
cart_prices = []

# Step 2:
cart_items.append("apple")
cart_items.append("banana")
cart_items.append("bread")

cart_prices.append(1.5)
cart_prices.append(0.75)
cart_prices.append(2)

# Step 3:
cart_items.insert(1, "milk")
cart_prices.insert(1, 2.5)

# Step 4:
cart_items.remove("banana")
cart_prices.remove(0.75)

# Step 5:
cart_items.pop()
cart_prices.pop()

# Step 6:
cart_items.sort()

# Step 7:

total = sum(cart_prices)
for item, price in zip(cart_items, cart_prices):
    print(f"{item} - ${price:.2f}")

print(f"Total cost: ${total:.2f}")

# Data Types:
# String -- Text surrounded by ""
# Integers -- A whole number with no decimal point
# Floats -- A number with a decimal point
# Lists (Mutable Collection) -- A collection of items, surrounded by [], and delineated with ,
# Tuple (Immutable Collection) -- A collection of items, surrounded by (), and delineated with ,
# Boolean -- True and False. No in between...

# Greater Than (>)
# Less Than (<)
# Equal To (==)
# Not Equal To (!=)
#           not (A == B)

# Greater Than or Equal To (>=)  A > B or A == B
# Less Than or Equal To (<=) A < B or A == B

# and -- A and B -- Both A and B must be true, for the output to be true.
# or -- A or B -- Either A or B (or both) must be true, for the output to be true.
# not -- not A -- If A was true, then not A is false. If A was false, then not A is true.

string_1 = "Hi"
string_2 = "Bye"

# Mathmatics Double Implication (Bi-directional)
print(not((string_1 == "Hi" and string_2 != "Bye") or (string_1 != "Hi" and string_2 == "Bye")))



