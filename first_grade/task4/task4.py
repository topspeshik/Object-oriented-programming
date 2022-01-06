pivo = input()
pivandopalo = list(pivo)
dlina = len(pivandopalo)

k = 0
c = 0
for i in pivandopalo:
    letter = i.lower()
    if letter == "c" or letter == "g":
        k += 1
if k != 0:
    c = k*100/dlina
print(c)

