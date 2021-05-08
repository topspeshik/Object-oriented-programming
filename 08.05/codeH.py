from math import log
def binary(n):
    s = ''
    for i in range(8):
        s = str(n%2) + s
        n //= 2
    return s

arr = []
letters = []
binaryLetters = []
word = input()
for i in word:
    letters.append(i)
    a = ord(i)
    a = binary(a)
    binaryLetters.append(a)

for i in binaryLetters[0]:
    arr.append(i)

print(letters)
print(binaryLetters)
print(arr)

for i in range(12):
    if (i & (i - 1)) == 0:
        arr.insert(i, "-")
arr.pop(0)

for i in range(1, 12):
    if (i & (i - 1)) == 0:
        print("--------------------")
