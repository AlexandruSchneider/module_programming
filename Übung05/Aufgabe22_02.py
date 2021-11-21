"""
Author: Alexandru Schneider
Datum: 21. 10. 2021
Programmiersprache: Python 3.8.8
Aufgabe 22_02
"""
import random

minZahl = 0
maxZahl = 100
anzZahl = 10

originalList = random.sample(range(minZahl, maxZahl), anzZahl)
reversedList =  []

for value in originalList:
	# Add the Value in front of the list (at the first spot)
	reversedList = [value] + reversedList

print(f"Original List: {originalList} Type: {type(originalList)}")
print(f"Reversed List: {reversedList} Type: {type(reversedList)}")