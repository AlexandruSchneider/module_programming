"""
Author: Alexandru Schneider
Datum: 14. 11. 2021
Programmiersprache: Python 3.8.8
Aufgabe 31
"""


def summieren(value) -> int:
    result = 0
    for number in range(value+1):
        result += number

    return result


value = int(input("Eine Ganzzahl zum summieren geben: "))
print(f"Die eingegebene Zahl ist: \n{value} und summiert ergibt das: {summieren(value)}")
