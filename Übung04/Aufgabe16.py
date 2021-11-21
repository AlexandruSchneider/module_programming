"""
Author: Alexandru Schneider
Datum: 13. 10. 2021
Programmiersprache: Python 3.8.8
Aufgabe 16
"""

def potenzierenMitBasis(num):
    anzLoops = int(input("Wie oft soll die Zahl " + str(num) + " hoch gerechnet werden? "))
    index = 1

    result = basis = num
    exponent = firstToEnd = 1

    # Teil 1 b)
    # Durchläufe bis Eingabe
    while index <= anzLoops:
        result = basis ** exponent
        print(str(index) + ". Durchlauf: [" + "letzte drei Stellen: " + str(result % 1000) + "]")
        if str(result).endswith("001"):
            firstToEnd = exponent
        exponent += 1
        index += 1

    # Teil 2
    if firstToEnd != 1:
        print("Dieser Exponent mit Basis " + str(basis) + " endet mit 001: " + str(firstToEnd))
    else:
        print("Die eingegebene Anzahl an Loops ist zu klein.\U0001F612")


# Teil 3
potenzierenMitBasis(3)
print("\n")
potenzierenMitBasis(7)