import random


def binary(n):
    s = ''
    for i in range(8):
        s = str(n % 2) + s
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

print(letters)
print(binaryLetters)

for g in range(len(word)):
    for n in binaryLetters[g]:
        arr.append(n)

    for i in range(12):
        if (i & (i - 1)) == 0:
            arr.insert(i, "-")
    arr.pop(0)
    print('Начало Хемминга', arr)

    end = 0
    decode = []
    res = ''
    suma = 0
    for i in range(1, 12):
        if (i & (i - 1)) == 0:
            if i % 2 == 1:
                a = i + 1
            else:
                a = i * 2
            print("-------------------")
            for j in range(i - 1, 12, a):

                end = j + i
                if end > 12:
                    end = 12

                decode.append(arr[j:end])
            for d in range(len(decode)):
                for e in range(len(decode[d])):
                    res += str(decode[d][e])
            res = res[1:]
            print('Декодирование', res)
            res = int(res)
            while res > 0:
                digit = res % 10
                suma = suma + digit
                res = res // 10

            if suma % 2 == 0:
                numb = 0
            else:
                numb = 1
            arr[i - 1] = str(numb)
            suma = 0
            decode = []
            res = ''

    print('Конец Хемминга', arr)
    randArr = [2, 5, 6, 8, 9, 10, 11, 12]
    randNumb = random.choice(randArr)
    if arr[randNumb] == 1:
        arr[randNumb] = 0
    else:
        arr[randNumb] = 1

    print('===================')
    print('randNumb = ', randNumb)
    print('===================')

    print('Массив с ошибкой', arr)
    decode = []

    res = ''
    count = 0

    for i in range(1, 12):
        if (i & (i - 1)) == 0:
            if i % 2 == 1:
                a = i + 1
            else:
                a = i * 2
            print("------------------")
            for j in range(i - 1, 12, a):

                end = j + i
                if end > 12:
                    end = 12

                decode.append(arr[j:end])
            for d in range(len(decode)):
                for e in range(len(decode[d])):
                    res += str(decode[d][e])
            res = res[1:]
            print('Декодирование', res)
            res = int(res)
            while res > 0:
                digit = res % 10
                suma = suma + digit
                res = res // 10

            if suma % 2 == 0:
                numb = 0
            else:
                numb = 1

            suma = 0
            decode = []
            res = ''
            if arr[i - 1] != str(numb):
                count += i

    if count == 0:
        print('===================')
        print('Ошибок нет')
        print('===================')
    else:
        print('===================')
        print('Ошибка под индексом - ', count - 1)
        print('===================')
    arr = []
