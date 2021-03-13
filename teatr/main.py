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

for i in range(0, len(textLines)-1):
    textLines[i] = str(i+1) + ") " + textLines[i]



for i in roles:
    arrJ.clear()
    for j in textLines:
      if j.find(i) > -1:

        arrJ.append(j.replace(i + ':' + " ", ""))
        teatr[i] = arrJ.copy()
        textLines.remove(j)


for i in list(teatr.keys()):
    print(i+":")
    for j in range(len(teatr[i])):
        print(teatr[i][j])

print(textLines)













