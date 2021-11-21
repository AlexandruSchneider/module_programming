"""
Author: Alexandru Schneider
Datum: 05. 11. 2021
Programmiersprache: Python 3.8.8
Aufgabe 30
"""
from sklearn.metrics import mean_squared_error

listeL = [11.1, 10.4, 320.4, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 6.9, 4.2, 1.78, 9.11, 3.14, 6.66]
listeS = sorted(listeL)

# Mit Funktion
print(f"Funktion von sklearn: {mean_squared_error(listeL, listeS)}")

# Ohne Funtion, also nach Formel
mse = 0
N = len(listeL)
for i in range(N):
    mse += (listeL[i] - listeS[i]) ** 2

mse = 1 / N * mse
print(f"Ohne Funktion: {mse}")
