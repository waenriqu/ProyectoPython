# -*- coding: cp1252 -*-
#Modulo main.py
#!\Users\Presario\Documents\python\PyDarkQuest
# -*- coding: utf-8 –*-

import sys, pygame
sys.path.append("C:\Users\Presario\Documents\python\PyDarkQuest")
from heroeclass import Heroe
import pygame.mixer
import time

pygame.mixer.init(22050,-16,2,2048)

pygame.mixer.music.load("C:\Python27\data\demoscar.mp3")
pygame.mixer.music.play()
time.sleep(3)

pygame.mixer.music.load("C:\Python27\data\ero.mp3")
pygame.mixer.music.play()

pygame.mixer.music.load("C:\Python27\data\ero2.mp3")
pygame.mixer.music.play()
nombre=raw_input("--> ")
pygame.mixer.music.load("C:\Python27\data\clase.mp3")
pygame.mixer.music.play()
select=0
heroe=Heroe()
while (select>3 or select<1):
    select=int(raw_input("--> "))
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
pygame.mixer.music.stop()

pygame.mixer.music.load("C:\Python27\data\intro1.mp3")
pygame.mixer.music.play()
time.sleep(25)
pygame.mixer.music.load("C:\Python27\data\intro2.mp3")
pygame.mixer.music.play()
time.sleep(25)
pygame.mixer.music.load("C:\Python27\data\intro3.mp3")
pygame.mixer.music.play()
time.sleep(15)
pygame.mixer.music.load("C:\Python27\data\intro4.mp3")
pygame.mixer.music.play()
time.sleep(25)
pygame.mixer.music.load("C:\Python27\data\intro5.mp3")
pygame.mixer.music.play()
time.sleep(15)
pygame.mixer.music.load("C:\Python27\data\intro6.mp3")
pygame.mixer.music.play()
time.sleep(15)

print "(1)Continuar"
print "(2)Salir de la cueva"
select=0
while (select>2 or select<1):
    select=int(raw_input("Your Choice: "))
    if select==1:
        pygame.mixer.music.load("C:\Python27\data\room2.mp3")
        pygame.mixer.music.play()
        time.sleep(15)
        pygame.mixer.music.load("C:\Python27\data\room2_1.mp3")
        pygame.mixer.music.play()
        time.sleep(15)
    elif select==2:
        ppygame.mixer.music.load("C:\Python27\data\over.mp3")
        pygame.mixer.music.play()
        time.sleep(15)
    else:
        print "Wrong Answer"

pygame.mixer.music.load("C:\Python27\data\PrevioBatalla.mp3")
pygame.mixer.music.play()
time.sleep(15)
#Codigo de Pelea

pygame.mixer.music.load("C:\Python27\data\DespuesBatalla.mp3")
pygame.mixer.music.play()
time.sleep(15)

pygame.mixer.music.load("C:\Python27\data\AntesRoom3-2.mp3")
pygame.mixer.music.play()
time.sleep(15)

pygame.mixer.music.load("C:\Python27\data\AnteRoom3-3.mp3")
pygame.mixer.music.play()
time.sleep(15)

#-----------------------Room 3------------------------------------

print "(1) Camino de la izquierda"
print "(2) Camino de la derecha"


select=0
while (select>2 or select<1):
    select=int(raw_input("Your Choice: "))
    if select==1:
        pygame.mixer.music.load("C:\Python27\data\Room3op1.mp3")
        pygame.mixer.music.play()
        time.sleep(15)
    elif select==2:
        ppygame.mixer.music.load("C:\Python27\data\Room3op2.mp3")
        pygame.mixer.music.play()
        time.sleep(15)
    else:
        print "Wrong Answer"

pygame.mixer.music.load("C:\Python27\data\DespRoom3.mp3")
pygame.mixer.music.play()
time.sleep(15)

pygame.mixer.music.load("C:\Python27\data\DespRoom3-2.mp3")
pygame.mixer.music.play()
time.sleep(15)

print "(1) Puerta de piedra"
print "(2) Puerta de huesos"
print "(3) Puerta de madera"

while (select>3 or select<1):
    select=int(raw_input("Your Choice: "))
    if select==1:
        pygame.mixer.music.load("C:\Python27\data\Room4op1.mp3")
        pygame.mixer.music.play()
        time.sleep(15)
        pygame.mixer.music.load("C:\Python27\data\Room4op1-2.mp3")
        pygame.mixer.music.play()
        time.sleep(15)
        
    if select==2:
        ppygame.mixer.music.load("C:\Python27\data\Room4op2.mp3")
        pygame.mixer.music.play()
        time.sleep(15)
    elif select==3:
        ppygame.mixer.music.load("C:\Python27\data\Room4op3.mp3")
        pygame.mixer.music.play()
        time.sleep(15)
    else:
        print "Wrong Answer"



pygame.mixer.music.stop()


