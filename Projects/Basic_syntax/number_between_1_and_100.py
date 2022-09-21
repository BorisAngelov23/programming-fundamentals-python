number = float(input())
if 1 <= number <= 100:
    print(f"The number {number} is between 1 and 100")
else:
    while 1 > number or 100 < number:
        number = float(input())
        if 1 <= number <= 100:
            print(f"The number {number} is between 1 and 100")
            break
