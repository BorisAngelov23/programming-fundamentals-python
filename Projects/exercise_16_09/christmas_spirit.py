quantity = int(input())
days = int(input())
ornament_sets = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15
total_points = 0
budget = 0
for day in range (1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        budget += ornament_sets * quantity
        total_points += 5
    if day % 3 == 0:
        budget += (tree_garland + tree_skirt) * quantity
        total_points += 13
    if day % 5 == 0:
        budget += tree_lights * quantity
        total_points += 17
        if day % 3 == 0:
            total_points += 30
    if day % 10 == 0:
        total_points -= 20
        budget += tree_skirt + tree_garland + tree_lights
if days % 10 == 0:
    total_points -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {total_points}")
