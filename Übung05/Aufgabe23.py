"""
Author: Alexandru Schneider
Datum: 21. 10. 2021
Programmiersprache: Python 3.8.8
Aufgabe 23
"""
listeA = [1,3,11,23,4,5]
listeB = [4,3,11,23,7,8]


# a) überprüfung der Listen auf Gleichheit
if listeA == listeB:
	print(f"Die Listen: {listeA} und {listeB} sind gleich.")
else:
	print(f"Die Listen: {listeA} und {listeB} sind nicht gleich.")


# b) Liste mit boolean Werten falls beide Werte in den Listen gleich sind
boolList = []
if len(listeA) == len(listeB):
	listLength = len(listeA)
	for index in range(listLength):
		boolValue = False
		if listeA[index] == listeB[index]:
			boolValue = True
		boolList.append(boolValue)
print(f"Die Werte der Listen: \n{listeA} und \n{listeB} verglichen ergeben: \n{boolList}")


# c) Länge der beiden Listen
if len(listeA) == len(listeB):
	print(f"Die Länge der Listen ist gleich und beträgt: {len(listeA)}")
else:
	print(f"Die Länge der Listen ist nicht gleich, der Unterschied beträgt: {abs(len(listeA) - len(listeB))}")


# d) 1) Listen Sortieren
listeACopy = listeA[::]
listeBCopy = listeB[::]
listeACopy.sort()
listeBCopy.sort()
print(f"Liste A: {listeA} \t\t\t\t----> {listeACopy}")
print(f"Liste B: {listeB} \t\t\t\t----> {listeBCopy}")

# d) 2) listen zusammenfügen und sortieren
listeC = listeA + listeB
listeC.sort()
print(f"Liste C: {listeA + listeB} \t----> {listeC}")
