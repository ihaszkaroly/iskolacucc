# gyumi = input("Gyümölcs: ")
# fp = open("gyumi.txt", "a", encoding="utf-8")
# fp.write(gyumi + "\n")

# gyumi = 1
# fp = open("gyumi.txt" , "a" , encoding="utf-8")
# print('Adjon meg gyümölcsöket "vege" végjelig.')
# while gyumi != "vege":
#     gyumi = input("Gyümölcs: ")
#     if gyumi != "vege":
#         fp.write(gyumi + "\n")

print('Adjon meg gyümölcsöket "vege" végjelig.')
def fajlbairas(gyumi):
    fp = open("gyumi.txt" , "a" , encoding="utf-8")
    while gyumi != "vege":
        gyumi = input("Gyümölcs: ")
        if gyumi != "vege":
            fp.write(gyumi + "\n")

gyumi = input("Gyümölcs: ")
fajlbairas(gyumi)
