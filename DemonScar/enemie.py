class Enemie:
    hp=0
    ataque=0
    defensa=0
    velocidad=0
    magia=0

    def defEnem(self, vida, atak, defense, spd, magic):
        self.hp=vida
        self.ataque=atak
        self.defensa=defense
        self.velocidad=spd
        self.magia=magic

    def hp_lost(self, atFoe):
        self.hp=self.hp-(atFoe/self.defensa)*10
