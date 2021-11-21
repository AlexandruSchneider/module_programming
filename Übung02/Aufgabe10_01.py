"""
Author: Alexandru Schneider
Datum: 06. 10. 2021
Programmiersprache: Python 3.8.8
Aufgabe 10
Das Problem liegt darin, dass wenn ein Leerzeichen zurückgegeben wird in pycharm (Jupyter Notebook),
ein leerer String abgespeichert wird, während aber in der Konsole das Leerzeichenabgespeichert wird.
Damit dies kein Problem ist, habe ich eine Abtrennung der beiden Fälle gemacht, da ansonsten ein Error ausgegeben wird.
"""

# Variante 2: Falls eine leere Ziffer auch akzeptiert wird. (Also nicht Aufgabenstellung)
string = input("Bitte einen beliebigen String eingeben:")
ziffer = input("Bitte eine beliebige Ziffer eingeben:")
result = "Ziffer darf laut Aufgabenstellung nur ein Zeichen lang sein"

# Falls die Ziffer nicht 1 charakter lang oder leer ist
if len(ziffer) == 1 or ziffer == '':
    result = "Gewählter Srting:\t" \
             +  "'" + string + "'" \
             + "\nGewählte Ziffer:\t" \
             + "'" + ziffer + "'"
    if ziffer == "":
        result += "\n" + str(string.split())
    else:
        result += "\n" + str(string.split(ziffer))
print(result)