#!/usr/bin/env python3

# la boucle for

for num_client in range(1,6):
    print("Vous ête le client n° {}".format(num_client))

listEmails = [
    "toto@toto.fr",
    "tata@tata.fr",
    "titi@titi.fr",
]

blacklist = ["nana@nana.fr", "tata@tata.fr"]
# boucle foreach
for email in listEmails:
    if email in blacklist:
        print("Cette e-mail est interdit {}".format(email))
        continue

    print("E-mail envoyé à {}".format(email))


# boucle while
salary = 1500
prime = 120
# tant que le salairé a le salaire < 2000 euros, il percoit une prime de 120 euros
while salary < 2000:
    salary +=prime
    print("Votre salaire est de {}".format(salary))


# Jeu juste prix
# Déterminer un prix pour un article
# Demander à l'utilisateur de saisir le prix
# tant que le prix proposé par l'utilisateur n'est pas égale au prix
# de l'article, la question doit être poser

prixArticle = 1220
compteur = 0
justPrix = False

while not justPrix:
    question = int(input("Quel est le prix de cet article ?"))
    compteur += 1

    if question < prixArticle :
        print("Le prix est suppérieur")
    elif question > prixArticle :
        print("Le prix est inférieur")
    else:
        justPrix = True
        print(" SUPER, Vous avez gagné !!! .. et c'est seulement après {} essais ".format(compteur))



