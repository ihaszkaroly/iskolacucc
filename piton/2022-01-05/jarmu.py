def benzin():
    file = open("jaribt.txt","r",encoding="utf-8")
    file2 = ""
    a = [""]
    while(file):
        file2 = file.readline()
        if len(file2) > 0:
            split = file2.split(":")
            if split[3] == "benzin":
                a.append(file2)
        
    print(a)

def olcsobb():
    o_file = open("jaribt.txt","r",encoding="utf-8")
    o_file2 = ""
    o_a = [""]
    while(o_file):
        o_file2 = o_file.readline()
        if len(o_file2) > 0:
            o_split = o_file2.split(":")
            if o_split[4] > 1000000:
                o_a.append(o_file2)
    print(o_a)

benzin()
olcsobb()