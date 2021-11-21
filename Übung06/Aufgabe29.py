"""
Author: Alexandru Schneider
Datum: 05. 11. 2021
Programmiersprache: Python 3.8.8
Aufgabe 29
"""


dict1 = {"Alex": 19, "Andre": 26, "Benito": 21, "Raphael": 24, "Rafael": 22, "Zwischenstuck": 12, "Zusatz": 99}
dict2 = {"Alex": 19, "Andre": 26, "Benito": 21, "Raphael": 25, "Rafaela": 22, "Zwischenstuck": 12, "Zusatz1": 999, "EchterZusatz": 666}

dict1Length = len(dict1)
dict2Length = len(dict2)

dict1Keys = list(dict1.keys())
dict2Keys = list(dict2.keys())

# a)
if dict1 == dict2:
    print(f"Die beiden Dicts: \n{dict1} und \n{dict2} \nsind gleich!")
else:
    print("Die beiden Dicts sind nicht gleich!")

# b)
resultList = []
resultListBool = []
iterator = 0
while iterator < min(dict1Length, dict2Length):
    dict1Val = dict1[dict1Keys[iterator]]
    dict2Val = dict2[dict2Keys[iterator]]
    if dict1Val != dict2Val or dict1Keys[iterator] != dict2Keys[iterator]:
        resultList.append(iterator)
        resultListBool.append(False)
    else:
        resultListBool.append(True)
    iterator += 1

def addIfDictionariesArentSameLength(list1, list2, dictLength, iterator_Val=0):
    iterator_Copy = iterator_Val
    while iterator_Copy < dictLength:
        list1.append(iterator_Copy)
        list2.append(False)
        iterator_Copy += 1
    return list1, list2

if dict1Length != dict2Length:
    resultList, resultListBool = addIfDictionariesArentSameLength(resultList, resultListBool, max(dict1Length, dict2Length), iterator)

print(f"Bei den Indizen: {resultList} sind die Werte und/oder Schlüssel unterschiedlich!")
print(f"Die Werte in einer Liste aus Booleans sehen so aus: {resultListBool}")

