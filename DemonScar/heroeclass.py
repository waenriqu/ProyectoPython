# -*- coding: cp1252 -*-
#Modulo heroeclass.py
#!\Users\Presario\Documents\python\PyDarkQuest

import sys, pygame
sys.path.append("C:\Users\Presario\Documents\python\PyDarkQuest")
from enemie import Enemie
import random
import pygame.mixer
import time


class Heroe:
    name=""
    clase=""
    hp=0
    ataque=0
    defensa=0
    velocidad=0
    magia=0
    spell=0

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
            pygame.mixer.music.load("C:\Python27\data\hpbien.mp3")
            pygame.mixer.music.play()
            time.sleep(3)
        elif self.hp>30:
            pygame.mixer.music.load("C:\Python27\data\hpmed.mp3")
            pygame.mixer.music.play()
            time.sleep(3)
        elif self.hp>23:
            pygame.mixer.music.load("C:\Python27\data\palido.mp3")
            pygame.mixer.music.play()
            time.sleep(3)
        elif self.hp>15:
            pygame.mixer.music.load("C:\Python27\data\sangre.mp3")
            pygame.mixer.music.play()
            time.sleep(3)
        elif self.hp>7:
            pygame.mixer.music.load("C:\Python27\data\hpmal.mp3")
            pygame.mixer.music.play()
            time.sleep(3)
        elif self.hp==1:
            pygame.mixer.music.load("C:\Python27\data\hp1.mp3")
            pygame.mixer.music.play()
            time.sleep(3)
    def pelea(self, enemigo):
        pygame.mixer.music.load("C:\Python27\data\ero.mp3")
        pygame.mixer.music.play()
        time.sleep(5)
        while (self.hp>0 and enemigo.hp>0):
                    if(enemigo.velocidad>self.velocidad):
                        aleat=random.randrange(1, 5)
                        #print aleat
                        if (aleat==1):
                            pygame.mixer.music.load("C:\Python27\data\observa.mp3")
                            pygame.mixer.music.play()
                            time.sleep(3)
                        else:
                            pygame.mixer.music.load("C:\Python27\data\hplost.mp3")
                            pygame.mixer.music.play()
                            time.sleep(3)
                            self.hp=self.hp-(enemigo.ataque/self.defensa)*10
                        
                        select=0
                        if self.hp>0:
                            
                            pygame.mixer.music.load("C:\Python27\data\menupelea.mp3")
                            pygame.mixer.music.play()
                            raw_input("Press enter to skip or to continue...")
                            pygame.mixer.music.stop()
                            while (select<1 or select>4):
                                print "(1)Ataque (2)Magia (3)Hechizo (4)Observar"
                                select=int(raw_input("Your Choise: "))
                                if (self.spell==0 and select==3):
                                    pygame.mixer.music.load("C:\Python27\data\ospel.mp3")
                                    pygame.mixer.music.play()
                                    time.sleep(3)
                                    select=0
                            if select==1:
                                enemigo.hp_lost(self.ataque)
                            elif select==2:
                                enemigo.hp_lost(self.magia)
                            elif select==3:
                                enemigo.hp_lost((self.spell/1000)*self.magia)
                                self.magia=self.magia*0.80                                
                            else:
                                pygame.mixer.music.load("C:\Python27\data\otac.mp3")
                                pygame.mixer.music.play()
                                time.sleep(3)
                    else:
                        pygame.mixer.music.load("C:\Python27\data\menupelea.mp3")
                        pygame.mixer.music.play()
                        raw_input("Press enter to skip or to continue...")
                        pygame.mixer.music.stop()
                        select=0
                        while (select<1 or select>4):
                            print "(1)Ataque (2)Magia (3)Hechizo (4)Observar"
                            select=int(raw_input("Your Choise: "))
                            if (self.spell==0 and select==3):
                                pygame.mixer.music.load("C:\Python27\data\ospel.mp3")
                                pygame.mixer.music.play()
                                time.sleep(3)
                                select=0
                        if select==1:
                            enemigo.hp_lost(self.ataque)
                        elif select==2:
                            enemigo.hp_lost(self.magia)
                        elif select==3:
                            enemigo.hp_lost((self.spell/1000)*self.magia)
                            self.magia=self.magia*0.80
                        else:
                            pygame.mixer.music.load("C:\Python27\data\otac.mp3")
                            pygame.mixer.music.play()
                            time.sleep(3)
                        if enemigo.hp>0:
                            aleat=random.randrange(1, 5)
                            #print aleat
                        
                            if (aleat==1):
                                pygame.mixer.music.load("C:\Python27\data\observa.mp3")
                                pygame.mixer.music.play()
                                time.sleep(3)   
                            else:
                                pygame.mixer.music.load("C:\Python27\data\hplost.mp3")
                                pygame.mixer.music.play()
                                time.sleep(3)
                                print "El enemigo ataca"
                    print "Tu vida ", self.hp, "Vida enemigo", enemigo.hp
                    self.indiVida()

