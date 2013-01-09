# -*- coding: cp1252 -*-
#Modulo main.py
#!\Users\Presario\Documents\python\PyDarkQuest
# -*- coding: utf-8 –*-

import sys, pygame
sys.path.append("C:\Users\Presario\Documents\python\PyDarkQuest")
from heroeclass import Heroe
from enemie import Enemie
import random
import pygame.mixer
import time

pygame.mixer.init(22050,-16,2,2048)
#print random.randrange(1,5)
pygame.mixer.music.load("C:\Python27\data\demoscar.mp3")
pygame.mixer.music.play()
raw_input("Press enter to skip or to continue...")

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
        pygame.mixer.music.load("C:\Python27\data\clase.mp3")
        pygame.mixer.music.play()

print nombre
heroe.mostrar()
pygame.mixer.music.stop()

pygame.mixer.music.load("C:\Python27\data\intro1.mp3")
pygame.mixer.music.play()
raw_input("Press enter to skip or to continue...")
pygame.mixer.music.load("C:\Python27\data\intro2.mp3")
pygame.mixer.music.play()
raw_input("Press enter to skip or to continue...")
pygame.mixer.music.load("C:\Python27\data\intro3.mp3")
pygame.mixer.music.play()
raw_input("Press enter to skip or to continue...")
pygame.mixer.music.load("C:\Python27\data\intro4.mp3")
pygame.mixer.music.play()
raw_input("Press enter to skip or to continue...")
pygame.mixer.music.load("C:\Python27\data\intro5.mp3")
pygame.mixer.music.play()
raw_input("Press enter to skip or to continue...")
pygame.mixer.music.load("C:\Python27\data\intro6.mp3")
pygame.mixer.music.play()
raw_input("Press enter to skip or to continue...")

print "(1)Continuar"
print "(2)Salir de la cueva"
select=0
while (select>2 or select<1):
    select=int(raw_input("Tu eleccion: "))
