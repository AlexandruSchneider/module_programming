"""
Author: Alexandru Schneider
Datum: 21. 10. 2021
Programmiersprache: Python 3.8.8
Aufgabe 21
"""
import random

minZahl = 0
maxZahl = 100
anzZahl = 10

# Generate List randomly
list1 = random.sample(range(minZahl, maxZahl), anzZahl)
list2 = random.sample(range(minZahl, maxZahl), anzZahl)

print(f"First List: {list1} Type: {type(list1)}")
print(f"Secnd List: {list2} Type: {type(list2)}")

# Add list1 and list2 together and save the result in list3
list3 = list1 + list2

print(f"Third List: {list3} Type: {type(list3)}")

# Make new list4, because list1 shouldn't be changed
# Iterate through list2 and add each value to list4
list4 = list1[::]
for value in list2:
	list4.append(value)

print(f"Forth List: {list4} Type: {type(list4)}")

# Make new list5, because list1 shouldn't be changed
# Use method: "extend" to add Values of list2 to list5 (which has the same values as list1)
list5 = list1[::]
list5.extend(list2)

print(f"First List 'extend' Second List: {list5}")