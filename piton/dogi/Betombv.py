import random
# File: Betombv.py
# Author: Ihász Károly
# Copyright: 2021, Ihász Károly
# Group: Ifra
# Date: 2021-12-07
# Github: https://github.com/ihaszkaroly/
# Licenc: GNU GPL

print("Ihász Károly | Ifra 13. | 2021. 12. 07.")

def fug():
    a = []
    b = 0
    for i in range(0 , 20):
        b = random.randrange(1,500)
        a.append(b)
    print(a)

fug()