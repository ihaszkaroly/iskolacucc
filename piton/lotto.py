import random

# lotto = []
# szam = []

# for i in range (1, 91):
#     lotto.append(i)

# #print(len(lotto))

# pool = 90
# for i in range(0 , 5):
#     c = random.randrange(1,pool)
#     szam.append(lotto[c])
#     pool -= 1
# #    lotto.remove(c)
# print(szam)

a = []
b = []
c = []
d = 0
y = int(input("Hány számot sorsoljon: "))
for i in range (0,y):
    d = random.randrange(1,1000)
    a.append(d)
for i in range (0 , y):
    if a[i] % 2:
        b.append(a[i])
    else:
        c.append(a[i])
print("Páros számok száma:",len(b))
print("Páratlan számok száma:",len(c))