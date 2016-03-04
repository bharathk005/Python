import pygame
import time
import random

pygame.init()

c_s=pygame.mixer.Sound("Crash.wav")
pygame.mixer.music.load("Burnt.wav")

width= 500  
height = 600

black=(0,0,0)
white=(255,255,255)
red = (255, 0, 0)
red_light=(200,0,0)
green=(0,255,0)
green_light=(0,200,0)
blue= (0,50,200)
home= (25,50,75)
textcol= (25,150,150)
thingcol=(75,20,20)
yellow=(230,220,38)
road=(70,70,70)


cw = 123
ch = 145

gDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('race it')
clock = pygame.time.Clock()



carImg= pygame.image.load('car1.png')

def score(count):
    font = pygame.font.SysFont("comicsansms", 40)
    text = font.render("Score:"+ str(count),True,yellow)
    gDisplay.blit(text, (0,0))
def car(x,y):
    gDisplay.blit(carImg,(x,y))

def button(msg,x,y,w,h,c,c_l,action1 = None):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h> mouse[1]>y:
       pygame.draw.rect(gDisplay,c,(x,y,w,h))
       if click[0]==1 and action1=="play":
           gameloop()
       if click[0]==1 and action1 =="quit":
           pygame.quit()
           quit()
        
    else:
        pygame.draw.rect(gDisplay, c_l , (x,y,w,h))
        

    smallText=pygame.font.SysFont("comicsansms",20)
    textSurf,textRect=text_objects(msg,smallText,black)
    textRect.center = ((x+(w/2)),(y+(h/2)))
    gDisplay.blit(textSurf,textRect)

   

def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gDisplay, color, [thingx,thingy,thingw,thingh])

def text_objects(text, font,tcolor):
    textSurface = font.render(text, True, tcolor)
    return textSurface , textSurface.get_rect()

def start_screen():

    start= True
    while start:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            
            largeText=pygame.font.SysFont('comicsansms',50)

            TextSurf, TextRect = text_objects("RAceY..", largeText,textcol)
            TextRect.center = ((width/2),(height/3))
            
            TextSurf1, TextRect1 = text_objects("by BK graphiX", largeText,textcol)
            TextRect1.center = ((width/2),(height/2))

            gDisplay.blit(TextSurf,TextRect)
            gDisplay.blit(TextSurf1,TextRect1)
            
            button("Risk it",50,450,100,50,green,green_light,"play")
            button("Go Home",300,450,100,50,red,red_light,"quit")
           
            
            pygame.display.update()
            clock.tick(15)

def message_display(text):
    largeText=pygame.font.SysFont('comicsansms',50)
    TextSurf, TextRect = text_objects(text, largeText,red)
    TextRect.center = ((width/2),(height/2))
    gDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    gameloop()

def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(c_s)
    message_display('You crashed..')
   


    
def gameloop():
        pygame.mixer.music.play(1)
        dodge = 0
        x= (width * 0.35)
        y= (height*0.65)

        delx= 0

        tx=random.randrange(0,width)
        ty=-600
        thing_speed=6
        thing_width=100
        thing_height=15
    
        tx1=width/2
        ty1=0
        thing_speed1=4
        thing_width1=10
        thing_height1=height/3

        gexit = False
        while not gexit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        delx = -5
                    elif event.key == pygame.K_RIGHT:
                        delx= 5 
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        delx=0

            x+=delx
                        
            
            gDisplay.fill(road)
            #pygame.draw.line(gDisplay,yellow,(width/2,0),(width/2,height),8)
           # things(tx1,ty1,thing_width1,thing_height1,white)
            
            ty+=thing_speed
            ty1+=thing_speed1
            if ty1>=0 and ty1<thing_height1:
                things(tx1,ty1+thing_height1,thing_width1,thing_height1,white)
                things(tx1,ty1-thing_height1,thing_width1,thing_height1,white)
            if ty1>=thing_height1 and ty1<2*thing_height1:
                things(tx1,ty1-(thing_height1),thing_width1,thing_height1,white)
                things(tx1,ty1+(thing_height1),thing_width1,thing_height1,white)
            if ty1>=2*thing_height1 and ty1<height:
                things(tx1,ty1-(1*thing_height1),thing_width1,thing_height1,white)
                things(tx1,ty1-(3*thing_height1),thing_width1,thing_height1,white)
                ty1=thing_speed1
            things(tx,ty,thing_width,thing_height,thingcol)    
            if ty > height:
                ty = 0-thing_height
                tx = random.randrange(0,width)
                dodge+=1
                thing_speed+=1
           
            car(x,y)
            score(dodge)
            
            if x>(width - cw) or x<0:
                crash()
            
            if ty>y and ty<(y+ch):
                if (tx+thing_width)>(x+10) and tx <(x+cw-10):
                    crash()
            
           
            pygame.display.update()
            clock.tick(60)
gDisplay.fill(home)
start_screen()
#gDisplay.fill(white)
#start_screen('Instructions..',4)
#start_screen('avoid screen edges',3)
#start_screen('avoid blocks',2.5)
#start_screen('use arrow keys',2)
gameloop() 
pygame.quit()
quit()
