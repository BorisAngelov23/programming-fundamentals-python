budget = float(input())
flour_price_kg = float(input())
milk_price_kg = 5 / 4 * flour_price_kg
eggs_price_pack = 3 / 4 * flour_price_kg
price_per_loave = eggs_price_pack + flour_price_kg + milk_price_kg / 4
total_loaves = int(budget // price_per_loave)
budget = budget - total_loaves * price_per_loave
eggs = total_loaves * 3
eggs_lost = 0
for i in range(1, total_loaves + 1):
    if i % 3 == 0:
        eggs_lost += i - 2
eggs -= eggs_lost
print(f"You made {total_loaves} loaves of Easter bread! Now you have {eggs} eggs and {budget:.2f}BGN left.")
