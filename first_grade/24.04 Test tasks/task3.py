import math

value = int(input())

mod = 0

sum = 0

arr = []

while(value!=0):
    mod = value % 3
    arr.append(mod)
    arr.append(mod)
    value = math.floor(value / 3)

for i in range(len(arr)):
    sum += (arr[i] * pow(3,i))

print(sum)
