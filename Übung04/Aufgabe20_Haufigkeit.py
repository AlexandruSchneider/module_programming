"""
Author: Alexandru Schneider
Datum: 13. 10. 2021
Programmiersprache: Python 3.8.8
Aufgabe 20
"""
from Aufgabe20 import wurfBisZwanzig

# ---------------------------------------- ACHTUNG -------------------------------------------
# Es wird die Funktion MIT den prints verwendet, die anzahl sollte somit KLEIN gehalten werden
# Es kann ansonsten sein, dass das Programm LANGE braucht um zu Ende zu kommen.
# --------------------------------------------------------------------------------------------
total = 0

# Anzahl an Berechnungen (Anz. Durchführungen)
anzahl = 1000

for i in range(0, anzahl):
    anzahlWurfe = wurfBisZwanzig()
    total += anzahlWurfe

print("Gesamtschnitt: " + str(total/anzahl))