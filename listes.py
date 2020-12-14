#!/usr/bin/env python3
#import statistics
from statistics import mean
from random import shuffle

# creation d'une liste vide 
# players = [];

players = ["Alex", "John", "Sara"]

for player in players:
    print("Le prénom du joueur {}".format(player))

# ajouter un prenom
players.append('Carla')

for player in players:
    print("Le prénom du joueur {}".format(player))

# afficher le prenom du 2eme joueur (indice 1) car on compte du 0
print("Le nom du 2ème joueur est : {}".format(players[1]))

# afficher le dernier nom des joueurs
print("Le nom du dernier joueur est : {}".format(players[len(players)-1]))

# insert un nom dans la liste (indice 3)
players.insert(3, "Karl")
print(players)

# modifier les prenoms dans la liste 
players[1:2] = ["Seb", "Nono"]
print(players)

# ajouter plusieurs nom a la fin de la liste
players.extend(["Tom", "Sami"])
print(players)

# suppression d'un nom de la liste 
del players[4]
print(players)

# OU autrement : suppression d'un nom de la liste 
players.pop(3)
print(players)

# OU autrement par le nom : suppression d'un nom de la liste 
players.remove("Tom")
print(players)

# vider la liste 
players.clear()
print(players)

# ____________########______________

notes = [11,2,15,8,17]

def avgNote(lista):
    sommeDesNotes = 0
    nbElementList = len(lista)
    moyenne = 0

    for n in lista:
        sommeDesNotes += n

    moyenne = sommeDesNotes/nbElementList
    return moyenne

print(avgNote(notes))

# calcul de la moyenne en utilisant le module statistics
# result = statistics.mean(notes)
result = mean(notes)
print(result)

# on melange des notes 
print(notes)
shuffle(notes)
print(notes)


# creation d'une table a partire d'un delimitateur
text = input("Entrer une chaine sous la forme (email-pseudo-motdepass)").split("-")
print(text)
print("Salut {}, ton e-mail est : {} et ton mot de passe est {}".format(text[1], text[0], text[2]))

