import time
start_time = time.time()

def div(numb):
    sum1 = 0
    for i in range(1, numb):
        if numb % i == 0:
            sum1 += i

    return sum1


for i in range(1, 10001):
    m = div(i)
    n = div(m)
    if (i == n) and (i < m):
        print(i, '', m)

print("--- %s seconds ---" % (time.time() - start_time))
