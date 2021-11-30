from ctypes import BigEndianStructure
import OpenGL.GL
from OpenGL.GL.glget import GLsize
import OpenGL.GLUT
import OpenGL.GLU

# program pertama
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def kotakUtama():
    glBegin(GL_QUADS)
    glColor3ub(255, 191, 0)
    glVertex2f(30,15)
    glVertex2f(367,15)
    glVertex2f(367,374)
    glVertex2f(30,374)
    glEnd()

def gambar1():
    glBegin(GL_QUADS)
    glColor3ub(0, 128, 255)
    glVertex2f(60,350)
    glVertex2f(100,350)
    glVertex2f(100,324)
    glVertex2f(60,324)
    glEnd()

def gambar2():
    glBegin(GL_QUADS)
    glColor3ub(0, 128, 255)
    glVertex2f(120,324)
    glVertex2f(168,324)
    glVertex2f(168,350)
    glVertex2f(120,350)
    glEnd()

def gambar3():
    glBegin(GL_POLYGON)
    glColor3ub(0, 128, 255)
    glVertex2f(191, 374)
    glVertex2f(191,324)
    glVertex2f(206,324)
    glVertex2f(206, 374)
    glEnd()

def gambar4():
    glBegin(GL_QUADS)
    glColor3ub(0, 128, 255)
    glVertex2f(230,350)
    glVertex2f(279,350)
    glVertex2f(279,324)
    glVertex2f(230,324)
    glEnd()

def gambar5():
    glBegin(GL_QUADS)
    glColor3ub(0, 128, 255)
    glVertex2f(300,350)
    glVertex2f(340,350)
    glVertex2f(340,324)
    glVertex2f(300,324)
    glEnd()

def gambar6():
    glBegin(GL_QUADS)
    glColor3ub(0, 128, 255)
    glVertex2f(60,303)
    glVertex2f(100,303)
    glVertex2f(100,289)
    glVertex2f(60,289)
    glEnd()

def gambar7():
    glBegin(GL_POLYGON)
    glColor3ub(0, 128, 255)
    glVertex2f(120, 220)
    glVertex2f(134, 220)
    glVertex2f(134, 303)
    glVertex2f(120, 303)
    glEnd()

def gambar8():
    glBegin(GL_POLYGON)
    glVertex2f(157, 288)
    glVertex2f(242, 288)
    glVertex2f(242, 303)
    glVertex2f(157, 303)
    glEnd()

def gambar9():
    glBegin(GL_POLYGON)
    glVertex2f(265, 220)
    glVertex2f(279, 220)
    glVertex2f(279, 303)
    glVertex2f(265, 303)
    glEnd()

def gambar10():
    glBegin(GL_QUADS)
    glVertex2f(300,303)
    glVertex2f(340,303)
    glVertex2f(340,289)
    glVertex2f(300,289)
    glEnd()

def gambar11():
    glBegin(GL_QUADS)
    glVertex2f(30,267)
    glVertex2f(100,267)
    glVertex2f(100,220)
    glVertex2f(30, 220)
    glEnd()

def gambar12():
    glBegin(GL_QUADS)
    glVertex2f(30, 196)
    glVertex2f(100,196)
    glVertex2f(100,147)
    glVertex2f(30, 147)
    glEnd()

def gambar13():
    glBegin(GL_QUADS)
    glVertex2f(120,196)
    glVertex2f(135,196)
    glVertex2f(135,147)
    glVertex2f(120,147)
    glEnd()

def gambar14():
    glBegin(GL_POLYGON)
    glVertex2f(156,267)
    glVertex2f(167,267)
    glVertex2f(167,181)
    glVertex2f(156,181.)
    glEnd()

def gambar15():
    glBegin(GL_POLYGON)
    glVertex2f(231,267)
    glVertex2f(242,267)
    glVertex2f(242,181)
    glVertex2f(231,181)
    glEnd()

# def gambar16():
#     glBegin(GL_QUADS)
#     glVertex2f(156,183)
#     glVertex2f(156,191)
#     glVertex2f(234,191)
#     glVertex2f(242,183)
#     glEnd()

def gambar17():
    glBegin(GL_QUADS)
    glVertex2f(265,196)
    glVertex2f(279,196)
    glVertex2f(279,147)
    glVertex2f(265,147)
    glEnd()

def gambar18():
    glBegin(GL_QUADS)
    glVertex2f(300,267)
    glVertex2f(367,267)
    glVertex2f(367,220)
    glVertex2f(300,220)
    glEnd()

def gambar19():
    glBegin(GL_QUADS)
    glVertex2f(300,196)
    glVertex2f(367,196)
    glVertex2f(367,147)
    glVertex2f(300,147)
    glEnd()

def gambar20():
    glBegin(GL_QUADS)
    glVertex2f(30,91)
    glVertex2f(63,91)
    glVertex2f(63,75)
    glVertex2f(30,75)
    glEnd()

def gambar21():
    glBegin(GL_POLYGON)
    glVertex2f(85,127)
    glVertex2f(100,127)
    glVertex2f(100,75)
    glVertex2f(85,75)
    glEnd()

def gambar22():
    glBegin(GL_QUADS)
    glVertex2f(120,127)
    glVertex2f(170,127)
    glVertex2f(170,110)
    glVertex2f(120,110)
    glEnd()

def gambar23():
    glBegin(GL_POLYGON)
    glVertex2f(156,163)
    glVertex2f(241,163)
    glVertex2f(241,147)
    glVertex2f(156,147)
    glEnd()

def gambar24():
    glBegin(GL_QUADS)
    glVertex2f(227,127)
    glVertex2f(279,127)
    glVertex2f(279,110)
    glVertex2f(227,110)
    glEnd()

def gambar25():
    glBegin(GL_POLYGON)
    glVertex2f(300,127)
    glVertex2f(315,127)
    glVertex2f(315,75)
    glVertex2f(300,75)
    glEnd()

def gambar26():
    glBegin(GL_POLYGON)
    glVertex2f(60,55)
    glVertex2f(169,55)
    glVertex2f(169,40)
    glVertex2f(60,40)
    glEnd()

def gambar27():
    glBegin(GL_POLYGON)
    glVertex2f(155,90)
    glVertex2f(242,90)
    glVertex2f(242,75)
    glVertex2f(155,75)
    glEnd()

def gambar28():
    glBegin(GL_POLYGON)
    glVertex2f(229,55)
    glVertex2f(340,55)
    glVertex2f(340,40)
    glVertex2f(229,40)
    glEnd()

def gambar29():
    glBegin(GL_QUADS)
    glVertex2f(337,91)
    glVertex2f(367,91)
    glVertex2f(367,75)
    glVertex2f(337,75)
    glEnd()
