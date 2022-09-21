n = input()
largest = ''
max_cifra = '0'
for i in range(0, len(n)):
    max_cifra = '0'
    for j in range(0, len(n)):
        if n[j] >= max_cifra:
            max_cifra = n[j]
    largest += max_cifra
    n = n.replace(max_cifra, '', 1)
print(largest)
