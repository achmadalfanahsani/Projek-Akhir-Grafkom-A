from ctypes import BigEndianStructure
import OpenGL.GL
from OpenGL.GL.glget import GLsize
import OpenGL.GLUT
import OpenGL.GLU

# program pertama
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *



# fungsi iterasi program
def iterate():
    # ke kanan, atas, kiri, bawah
    glViewport(-50, -20, 700, 655)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 400, 0, 400, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def kotakUtama():
    glBegin(GL_QUADS)
    glColor3ub(255, 191, 0)
    glVertex2f(30.15129,15.06681)
    glVertex2f(367.61788,15.05619)
    glVertex2f(367.5514,374.24973)
    glVertex2f(30.05158,374.26566)
    glEnd()

def gambar1():
    glBegin(GL_QUADS)
    glColor3ub(0, 128, 255)
    glVertex2f(60,350)
    glVertex2f(100,350)
    glVertex2f(100,326)
    glVertex2f(60,326)
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
    glVertex2f(191, 375)
    glVertex2f(191,331)
    glVertex2f(198,325)
    glVertex2f(206,331)
    glVertex2f(206, 375)
    glEnd()

def gambar4():
    glBegin(GL_QUADS)
    glColor3ub(0, 128, 255)
    glVertex2f(230,349)
    glVertex2f(279,349)
    glVertex2f(279,325)
    glVertex2f(230,325)
    glEnd()

def gambar5():
    glBegin(GL_QUADS)
    glColor3ub(0, 128, 255)
    glVertex2f(300,349)
    glVertex2f(340,349)
    glVertex2f(340,325)
    glVertex2f(300,325)
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
    glVertex2f(134,267)
    glVertex2f(167,267)
    glVertex2f(167,252)
    glVertex2f(134,252)
    glVertex2f(134,220)
    glVertex2f(120,220)
    glVertex2f(120,303)
    glVertex2f(134,303)
    glEnd()

def gambar8():
    glBegin(GL_POLYGON)
    glVertex2f(193,287)
    glVertex2f(157,287)
    glVertex2f(157,303)
    glVertex2f(242,303)
    glVertex2f(242,288)
    glVertex2f(207,288)
    glVertex2f(207,253)
    glVertex2f(193,253)
    glEnd()

def gambar9():
    glBegin(GL_POLYGON)
    glVertex2f(265,266)
    glVertex2f(265,303)
    glVertex2f(279,303)
    glVertex2f(279,220)
    glVertex2f(265,220)
    glVertex2f(265,252)
    glVertex2f(228,252)
    glVertex2f(228,266)
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
    glVertex2f(156,232)
    glVertex2f(185,232)
    glVertex2f(185,223)
    glVertex2f(164,223)
    glVertex2f(164,190)
    glVertex2f(156,183)
    glEnd()

def gambar15():
    glBegin(GL_POLYGON)
    glVertex2f(234,223)
    glVertex2f(216,223)
    glVertex2f(216,232)
    glVertex2f(242,232)
    glVertex2f(242,183)
    glVertex2f(234,191)
    glEnd()

def gambar16():
    glBegin(GL_QUADS)
    glVertex2f(156,183)
    glVertex2f(156,191)
    glVertex2f(234,191)
    glVertex2f(242,183)
    glEnd()

def gambar17():
    glBegin(GL_QUADS)
    glVertex2f(264,196)
    glVertex2f(279,196)
    glVertex2f(279,147)
    glVertex2f(264,147)
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
    glVertex2f(100,125)
    glVertex2f(100,75)
    glVertex2f(85,75)
    glVertex2f(85,110)
    glVertex2f(61,110)
    glVertex2f(61,125)
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
    glVertex2f(206,147)
    glVertex2f(206,110)
    glVertex2f(191,110)
    glVertex2f(191,147)
    glVertex2f(156,147)
    glVertex2f(156,163)
    glVertex2f(241,163)
    glVertex2f(241,147)
    glEnd()

def gambar24():
    glBegin(GL_QUADS)
    glVertex2f(227,125)
    glVertex2f(279,125)
    glVertex2f(279,110)
    glVertex2f(227,110)
    glEnd()

def gambar25():
    glBegin(GL_POLYGON)
    glVertex2f(300,126)
    glVertex2f(340,126)
    glVertex2f(340,111)
    glVertex2f(315,111)
    glVertex2f(315,75)
    glVertex2f(300,75)
    glEnd()

