"""
Author: Alexandru Schneider
Datum: 16. 11. 2021
Programmiersprache: Python 3.8.8
Aufgabe 33
"""


def auswertenString(string):
    laenge = len(string)
    anzKlein = sum(map(str.islower, string))
    anzGross = 0
    for char in string:
        if char.isupper():
            anzGross += 1
    return laenge, anzKlein, anzGross


text = input("Irgendeinen String eingeben: ")
laenge, anzKlein, anzGross = auswertenString(string=text)

print(f"Der String \"{text}\" ist {laenge} Zeichen lang. \nBesitzt {anzKlein} Kleinbuchstaben und {anzGross} Grossbuchstaben")
