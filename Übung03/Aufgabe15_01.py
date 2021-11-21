"""
Author: Alexandru Schneider
Datum: 07. 10. 2021
Programmiersprache: Python 3.8.8
Aufgabe 15 Variante 1
"""
# Variante 1: Es werden 5 if in einander geschachtelt:
# Vorteil dieser Variante: Es kann für jeden Fall eine eigene Folge ausgegeben werden.
zahlInt = int(input("Eine Ganzzahl zwischen 7 und 101 (also ab ab 8 und ohne 101): "))

if 7 < zahlInt <= 100:
    if zahlInt % 2 != 0:
        if zahlInt % 3 != 0:
            if zahlInt % 5 != 0:
                if zahlInt % 7 != 0:
                    print(str(zahlInt) + " ist eine Primzahl!")
                else:
                    print(str(zahlInt) + " ist durch 7 teilbar!")
            else:
                print(str(zahlInt) + " ist durch 5 teilbar!")
        else:
            print(str(zahlInt) + " ist durch 3 teilbar!")
    else:
        print(str(zahlInt) + " ist durch 2 teilbar!")
else:
    print("Die Zahl " + str(zahlInt) + " ist nicht zwischen 7 und 101 (ohne 7 und 101)")
