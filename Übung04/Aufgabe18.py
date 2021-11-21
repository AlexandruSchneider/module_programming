"""
Author: Alexandru Schneider
Datum: 13. 10. 2021
Programmiersprache: Python 3.8.8
Aufgabe 18
"""

# Variable deklarieren
resultat = 0

# range benutzt die beiden ersten Parameter nicht
# und die Inkrementierung ist default 1, deswegen 0 und 11 weil die Zahlen bis und mit 10 sind
for i in range(0, 11):
    for j in range(0, 16):
        for k in range(0, 21):
            # Resultat wird berechnet
            resultat = i * j * k

            # Wurzel wird mit der Potenzierung von 0.5 errechnet
            # und mit Modulo 1 == 0 wird überprüft ob das Ergebnis eine Ganzzahl ist.
            if resultat != 0 and resultat**0.5%1 == 0:
                print("Quadratwurzel: " + str(resultat) + "\t : [i=\"" + str(i) + "\", j=\"" + str(j) + "\", k=\"" + str(k) + "\"] \tFaktor: " + str(resultat**0.5))
