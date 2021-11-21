"""
Author: Alexandru Schneider
Datum: 05. 11. 2021
Programmiersprache: Python 3.8.8
Aufgabe 27
"""
name = input("Namen eingeben: ")
multiplikation = 1
summe = 0

print(f"Eingegebener Name: {name}\nIn Zahlen: ")
for letter in name:
    # Get Ascii Value
    value = ord(letter)

    # Get the Values for encoding
    multiplikation *= value
    summe += value

    print(f"{letter}:[{value}]", end=" ")

print(f"\nProdukt aller Werte: {multiplikation}\n{multiplikation} durch {summe} ergibt: ")

# Print and Encode number
print(int(multiplikation/summe))
