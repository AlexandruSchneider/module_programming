"""
Author: Alexandru Schneider
Datum: 14. 11. 2021
Programmiersprache: Python 3.8.8
Aufgabe 32
"""
from math import pi, e


def fakRek(number) -> int:
    if number == 1 or number == 0:
        return 1
    else:
        return number * fakRek(number-1)


def fakIter(number) -> int:
    result = 1
    for value in range(1, number+1):
        if number == 1 or number == 0:
            return result
        result *= value
    return result


def stirling(number) -> int:
    return (2*pi*number)**0.5*((number/e)**number)


number = int(input("Eine Ganzzahl eingeben: "))
print(f"Rekursiv: {fakRek(number)}\n")
print(f"Iterativ: {fakIter(number)}\n")
print(f"Sterling: {stirling(number)}\n")

differenz = []
relDifferenz = []
for i in range(1, 101):
    resFak = fakRek(i)
    resSti = stirling(i)
    diff = resFak-resSti
    relDiff = (resFak-resSti)/resSti*100
    differenz.append(diff)
    relDifferenz.append(relDiff)
    print(f"Fakultät von {i} | Differenz: {diff} | realtive Differenz: {relDiff}")