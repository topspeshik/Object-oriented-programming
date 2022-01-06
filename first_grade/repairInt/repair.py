print('Write 0 0 to exit')
N = int(input())
arr = list(range(1, N + 1))
number = 1
arrUP = [0] * N
i = 0

while i != N:
    i += 1
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    for j in range(N):
        if a == arr[j]:
            if arrUP[a - 1] == 0 and arrUP[b - 1] == 0:
                arrUP[a - 1] = number
            elif arrUP[a - 1] != arrUP[b - 1] and arrUP[a - 1] !=0:
                if arrUP[a - 1] > arrUP[b - 1]:
                    endNumb = arrUP[a - 1]
                else:
                    endNumb = arrUP[b - 1]
                for g in range(N):
                    if arrUP[g] == endNumb:
                        arrUP[g] = arrUP[a - 1]
            elif arrUP[b - 1] != 0:
                arrUP[a - 1] = arrUP[b - 1]
        if b == arr[j]:
            if arrUP[b - 1] == 0 and arrUP[a - 1] == 0:
                arrUP[b - 1] = number
            elif arrUP[a - 1] != arrUP[b - 1] and arrUP[b - 1] !=0:
                if arrUP[a - 1] > arrUP[b - 1]:
                    endNumb = arrUP[a - 1]
                else:
                    endNumb = arrUP[b - 1]

                for g in range(N):
                    if arrUP[g] == endNumb:
                        arrUP[g] = arrUP[b - 1]

            elif arrUP[a-1] != 0:
                arrUP[b - 1] = arrUP[a - 1]


    number = max(arrUP) + 1

for i in range(N):
    if arrUP[i] == 0:
        arrUP[i] = max(arrUP) + 1

count = 0
arrUPsort = sorted(arrUP)
for i in range(N-1):
    if arrUPsort[i] != arrUPsort[i+1]:
        count+=1
print(arrUP)
print(max(arrUP) - 1)
print(arrUPsort)
print(count)