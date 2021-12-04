from sys import float_repr_style
import OpenGL.GL
from OpenGL.GL.glget import GLsize
import OpenGL.GLUT
import OpenGL.GLU

# program pertama
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from maze import *
from colosion_point import *
from colosion_lawan import *


# fungsi iterasi program
def iterate():
    # ke kanan, atas, kiri, bawah
    glViewport(-50, -20, 700, 655)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 400, 0, 400, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


# koordinat x dan y untuk posisi kotak utama
deltaX = 0
boolGerakX = False

deltaY = 0
boolGerakY = False
boolgerakHorizontal=False
recordK1 = [False,]
aksiColosion  = [False, True]
colosionX1 = 195
colosionX2 = 205
colosionY1 = 200
colosionY2 = 210
gerakKotakX = 1
gerakKotakY = 1

# karakter lain ?? coming soon

# lawan 1
dy_lw1 = 0
bg_lw1_y = False
g_lw1 = 1
cl_lw1_y1 = 229
cl_lw1_y2 = 246
cl_lw1_x1 = 102
cl_lw1_x2 = 119


def keyboard_coba(key, x, y):
    global boolGerakX
    global boolGerakY
    global boolgerakHorizontal
    global recordK1
    global aksiColosion

    recordK1.pop()
    
    
    if key == GLUT_KEY_UP:
        if aksiColosion[0]!='atas':
            boolgerakHorizontal=False
            boolGerakY = True
        else:
            boolgerakHorizontal = None
            boolGerakY = False
        recordK1.append('atas')
        aksiColosion.clear()
        aksiColosion.append('a')
    elif  key == GLUT_KEY_DOWN:
        if aksiColosion[0] != 'bawah':
            boolgerakHorizontal=False
            boolGerakY = False
        else:
            boolgerakHorizontal = None
            boolGerakX = None
        recordK1.append('bawah')
        aksiColosion.clear()
        aksiColosion.append('b')
        
    elif key == GLUT_KEY_RIGHT:
        if aksiColosion[0] != 'kanan':
            boolgerakHorizontal=True
            boolGerakX = True
        else:
            boolgerakHorizontal = None
            boolGerakX = None
        recordK1.append('kanan')
        aksiColosion.clear()
        aksiColosion.append('ka')
       
    elif key==GLUT_KEY_LEFT:
        if aksiColosion[0] != 'kiri':
            boolgerakHorizontal=True
            boolGerakX = False
        else:
            boolgerakHorizontal = None
            boolGerakX = None
        recordK1.append('kiri')
        aksiColosion.clear()
        aksiColosion.append('ka')
       





