# Autor: Alexandru Schneider
# Programmiersprache: Python 3.8.8
# Datum: 24. 09. 2021

# Da die Basis hoch 1 immer die Basis ist,
# können diese Werte direkt gesetzt werden
resultat = basis = 3
potenz = 1

# Ich überprüfe auf die letzten beiden Stellen 
# Wenn also nicht 01 in den letzten  beiden Stellen steht
# wird wieder der While Loop begonnen 
while (resultat%100) != 1:
   resultat *= basis
   potenz += 1
   print("3 hoch", potenz, "ergibt", resultat)
else:
   print("Resultat wurde nach", potenz, "Potenzierungen gefunden")