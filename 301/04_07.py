inventory = [
    ("bananas", 30, 0.8),
    ("t-shirts", 60, 10),
    ("Xbox", 3, 400)
]

for item in inventory:
    print(f"{item[0].title()} has a stock of {item[1]}, and a price of ${item[2]}")

