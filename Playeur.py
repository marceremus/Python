class Playeur:

    def __init__(self, pseudo, health, attack):  # constructeur
        self.pseudo = pseudo
        self.health = health
        self.attack = attack

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def damage(self, damage):
        self.health -= damage
        print("Aie.. vous venez de subir ", damage, " dégats !")

    def attack_playeur(self, target_playeur):
        target_playeur.damage(self.attack)