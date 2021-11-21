# Autor: Alexandru Schneider
# Programmiersprache: Python 3.8.8
# Datum: 24. 09. 2021

# Variable Potenz auf 0 gestellt damit potenzzählung nicht
# um 4 verschoben wird (da nur alle 4 Potenzierungen auf
# die Zahl 1 enden, können die restlichen potenzierungen
# ignoriert werden)
resultat = basis = 3
potenz = 0

while (resultat%100) != 1:
    potenz += 4
    resultat = basis**potenz
    print("3 hoch", potenz, "ergibt", resultat)
else:
    print("Resultat wurde nach", potenz, "Potenzierungen gefunden")