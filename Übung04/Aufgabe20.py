"""
Author: Alexandru Schneider
Datum: 13. 10. 2021
Programmiersprache: Python 3.8.8
Aufgabe 20
"""
import random


# Gibt die Anzahl, welche gewürfelt wurde zurück
def wurfBisZwanzig():
    anzSechser = 0
    anzWurf = 0

    while anzSechser < 20:
        zufallsZahl = random.randint(1, 6)
        if zufallsZahl == 6:
            anzSechser += 1
            print(str(zufallsZahl) + " <---- " + str(anzSechser))
        anzWurf += 1
        print(str(zufallsZahl))

    print("Anzahl Sechser: " + str(anzSechser))
    print("Anzahl Würfe: " + str(anzWurf))
    return anzWurf


wurfBisZwanzig()