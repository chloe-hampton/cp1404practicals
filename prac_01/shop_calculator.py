DISCOUNT_RATE = 0.10 # 10%

number_of_items = int(input("Number of items: "))
total_price = 0

for i in range(number_of_items):
    price_of_item = float(input("Price of item: $"))
    total_price += price_of_item

if total_price > 100:
    total_price = total_price - (total_price * DISCOUNT_RATE)

print(f"Total price for {number_of_items} items is: ${total_price:.2f}")

