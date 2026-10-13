"""Exercise 6 - Cafe order. Read the task in README.md."""

menu = {
    "plov": 35000,
    "lagman": 30000,
    "somsa": 8000,
    "salad": 15000,
    "tea": 5000,
}

# Write your solution below.
menu = {
    "plov": 35000,
    "lagman": 30000,
    "somsa": 8000,
    "salad": 15000,
    "tea": 5000,
}

print("Menu:")
for dish, price in menu.items():
    print(f"{dish}: {price} so'm")

order = {}

while True:
    dish = input("Enter a dish name (or 'done' to finish): ").strip().lower()

    if dish == "done":
        break

    if dish not in menu:
        print("This dish is not on the menu.")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Quantity must be greater than 0.")
        continue

    order[dish] = order.get(dish, 0) + quantity

print("\nReceipt:")
subtotal = 0

for dish, quantity in order.items():
    price = menu[dish]
    line_total = price * quantity
    subtotal += line_total
    print(f"{dish}: {quantity} x {price} = {line_total} so'm")

if subtotal >= 100000:
    discount = subtotal * 0.10
    total = subtotal - discount
    print(f"Discount: {discount} so'm")
else:
    discount = 0
    total = subtotal

print(f"Total: {total} so'm")
