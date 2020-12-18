# from Playeur import Playeur

class Guerrier(Playeur):
    def __init__(self, pseudo, health, attack, armor=3):  # constructeur
        super().__init__(pseudo, health, attack)
        # self.pseudo = pseudo
        # self.health = health
        # self.attack = attack
        __
        self.armor = armor
        print("Bienvenue au guerrier", pseudo, "/Points de vie: ", health, "/ Attaque", attack, " et de défonce", armor)

    # def get_pseudo(self):
    #    return self.pseudo

    # def get_health(self):
    #    return self.health

    # def get_attack(self):
    #    return self.attack

    def makeDamage(self, damage):
        if self.armor > 0:
            self.armor -= 1
            damage = 0

        super().makeDamage(damage)
        # self.health -= damage

    def blade(self):
        self.armor = 3
        print("Les points d'armure ont été rechargés")

    def getArmorPoint(self):
        return self.armor