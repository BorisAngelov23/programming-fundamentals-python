string = input()
j = 0
for i in range(0, len(string)):
    if 'A' <= string[i] <= 'Z':
        j += 1
capitals = list(range(j))
j = 0
for i in range(0, len(string)):
    if 'A' <= string[i] <= 'Z':
        capitals[j] = i
        j += 1
print(capitals)
