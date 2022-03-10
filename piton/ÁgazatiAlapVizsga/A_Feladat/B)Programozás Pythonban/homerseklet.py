# Ihász Károly 2021-12-08
print("Ihász károly 2021-12-08\nA program kiszámolja 3 nap átlag hőmérsékletét.\nA fűtést csak 15 átlag fok alatt kell bekapcsolni.")
a = 11.4
b = 18.2
c = 16
d = (a+b+c)/3
if d < 15:
    print("Az átlaghőmérséklet: %.2f"%d,"fok, indítsa el a fűtést")
else:
    print("Az átlaghőmérséklet: %.2f"%d,"fok, nem kell fűteni.")
