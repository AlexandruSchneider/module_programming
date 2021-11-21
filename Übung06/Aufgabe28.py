"""
Author: Alexandru Schneider
Datum: 05. 11. 2021
Programmiersprache: Python 3.8.8
Aufgabe 28
"""
import re

id = input("Eine ID eingeben: ")

# [A-Z]: alle Buchstaben
# {1,3}: eins bis 3 Buchststaben
# [0-9]: Zahlen bzw. Ziffern von 0 bis 9
# {5}: Genau 5 Zeichen
validationStringA = "[A-Z]{1,3}[0-9]{5}"
validationStringB = "[A-Z]{2}[0-9]{1}"

# a)
if re.fullmatch(validationStringA, id):
    print("Bedingung A ist erfüllt!")
# b)
elif re.fullmatch(validationStringB, id):
    print("Bedingung B ist erfüllt!")
else:
    print("Keine der in der Aufgabenstellung genannten Bedingungen ist erfüllt!")
