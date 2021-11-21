"""
Author: Alexandru Schneider
Datum: 13. 10. 2021
Programmiersprache: Python 3.8.8
Aufgabe 17
"""
import random

givenString2 = list(input("Einen String eingeben: "))
wordLength = int(input("Wie lange sollte der String sein? "))
finalString = ""

for elements in range(0, wordLength):
    finalString = finalString + givenString2[random.randint(0, len(givenString2)-1)]

print(finalString)