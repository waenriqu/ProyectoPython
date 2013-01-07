# -*- coding: cp1252 -*-
#Modulo heroeclass.py
#!\Users\Presario\Documents\python\PyDarkQuest

import sys, pygame
sys.path.append("C:\Users\Presario\Documents\python\PyDarkQuest")
from enemie import Enemie
import random

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
        print "Damage ", (atFoe/self.defensa)*10
        Heroe.hp=Heroe.hp-(atFoe/self.defensa)*10

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
    def pelea(self, enemigo):
        while (self.hp>0 and enemigo.hp>0):
                    if(enemigo.velocidad>self.velocidad):
                        aleat=random.randrange(1, 5)
                        print aleat
                        if (aleat==1):
                            print "goblin is watching"
                        else:
                            print "goblin ataca"
                            self.hp=self.hp-(enemigo.ataque/self.defensa)*10
                        print "Atacaras? (1)si (2)no"
                        select=0
                        while (select<1 or select>2):
                            select=int(raw_input("Your Choise: "))
                        if select==1:
                           enemigo.hp_lost(self.ataque)
                        else:
                            print "No dejes que te engañe"
                    else:
                        print "Atacaras? (1)si (2)no"
                        select=0
                        while (select<1 or select>2):
                            select=int(raw_input("Your Choise: "))
                        if select==1:
                            enemigo.hp_lost(self.ataque)
                        else:
                            print "No dejes que te engañe"
                        aleat=random.randrange(1, 5)
                        print aleat
                        if (aleat==1):
                            print "goblin is watching"
                        else:
                            self.hp=self.hp-(enemigo.ataque/self.defensa)*10
                            print "goblin ataca"
                    print self.hp, enemigo.hp
                    self.indiVida()

