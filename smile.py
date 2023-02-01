import pygame
import sys,time,os
from pygame.draw import *

pygame.init() # После импорта библиотеки, необходимо её инициализировать:
#Цвета
YELLOW = (225, 225, 0)
BLACK = (0,0,0)
RED =(255, 0 ,0)
GREY = (128,128,128)

FPS = 30
screen = pygame.display.set_mode((600, 600))  # создать экран 
rect(screen,GREY,(0,0,600,600)) #фон
circle(screen, YELLOW, (300, 300),(150),) # Лицо смайла
circle(screen,BLACK,(300,300),(150),(1)) # вокруг черная линия

circle(screen,RED, (240,250),(30)) #left eye``
circle(screen,BLACK,(240,250),(30),(1))# black boardar
circle(screen,BLACK,(240,250),(15)) #pupil

circle(screen,RED, (360,250),(19)) # right eye
circle(screen,BLACK,(360,250),(19),(1)) #black boarder
circle(screen,BLACK,(360,250),(9)) #pupil

rect(screen,BLACK,(230,370,130,15)) #mouth

line(screen,BLACK,(260,220),(211,187),(10)) #brow left
line(screen,BLACK,(340,230),(380,200),(10))  #brow right
pygame.display.update()   # после чего, чтобы они отобразились на экране, экран нужно обновить:
clock = pygame.time.Clock() # фпс
finished = False

while not finished: 
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:   # это цикл показывает координаты 
            x, y = event.pos
            print(x,y)
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()


 
