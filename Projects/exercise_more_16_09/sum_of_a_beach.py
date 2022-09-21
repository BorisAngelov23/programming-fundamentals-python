string = input()
sand = 'sand'
water = 'water'
fish = 'fish'
sun = 'sun'
total = string.lower().count(sand) + string.lower().count(sun) + string.lower().count(water) + string.lower().count(fish)
print(total)
