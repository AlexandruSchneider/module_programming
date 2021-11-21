"""
Author: Alexandru Schneider
Datum: 30. 09. 2021
Programmiersprache: Python 3.8.8
Aufgabe 10
"""
string = input("Bitte einen beliebigen String eingeben: ")
ziffer = input("Bitte eine beliebige Ziffer eingeben: ")
result = "Ziffer darf laut Aufgabenstellung nur ein Zeichen lang sein."

if len(ziffer) == 1:
    result = "\nGewählter Srting:\t" \
             +  "'" + string + "'" \
             + "\nGewählte Ziffer:\t" \
             + "'" + ziffer + "'" \
             + "\n" + str(string.split(ziffer))
print(result)