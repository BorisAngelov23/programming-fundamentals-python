n = int(input())
total = 0
for i in range(0, n):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if 0.01 <= price_per_capsule <= 100 and 31 >= days >= 1 and 2000 >= capsules_per_day >= 1:
        coffee_price = price_per_capsule * days * capsules_per_day
        print(f"The price for the coffee is: ${coffee_price:.2f}")
        total += coffee_price
print(f"Total: ${total:.2f}")
