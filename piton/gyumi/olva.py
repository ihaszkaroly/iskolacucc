deli = ["narancs","citrom","mandarin","avokádó","kókusz"]

fp = open("gyumi.txt","r", encoding="utf-8")
lines = fp.readlines()
fp.close()

for line in lines:
    gyumolcs = line.rstrip()
    if gyumolcs not in deli:
        print(gyumolcs.rstrip())