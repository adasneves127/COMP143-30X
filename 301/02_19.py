
# for <iter variable> in <collection variable>:
#   The body of the loop will be indented.

my_list = [10, 20, 30, 40, 50, 60]

for element in my_list:
    print(element)

for i in range(len(my_list)):
    print(my_list[i])

cart_items =  ["apple", "banana", "orange", "mango"]
cart_prices = [1.2,     3.1,      2.4,       5.5]

for cart_index in range(len(cart_items)):
    print(f"{cart_items[cart_index]} - ${cart_prices[cart_index]}")

zipped_list = list(zip(cart_items, cart_prices))
zipped_list.sort()
cart_items.sort()

total = 0
for item_pair in zipped_list:
    print(f"{item_pair[0]} - ${item_pair[1]}")
    total = total + item_pair[1]
print(f"Cart total: {total}")
print(f"Cart total: {sum(cart_prices)}")

