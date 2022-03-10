# Ihász Károly 2021-12-08
print("Ihász Károly 2021-12-08\nA program kiszámolja a téglatest térfogatát")

b = []
for i in range(0 ,3):
    a = int(input("Adja meg a téglatest oldalát: "))
    b.append(a)

def szamit():
    c = 1
    for i in range(len(b)):
        c = c * b[i]
    print("A téglatest Térfogata:",c)
szamit()