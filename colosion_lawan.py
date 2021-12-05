from ctypes import BigEndianStructure
import OpenGL.GL
from OpenGL.GL.glget import GLsize
import OpenGL.GLUT
import OpenGL.GLU

# program pertama
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

'''
olosion X1 = 102
colosion X2 = 119
colosion Y1 = 229
colosion Y2 = 246
'''
def lawan1(deltaX, deltaY):
    glPushMatrix()
    glTranslate(deltaX, deltaY)
    glBegin(GL_QUADS)
    glVertex2f(102, 229)
    glVertex2f(119, 229)
    glVertex2f(119, 246)
    glVertex2f(102, 246)
    glEnd()
    glPopMatrix()
    glEnd()