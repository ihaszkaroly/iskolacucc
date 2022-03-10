kutya = ["dalmata","agár","terrier","kuvasz"]
a = input("Kutya fajta: ")
if a == "":
    exit()
elif a in kutya:
    print("Van ilyen.")
else:
    print("Nincs ilyen fajta.")