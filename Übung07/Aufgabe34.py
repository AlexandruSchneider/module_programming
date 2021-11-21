"""
Author: Alexandru Schneider
Datum: 16. 11. 2021
Programmiersprache: Python 3.8.8
Aufgabe 34
"""


def sortingLists(list) -> list:
    sortedList = sorted(list)
    sortedReversed = sortedList[::-1]
    return sortedList + sortedReversed


testList = [3, 67, 1, 8, 3, 7]
print(sortingLists(list=testList))
