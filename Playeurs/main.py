from models.Playeur import Playeur
from models.Arme import *
from models.Guerrier import Guerrier

if __name__ == '__main__':

    couteau = Arme("Couteau", 3)
    pistolet = Arme("Pistolet", 6)

    playeur1 = Playeur("toto", 20, 3)
    playeur1.setArme(couteau)

    playeur2 = Playeur("tata", 15, 5)
    playeur2.setArme(pistolet)

    playeur1.attackPlayeur(playeur2)
    playeur2.attackPlayeur(playeur1)

    print(playeur1.get_pseudo(), " attaque ", playeur2.pseudo)

    print("Player1, vous possèdez désormais : ", playeur1.health , " points de vie.")
    print("Player2, vous possèdez désormais : ", playeur2.health , " points de vie.")


    guerrier = Guerrier("Guerrier 1", 18, 7, 8)
    print(guerrier)
    guerrier.makeDamage(4)
    print("Le guerrier",guerrier.pseudo, "a", guerrier.get_health(), "points de vie et l'armure : ", guerrier.getArmorPoint())