def timer1(value1): #fungsi timer
    global deltaX
    global deltaY
    global colosionY1
    global colosionY2
    global colosionX1
    global colosionX2
    global boolGerakX
    global boolGerakY
    global gerakKotakX
    global gerakKotakY
    global recordK1
    global boolgerakHorizontal
    global aksiColosion

    #lawan1
    global bg_lw1_y
    global dy_lw1
    global g_lw1
    global cl_lw1_y1
    global cl_lw1_y2
    global cl_lw1_x1
    global cl_lw1_x2
    
    # print(aksiColosion)
    
    if len(aksiColosion)==2:
        aksiColosion.pop(0)
    glutTimerFunc(1000//30, timer1, 0) 
    # kotak
    if aksiColosion[0] == 'kanan':
        deltaX += 0
        colosionX1 += 0
        colosionX2 += 0    

    elif aksiColosion[0] == 'kiri':
        deltaX -= 0
        colosionX1 -= 0
        colosionX2 -= 0

    elif aksiColosion[0] == 'atas':
        deltaY += 0
        colosionY2 += 0
        colosionY1 += 0

    elif aksiColosion[0] == 'bawah':
        deltaY -= 0
        colosionY2 -= 0
        colosionY1 -= 0
        
    elif boolGerakY == True and colosionY2<374 and boolgerakHorizontal==False :
        deltaY += gerakKotakY
        colosionY2 += gerakKotakY
        colosionY1 += gerakKotakY

    elif boolGerakY == False and colosionY1>15 and boolgerakHorizontal==False:
        deltaY -= gerakKotakY
        colosionY2 -= gerakKotakY
        colosionY1 -= gerakKotakY

    elif boolGerakX == False and  colosionX1>30 and boolgerakHorizontal==True :
        deltaX -= gerakKotakX
        colosionX1 -= gerakKotakX
        colosionX2 -= gerakKotakX
        
    elif boolGerakX == True and colosionX2<367 and boolgerakHorizontal==True:
        deltaX += gerakKotakX
        colosionX1 += gerakKotakX
        colosionX2 += gerakKotakX
    # print('colosion X1 =', colosionX1)
    # print('colosion X2 =', colosionX2)
    # print('colosion Y1 =', colosionY1)
    # print('colosion Y2 =', colosionY2)
    # print()
    



    if (recordK1[0] == 'kiri') or (recordK1[0] == 'kanan'):
        # gambar 1
        # nabrak ke kiri
        if ((324<=colosionY1<=350 or 324<=colosionY2<=350) and 60<=colosionX1<=100):
            aksiColosion.append('kiri')
        # nabrak ke kanan
        elif ((324<=colosionY1<=350 or 324<=colosionY2<=350) and 60<=colosionX2<=100):
            aksiColosion.append('kanan')
        # gambar 2
        elif ((324<=colosionY1<=350 or 324<=colosionY2<=350) and 120<=colosionX1<=168):
            aksiColosion.append('kiri')
        elif((324<=colosionY1<=350 or 324<=colosionY2<=350) and 120<=colosionX2<=168):
            aksiColosion.append('kanan')        
        # gambar 3
        elif ((324<=colosionY1<=374 or 324<=colosionY2<=374) and 191<=colosionX1<=206):
            aksiColosion.append('kiri')        
        elif((324<=colosionY1<=374 or 324<=colosionY2<=374) and 191<=colosionX2<=206):
            aksiColosion.append('kanan')       
        # gambar 4
        elif ((324<=colosionY1<=350 or 324<=colosionY2<=350) and 230<=colosionX1<=279):
            aksiColosion.append('kiri')       
        elif((324<=colosionY1<=350 or 324<=colosionY2<=350) and 230<=colosionX2<=279):
            aksiColosion.append('kanan')       
        # gambar 5
        elif ((324<=colosionY1<=350 or 324<=colosionY2<=350) and 300<=colosionX1<=340):
            aksiColosion.append('kiri')        
        elif((324<=colosionY1<=350 or 324<=colosionY2<=350) and 300<=colosionX2<=340):
            aksiColosion.append('kanan')        
        # gambar 6
        elif ((289<=colosionY1<=303 or 289<=colosionY2<=303) and 60<=colosionX1<=100):
            aksiColosion.append('kiri')       
        elif((289<=colosionY1<=303 or 289<=colosionY2<=303) and 60<=colosionX2<=100):
            aksiColosion.append('kanan')      
        # gambar 7
        elif ((220<=colosionY1<=303 or 220<=colosionY2<=303) and 120<=colosionX1<=134):
            aksiColosion.append('kiri')       
        elif ((220<=colosionY1<=303 or 220<=colosionY2<=303) and 120<=colosionX2<=134):
            aksiColosion.append('kanan')        
        # gambar 8
        elif ((288<=colosionY1<=303 or 288<=colosionY2<=303) and 157<=colosionX1<=242):
            aksiColosion.append('kiri')       
        elif ((288<=colosionY1<=303 or 288<=colosionY2<=303) and 157<=colosionX2<=242):
            aksiColosion.append('kanan')       
        # gambar 9
        elif ((220<=colosionY1<=303 or 220<=colosionY2<=303) and 265<=colosionX1<=279):
            aksiColosion.append('kiri')       
        elif ((220<=colosionY1<=303 or 220<=colosionY2<=303) and 265<=colosionX2<=279):
            aksiColosion.append('kanan')      
        # gambar 10
        elif ((289<=colosionY1<=303 or 289<=colosionY2<=303) and 300<=colosionX1<=340):
            aksiColosion.append('kiri')       
        elif ((289<=colosionY1<=303 or 289<=colosionY2<=303) and 300<=colosionX2<=340):
            aksiColosion.append('kanan')      
        # gambar 11
        elif ((220<=colosionY1<=267 or 220<=colosionY2<=267) and 30<=colosionX1<=100):
            aksiColosion.append('kiri')     
        elif ((220<=colosionY1<=267 or 220<=colosionY2<=267) and 30<=colosionX2<=100):
            aksiColosion.append('kanan')     
        # gambar 12
        elif ((147<=colosionY1<=196 or 147<=colosionY2<=196) and 30<=colosionX1<=100):
            aksiColosion.append('kiri')        
        elif ((147<=colosionY1<=196 or 147<=colosionY2<=196) and 30<=colosionX2<=100):
            aksiColosion.append('kanan')        
        # gambar 13
        elif ((147<=colosionY1<=196 or 147<=colosionY2<=196) and 120<=colosionX1<=135):
            aksiColosion.append('kiri')       
        elif ((147<=colosionY1<=196 or 147<=colosionY2<=196) and 120<=colosionX2<=135):
            aksiColosion.append('kanan')       
        # gambar 14
        elif ((181<=colosionY1<=267 or 181<=colosionY2<=267) and 156<=colosionX1<=167):
            aksiColosion.append('kiri')       
        elif ((181<=colosionY1<=267 or 181<=colosionY2<=267) and 156<=colosionX2<=167):
            aksiColosion.append('kanan')       
        # gambar 15
        elif ((181<=colosionY1<=267 or 181<=colosionY2<=267) and 231<=colosionX1<=242):
            aksiColosion.append('kiri')       
        elif ((181<=colosionY1<=267 or 181<=colosionY2<=267) and 231<=colosionX2<=242):
            aksiColosion.append('kanan')       
        # # gambar 16
        # elif ((220<=colosionY1<=303 or 220<=colosionY2<=303) and 265<=colosionX1<=279) or ((220<=colosionY1<=303 or 220<=colosionY2<=303) and 265<=colosionX2<=279):
        #    
        # gambar 17
        elif ((147<=colosionY1<=196 or 147<=colosionY2<=196) and 265<=colosionX1<=279):
            aksiColosion.append('kiri')       
        elif ((147<=colosionY1<=196 or 147<=colosionY2<=196) and 265<=colosionX2<=279):
            aksiColosion.append('kanan')     
        # gambar 18
        elif ((220<=colosionY1<=267 or 220<=colosionY2<=267) and 300<=colosionX1<=367):
            aksiColosion.append('kiri')     
        elif ((220<=colosionY1<=267 or 220<=colosionY2<=267) and 300<=colosionX2<=367):
            aksiColosion.append('kanan')      
        # gambar 19
        elif ((147<=colosionY1<=196 or 147<=colosionY2<=196) and 300<=colosionX1<=367):
            aksiColosion.append('kiri')       
        elif ((147<=colosionY1<=196 or 147<=colosionY2<=196) and 300<=colosionX2<=367):
            aksiColosion.append('kanan')       
        # gambar 20
        elif ((75<=colosionY1<=91 or 75<=colosionY2<=91) and 30<=colosionX1<=63):
            aksiColosion.append('kiri')       
        elif ((75<=colosionY1<=91 or 75<=colosionY2<=91) and 30<=colosionX2<=63):
            aksiColosion.append('kanan')       
        # gambar 21
        elif ((75<=colosionY1<=127 or 75<=colosionY2<=127) and 85<=colosionX1<=100):
            aksiColosion.append('kiri')       
        elif ((75<=colosionY1<=127 or 75<=colosionY2<=127) and 85<=colosionX2<=100):
            aksiColosion.append('kanan')      
        # gambar 22
        elif ((110<=colosionY1<=127 or 110<=colosionY2<=127) and 120<=colosionX1<=170):
            aksiColosion.append('kiri')      
        elif ((110<=colosionY1<=127 or 110<=colosionY2<=127) and 120<=colosionX2<=170):
            aksiColosion.append('kanan')      
        # gambar 23
        elif ((147<=colosionY1<=163 or 147<=colosionY2<=163) and 156<=colosionX1<=241):
            aksiColosion.append('kiri')      
        elif ((147<=colosionY1<=163 or 147<=colosionY2<=163) and 156<=colosionX2<=241):
            aksiColosion.append('kanan')      
        # gambar 24
        elif ((110<=colosionY1<=127 or 110<=colosionY2<=127) and 227<=colosionX1<=279):
            aksiColosion.append('kiri')      
        elif ((110<=colosionY1<=127 or 110<=colosionY2<=127) and 227<=colosionX2<=279):
            aksiColosion.append('kanan')      
        # gambar 25
        elif ((75<=colosionY1<=127 or 75<=colosionY2<=127) and 300<=colosionX1<=315):
            aksiColosion.append('kiri')      
        elif ((75<=colosionY1<=127 or 75<=colosionY2<=127) and 300<=colosionX2<=315):
            aksiColosion.append('kanan')
        # gambar 26
        elif ((40<=colosionY1<=55 or 40<=colosionY2<=55) and 60<=colosionX1<=169):
            aksiColosion.append('kiri')
        elif ((40<=colosionY1<=55 or 40<=colosionY2<=55) and 60<=colosionX2<=169):
            aksiColosion.append('kanan')        
        # gambar 27
        elif ((75<=colosionY1<=90 or 75<=colosionY2<=90) and 155<=colosionX1<=242):
            aksiColosion.append('kiri')
        elif ((75<=colosionY1<=90 or 75<=colosionY2<=90) and 155<=colosionX2<=242):
            aksiColosion.append('kanan')
        # gambar 28
        elif ((40<=colosionY1<=55 or 40<=colosionY2<=55) and 229<=colosionX1<=340):
            aksiColosion.append('kiri')
        elif ((40<=colosionY1<=55 or 40<=colosionY2<=55) and 229<=colosionX2<=340):
            aksiColosion.append('kanan')
        # gambar 29
        elif ((75<=colosionY1<=91 or 75<=colosionY2<=91) and 337<=colosionX1<=367):
            aksiColosion.append('kiri')
        elif ((75<=colosionY1<=91 or 75<=colosionY2<=91) and 337<=colosionX2<=367):
            aksiColosion.append('kanan')
        
             



        # colosion point
        # # point 1
        # elif ((349<=colosionY1<=366 or 349<=colosionY2<=366) and 36<=colosionX1<=53) or ((349<=colosionY1<=366 or 349<=colosionY2<=366) and 36<=colosionX2<=53):
        #    boolgerakHorizontal = False
        # # point 2
        # elif ((24<=colosionY1<=41 or 24<=colosionY2<=41) and 36<=colosionX1<=53) or ((24<=colosionY1<=41 or 24<=colosionY2<=41) and 36<=colosionX2<=53):
        #     boolgerakHorizontal = False
        # # point 3
        # elif ((199<=colosionY1<=216 or 199<=colosionY2<=216) and 189<=colosionX1<=206) or ((199<=colosionY1<=216 or 199<=colosionY2<=216) and 189<=colosionX2<=206):
        #     boolgerakHorizontal = False
        # # point 4
        # elif ((165<=colosionY1<=182 or 165<=colosionY2<=182) and 194<=colosionX1<=211) or ((165<=colosionY1<=182 or 165<=colosionY2<=182) and 194<=colosionX2<=211):
        #     boolgerakHorizontal = False
        # # point 5
        # elif ((106<=colosionY1<=123 or 106<=colosionY2<=123) and 172<=colosionX1<=189) or ((106<=colosionY1<=123 or 106<=colosionY2<=123) and 172<=colosionX2<=189):
        #     boolgerakHorizontal = False
        # # point 6
        # elif ((199<=colosionY1<=216 or 199<=colosionY2<=216) and 282<=colosionX1<=299) or ((199<=colosionY1<=216 or 199<=colosionY2<=216) and 282<=colosionX2<=299):
        #     boolgerakHorizontal = False
        # # point 7
        # elif ((305<=colosionY1<=322 or 305<=colosionY2<=322) and 137<=colosionX1<=154) or ((305<=colosionY1<=322 or 305<=colosionY2<=322) and 137<=colosionX2<=154):
        #     boolgerakHorizontal = False
        # # point 8
        # elif ((56<=colosionY1<=73 or 56<=colosionY2<=73) and 246<=colosionX1<=263) or ((56<=colosionY1<=73 or 56<=colosionY2<=73) and 246<=colosionX2<=263):
        #     boolgerakHorizontal = False
        # # point 9
        # elif ((22<=colosionY1<=39 or 22<=colosionY2<=39) and 343<=colosionX1<=360) or ((22<=colosionY1<=39 or 22<=colosionY2<=39) and 343<=colosionX2<=360):
        #     boolgerakHorizontal = False
        # # point 10
        # elif ((270<=colosionY1<=287 or 270<=colosionY2<=287) and 320<=colosionX1<=337) or ((270<=colosionY1<=287 or 270<=colosionY2<=287) and 320<=colosionX2<=337):
        #     boolgerakHorizontal = False

          
        
        
    # colosion maze : dari atas atau bawah 
    elif (recordK1[0] == 'atas') or (recordK1[0] == 'bawah'):

        # gambar 1
        if ((100>=colosionX1>=60 or 60<=colosionX2<=100) and colosionY2==324): 
            aksiColosion.append('atas')
        elif ((100>=colosionX1>=60 or 60<=colosionX2<=100) and 350>=colosionY1>=324):
            aksiColosion.append('bawah')
        # gambar 2
        elif ((168>=colosionX1>=120 or 120<=colosionX2<=168) and 350>=colosionY2>=324):
            aksiColosion.append('atas')
        elif ((168>=colosionX1>=120 or 120<=colosionX2<=168) and 350>=colosionY1>=324):
            aksiColosion.append('bawah')
        # gambar 3
        elif ((206>=colosionX1>=191 or 191<=colosionX2<=206) and 350>=colosionY2>=324):
            aksiColosion.append('atas')
        elif ((206>=colosionX1>=191 or 191<=colosionX2<=206) and 350>=colosionY1>=324):
            aksiColosion.append('bawah')
        # gambar  4
        elif ((279>=colosionX1>=230 or 230<=colosionX2<=279) and 350>=colosionY2>=324):
            aksiColosion.append('atas')
        elif ((279>=colosionX1>=230 or 230<=colosionX2<=279) and 350>=colosionY1>=324):
            aksiColosion.append('bawah')
        # gambar  5
        elif ((340>=colosionX1>=300 or 300<=colosionX2<=340) and 350>=colosionY2>=324):
            aksiColosion.append('atas')
        elif ((340>=colosionX1>=300 or 300<=colosionX2<=340) and 350>=colosionY1>=324):
            aksiColosion.append('bawah')
        # gambar  6
        elif ((100>=colosionX1>=60 or 60<=colosionX2<=100) and 303>=colosionY2>=289):
            aksiColosion.append('atas')
        elif ((100>=colosionX1>=60 or 60<=colosionX2<=100) and 303>=colosionY1>=289):
            aksiColosion.append('bawah')
        # gambar  7
        elif ((134>=colosionX1>=120 or 120<=colosionX2<=134) and 303>=colosionY2>=220):
            aksiColosion.append('atas')
        elif ((134>=colosionX1>=120 or 120<=colosionX2<=134) and 303>=colosionY1>=220):
            aksiColosion.append('bawah')
        # gambar  8
        elif ((242>=colosionX1>=157 or 157<=colosionX2<=242) and 303>=colosionY2>=288):
            aksiColosion.append('atas')
        elif ((242>=colosionX1>=157 or 157<=colosionX2<=242) and 303>=colosionY1>=288):
            aksiColosion.append('bawah')
        # gambar  9
        elif ((279>=colosionX1>=265 or 265<=colosionX2<=279) and 303>=colosionY2>=220):
            aksiColosion.append('atas')
        elif ((279>=colosionX1>=265 or 265<=colosionX2<=279) and 303>=colosionY1>=220):
            aksiColosion.append('bawah')
        # gambar  10
        elif ((340>=colosionX1>=300 or 300<=colosionX2<=340) and 303>=colosionY2>=289):
            aksiColosion.append('atas')
        elif ((340>=colosionX1>=300 or 300<=colosionX2<=340) and 303>=colosionY1>=289):
            aksiColosion.append('bawah')
        # gambar  11
        elif ((100>=colosionX1>=30 or 30<=colosionX2<=100) and 267>=colosionY2>=220):
            aksiColosion.append('atas')
        elif ((100>=colosionX1>=30 or 30<=colosionX2<=100) and 267>=colosionY1>=220):
            aksiColosion.append('bawah')
        # gambar  12
        elif ((100>=colosionX1>=30 or 30<=colosionX2<=100) and 196>=colosionY2>=147):
            aksiColosion.append('atas')
        elif ((100>=colosionX1>=30 or 30<=colosionX2<=100) and 196>=colosionY1>=147):
            aksiColosion.append('bawah')
        # gambar  13
        elif ((135>=colosionX1>=120 or 120<=colosionX2<=135) and 196>=colosionY2>=147):
            aksiColosion.append('atas')
        elif ((135>=colosionX1>=120 or 120<=colosionX2<=135) and 196>=colosionY1>=147):
            aksiColosion.append('bawah')
        # gambar  14
        elif ((167>=colosionX1>=156 or 156<=colosionX2<=167) and 267>=colosionY2>=181):
            aksiColosion.append('atas')
        elif ((167>=colosionX1>=156 or 156<=colosionX2<=167) and 267>=colosionY1>=181):
            aksiColosion.append('bawah')
        # gambar  15
        elif ((242>=colosionX1>=231 or 231<=colosionX2<=242) and 267>=colosionY2>=181):
            aksiColosion.append('atas')
        elif ((242>=colosionX1>=231 or 231<=colosionX2<=242) and 267>=colosionY1>=181):
            aksiColosion.append('bawah')
        # # gambar  16
        # elif ((279>=colosionX1>=265 or 265<=colosionX2<=279) and 303>=colosionY2>=220) or ((279>=colosionX1>=265 or 265<=colosionX2<=279) and 303>=colosionY1>=220):
        # 
        # gambar  17
        elif ((279>=colosionX1>=265 or 265<=colosionX2<=279) and 196>=colosionY2>=147):
            aksiColosion.append('atas')
        elif ((279>=colosionX1>=265 or 265<=colosionX2<=279) and 196>=colosionY1>=147):
            aksiColosion.append('bawah')
        # gambar  18
        elif ((367>=colosionX1>=300 or 300<=colosionX2<=367) and 196>=colosionY2>=147):
            aksiColosion.append('atas')
        elif ((367>=colosionX1>=300 or 300<=colosionX2<=367) and 196>=colosionY1>=147):
            aksiColosion.append('bawah')
        # gambar  19
        elif ((367>=colosionX1>=300 or 300<=colosionX2<=367) and 196>=colosionY2>=147):
            aksiColosion.append('atas')
        elif ((367>=colosionX1>=300 or 300<=colosionX2<=367) and 196>=colosionY1>=147):
            aksiColosion.append('bawah')
        # gambar  20
        elif ((63>=colosionX1>=30 or 30<=colosionX2<=63) and 91>=colosionY2>=75):
            aksiColosion.append('atas')
        elif ((63>=colosionX1>=30 or 30<=colosionX2<=63) and 91>=colosionY1>=75):
            aksiColosion.append('bawah')
        # gambar  21
        elif ((100>=colosionX1>=85 or 85<=colosionX2<=100) and 127>=colosionY2>=75):
            aksiColosion.append('atas')
        elif ((100>=colosionX1>=85 or 85<=colosionX2<=100) and 127>=colosionY1>=75):
            aksiColosion.append('bawah')
        # gambar  22
        elif ((170>=colosionX1>=120 or 120<=colosionX2<=170) and 127>=colosionY2>=110):
            aksiColosion.append('atas')
        elif ((170>=colosionX1>=120 or 120<=colosionX2<=170) and 127>=colosionY1>=110):
            aksiColosion.append('bawah')
        # gambar  23
        elif ((241>=colosionX1>=156 or 156<=colosionX2<=241) and 163>=colosionY2>=147):
            aksiColosion.append('atas')
        elif ((241>=colosionX1>=156 or 156<=colosionX2<=241) and 163>=colosionY1>=147):
            aksiColosion.append('bawah')
        # gambar  24
        elif ((279>=colosionX1>=227 or 227<=colosionX2<=279) and 127>=colosionY2>=110):
            aksiColosion.append('atas')
        elif ((279>=colosionX1>=227 or 227<=colosionX2<=279) and 127>=colosionY1>=110):
            aksiColosion.append('bawah')
        # gambar  25
        elif ((315>=colosionX1>=300 or 300<=colosionX2<=315) and 127>=colosionY2>=75):
            aksiColosion.append('atas')
        elif ((315>=colosionX1>=300 or 300<=colosionX2<=315) and 127>=colosionY1>=75):
            aksiColosion.append('bawah')
        # gambar  26
        elif ((169>=colosionX1>=60 or 60<=colosionX2<=169) and 55>=colosionY2>=40):
            aksiColosion.append('atas')
        elif ((169>=colosionX1>=60 or 60<=colosionX2<=169) and 55>=colosionY1>=40):
            aksiColosion.append('bawah')
        # gambar  27
        elif ((242>=colosionX1>=155 or 155<=colosionX2<=242) and 90>=colosionY2>=75):
            aksiColosion.append('atas')
        elif ((242>=colosionX1>=155 or 155<=colosionX2<=242) and 90>=colosionY1>=75):
            aksiColosion.append('bawah')
        # gambar  28
        elif ((340>=colosionX1>=229 or 229<=colosionX2<=340) and 55>=colosionY2>=40):
            aksiColosion.append('atas')
        elif ((340>=colosionX1>=229 or 229<=colosionX2<=340) and 55>=colosionY1>=40):
            aksiColosion.append('bawah')
        # gambar  29
        elif ((367>=colosionX1>=337 or 337<=colosionX2<=367) and 91>=colosionY2>=75):
            aksiColosion.append('atas')
        elif ((367>=colosionX1>=337 or 337<=colosionX2<=367) and 91>=colosionY1>=75):
            aksiColosion.append('bawah')
        


        # colosion point
        # #point 1
        # elif ((53>=colosionX1>=36 or 36<=colosionX2<=53) and 366>=colosionY2>=349) or ((53>=colosionX1>=36 or 36<=colosionX2<=53) and 366>=colosionY1>=349):
        #     boolgerakHorizontal = True
        # #point 2
        # elif ((53>=colosionX1>=36 or 36<=colosionX2<=53) and 41>=colosionY2>=24) or ((53>=colosionX1>=36 or 36<=colosionX2<=53) and 41>=colosionY1>=24):
        #     boolgerakHorizontal = True
        # #point 3
        # elif ((206>=colosionX1>=189 or 189<=colosionX2<=206) and 216>=colosionY2>=199) or ((206>=colosionX1>=189 or 189<=colosionX2<=206) and 216>=colosionY1>=199):
        #     boolgerakHorizontal = True
        # #point 4
        # elif ((221>=colosionX1>=194 or 194<=colosionX2<=221) and 182>=colosionY2>=165) or ((221>=colosionX1>=194 or 194<=colosionX2<=221) and 182>=colosionY1>=165):
        #     boolgerakHorizontal = True
        # #point 5
        # elif ((189>=colosionX1>=172 or 172<=colosionX2<=189) and 123>=colosionY2>=106) or ((189>=colosionX1>=172 or 172<=colosionX2<=189) and 123>=colosionY1>=106):
        #     boolgerakHorizontal = True
        # #point 6
        # elif ((299>=colosionX1>=282 or 282<=colosionX2<=299) and 216>=colosionY2>=199) or ((299>=colosionX1>=282 or 282<=colosionX2<=299) and 216>=colosionY1>=199):
        #     boolgerakHorizontal = True
        # #point 7
        # elif ((154>=colosionX1>=137 or 137<=colosionX2<=154) and 322>=colosionY2>=305) or ((154>=colosionX1>=137 or 137<=colosionX2<=154) and 322>=colosionY1>=305):
        #     boolgerakHorizontal = True
        # #point 8
        # elif ((263>=colosionX1>=246 or 246<=colosionX2<=263) and 73>=colosionY2>=56) or ((263>=colosionX1>=246 or 246<=colosionX2<=263) and 73>=colosionY1>=56):
        #     boolgerakHorizontal = True
        # #point 9
        # elif ((367>=colosionX1>=343 or 343<=colosionX2<=367) and 39>=colosionY2>=22) or ((367>=colosionX1>=343 or 343<=colosionX2<=367) and 39>=colosionY1>=22):
        #     boolgerakHorizontal = True
        # #point 10
        # elif ((337>=colosionX1>=320 or 320<=colosionX2<=337) and 287>=colosionY2>=270) or ((337>=colosionX1>=320 or 320<=colosionX2<=337) and 287>=colosionY1>=270):
        #     boolgerakHorizontal = True

    # lawan 1
    if bg_lw1_y == False:
        dy_lw1 -= g_lw1
        cl_lw1_y1 -= g_lw1
        cl_lw1_y2 -= g_lw1
    elif bg_lw1_y == True:
        dy_lw1 += g_lw1
        cl_lw1_y1 += g_lw1
        cl_lw1_y2 += g_lw1

    if cl_lw1_y2 == 374:
        bg_lw1_y = False
    elif cl_lw1_y1 == 55:
        bg_lw1_y = True

    if ((cl_lw1_y1<=colosionY1<=cl_lw1_y2 or cl_lw1_y1<=colosionY2<=cl_lw1_y2) and cl_lw1_x1<=colosionX1<=cl_lw1_x2):
        aksiColosion.append('kiri')
        bg_lw1_y = None
    elif ((cl_lw1_y1<=colosionY1<=cl_lw1_y2 or cl_lw1_y1<=colosionY2<=cl_lw1_y2) and cl_lw1_x1<=colosionX2<=cl_lw1_x2):
        aksiColosion.append('kanan')
        bg_lw1_y = None
    elif ((cl_lw1_x2>=colosionX1>=cl_lw1_x1 or cl_lw1_x1<=colosionX2<=cl_lw1_x2) and cl_lw1_y2>=colosionY2>=cl_lw1_y1):
        aksiColosion.append('atas')
        bg_lw1_y = None
    elif ((cl_lw1_x2>=colosionX1>=cl_lw1_x1 or cl_lw1_x1<=colosionX2<=cl_lw1_x2) and cl_lw1_y2>=colosionY1>=cl_lw1_y1):
        aksiColosion.append('bawah')
        bg_lw1_y = None
   




def update(value):
    glutPostRedisplay()
    glutTimerFunc(10, update, 0)

def kotak():
    glPushMatrix()
    # global pos_x, pos_y
    glTranslate(deltaX, deltaY, 0)
    glBegin(GL_QUADS)
    glColor3ub(255, 77, 77)
    glVertex2f(195,210)
    glVertex2f(195,200)
    glVertex2f(205,200)
    glVertex2f(205,210)
    glEnd()
    glPopMatrix()
    '''
    glVertex2f(189,216)
    glVertex2f(206,216)
    glVertex2f(206,199)
    glVertex2f(189,199)
    '''
def lawan1():
    glPushMatrix()
    glTranslate(0, dy_lw1, 0)
    glBegin(GL_QUADS)
    glVertex2f(102, 229)
    glVertex2f(119, 229)
    glVertex2f(119, 246)
    glVertex2f(102, 246)
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
    # gambar16()
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

    # point1()
    # point2()
    # point3()
    # point4()
    point5()
    # point6()
    # point7()
    # point8()
    # point9()
    # point10()

    lawan1()

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
glutSpecialFunc(keyboard_coba)
glutTimerFunc(50, update, 0)
glutTimerFunc(0, timer1, 0)


glutMainLoop() #untuk memulai segalanya