def gambar26():
    glBegin(GL_POLYGON)
    glVertex2f(120,55)
    glVertex2f(120,88)
    glVertex2f(134,88)
    glVertex2f(134,55)
    glVertex2f(169,55)
    glVertex2f(169,40)
    glVertex2f(60,40)
    glVertex2f(60,55)
    glEnd()

def gambar27():
    glBegin(GL_POLYGON)
    glVertex2f(207,75)
    glVertex2f(207,40)
    glVertex2f(192,40)
    glVertex2f(192,75)
    glVertex2f(155,75)
    glVertex2f(155,90)
    glVertex2f(242,90)
    glVertex2f(242,75)
    glEnd()

def gambar28():
    glBegin(GL_POLYGON)
    glVertex2f(264,55)
    glVertex2f(264,88)
    glVertex2f(279,88)
    glVertex2f(279,55)
    glVertex2f(340,55)
    glVertex2f(340,40)
    glVertex2f(229,40)
    glVertex2f(229,55)
    glEnd()

def gambar29():
    glBegin(GL_QUADS)
    glVertex2f(337,91)
    glVertex2f(367,91)
    glVertex2f(367,75)
    glVertex2f(337,75)
    glEnd()

# variabel gerak karakter
deltaX = 0
boolGerakX = False

deltaY = 0
boolGerakY = False

def control_karakter(key, x, y):
    global boolGerakX
    global boolGerakY
    if key == GLUT_KEY_UP:
        boolGerakY = 'atas'
        boolGerakX = False
    if key == GLUT_KEY_DOWN:
        boolGerakY = 'bawah'
        boolGerakX = False
    if key == GLUT_KEY_RIGHT:
        boolGerakX  = 'kanan'
        boolGerakY = False
    if key == GLUT_KEY_LEFT:
        boolGerakX  = 'kiri'
        boolGerakY = False


def timer_karakter(value1): #fungsi timer
    global deltaX
    global deltaY
    if boolGerakY == 'atas':
        deltaY += 0.5
    if boolGerakY == 'bawah':
        deltaY -= 0.5
    if boolGerakX == 'kiri':
        deltaX -= 0.5
    if boolGerakX == 'kanan':
        deltaX += 0.5
    
    glutTimerFunc(1000//30, timer_karakter, 0) 


def update(value):
    glutPostRedisplay()
    glutTimerFunc(10, update, 0)

def kotak():
    glPushMatrix()
    # global pos_x, pos_y
    glTranslate(deltaX, deltaY, 0)
    glBegin(GL_QUADS)
    glColor3ub(255, 77, 77)
    glVertex2f(189.0756,216.07001)
    glVertex2f(206.05254,216.0687)
    glVertex2f(206.03535,199.06961)
    glVertex2f(189.01729,199.0048)
    glEnd()
    glPopMatrix()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # untuk membersihkan layar
    glLoadIdentity() # untuk mereset semua posisi grafik/bentuk
    iterate() # fungsi looping
    glColor3f(1.0, 0.0, 0.0) # untuk mewarnai objek

    # Pemanggilan fungsi
    kotakUtama()
    #baris 1
    gambar1()
    gambar2()
    gambar3()
    gambar4()
    gambar5()
    gambar6()
    gambar7()
    gambar8()
    gambar9()
    gambar10()
    gambar11()
    gambar12()
    gambar13()
    gambar14()
    gambar15()
    gambar16()
    gambar17()
    gambar18()
    gambar19()
    gambar20()
    gambar21()
    gambar22()
    gambar23()
    gambar24()
    gambar25()
    gambar26()
    gambar27()
    gambar28()
    gambar29()

    kotak()

    glFlush()
    glutSwapBuffers()

# inisialisasi
glutInit(sys.argv)  # inisialisasi glut
glutInitDisplayMode(GLUT_RGBA) # mengatur layar supaya berwarna
glutInitWindowSize(600, 600) # mengatur ukuran layar/window
glutInitWindowPosition(750, 0) # mangatur posisi window
wind = glutCreateWindow("Snake Man") # untuk memberi nama window
glutDisplayFunc(showScreen) # untuk menampilkan objek pada layar
glutIdleFunc(showScreen) # untuk menuruh opengl untuk selalu menampilkan dan membuka objek
glutSpecialFunc(control_karakter)
glutTimerFunc(50, update, 0)
glutTimerFunc(0, timer_karakter, 0)
glutMainLoop() #untuk memulai segalanya

