# -*- coding: cp1252 -*-

import random
import pygame.mixer
import time


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
        damage=(atFoe/self.defensa)*10
        print "Damage ", damage
        self.hp=self.hp-(atFoe/self.defensa)*10
        if damage>=30:
            pygame.mixer.music.load("C:\Python27\data\epico.mp3")
            pygame.mixer.music.play()
            time.sleep(3)
        elif damage>=20:
            pygame.mixer.music.load("C:\Python27\data\excele.mp3")
            pygame.mixer.music.play()
            time.sleep(3)
        elif damage>=10:
            pygame.mixer.music.load("C:\Python27\data\moderado.mp3")
            pygame.mixer.music.play()
            time.sleep(3)
        elif damage>0:
            pygame.mixer.music.load("C:\Python27\data\inefec.mp3")
            pygame.mixer.music.play()
            time.sleep(3)
        elif damage<=0:
            pygame.mixer.music.load("C:\Python27\data\odan.mp3")
            pygame.mixer.music.play()
            time.sleep(3)
