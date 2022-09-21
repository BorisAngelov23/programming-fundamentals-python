string = input()
animals = list(string.split(", "))
for i in range(0, len(animals)):
    if animals[i] == 'wolf' and i == len(animals) - 1:
        print("Please go away and stop eating my sheep")
        break
    if animals[i] == 'wolf' and animals[i + 1] == 'sheep':
        print(f"Oi! Sheep number {len(animals) - i - 1}! You are about to be eaten by a wolf!")
        break
