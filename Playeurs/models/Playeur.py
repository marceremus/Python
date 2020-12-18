class Playeur:

    def __init__(self, pseudo, health, attack):  # constructeur
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.arme = None
        print("Bienvenue au joueur", pseudo, "/Points de vie: ", health, "/ Attaque", attack)

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def makeDamage(self, damage):
        self.health -= damage
        print("Aie.. vous venez de subir ", damage, " dégats !")

    def attackPlayeur(self, target_playeur):
        damage = self.attack

        if self.hasArme():
            damage += self.arme.getDamageAmount()

        target_playeur.makeDamage(damage)

    def hasArme(self):
        return self.arme is not None

    def setArme(self, arme):
        self.arme = arme
