"""
scrivere un programma che :

chiede all'utente la distanza percorsa (in km)e il tempo impiegasto(in ore)
calcola la velocità media
stampa il risultato con due cifre decimale e indica l'unità di misura

"""

distanza=input("inserire la distanza in Km")
distanza=float(distanza)
tempo=input("inserire il tempo impiegato in ore")
tempo=int(tempo)
velocita=distanza/tempo
velocita=round(velocita,2)
print(velocita)