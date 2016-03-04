import random
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


colors = (
            (1,0,1),
            (0.8,1,0.5),
            (0.0,0.5,0.9),
            (0.7,0.7,0.2),
            (0.3,1,0.2),
            (0.2,0.9,0.7),
            (0.6,0.2,0.4),
            (0.5,0.2,0.9)
            
            
            )
vertices = (     (1 , 0, -1),
                 (1, 1, -1),
                 (-1, 1, -1),
                 (-1, 0 , -1),
                 (1, 0, 1),
                 (1,1,1),
                 (-1,0,1),
                 (-1,1,1)


                )

edges = (
                (0,1),
                (0,3),
                (0,4),
                (2,1),
                (2,3),
                (2,7),
                (6,3),
                (6,4),
                (6,7),
                (5,1),
                (5,4),
                (5,7),

            )

surfaces = (
                (0,1,2,3),
                (3,2,7,6),
                (6,7,5,4),
                (4,5,1,0),
                (1,5,7,2),
                (4,0,3,6),



            )

floor = (
            (50,-0.1,-100),
            (-50,-0.1,-100),
            (-50,-0.1,0),
            (50,-0.1,0)
            



        )

def newcubes(dist,dist_min = 20,camera_x = 0):
    camera_x = -1 *int(camera_x)
    
    delxc = random.randrange(camera_x - 10 , camera_x + 10)
    delyc = 0
    delzc = random.randrange((-1*dist) ,(-1*dist_min))

    new_vertices = []

    for vert in vertices:
        new_vert = []
        new_x = vert[0] + delxc
        new_y = vert[1] + delyc
        new_z = vert[2] + delzc

        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert)

    return new_vertices
        
def ground(c_z,c_x):
    n_f = []
    for n in floor:
        n_c = []
        n_z  = int(c_z) + n[2]
        n_x = n[0] - int(c_x)
        n_y = n[1]

        n_c.append(n_x)
        n_c.append(n_y)
        n_c.append(n_z)

        n_f.append(n_c)
        
        
    
        
       
    glBegin(GL_QUADS)
    for n in n_f:
        glVertex3fv(n)
        glColor3fv((1,1,1))


    glEnd()
        

def cube(vertices):
    glBegin(GL_QUADS)
    for surface in surfaces:
        for vertex in surface:
            glVertex3fv(vertices[vertex])
            glColor3fv(colors[vertex])
       
        
    glEnd()
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv((vertices[vertex]))
            glColor3fv((0,0,1))
    glEnd()

def bg(z,y,x,n):
    img = pygame.image.load('wat'+str(n)+'.png')
    textureData = pygame.image.tostring(img , "RGB" , 1)
    width = img.get_width()
    height = img.get_height()
    im = glGenTextures(1)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
    glBindTexture(GL_TEXTURE_2D , im)

    
    glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT )
    glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT ) 
    glTexParameteri(GL_TEXTURE_2D , GL_TEXTURE_MIN_FILTER ,GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER , GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D , 0 , GL_RGB , width,height , 0 ,GL_RGB, GL_UNSIGNED_BYTE , textureData)
    glEnable(GL_TEXTURE_2D)
    
    glBegin(GL_QUADS)
    glTexCoord2f(0,0)
    glVertex3f(-6-x,-5,z-10)
    glTexCoord2f(1,0)
    glVertex3f(6-x,-5,z-10)
    glTexCoord2f(1,1)
    glVertex3f(6-x,5,z-10)
    glTexCoord2f(0,1)
    glVertex3f(-6-x,5,z-10)

   # glTexCoord2f(1,1)
   # glVertex3f(-10-x,-0.1,z)
   # glTexCoord2f(0,1)
   # glVertex3f(10-x,-0.1,z)
   # glTexCoord2f(0,0)
   # glVertex3f(10-x,-0.1,z-100)
   # glTexCoord2f(1,0)
   # glVertex3f(-10-x,-0.1,z-100)


    glEnd()

    glDisable(GL_TEXTURE_2D)


def main():
    
    pygame.init()
    max_dist = 100
    delx = 0
    dely = 0
    display = (800,600)
    gDisplay =  pygame.display.set_mode(display , DOUBLEBUF|OPENGL)

    gluPerspective(45 , (display[0]/display[1]),0.1,max_dist)
    glTranslatef(0,0,-50)
  
    cur_x= 0
    cur_y = 0
    
    s =1

    
    
    cubes_dict = {} 

    for n in range(20):
        cubes_dict[n] = newcubes(max_dist)
  
    #glRotatef(45,2,0,0)
 
  
    while True:
        
        for event in pygame.event.get():
           # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    delx = 0.2
                if event.key == pygame.K_RIGHT:
                    delx = -0.2

                if event.key == pygame.K_UP:
                    dely= -0.2
          
                if event.key == pygame.K_DOWN:
                    dely=0.2

            if event.type==pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    delx = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    dely= 0

                


            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,0.5)

                if event.button == 5:
                    glTranslatef(0,0,-0.5)
                    
        #glRotatef(2,1 ,3,1)
        
        x=glGetDoublev(GL_MODELVIEW_MATRIX)
        camera_x = x[3][0]
        camera_y = x[3][1]
        camera_z = x[3][2]
        cur_x += delx
        cur_y += dely
      
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glTranslate(delx,dely,2)


        for eachCube in cubes_dict:
            if camera_z <= cubes_dict[eachCube][0][2]:
                
                new_max = int(-1*(camera_z - max_dist))
                cubes_dict[eachCube] = newcubes(new_max,int(camera_z+20),cur_x)
    
        #gDisplay.blit(img,(-10,10))    
        
        bg(camera_z,cur_y,cur_x,s)
        s = s+1
        if(s == 17):
            s = 1
        #ground(camera_z,cur_x)
        for eachCube in cubes_dict:
            cube(cubes_dict[eachCube])

       
        
                
        
        pygame.display.flip()
        #pygame.time.wait(15)

main()
pygame.quit()
quit()

    
