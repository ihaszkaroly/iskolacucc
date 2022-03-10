#lista = ["r","d","1","asd","z","y"]
#szoveg = "".join(lista)
#print("eredmény:",szoveg)
#mondat = "dfjda bghufb ahgb jifag ijra jgj irbg ipbfa ighpo"
#print(mondat.capitalize())
#print(mondat.title())

#ureslista = []
#print(ureslista)
#ureslista.append(35)
#ureslista.append(48)
#print(ureslista)
#ureslista[0] = 107
#print(ureslista)
#print(ureslista[0])

#masik = [10, 45, 11]
#a = masik

#print(ureslista==masik)
#print(ureslista is masik)
#print(a is masik)
#print(len(a))

#szamok = []
#szamok.extend(range(50 , 100))
#print(szamok)

#lista = [1,2,3,4,5,6,7,8,9,1,0,1,1,1]
#for elem in lista:
#    print(elem, end=" ")
#print()
#lista.insert(1,50)
#for elem in lista:
#    print(elem, end=" ")
#print()
#print(lista.index(0))
#lista.clear()
#print(lista)

list1 = [1,2,3,4,5,6,7,9,0]
list2 = list1
list3 = list1.copy()
list1[0] = 1008
print(list2)
print(list3)