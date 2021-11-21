"""
Author: Alexandru Schneider
Datum: 21. 10. 2021
Programmiersprache: Python 3.8.8
Aufgabe 22_01
"""
import random

minZahl = 0
maxZahl = 100
anzZahl = 10

reverse = -1

originalList = random.sample(range(minZahl, maxZahl), anzZahl)
reversedList = originalList[::reverse]

print(f"Original List: {originalList} Type: {type(originalList)}")
print(f"Reversed List: {reversedList} Type: {type(reversedList)}")