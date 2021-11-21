"""
Author: Alexandru Schneider
Datum: 07. 10. 2021
Programmiersprache: Python 3.8.8
Aufgabe 14
"""
#Der erste Teil ist schon "False" da Wahr und Falsch nicht Wahr sind
print(True and False and True or False)

# 3 < 3.0 ist   false
# or
# not not       negiert sich selber
# True or False true
print((3 < 3.0) or (not(not(True or False))))

# 3 ist ungleich 4
# 4 ist ungleich 5
# 5 ist ungleich 6
# 6 ist ungleich 3
print(3 != 4 != 5 != 6 != 3)

a = 3
b = 4
c = 5
# 3*3 = 9
# 4*4 = 16
# Summe = 25
# 5*5 = 25
print(a**2 + b**2 == c**2)