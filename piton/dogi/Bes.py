# File: Bes.py
# Author: Ihász Károly
# Copyright: 2021, Ihász Károly
# Group: Ifra
# Date: 2021-12-07
# Github: https://github.com/ihaszkaroly/
# Licenc: GNU GPL

print("Ihász Károly | Ifra 13. | 2021. 12. 07.")

a = input("Karakterlánc: ")
c = 0
for kar in a:
    if kar in "b":
        c += 1
print("b betük száma:",c)