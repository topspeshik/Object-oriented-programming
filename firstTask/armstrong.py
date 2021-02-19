

for i in range(0, 32000):

    if i < 10:
        powPow = 1
    elif i < 100:
        powPow = 2
    elif i < 1000:
        powPow = 3
    elif i < 10000:
        powPow = 4
    elif i < 100000:
        powPow = 5

    a1 = 1
    b1 = 1
    c1 = 1
    d1 = 1
    e1 = 1
    f1 = 1

    a = int(i / 100000)
    b = int(i / 10000 % 10)
    c = int(i / 1000 % 10)
    d = int(i / 100 % 10)
    e = int(i / 10 % 10)
    f = int(i % 10)

    for j in range(0, powPow):
        a1 = a1 * a
        b1 = b1 * b
        c1 = c1 * c
        d1 = d1 * d
        e1 = e1 * e
        f1 = f1 * f

    if (a1 + b1 + c1 + d1 + e1 + f1) == i:
        print(i)





