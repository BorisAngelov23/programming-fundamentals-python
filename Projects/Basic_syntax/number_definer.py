number = float(input())
if number == 0:
    print('zero')
elif number > 0:
    if number > 1000000:
        print('large positive')
    elif number < 1:
        print('small positive')
    else:
        print('positive')
else:
    if 1 > abs(number) > 0:
        print('small negative')
    elif abs(number) > 1000000:
        print('large negative')
    else:
        print('negative')