if select==1:
    pygame.mixer.music.load("C:\Python27\data\om2.mp3")
    pygame.mixer.music.play()
    raw_input("Press enter to skip or to continue...")
    pygame.mixer.music.load("C:\Python27\data\om2_1.mp3")
    pygame.mixer.music.play()
    raw_input("Press enter to skip or to continue...")
    pygame.mixer.music.stop()
    select=0
    while (select>2 or select<1):
        print "(1)Subir la ladera \n(2)Continuar recto"
        select=int(raw_input("Tu eleccion: "))
    if select==2:
        heroe.hp=heroe.hp-5
        pygame.mixer.music.load("C:\Python27\data\intro7.mp3")
        pygame.mixer.music.play()
        raw_input("Press enter to skip or to continue...")
        enemigo=Enemie()
        enemigo.defEnem(20, 15, 10, 12, 10)
        pygame.mixer.music.load("C:\Python27\data\intro8.mp3")
        pygame.mixer.music.play()
        time.sleep(4)
        heroe.pelea(enemigo)
        if heroe.hp<=0:
            pygame.mixer.music.load("C:\Python27\data\over.mp3")
            pygame.mixer.music.play()
            time.sleep(4)
            sys.exit()
        pygame.mixer.music.load("C:\Python27\data\gana1.mp3")
        pygame.mixer.music.play()
        raw_input("Press enter to skip or to continue...")
        pygame.mixer.music.stop()
        heroe.hp=heroe.hp+5
        pygame.mixer.music.load("C:\Python27\data\intro9.mp3")
        pygame.mixer.music.play()
        raw_input("Press enter to skip or to continue...")
        pygame.mixer.music.stop()
        
        select=0
        while (select>2 or select<1):
            print "(1) Salida de enfrente \n(2) Hueco"
            pygame.mixer.music.load("C:\Python27\data\sHueco.mp3")
            pygame.mixer.music.play()
            raw_input("Press enter to skip or to continue...")
            pygame.mixer.music.stop()
            select=int(raw_input("Tu eleccion: "))
        if select==1:
            pygame.mixer.music.load("C:\Python27\data\intro10.mp3")
            pygame.mixer.music.play()
            raw_input("Press enter to skip or to continue...")
            pygame.mixer.music.stop()
            select=0
            while (select>2 or select<1):
                pygame.mixer.music.load("C:\Python27\data\sino.mp3")
                pygame.mixer.music.play()
                raw_input("Press enter to skip or to continue...")
                pygame.mixer.music.stop()
                select=int(raw_input("Tu eleccion: "))
            if select==1:
                pygame.mixer.music.load("C:\Python27\data\caegol.mp3")
                pygame.mixer.music.play()
                raw_input("Press enter to skip or to continue...")
                pygame.mixer.music.stop()
                enemigo.defEnem(30, 25, 15, 10, 5)
                pygame.mixer.music.load("C:\Python27\data\golem.mp3")
                pygame.mixer.music.play()
                time.sleep(3)
                heroe.pelea(enemigo)
                if heroe.hp<=0:
                    pygame.mixer.music.load("C:\Python27\data\over.mp3")
                    pygame.mixer.music.play()
                    time.sleep(5)
                    sys.exit()
                
            elif select==2:
                pygame.mixer.music.load("C:\Python27\data\serp.mp3")
                pygame.mixer.music.play()
                raw_input("Press enter to skip or to continue...")
                pygame.mixer.music.stop()
                pygame.mixer.music.load("C:\Python27\data\serp2.mp3")
                pygame.mixer.music.play()
                time.sleep(3)
                enemigo.defEnem(25, 20, 15, 40, 20)
                heroe.pelea(enemigo)
                if heroe.hp<=0:
                    pygame.mixer.music.load("C:\Python27\data\over.mp3")
                    pygame.mixer.music.play()
                    time.sleep(5)
                    sys.exit()
            pygame.mixer.music.load("C:\Python27\data\intro11.mp3")
            pygame.mixer.music.play()
            raw_input("Press enter to skip or to continue...")
            pygame.mixer.music.stop()
            select=0
            while (select!=1):
                print "Avanzar? (1)Si (2)Observar un rato mas"
                pygame.mixer.music.load("C:\Python27\data\onza.mp3")
                pygame.mixer.music.play()
                select=int(raw_input("Tu eleccion: "))
        if select==2:
            
            heroe.hp=heroe.hp-5
            pygame.mixer.music.load("C:\Python27\data\charco.mp3")
            pygame.mixer.music.play()
            raw_input("Press enter to skip or to continue...")
            pygame.mixer.music.stop()
            heroe.spell=3000
            pygame.mixer.music.load("C:\Python27\data\hechizo.mp3")
            pygame.mixer.music.play()
            raw_input("Press enter to skip or to continue...")
            pygame.mixer.music.stop()
            pygame.mixer.music.load("C:\Python27\data\escal.mp3")
            pygame.mixer.music.play()
            raw_input("Press enter to skip or to continue...")
            pygame.mixer.music.stop()
            select=0
            while select!=1:
                pygame.mixer.music.load("C:\Python27\data\conti.mp3")
                pygame.mixer.music.play()
                time.sleep(3)
                select=int(raw_input("Tu eleccion: "))
                
         
        pygame.mixer.music.load("C:\Python27\data\salon.mp3")
        pygame.mixer.music.play()
        raw_input("Press enter to skip or to continue...")
        pygame.mixer.music.stop()
        select=int(raw_input("Digitalos: "))
        pygame.mixer.music.load("C:\Python27\data\pedes.mp3")
        pygame.mixer.music.play()
        raw_input("Press enter to skip or to continue...")
        pygame.mixer.music.stop()
        if select==729:
            print "Pilas loco aqui debes poner el final final con el evento y todo"
        elif select==297 or select==972 or select==927 or select==279 or select==792:
            pygame.mixer.music.load("C:\Python27\data\kirian.mp3")
            pygame.mixer.music.play()
            raw_input("Press enter to skip or to continue...")
            pygame.mixer.music.stop()
            enemigo.defEnem(50, 35, 20, 10, 10)
            pygame.mixer.music.load("C:\Python27\data\kapari.mp3")
            pygame.mixer.music.play()
            time.sleep(3)
            heroe.pelea(enemigo)
            if heroe.hp<=0:
                pygame.mixer.music.load("C:\Python27\data\over.mp3")
                pygame.mixer.music.play()
                time.sleep(5)
                sys.exit()
            pygame.mixer.music.load("C:\Python27\data\poses.mp3")
            pygame.mixer.music.play()
            raw_input("Press enter to skip or to continue...")
            pygame.mixer.music.stop()
            
            
        else:
            pygame.mixer.music.load("C:\Python27\data\oturn.mp3")
            pygame.mixer.music.play()
            raw_input("Press enter to skip or to continue...")
            pygame.mixer.music.stop()
                
    elif select==1:
        print "la otra ruta"
                        
                        
                
                 
elif select==2:
    pygame.mixer.music.load("C:\Python27\data\over.mp3")
    pygame.mixer.music.play()
    time.sleep(5)
    sys.exit()
pygame.mixer.music.load("C:\Python27\data\ero.mp3")
pygame.mixer.music.play()
time.sleep(10)
pygame.mixer.music.stop()
pygame.mixer.music.load("C:\Python27\data\introf.mp3")
pygame.mixer.music.play()
time.sleep(3)



