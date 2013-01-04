# -*- coding: cp1252 -*-
#Modulo main.py
#!\Users\Presario\Documents\python\PyDarkQuest
# -*- coding: utf-8 –*-

import sys
sys.path.append("C:\Users\Presario\Documents\python\PyDarkQuest")
from heroeclass import Heroe
import pygame.mixer

pygame.mixer.init(22050,-16,2,2048)
pygame.mixer.music.load("C:\Python27\data\ero.mp3")
pygame.mixer.music.play()


nombre=raw_input("Choose your name: ")
print "Choose your Class:"
print "(1)Warrior"
print "(2)Mage"
print "(3)Rouge"
select=0
heroe=Heroe()
while (select>3 or select<1):
    select=int(raw_input("Your Choise: "))
    if select==1:
        heroe.clasWar()
    elif select==2:
        heroe.clasMage()
    elif select==3:
        heroe.clasRou()
    else:
        print "Wrong Answer"

print nombre
heroe.mostrar()

raw_input()

pygame.mixer.music.stop()
