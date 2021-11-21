"""
Author: Alexandru Schneider
Datum: 05. 11. 2021
Programmiersprache: Python 3.8.8
Aufgabe 26
"""
studenten = ["Alex", "Andre", "Benito", "Raphael", "Rafael"]
punkteListe = []

try:
    for student in studenten:
        note = float(input(f"Note für Student {student} zwischen 1 und 6 eingeben: "))
        if 1 <= note <= 6:
            punkteListe.append(note)
        else:
            raise Exception("Zahl sollte zwischen 1 und 6 liegen!")
except:
    print("Bitte eine Zahl als gültige Note eingeben!")
    raise Exception("Ungültige Note!")
else:
    print(studenten)
    print(punkteListe)
