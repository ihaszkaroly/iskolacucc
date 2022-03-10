def countworker():
    file = open("feherBt.txt", "r" , encoding="utf-8")
    row = file.readline()
    counter = 0
    while(row):
        row = file.readline()
        if(len(row) > 0):
            counter += 1
    print("Dolgozók száma:",counter)
    file.close()

def miskolc():
    file = open("feherBt.txt", "r" , encoding="utf-8")
    row = file.readline()
    miskolcSalary = 0
    while(row):
        row = file.readline()
        if(len(row) > 0):
            rowspt = row.split(":")
            if(rowspt[1] == "Miskolc"):
                miskolcSalary += int(rowspt[3])
    print("Miskolciak fizuja:",miskolcSalary)

def lajos():
    file = open("feherBt.txt", "r" , encoding="utf-8")
    row = file.readline()
    lali = 0
    while(row):
        row= file.readline()
        if(len(row) > 0):
            rowspt = row.split(":")
            namespt = rowspt[0].split(" ")
            if(namespt[1] == "Lajos"):
                lali += 1
    if(lali > 0):
        print("Lalik száma:",lali)
    else:
        print("nincs lali")

def start():
    countworker()
    miskolc()
    lajos()

start()
