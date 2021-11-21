"""
Author: Alexandru Schneider
Datum: 16. 11. 2021
Programmiersprache: Python 3.8.8
Aufgabe 35
"""


def isPrime(number) -> bool:
    if number == 2 or number == 3: return True
    if number % 2 == 0 or number < 2: return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def primNumbers(number) -> int:
    result = 0
    for value in range(number+1):
        if isPrime(value):
            result += 1
    return result


nummern = 100000
anz_Zahlen = primNumbers(nummern)
print(f"Es gibt {anz_Zahlen} Primzahlen kleiner als {nummern}")
