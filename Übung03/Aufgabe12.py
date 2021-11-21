"""
Author: Alexandru Schneider
Datum: 07. 10. 2021
Programmiersprache: Python 3.8.8
Aufgabe 12
"""
# Die Bibliothek Random wird importiert
import random

inputInt = int(input("Geben Sie eine ganze Zahl ein: "))

# Ein zufälliger Integer zwischen 0 und 100 wird gewählt
randomInt = random.randint(0, 100)

print("Eingegebene Zahl: " + str(inputInt))
print("Zufallszahl: " + str(randomInt))

# Falls die Zahlen gleich sind hat der Spieler gewonnen, ansonsten hat der Spieler verloren
if inputInt == randomInt:
    print("Gewonnen!")
else:
    print("Verloren")
