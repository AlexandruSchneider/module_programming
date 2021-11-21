"""
Author: Alexandru Schneider
Datum: 07. 10. 2021
Programmiersprache: Python 3.8.8
Aufgabe 15 Variante 2
"""
# Variante 2: Es wird zuerst geprüft ob die Zahl zwischen 7 und 101 ist und
# dann in einem if alles abgefragt (mit and-Operator)
zahlInt = int(input("Eine Ganzzahl zwischen 7 und 101 (also ab ab 8 und ohne 101): "))

if (7 < zahlInt <= 100) and (zahlInt % 2 != 0 and zahlInt % 3 != 0 and zahlInt % 5 != 0 and zahlInt % 7 != 0):
    print(str(zahlInt) + " ist eine Primzahl!")
else:
    print("Die Zahl " + str(zahlInt) + " ist keine Primzahl oder nicht zwischen 7 und 101!")