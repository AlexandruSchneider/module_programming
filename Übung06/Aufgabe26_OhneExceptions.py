"""
Author: Alexandru Schneider
Datum: 09. 11. 2021
Programmiersprache: Python 3.8.8
Aufgabe 26 ohne Exceptions
"""
import re

# Exceptions sollten grundsätzlich vermieden werden
# somit kann das Ganze zum Beispiel auch so gelöst werden:
studenten = ["Alex", "Andre", "Benito", "Raphael", "Rafael"]
punkteListe = []

# This checks if the grad is in between 1.0 and 6.0
# First part checks if number is in between 1.0 and 5.9 and
# last past checks if number is 6.0
# The value is also possible to write in , or .
numFormat = re.compile("^[1-5]([,.][0-9])?$|^[6]([,.][0])?$")

for student in studenten:
    validNote = False
    inputString = f"Note für Student {student} zwischen 1 und 6 eingeben: "
    while not validNote:
        note = input(inputString)
        if re.fullmatch(numFormat, note):
            validNote = True
            punkteListe.append(float(note))
        else:
            inputString = f"Für {student} eine gültige Note eingeben: "

print(studenten)
print(punkteListe)
