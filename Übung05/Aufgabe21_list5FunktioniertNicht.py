"""
Author: Alexandru Schneider
Datum: 21. 10. 2021
Programmiersprache: Python 3.8.8
Aufgabe 21_list5 funktioniert nicht
"""
import random

minZahl = 0
maxZahl = 100
anzZahl = 10

list1 = random.sample(range(minZahl, maxZahl), anzZahl)
list2 = random.sample(range(minZahl, maxZahl), anzZahl)

print(f"First List: {list1} Type: {type(list1)}")
print(f"Secnd List: {list2} Type: {type(list2)}")

list3 = list1 + list2
print(f"Third List: {list3} Type: {type(list3)}")

list4 = list1
for value in list2:
	list4.append(value)

print(f"Forth List: {list4} Type: {type(list4)}")

list5 = list1
list5.extend(list2)

print(f"First List 'extend' Second List: {list5}")