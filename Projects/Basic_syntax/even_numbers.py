n = int(input())
printed_nums = 0
for i in range(0, n):
    current_number = int(input())
    if current_number % 2 == 1:
        print(f'{current_number} is odd!')
        break
    printed_nums += 1
if printed_nums == n:
    print("All numbers are even.")
