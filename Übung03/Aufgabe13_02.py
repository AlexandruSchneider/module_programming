"""
Author: Alexandru Schneider
Datum: 08. 10. 2021
Programmiersprache: Python 3.8.8
Aufgabe 13_02
"""
import random

# Teil 1: Zuweisung Variabeln
var1 = random.randint(0, 6)
var2 = random.randint(0, 6)
var3 = random.randint(0, 6)
var4 = random.randint(0, 6)
var5 = random.randint(0, 6)

print("1. Zahl: " + str(var1))
print("2. Zahl: " + str(var2))
print("3. Zahl: " + str(var3))
print("4. Zahl: " + str(var4))
print("5. Zahl: " + str(var5))

# für b)
gleichWieVar1 = var1 != var2 and var1 != var3 and var1 != var4 and var1 != var5
gleichWieVar2 = var2 != var3 and var2 != var4 and var2 != var5
gleichWieVar3 = var3 != var4 and var3 != var5
gleichWieVar4 = var4 != var5

# Teil 2: a)
if var1 == var2 == var3 == var4 == var5:
    print("Alle Variabeln haben die gleiche Zahl drin!")

# Teil 3: b)
elif gleichWieVar1 and gleichWieVar2 and gleichWieVar3 and gleichWieVar4:
    print("Alle Variabeln sind unterschiedlich!")

else:
    print("Die Zahlen entsprechen keiner der Kriterien in der Aufgabenstellung")

# Teil 4: c)
summe = var1 + var2 + var3 + var4 + var5
if 20 < summe < 25:
    print("Die summe der Zahlen: ")
    print(var1)
    print(var2)
    print(var3)
    print(var4)
    print(var5)
    print("ist: " + summe)
else:
    print("Die Summe ist nicht zwischen 20 und 25")
