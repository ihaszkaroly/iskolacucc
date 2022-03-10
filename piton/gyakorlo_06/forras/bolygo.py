bolyi = input("A bolygó neve: ")
if bolyi == "":
    exit()
bolyi2 = ["Ceres","Haumea","Eris","Makemake"]
if bolyi in bolyi2:
    print("Törpebolygó")
else:
    print("Nem besorolt.")