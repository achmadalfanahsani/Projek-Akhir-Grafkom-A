from ctypes import BigEndianStructure
from sys import flags
import OpenGL.GL
from OpenGL.GL.glget import GLsize
import OpenGL.GLUT
import OpenGL.GLU
import math

# program pertama
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def gp_1():
    posx, posy = 0,0    
    sides = 40
    radius = 8.8   
    glPushMatrix()
    glTranslated(44.5,357.5,0) 
    glColor3ub(0, 255, 255)
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()

def gp_2():
    posx, posy = 0,0    
    sides = 40
    radius = 8.8   
    glPushMatrix()
    glTranslated(44.5,32.5,0) 
    glColor3ub(0, 255, 255)    
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()

def gp_3():
    posx, posy = 0,0    
    sides = 40
    radius = 8.8   
    glPushMatrix()
    glTranslated(197.5,207.5,0) 
    glColor3ub(0, 255, 255)
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()

def gp_4():
    posx, posy = 0,0    
    sides = 40
    radius = 8.8   
    glPushMatrix()
    glTranslated(202.5,173.5,0) 
    glColor3ub(0, 255, 255)
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()

def gp_5():
    posx, posy = 0,0    
    sides = 40
    radius = 8.8   
    glPushMatrix()
    glTranslated(180.5,114.5,0) 
    glColor3ub(0, 255, 255)
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()

def gp_6():
    posx, posy = 0,0    
    sides = 40
    radius = 8.8   
    glPushMatrix()
    glTranslated(290.5,207.5,0) 
    glColor3ub(0, 255, 255)
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()

def gp_7():
    posx, posy = 0,0    
    sides = 40
    radius = 8.8   
    glPushMatrix()
    glTranslated(145.5,313.5,0) 
    glColor3ub(0, 255, 255)
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()

def gp_8():
    posx, posy = 0,0    
    sides = 40
    radius = 8.8   
    glPushMatrix()
    glTranslated(254.5,64.5,0) 
    glColor3ub(0, 255, 255)
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()

def gp_9():
    posx, posy = 0,0    
    sides = 40
    radius = 8.8   
    glPushMatrix()
    glTranslated(351.5,30,0) 
    glColor3ub(0, 255, 255)
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()

def gp_10():
    posx, posy = 0,0    
    sides = 40
    radius = 8.8   
    glPushMatrix()
    glTranslated(328.5,278.5,0) 
    glColor3ub(0, 255, 255)
    glBegin(GL_POLYGON)    
    for i in range(100):    
        cosine= radius * math.cos(i*2* math.pi/sides) + posx    
        sine  = radius * math.sin(i*2* math.pi/sides) + posy    
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()





