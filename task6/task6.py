import random
print("Введите размерность строка - столбец")
rows = int(input())
cols = int(input())
sumArr = 0
maxArr = 0


arr = [[random.randint(0, 15) for j in range(cols+1)] for i in range(rows+1)]

for i in range(rows+1):
    print(arr[i])

for i in range(rows+1):
    for j in range(cols+1):
        sumArr += arr[i][j]
        if sumArr>maxArr:
            maxArr = sumArr
            index = i
    sumArr = 0

print("Max:", maxArr, "Number:", index)


