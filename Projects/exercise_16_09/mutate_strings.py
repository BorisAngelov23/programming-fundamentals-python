string1 = input()
string2 = input()
word = ''
prevword = string1
for i in range(0, len(string2) + 1):
    word = ''
    for j in range(0, i):
        word += string2[j]
    for j in range(i, len(string2)):
        word += string1[j]
    if word != prevword:
        print(word)
    prevword = word
