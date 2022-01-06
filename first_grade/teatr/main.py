# Неиспользованные роли и слова автора сделаны немножко убого, но работает
file = open('role.txt', encoding='utf-8')
theatre = []
for row in file:
    theatre.append(row)
theatre = [role.rstrip() for role in theatre]

roles = []
textLines = []
count = 0
teatr = dict()


for i in theatre:
    count = count + 1
    if i == 'textLines:':
        break
    roles.append(i)

del theatre[0:count]
del roles[0]

textLines = theatre
arrJ = []

for i in range(0, len(textLines)):
    textLines[i] = str(i+1) + ") " + textLines[i]

indexI = 0
for i in roles:
    indexJ = -1
    arrJ.clear()
    for j in textLines:
        indexJ += 1
        if j.find(i) > -1:
            foundRole = 1
            arrJ.append(j.replace(i + ':' + " ", ""))
            teatr[i] = arrJ.copy()
            textLines[indexJ] = "used"
    if foundRole == 1:
        roles[indexI] = "used"
        indexI += 1
        foundRole = 0



for i in list(teatr.keys()):
    print(i+":")
    for j in range(len(teatr[i])):
        print(teatr[i][j])

print("Слова автора: ")

for i in textLines:
    if i.find("used") == -1:
        print(i)

print("Неиспользованные роли: ")
for i in roles:
    if i.find("used") == -1:
        print(i)