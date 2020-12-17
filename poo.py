from Playeur import Playeur


#playeur = Playeur()
# print("Hello {}, votre vie est de {} et vous avez {} points d'attaque ".format(playeur.pseudo, playeur.health, playeur.attack))

playeur = Playeur("toto", 20, 3)

playeur1 = Playeur("tata", 15, 5)
# playeur.damage(2)
playeur.attack_playeur(playeur1)
print(playeur.get_pseudo(), " attaque ", playeur1.pseudo)

print("Vous possèdez désormais : ", playeur.health , " points de vie.")
print("Vous possèdez désormais : ", playeur1.health , " points de vie.")
