n = int(input())
pure = True
for i in range(0, n):
    pure = True
    string = input()
    for j in range(0, len(string)):
        if string[j] == ',' or string[j] == '_' or string[j] == '.':
            pure = False
            break
    if not pure:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")
