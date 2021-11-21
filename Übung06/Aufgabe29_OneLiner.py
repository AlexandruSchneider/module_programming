"""
Author: Alexandru Schneider
Datum: 05. 11. 2021
Programmiersprache: Python 3.8.8
Aufgabe 29 one liner
"""
# Nicht zu empfehlen, da one liner nicht gut wartbar sind!!

d1 = {"Alex": 19, "Andre": 26, "Benito": 21, "Raphael": 24, "Rafael": 22, "Zwischenstuck": 12, "Zusatz": 99}
d2 = {"Alex": 19, "Andre": 26, "Benito": 21, "Raphael": 25, "Rafaela": 22, "Zwischenstuck": 12, "Zusatz1": 999, "EchterZusatz": 666}

# a)
print(f"Die beiden Dicts: \n{d1} und \n{d2} \nsind gleich!" if d1 == d2 else "Die beiden Dicts sind nicht gleich!")

# b)
print([(key in list(d1.keys())) and (key in list(d2.keys())) and (d1[key] == d2[key]) for key in list(dict.fromkeys(list(d1.keys()) + list(d2.keys())))])
