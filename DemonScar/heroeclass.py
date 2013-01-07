#Modulo heroeclass.py
#!\Users\Presario\Documents\python\PyDarkQuest


class Heroe:
    name=""
    clase=""
    hp=0
    ataque=0
    defensa=0
    velocidad=0
    magia=0

    def clasWar(self):
        Heroe.clase="Warrior"
        Heroe.hp=50
        Heroe.ataque=23
        Heroe.defensa=21
        Heroe.velocidad=13
        Heroe.magia=10

    def clasMage(self):
        Heroe.clase="Mage"
        Heroe.hp=36
        Heroe.ataque=12
        Heroe.defensa=14
        Heroe.velocidad=21
        Heroe.magia=28

    def clasRou(self):
        Heroe.clase="Rouge"
        Heroe.hp=41
        Heroe.ataque=19
        Heroe.defensa=15
        Heroe.velocidad=29
        Heroe.magia=19

    def hp_lost(self, atFoe):
        Heroe.hp=Heroe.hp-(atFoe/defensa)*10

    def hp_gain(self, itemRec):
        Heroe.hp=Heroe.hp+itemRec
    
    def mostrar(self):
        print "Clase:", Heroe.clase
        print "Vida:", Heroe.hp
        print "Ataque:", Heroe.ataque
        print "Defensa:", Heroe.defensa
        print "Velocidad:", Heroe.velocidad
        print "Magia:", Heroe.magia

        def indiVida(self):
        if self.hp>35:
            print "Estas muy bien"
        elif self.hp>30:
            print "Suenas agotado"
        elif self.hp>23:
            print "Te estas poniendo palido"
        elif self.hp>15:
            print "Veo tu sangre correr"
        elif self.hp>7:
            print "Tu vista se nubla, ya no puedes avanzar mas"
        elif self.hp==1:
            print "Deshecho ya ni arrastrarte te servira"
