"""
Author: Alexandru Schneider
Datum: 13. 10. 2021
Programmiersprache: Python 3.8.8
Aufgabe 19
"""
# for Schleife (Aufgabenstellung)
print("\nFor Schleife: ")
j = 0
for i in range (1, 100):
    j += i
    print(j, end = " ")

# while Schleife (Mein Code)
print("\n\nWhile Schleife: ")
# Index ist zwei, weil bei range der Wert 1 nicht mitgezählt wird
index = 2

# j ist 1, weil Bei der Zahl 1 begonnen wird
j = 1
while index < 101:
    print(j, end = " ")
    j += index
    # Als letztes den Index erhöhen
    index += 1