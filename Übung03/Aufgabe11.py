"""
Author: Alexandru Schneider
Datum: 07. 10. 2021
Programmiersprache: Python 3.8.8
Aufgabe 11
"""
zahl1 = float(input("1. Zahl: "))
zahl2 = float(input("2. Zahl: "))

# Die Variabeln werden als Float definiert
minimum = 0.0
maximum = 0.0

if zahl1 < zahl2:
    minimum = zahl1
    maximum = zahl2
    print("Die Variable Minimum: " + str(minimum) + " (1. Zahl)")
    print("Die Variable Maximum: " + str(maximum) + " (2. Zahl)")

if zahl1 > zahl2:
    minimum = zahl2
    maximum = zahl1
    print("Die Variable Minimum: " + str(minimum) + " (2. Zahl)")
    print("Die Variable Maximum: " + str(maximum) + " (1. Zahl)")

if zahl1 == zahl2:
    print("Die beiden Zahlen sind gleichgross: \n" + "1. Zahl: " + str(zahl1) + "\n2. Zahl: "+ str(zahl2))
