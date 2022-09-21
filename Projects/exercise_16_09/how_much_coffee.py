task = input()
amount = 0
while task != 'END':
    if task == 'cat' or task == 'dog' or task == 'coding' or task == 'movie':
        amount += 1
    if task == 'CAT' or task == 'DOG' or task == 'CODING' or task == 'MOVIE':
        amount += 2
    task = input()
if amount > 5:
    print("You need extra sleep")
else:
    print(amount)
