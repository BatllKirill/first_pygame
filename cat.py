import pygame
import sys,time,os
from pygame.draw import *

pygame.init() # После импорта библиотеки, необходимо её инициализировать:
#Цвета
YELLOW = (225, 225, 0);      BLACK = (0,0,0);           GREEN=(0, 128, 0)
RED =(255, 0 ,0);            GREY = (128,128,128);      BROWNCAT=(210, 105, 30)
BROWN =(139, 69, 19);        BLUE=(0, 191, 255);        WHITE = (255,255,255)
BROWNGOLDEN=(218, 165, 32);  BLUEAQUA=(135, 206, 235)




FPS = 30
screen = pygame.display.set_mode((600, 900))  # создать экран 



def background ():
    rect(screen,BROWN,[(0,0),(600,450)])
    rect(screen,BROWNGOLDEN,[(0,450),(600,900)])
    
def window(move):
    polygon(screen,BLUE,[(373,36),(560,36),(560,400),(373,400)]) #big xy xy xy xy
    x=390+move; y=50; width=60; heigt=60
    rect(screen,BLUEAQUA,[(x,y),(width,heigt)]) #small window 
    x=390+move; y=150; width=60; heigt=60
    rect(screen,BLUEAQUA,[(x,y),(width,heigt)]) #small window 
    x=390+move; y=250; width=60; heigt=130
    rect(screen,BLUEAQUA,[(x,y),(width,heigt)]) #semi smal
    
    x=480+move; y=50; width=60; heigt=60
    rect(screen,BLUEAQUA,[(x,y),(width,heigt)]) #small window 
    x=480+move; y=150; width=60; heigt=60
    rect(screen,BLUEAQUA,[(x,y),(width,heigt)])#small window 
    x=480+move; y=250; width=60; heigt=130
    rect(screen,BLUEAQUA,[(x,y),(width,heigt)]) #semi smal
    
def cat_body ():

    
    ellipse1 = pygame.Surface((100, 50)) # crate surface tail
    ellipse1.fill((BROWNGOLDEN)) # fill surafce  
    ellipse(ellipse1, (BROWNCAT), (0, 0, 100, 50)) #create elise on surface
    ellipse(ellipse1, (BLACK), (0, 0, 100, 50),1) #create boarder elise on surface
    ellipse1 = pygame.transform.rotate(ellipse1, 45) #rotate surface
    screen.blit(ellipse1, (404, 540)) #move surface
    

      
    x=129; y=589; heigt=302; width=82; 
    ellipse(screen, BLACK,(x,y,heigt,width,)) #body boarder
    x=130; y=590; heigt=300; width=80; 
    ellipse(screen, BROWNCAT,(x,y,heigt,width)) #body

    x=380; y=680; radius=40; widht=0
    circle(screen,BROWNCAT,(x,y),radius,widht) #leg_right_1
    x=380; y=680; radius=40; widht=1
    circle(screen,BLACK,(x,y),radius,widht) #boarder leg_rigt_1
    
    x=379; y=699; heigt=32; width=71; boarder=1 
    ellipse(screen, BLACK,(x,y,heigt,width,),boarder) #leg_rigght_1_1 boarder
    x=380; y=700; heigt=30; width=70; 
    ellipse(screen, BROWNCAT,(x,y,heigt,width),0) #leg_right1_1
    
    x=180; y=660; heigt=71; width=31; boarder=4 
    ellipse(screen, BLACK,(x,y,heigt,width,),boarder) #left_hand_boarder
    x=180; y=661; heigt=70; width=30; 
    ellipse(screen, BROWNCAT,(x,y,heigt,width),0) #left_hand
    
    x=103; y=625; heigt=31; width=41; boarder=3
    ellipse(screen, BLACK,(x,y,heigt,width,),boarder) #right_hand
    x=103; y=625; heigt=30; width=40; 
    ellipse(screen, BROWNCAT,(x,y,heigt,width),0) 
    
    
    x=105; y=600; radius=50; widht=0
    circle(screen,BROWNCAT,(x,y),radius,widht) #head
    x=105; y=600; radius=50; widht=1
    circle(screen,BLACK,(x,y),radius,widht) #head
    
def ball():
    circle
background()
window(1)

cat_body ()
    
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

