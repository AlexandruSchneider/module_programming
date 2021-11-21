"""
Author: Alexandru Schneider
Datum: 21. 10. 2021
Programmiersprache: Python 3.8.8
Aufgabe 24
"""
import random

intInput = int(input("Geben sie eine Ganzzahl ein: "))

minZahl = 0
zufallsZahl = int(input("Wie gross ist der Zufallszahlenbereich? "))

resultList = random.sample(range(minZahl, zufallsZahl), intInput)

print(f"Die Zufallsliste unsortiert: \t{resultList}")

resultList.sort()

print(f"Die Zufallsliste sortiert: \t{resultList}")