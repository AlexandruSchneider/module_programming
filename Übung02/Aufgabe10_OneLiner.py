"""
Author: Alexandru Schneider
Datum: 06. 10. 2021
Programmiersprache: Python 3.8.8
Aufgabe 10
"""

# Variante 3: One-liner
# Das ist nicht semantisch schön und sollte allgemein vermieden werden
# Lesbarkeit und wartbarkeit, sowie fehleranfälligkeit sind höher

print(input("String eingeben: ").split(input("Ziffer eingeben: ")))