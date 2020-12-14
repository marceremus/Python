#!/usr/bin/env python3
prixTicketAdulte = 7
prixTicketEnfant = 5
prixPopcorn = 5
choixTicketAdulte = False
choixTicketEnfant = False
choixPopcorn = False
aPayer = 0

responseChoixTicketAdulte = input("Souhaitez vous acheter un ticket adulte? (pappez o pour 'oui', n pour 'non')")
responseChoixTicketEnfant = input("Souhaitez vous acheter un ticket enfant? (pappez o pour 'oui', n pour 'non')")
responseChoixPopcorn = input("Souhaitez vous acheter le popcorn? (pappez o pour 'oui', n pour 'non')")

if(responseChoixTicketAdulte == "o"):
    choixTicketAdulte = True


if(responseChoixTicketEnfant == "o"):
    choixTicketEnfant = True


if(responseChoixPopcorn == "o"):
    choixPopcorn = True


if((choixTicketAdulte == True) and (choixTicketEnfant == True) and (choixPopcorn == True)):
    aPayer = prixTicketAdulte + prixTicketEnfant + prixPopcorn
elif ((choixTicketAdulte == True) and (choixTicketEnfant == True)):
    aPayer = prixTicketAdulte + prixTicketEnfant
elif ((choixTicketEnfant == True) and (choixPopcorn == True)):
    aPayer = prixTicketEnfant + prixPopcorn
elif((choixTicketAdulte == True)):
    aPayer = prixTicketAdulte
else:
    aPayer = prixTicketEnfant


print("Vous devez payer {} euros".format(aPayer))