#a = [10,20,30,45,12,5,46,11]
#b = len(a)
#c = 0
#for i in range(0 , b):
#    c = c + a[i]
#print(c)

#a = input("Karakterek: ")
#h = len(a)
#for i in range(0 , h):
#    print(a[i])
#    for j in range(-1,1):
#        print(" ",end=" ")

#a = []
#b = 0
#c = 0
#for i in range(0 , 7):
#    b = print(int(input("Adj meg hőmérsékletet: ")))
#    a = a.append(b)
#     if b <= 0:
#        c = c+1
#print("A héten ennyiszer volt fagy:",c)
#
import random
#szam = []
#for i in range (0 , 10):
#    nuberrand = random.randrange(1 , 101)
#    szam.append(nuberrand)
#print(szam)
import math

# szam1 = []
# szam2 = []

# for i in range(0 , 5000):
#     rand = random.randrange(1,200)
#     szam1.append(rand)
# print(len(szam1))
# for number in szam1:
#     powered = math.pow(number, 3)
#     szam2.append(powered)

# print(szam2[6])
# szam1sum = 0
# szam2sum = 0
# for number in szam1:
#     szam1sum += number
# for number in szam2:
#     szam2sum += number
# print(szam1sum)
# print(szam2sum)

a = []
c = 0
for i in range(0 , 500):
    b = random.randrange(1 , 500)
    a.append(b)

for h in range(0 ,500):
    k = a[h]
    if k < 250:
        c = c+1
print(c)

