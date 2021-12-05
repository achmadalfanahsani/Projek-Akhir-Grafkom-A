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

'''
colosion X1 = 280
colosion X2 = 297
colosion Y1 = 170
colosion Y2 = 187
'''
def lawan2(deltaX, deltaY):
    glPushMatrix()
    glTranslate(deltaX, deltaY)
    glBegin(GL_QUADS)
    glVertex2f(280, 170)
    glVertex2f(297, 170)
    glVertex2f(297, 187)
    glVertex2f(280, 187)
    glEnd()
    glPopMatrix()
    glEnd()

'''
colosion X1 = 228
colosion X2 = 245
colosion Y1 = 57
colosion Y2 = 74
'''
def lawan3(deltaX, deltaY):
    glPushMatrix()
    glTranslate(deltaX, deltaY)
    glBegin(GL_QUADS)
    glVertex2f(228, 57)
    glVertex2f(245, 57)
    glVertex2f(245, 74)
    glVertex2f(228, 74)
    glEnd()
    glPopMatrix()
    glEnd()

'''
colosion X1 = 261
colosion X2 = 278
colosion Y1 = 306
colosion Y2 = 323
'''
def lawan4(deltaX, deltaY):
    glPushMatrix()
    glTranslate(deltaX, deltaY)
    glBegin(GL_QUADS)
    glVertex2f(261, 306)
    glVertex2f(278, 306)
    glVertex2f(278, 323)
    glVertex2f(261, 323)
    glEnd()
    glPopMatrix()
    glEnd()

'''
colosion X1 = 245
colosion X2 = 262
colosion Y1 = 252
colosion Y2 = 269
'''
def lawan5(deltaX, deltaY):
    glPushMatrix()
    glTranslate(deltaX, deltaY)
    glBegin(GL_QUADS)
    glVertex2f(245, 252)
    glVertex2f(262, 252)
    glVertex2f(262, 269)
    glVertex2f(245, 269)
    glEnd()
    glPopMatrix()
    glEnd()

'''
colosion X1 = 137
colosion X2 = 154
colosion Y1 = 243
colosion Y2 = 260
'''
def lawan6(deltaX, deltaY):
    glPushMatrix()
    glTranslate(deltaX, deltaY)
    glBegin(GL_QUADS)
    glVertex2f(137, 243)
    glVertex2f(154, 243)
    glVertex2f(154, 260)
    glVertex2f(137, 260)
    glEnd()
    glPopMatrix()
    glEnd()
