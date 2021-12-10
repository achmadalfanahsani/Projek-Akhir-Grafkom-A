from sys import float_repr_style
import OpenGL.GL
from OpenGL.GL.glget import GLsize
import OpenGL.GLUT
import OpenGL.GLU
import random 

# program pertama
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from maze import *
from gambar_point import *


# fungsi iterasi program
def iterate():
    # ke kanan, atas, kiri, bawah
    glViewport(-50, -20, 705, 638)
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
recordK1 = ['bawah',]
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

# lawan 2
dy_lw2 = 0
bg_lw2_y = False
g_lw2 = 1
cl_lw2_y1 = 170
cl_lw2_y2 = 187
cl_lw2_x1 = 280
cl_lw2_x2 = 297

# lawan 3
dx_lw3 = 0
bg_lw3_x = False
g_lw3 = 1
cl_lw3_y1 = 57
cl_lw3_y2 = 74
cl_lw3_x1 = 228
cl_lw3_x2 = 245

# lawan 4
dx_lw4 = 0
bg_lw4_x = False
g_lw4 = 1
cl_lw4_y1 = 306
cl_lw4_y2 = 323
cl_lw4_x1 = 261
cl_lw4_x2 = 278

# lawan 5
dy_lw5 = 0
bg_lw5_y = False
g_lw5 = 1
cl_lw5_y1 = 252
cl_lw5_y2 = 269
cl_lw5_x1 = 245
cl_lw5_x2 = 262

# lawan 6
dy_lw6 = 0
bg_lw6_y = False
g_lw6 = 1
cl_lw6_y1 = 243
cl_lw6_y2 = 260
cl_lw6_x1 = 137
cl_lw6_x2 = 154

# point
index = 5
angka = 0

# semua
arah_karakter = 'bawah'
kecepatan = 20
sesi = [False, False, False, False, False, False]

def keyboard_coba(key, x, y):
    global boolGerakX
    global boolGerakY
    global boolgerakHorizontal
    global recordK1
    global aksiColosion
    global arah_karakter

    recordK1.pop()
    
    
    if key == GLUT_KEY_UP:
        if aksiColosion[0]!='atas':
            boolgerakHorizontal=False
            boolGerakY = True
        else:
            boolgerakHorizontal = None
            boolGerakY = None
        recordK1.append('atas')
        aksiColosion.clear()
        aksiColosion.append('a')
        arah_karakter = 'atas'

    elif  key == GLUT_KEY_DOWN:
        if aksiColosion[0] != 'bawah':
            boolgerakHorizontal=False
            boolGerakY = False
        else:
            boolgerakHorizontal = None
            boolGerakY = None
        recordK1.append('bawah')
        aksiColosion.clear()
        aksiColosion.append('b')
        arah_karakter = 'bawah'

        
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
        arah_karakter = 'kanan'
       
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
        arah_karakter = 'kiri'
       





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
    
    #lawan2
    global bg_lw2_y
    global dy_lw2
    global g_lw2
    global cl_lw2_y1
    global cl_lw2_y2
    global cl_lw2_x1
    global cl_lw2_x2

    #lawan3
    global bg_lw3_x
    global dx_lw3
    global g_lw3
    global cl_lw3_y1
    global cl_lw3_y2
    global cl_lw3_x1
    global cl_lw3_x2

    #lawan4
    global bg_lw4_x
    global dx_lw4
    global g_lw4
    global cl_lw4_y1
    global cl_lw4_y2
    global cl_lw4_x1
    global cl_lw4_x2

    #lawan5
    global bg_lw5_y
    global dy_lw5
    global g_lw5
    global cl_lw5_y1
    global cl_lw5_y2
    global cl_lw5_x1
    global cl_lw5_x2

    #lawan1
    global bg_lw6_y
    global dy_lw6
    global g_lw6
    global cl_lw6_y1
    global cl_lw6_y2
    global cl_lw6_x1
    global cl_lw6_x2

    #point
    global index
    global angka
    global sesi


    # semua
    global kecepatan

    # print(aksiColosion)

    # if angka>0 and (angka % 10 == 0):
    #     kecepatan -= 5
    
    if angka == 10:
        sesi[0] = True
        kecepatan = 19
    elif angka == 15:
        sesi[1] = True
        kecepatan = 18
    elif angka == 20:
        sesi[2] = True
        kecepatan = 17
    elif angka == 25:
        sesi[3] = True
        kecepatan = 16
    elif angka == 30:
        sesi[4] = True
        kecepatan = 15
    elif angka == 35:
        sesi[5] = True
        kecepatan = 14
    elif angka == 40:
        kecepatan = 13
    elif angka == 45:
        kecepatan = 12
    elif angka == 50:
        kecepatan = 11
    elif angka == 55:
        kecepatan = 10
        
    if len(aksiColosion)==2:
        aksiColosion.pop(0)

    glutTimerFunc(kecepatan, timer1, 0) 
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
        # point 1
        elif ((349<=colosionY1<=366 or 349<=colosionY2<=366) and 36<=colosionX1<=53) and index == 0:
           index = random.randrange(10)
           angka += 1
        elif ((349<=colosionY1<=366 or 349<=colosionY2<=366) and 36<=colosionX2<=53) and index == 0:
           index = random.randrange(10)
           angka += 1
        # point 2
        elif ((24<=colosionY1<=41 or 24<=colosionY2<=41) and 36<=colosionX1<=53) and index == 1:
            index = random.randrange(10)
            angka += 1
        elif ((24<=colosionY1<=41 or 24<=colosionY2<=41) and 36<=colosionX2<=53) and index == 1:
            index = random.randrange(10)
            angka += 1
        # point 3
        elif ((199<=colosionY1<=216 or 199<=colosionY2<=216) and 189<=colosionX1<=206) and index == 2:
            index = random.randrange(10)
            angka += 1
        elif ((199<=colosionY1<=216 or 199<=colosionY2<=216) and 189<=colosionX2<=206) and index==2:
            index = random.randrange(10)
            angka += 1
        # point 4
        elif ((165<=colosionY1<=182 or 165<=colosionY2<=182) and 194<=colosionX1<=211) and index == 3:
            index = random.randrange(10)
            angka += 1
        elif ((165<=colosionY1<=182 or 165<=colosionY2<=182) and 194<=colosionX2<=211) and index == 3:
            index = random.randrange(10)
            angka += 1
        # point 5
        elif ((106<=colosionY1<=123 or 106<=colosionY2<=123) and 172<=colosionX1<=189) and index == 4:
            index = random.randrange(10)
            angka += 1
        elif ((106<=colosionY1<=123 or 106<=colosionY2<=123) and 172<=colosionX2<=189) and index == 4:
            index = random.randrange(10)
            angka += 1
        # point 6
        elif ((199<=colosionY1<=216 or 199<=colosionY2<=216) and 282<=colosionX1<=299) and index == 5:
            index = random.randrange(10)
            angka += 1
        elif ((199<=colosionY1<=216 or 199<=colosionY2<=216) and 282<=colosionX2<=299) and index == 5:
            index = random.randrange(10)
            angka += 1
        # point 7
        elif ((305<=colosionY1<=322 or 305<=colosionY2<=322) and 137<=colosionX1<=154) and index == 6:
            index = random.randrange(10)
            angka += 1
        elif ((305<=colosionY1<=322 or 305<=colosionY2<=322) and 137<=colosionX2<=154) and index == 6:
            index = random.randrange(10)
            angka += 1
        # point 8
        elif ((56<=colosionY1<=73 or 56<=colosionY2<=73) and 246<=colosionX1<=263) and index == 7:
            index = random.randrange(10)
            angka += 1
        elif ((56<=colosionY1<=73 or 56<=colosionY2<=73) and 246<=colosionX2<=263) and index == 7:
            index = random.randrange(10)
            angka += 1
        # point 9
        elif ((22<=colosionY1<=39 or 22<=colosionY2<=39) and 343<=colosionX1<=360) and index == 8:
            index = random.randrange(10)
            angka += 1
        elif ((22<=colosionY1<=39 or 22<=colosionY2<=39) and 343<=colosionX2<=360) and index == 8:
            index = random.randrange(10)
            angka += 1
        # point 10
        elif ((270<=colosionY1<=287 or 270<=colosionY2<=287) and 320<=colosionX1<=337) and index == 9:
            index = random.randrange(10)
            angka += 1
        elif ((270<=colosionY1<=287 or 270<=colosionY2<=287) and 320<=colosionX2<=337) and index == 9:
            index = random.randrange(10)
            angka += 1

          
        
        
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
        elif ((367>=colosionX1>=300 or 300<=colosionX2<=367) and 267>=colosionY2>=220):
            aksiColosion.append('atas')
        elif ((367>=colosionX1>=300 or 300<=colosionX2<=367) and 267>=colosionY1>=220):
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
        #point 1
        elif ((53>=colosionX1>=36 or 36<=colosionX2<=53) and 366>=colosionY2>=349) and index == 0:
            index = random.randrange(10)
            angka += 1
        elif ((53>=colosionX1>=36 or 36<=colosionX2<=53) and 366>=colosionY1>=349) and index == 0:
            index = random.randrange(10)
            angka += 1
        #point 2
        elif ((53>=colosionX1>=36 or 36<=colosionX2<=53) and 41>=colosionY2>=24) and index == 1:
            index = random.randrange(10)
            angka += 1
        elif ((53>=colosionX1>=36 or 36<=colosionX2<=53) and 41>=colosionY1>=24) and index == 1:
            index = random.randrange(10)
            angka += 1
        #point 3
        elif ((206>=colosionX1>=189 or 189<=colosionX2<=206) and 216>=colosionY2>=199) and index == 2:
            index = random.randrange(10)
            angka += 1
        elif ((206>=colosionX1>=189 or 189<=colosionX2<=206) and 216>=colosionY1>=199) and index == 2:
            index = random.randrange(10)
            angka += 1
        #point 4
        elif ((211>=colosionX1>=194 or 194<=colosionX2<=211) and 182>=colosionY2>=165) and index == 3:
            index = random.randrange(10)
            angka += 1
        elif ((211>=colosionX1>=194 or 194<=colosionX2<=211) and 182>=colosionY1>=165) and index == 3:
            index = random.randrange(10)
            angka += 1
        #point 5
        elif ((189>=colosionX1>=172 or 172<=colosionX2<=189) and 123>=colosionY2>=106) and index == 4:
            index = random.randrange(10)
            angka += 1
        elif ((189>=colosionX1>=172 or 172<=colosionX2<=189) and 123>=colosionY1>=106) and index == 4:
            index = random.randrange(10)
            angka += 1
        #point 6
        elif ((299>=colosionX1>=282 or 282<=colosionX2<=299) and 216>=colosionY2>=199) and index == 5:
            index = random.randrange(10)
            angka += 1
        elif ((299>=colosionX1>=282 or 282<=colosionX2<=299) and 216>=colosionY1>=199) and index == 5:
            index = random.randrange(10)
            angka += 1
        #point 7
        elif ((154>=colosionX1>=137 or 137<=colosionX2<=154) and 322>=colosionY2>=305) and index == 6:
            index = random.randrange(10)
            angka += 1
        elif ((154>=colosionX1>=137 or 137<=colosionX2<=154) and 322>=colosionY1>=305) and index == 6:
            index = random.randrange(10)
            angka += 1
        #point 8
        elif ((263>=colosionX1>=246 or 246<=colosionX2<=263) and 73>=colosionY2>=56) and index == 7:
            index = random.randrange(10)
            angka += 1
        elif ((263>=colosionX1>=246 or 246<=colosionX2<=263) and 73>=colosionY1>=56) and index == 7:
            index = random.randrange(10)
            angka += 1
        #point 9
        elif ((367>=colosionX1>=343 or 343<=colosionX2<=367) and 39>=colosionY2>=22) and index == 8:
            index = random.randrange(10)
            angka += 1
        elif ((367>=colosionX1>=343 or 343<=colosionX2<=367) and 39>=colosionY1>=22) and index == 8:
            index = random.randrange(10)
            angka += 1
        #point 10
        elif ((337>=colosionX1>=320 or 320<=colosionX2<=337) and 287>=colosionY2>=270) and index == 9:
            index = random.randrange(10)
            angka += 1
        elif ((337>=colosionX1>=320 or 320<=colosionX2<=337) and 287>=colosionY1>=270) and index == 9:
            index = random.randrange(10)
            angka += 1

    # lawan 1
    if sesi[0] == True:
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
   
    # lawan 2
    if sesi[1] == True:
        if bg_lw2_y == False:
            dy_lw2 -= g_lw2
            cl_lw2_y1 -= g_lw2
            cl_lw2_y2 -= g_lw2
        elif bg_lw2_y == True:
            dy_lw2 += g_lw2
            cl_lw2_y1 += g_lw2
            cl_lw2_y2 += g_lw2

        if cl_lw2_y2 == 374:
            bg_lw2_y = False
        elif cl_lw2_y1 == 55:
            bg_lw2_y = True

        if ((cl_lw2_y1<=colosionY1<=cl_lw2_y2 or cl_lw2_y1<=colosionY2<=cl_lw2_y2) and cl_lw2_x1<=colosionX1<=cl_lw2_x2):
            aksiColosion.append('kiri')
            bg_lw2_y = None
        elif ((cl_lw2_y1<=colosionY1<=cl_lw2_y2 or cl_lw2_y1<=colosionY2<=cl_lw2_y2) and cl_lw2_x1<=colosionX2<=cl_lw2_x2):
            aksiColosion.append('kanan')
            bg_lw2_y = None
        elif ((cl_lw2_x2>=colosionX1>=cl_lw2_x1 or cl_lw2_x1<=colosionX2<=cl_lw2_x2) and cl_lw2_y2>=colosionY2>=cl_lw2_y1):
            aksiColosion.append('atas')
            bg_lw2_y = None
        elif ((cl_lw2_x2>=colosionX1>=cl_lw2_x1 or cl_lw2_x1<=colosionX2<=cl_lw2_x2) and cl_lw2_y2>=colosionY1>=cl_lw2_y1):
            aksiColosion.append('bawah')
            bg_lw2_y = None


    # lawan 3
    if sesi[2] == True:
        if bg_lw3_x == False:
            dx_lw3 -= g_lw3
            cl_lw3_x1 -= g_lw3
            cl_lw3_x2 -= g_lw3
        elif bg_lw3_x == True:
            dx_lw3 += g_lw3
            cl_lw3_x1 += g_lw3
            cl_lw3_x2 += g_lw3

        if cl_lw3_x2 == 367:
            bg_lw3_x = False
        elif cl_lw3_x1 == 30:
            bg_lw3_x = True

        if ((cl_lw3_y1<=colosionY1<=cl_lw3_y2 or cl_lw3_y1<=colosionY2<=cl_lw3_y2) and cl_lw3_x1<=colosionX1<=cl_lw3_x2):
            aksiColosion.append('kiri')
            bg_lw3_x = None
        elif ((cl_lw3_y1<=colosionY1<=cl_lw3_y2 or cl_lw3_y1<=colosionY2<=cl_lw3_y2) and cl_lw3_x1<=colosionX2<=cl_lw3_x2):
            aksiColosion.append('kanan')
            bg_lw3_x = None
        elif ((cl_lw3_x2>=colosionX1>=cl_lw3_x1 or cl_lw3_x1<=colosionX2<=cl_lw3_x2) and cl_lw3_y2>=colosionY2>=cl_lw3_y1):
            aksiColosion.append('atas')
            bg_lw3_x = None
        elif ((cl_lw3_x2>=colosionX1>=cl_lw3_x1 or cl_lw3_x1<=colosionX2<=cl_lw3_x2) and cl_lw3_y2>=colosionY1>=cl_lw3_y1):
            aksiColosion.append('bawah')
            bg_lw3_x = None

    # lawan 4
    if sesi[3] == True:
        if bg_lw4_x == False:
            dx_lw4 -= g_lw4
            cl_lw4_x1 -= g_lw4
            cl_lw4_x2 -= g_lw4
        elif bg_lw4_x == True:
            dx_lw4 += g_lw4
            cl_lw4_x1 += g_lw4
            cl_lw4_x2 += g_lw4

        if cl_lw4_x2 == 367:
            bg_lw4_x = False
        elif cl_lw4_x1 == 30:
            bg_lw4_x = True

        if ((cl_lw4_y1<=colosionY1<=cl_lw4_y2 or cl_lw4_y1<=colosionY2<=cl_lw4_y2) and cl_lw4_x1<=colosionX1<=cl_lw4_x2):
            aksiColosion.append('kiri')
            bg_lw4_x = None
        elif ((cl_lw4_y1<=colosionY1<=cl_lw4_y2 or cl_lw4_y1<=colosionY2<=cl_lw4_y2) and cl_lw4_x1<=colosionX2<=cl_lw4_x2):
            aksiColosion.append('kanan')
            bg_lw4_x = None
        elif ((cl_lw4_x2>=colosionX1>=cl_lw4_x1 or cl_lw4_x1<=colosionX2<=cl_lw4_x2) and cl_lw4_y2>=colosionY2>=cl_lw4_y1):
            aksiColosion.append('atas')
            bg_lw4_x = None
        elif ((cl_lw4_x2>=colosionX1>=cl_lw4_x1 or cl_lw4_x1<=colosionX2<=cl_lw4_x2) and cl_lw4_y2>=colosionY1>=cl_lw4_y1):
            aksiColosion.append('bawah')
            bg_lw4_x = None

    # lawan 5
    if sesi[4] == True:
        if bg_lw5_y == False:
            dy_lw5 -= g_lw5
            cl_lw5_y1 -= g_lw5
            cl_lw5_y2 -= g_lw5
        elif bg_lw5_y == True:
            dy_lw5 += g_lw5
            cl_lw5_y1 += g_lw5
            cl_lw5_y2 += g_lw5

        if cl_lw5_y2 == 324:
            bg_lw5_y = False
        elif cl_lw5_y1 == 127:
            bg_lw5_y = True

        if ((cl_lw5_y1<=colosionY1<=cl_lw5_y2 or cl_lw5_y1<=colosionY2<=cl_lw5_y2) and cl_lw5_x1<=colosionX1<=cl_lw5_x2):
            aksiColosion.append('kiri')
            bg_lw5_y = None
        elif ((cl_lw5_y1<=colosionY1<=cl_lw5_y2 or cl_lw5_y1<=colosionY2<=cl_lw5_y2) and cl_lw5_x1<=colosionX2<=cl_lw5_x2):
            aksiColosion.append('kanan')
            bg_lw5_y = None
        elif ((cl_lw5_x2>=colosionX1>=cl_lw5_x1 or cl_lw5_x1<=colosionX2<=cl_lw5_x2) and cl_lw5_y2>=colosionY2>=cl_lw5_y1):
            aksiColosion.append('atas')
            bg_lw5_y = None
        elif ((cl_lw5_x2>=colosionX1>=cl_lw5_x1 or cl_lw5_x1<=colosionX2<=cl_lw5_x2) and cl_lw5_y2>=colosionY1>=cl_lw5_y1):
            aksiColosion.append('bawah')
            bg_lw5_y = None

    # lawan 6
    if sesi[5] == True:
        if bg_lw6_y == False:
            dy_lw6 -= g_lw6
            cl_lw6_y1 -= g_lw6
            cl_lw6_y2 -= g_lw6
        elif bg_lw6_y == True:
            dy_lw6 += g_lw6
            cl_lw6_y1 += g_lw6
            cl_lw6_y2 += g_lw6

        if cl_lw6_y2 == 324:
            bg_lw6_y = False
        elif cl_lw6_y1 == 127:
            bg_lw6_y = True

        if ((cl_lw6_y1<=colosionY1<=cl_lw6_y2 or cl_lw6_y1<=colosionY2<=cl_lw6_y2) and cl_lw6_x1<=colosionX1<=cl_lw6_x2):
            aksiColosion.append('kiri')
            bg_lw6_y = None
        elif ((cl_lw6_y1<=colosionY1<=cl_lw6_y2 or cl_lw6_y1<=colosionY2<=cl_lw6_y2) and cl_lw6_x1<=colosionX2<=cl_lw6_x2):
            aksiColosion.append('kanan')
            bg_lw6_y = None
        elif ((cl_lw6_x2>=colosionX1>=cl_lw6_x1 or cl_lw6_x1<=colosionX2<=cl_lw6_x2) and cl_lw6_y2>=colosionY2>=cl_lw6_y1):
            aksiColosion.append('atas')
            bg_lw6_y = None
        elif ((cl_lw6_x2>=colosionX1>=cl_lw6_x1 or cl_lw6_x1<=colosionX2<=cl_lw6_x2) and cl_lw6_y2>=colosionY1>=cl_lw6_y1):
            aksiColosion.append('bawah')
            bg_lw6_y = None

    # colosion antar lawan 1 ke lawan 3
    if ((cl_lw3_x2>=cl_lw1_x1>=cl_lw3_x1 or cl_lw3_x1<=cl_lw1_x2<=cl_lw3_x2) and cl_lw3_y2>=cl_lw1_y1>=cl_lw3_y1):
        bg_lw1_y = True
    # colosion antara lawan 3 ke lawan 1
    if ((cl_lw1_y1<=cl_lw3_y1<=cl_lw1_y2 or cl_lw1_y1<=cl_lw3_y2<=cl_lw1_y2) and cl_lw1_x1<=cl_lw3_x1<=cl_lw1_x2):
        bg_lw3_x = True
    elif ((cl_lw1_y1<=cl_lw3_y1<=cl_lw1_y2 or cl_lw1_y1<=cl_lw3_y2<=cl_lw1_y2) and cl_lw1_x1<=cl_lw3_x2<=cl_lw1_x2):
        bg_lw3_x = False

    # colosion antar lawan 2 ke lawan 3
    if ((cl_lw3_x2>=cl_lw2_x1>=cl_lw3_x1 or cl_lw3_x1<=cl_lw2_x2<=cl_lw3_x2) and cl_lw3_y2>=cl_lw2_y1>=cl_lw3_y1):
        bg_lw2_y = True
    # colosion antara lawan 3 ke lawan 2
    if ((cl_lw2_y1<=cl_lw3_y1<=cl_lw2_y2 or cl_lw2_y1<=cl_lw3_y2<=cl_lw2_y2) and cl_lw2_x1<=cl_lw3_x1<=cl_lw2_x2):
        bg_lw3_x = True
    elif ((cl_lw2_y1<=cl_lw3_y1<=cl_lw2_y2 or cl_lw2_y1<=cl_lw3_y2<=cl_lw2_y2) and cl_lw2_x1<=cl_lw3_x2<=cl_lw2_x2):
        bg_lw3_x = False

    # colosion antar lawan 1 ke lawan 4
    if ((cl_lw4_x2>=cl_lw1_x1>=cl_lw4_x1 or cl_lw4_x1<=cl_lw1_x2<=cl_lw4_x2) and cl_lw4_y2>=cl_lw1_y2>=cl_lw4_y1):
        bg_lw1_y = False
    elif ((cl_lw4_x2>=cl_lw1_x1>=cl_lw4_x1 or cl_lw4_x1<=cl_lw1_x2<=cl_lw4_x2) and cl_lw4_y2>=cl_lw1_y1>=cl_lw4_y1):
        bg_lw1_y = True
    # colosion antara lawan 4 ke lawan 1
    if ((cl_lw1_y1<=cl_lw4_y1<=cl_lw1_y2 or cl_lw1_y1<=cl_lw4_y2<=cl_lw1_y2) and cl_lw1_x1<=cl_lw4_x2<=cl_lw1_x2):
        bg_lw4_x = False
    elif ((cl_lw1_y1<=cl_lw4_y1<=cl_lw1_y2 or cl_lw1_y1<=cl_lw4_y2<=cl_lw1_y2) and cl_lw1_x1<=cl_lw4_x1<=cl_lw1_x2):
        bg_lw4_x = True

    # colosion antar lawan 2 ke lawan 4
    if ((cl_lw4_x2>=cl_lw2_x1>=cl_lw4_x1 or cl_lw4_x1<=cl_lw2_x2<=cl_lw4_x2) and cl_lw4_y2>=cl_lw2_y2>=cl_lw4_y1):
        bg_lw2_y = False
    elif ((cl_lw4_x2>=cl_lw2_x1>=cl_lw4_x1 or cl_lw4_x1<=cl_lw2_x2<=cl_lw4_x2) and cl_lw4_y2>=cl_lw2_y1>=cl_lw4_y1):
        bg_lw2_y = True
    # colosion antara lawan 4 ke lawan 2
    if ((cl_lw2_y1<=cl_lw4_y1<=cl_lw2_y2 or cl_lw2_y1<=cl_lw4_y2<=cl_lw2_y2) and cl_lw2_x1<=cl_lw4_x1<=cl_lw2_x2):
        bg_lw4_x = True
    elif ((cl_lw2_y1<=cl_lw4_y1<=cl_lw2_y2 or cl_lw2_y1<=cl_lw4_y2<=cl_lw2_y2) and cl_lw2_x1<=cl_lw4_x2<=cl_lw2_x2):
        bg_lw4_x = False

    # colosion antar lawan 5 ke lawan 4
    if ((cl_lw5_y1<=cl_lw4_y1<=cl_lw5_y2 or cl_lw5_y1<=cl_lw4_y2<=cl_lw5_y2) and cl_lw5_x1<=cl_lw4_x1<=cl_lw5_x2):
        bg_lw4_x = True
    elif ((cl_lw5_y1<=cl_lw4_y1<=cl_lw5_y2 or cl_lw5_y1<=cl_lw4_y2<=cl_lw5_y2) and cl_lw5_x1<=cl_lw4_x2<=cl_lw5_x2):
        bg_lw4_x = False
    if ((cl_lw4_x2>=cl_lw5_x1>=cl_lw4_x1 or cl_lw4_x1<=cl_lw5_x2<=cl_lw4_x2) and cl_lw4_y2>=cl_lw5_y2>=cl_lw4_y1):
        bg_lw5_y = False
    # colosion antara lawan 4 ke lawan 5

    # colosion antar lawan 6 ke lawan 4
    if ((cl_lw4_x2>=cl_lw6_x1>=cl_lw4_x1 or cl_lw4_x1<=cl_lw6_x2<=cl_lw4_x2) and cl_lw4_y2>=cl_lw6_y2>=cl_lw4_y1):
        bg_lw6_y = False
    # colosion antara lawan 4 ke lawan 6
    if ((cl_lw6_y1<=cl_lw4_y1<=cl_lw6_y2 or cl_lw6_y1<=cl_lw4_y2<=cl_lw6_y2) and cl_lw6_x1<=cl_lw4_x1<=cl_lw6_x2):
        bg_lw4_x = True
    elif ((cl_lw6_y1<=cl_lw4_y1<=cl_lw6_y2 or cl_lw6_y1<=cl_lw4_y2<=cl_lw6_y2) and cl_lw6_x1<=cl_lw4_x2<=cl_lw6_x2):
        bg_lw4_x = False



def skor_display(skor):
    glColor(0,0,0)
    glRasterPos(282, 377)
    for i in str(skor):
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10, update, 0)

# def kotak():
#     glPushMatrix()
#     # global pos_x, pos_y
#     glTranslate(deltaX, deltaY, 0)
#     glBegin(GL_QUADS)
#     glColor3ub(255, 77, 77)
#     glVertex2f(195,210)
#     glVertex2f(195,200)
#     glVertex2f(205,200)
#     glVertex2f(205,210)
#     glEnd()
#     glPopMatrix()

def karakter_kanan():
    glPushMatrix()
    glTranslate(deltaX, deltaY, 0)
    glBegin(GL_POLYGON)
    glColor3ub(247, 240, 12)
    glVertex2f(200.23179,204.91379)
    glVertex2f(204.38224,202.59345)
    glVertex2f(204,202)
    glVertex2f(203.50933,201.38194)
    glVertex2f(202.88346,200.88912)
    glVertex2f(202.19172,200.51951)
    glVertex2f(201.58233,200.25257)
    glVertex2f(201.00588,200.15257)
    glVertex2f(200.39649,200.1115)
    glVertex2f(199.70999,200.12096)
    glVertex2f(198.75542,200.33098)
    glVertex2f(198.02547,200.667)
    glVertex2f(197.39658,201.01703)
    glVertex2f(196.70031,201.68909)
    glVertex2f(196.29194,202.3147)
    glVertex2f(195.87694,202.86345)
    glVertex2f(195.638,203.58467)
    glVertex2f(195.51225,204.47836)
    glVertex2f(195.4871,205.38773)
    glVertex2f(195.56255,206.01488)
    glVertex2f(195.77634,206.67338)
    glVertex2f(196.12846,207.33189)
    glVertex2f(196.5183,207.92768)
    glVertex2f(197.05906,208.57051)
    glVertex2f(197.70041,209.04087)
    glVertex2f(198.48011,209.44852)
    glVertex2f(199.10889,209.69938)
    glVertex2f(199.7754,209.80913)
    glVertex2f(200.49221,209.84048)
    glVertex2f(201.13357,209.74641)
    glVertex2f(201.74978,209.57395)
    glVertex2f(202.37856,209.29173)
    glVertex2f(203,209)
    glVertex2f(203.64871,208.35101)
    glVertex2f(204,208)
    glVertex2f(204.32779,207.37892)
    glEnd()
    glPopMatrix()

def karakter_bawah():
    glPushMatrix()
    glTranslate(deltaX, deltaY, 0)
    glColor3ub(247, 240, 12)
    glBegin(GL_POLYGON)
    glVertex2f(200.01217,204.81232)
    glVertex2f(197.69841,200.8241)
    glVertex2f(197.0928,201.17259)
    glVertex2f(196.58035,201.67596)
    glVertex2f(196.1145,202.17932)
    glVertex2f(195.77287,202.77949)
    glVertex2f(195.43124,203.5539)
    glVertex2f(195.29148,204.34767)
    glVertex2f(195.26042,204.98656)
    glVertex2f(195.29148,205.62545)
    glVertex2f(195.44677,206.26434)
    glVertex2f(195.72628,207.01939)
    glVertex2f(196.06791,207.67764)
    glVertex2f(196.59588,208.29717)
    glVertex2f(197.0928,208.68438)
    glVertex2f(197.5276,208.97478)
    glVertex2f(197.97793,209.2071)
    glVertex2f(198.6146,209.43943)
    glVertex2f(199.1581,209.59431)
    glVertex2f(199.68607,209.61367)
    glVertex2f(200.33827,209.57495)
    glVertex2f(200.97494,209.57495)
    glVertex2f(201.64267,209.34263)
    glVertex2f(202.29487,209.03286)
    glVertex2f(202.82285,208.60693)
    glVertex2f(203.35082,208.31653)
    glVertex2f(203.81668,207.73572)
    glVertex2f(204.17383,207.19363)
    glVertex2f(204.49993,206.45794)
    glVertex2f(204.67075,205.74161)
    glVertex2f(204.76392,204.94784)
    glVertex2f(204.74839,204.17343)
    glVertex2f(204.54652,203.5539)
    glVertex2f(204.32912,202.91501)
    glVertex2f(204.01855,202.31484)
    glVertex2f(203.66139,201.86956)
    glVertex2f(203.27318,201.46299)
    glVertex2f(202.8539,201.11451)
    glVertex2f(202.37252,200.84346)
    glEnd()
    glPopMatrix()

def karakter_kiri():
    glPushMatrix()
    glTranslate(deltaX, deltaY, 0)
    glBegin(GL_POLYGON)
    glColor3ub(247, 240, 12)
    glVertex2f(199.85639,204.92952)
    glVertex2f(195.68735,202.63639)
    glVertex2f(196,202)
    glVertex2f(196.39089,201.52428)
    glVertex2f(196.78126,201.17664)
    glVertex2f(197.36681,200.77686)
    glVertex2f(197.89659,200.49875)
    glVertex2f(198.44032,200.32494)
    glVertex2f(198.92828,200.18588)
    glVertex2f(199.45806,200.1685)
    glVertex2f(200.08544,200.1685)
    glVertex2f(200.79646,200.25541)
    glVertex2f(201.4796,200.44661)
    glVertex2f(202.13486,200.7421)
    glVertex2f(202.83195,201.21141)
    glVertex2f(203.34779,201.64595)
    glVertex2f(203.72422,202.16741)
    glVertex2f(203.93334,202.63672)
    glVertex2f(204.26794,203.14079)
    glVertex2f(204.47707,203.87082)
    glVertex2f(204.54678,205.74806)
    glVertex2f(204.35252,206.43231)
    glVertex2f(204.14246,206.98003)
    glVertex2f(203.91648,207.39522)
    glVertex2f(203.59536,207.94387)
    glVertex2f(203.03636,208.52217)
    glVertex2f(202.54873,208.98185)
    glVertex2f(201.8589,209.35255)
    glVertex2f(201.24044,209.61946)
    glVertex2f(200.55061,209.73809)
    glVertex2f(199.81321,209.76775)
    glVertex2f(199.0996,209.69361)
    glVertex2f(198.39788,209.60464)
    glVertex2f(197.88646,209.44152)
    glVertex2f(197.35125,209.17462)
    glVertex2f(196.91118,208.83356)
    glVertex2f(196.44734,208.4332)
    glVertex2f(196.1,208)
    glVertex2f(195.67426,207.38039)
    glEnd()
    glPopMatrix()

def karakter_atas():
    glPushMatrix()
    glTranslate(deltaX, deltaY, 0)
    glColor3ub(247, 240, 12)
    glBegin(GL_POLYGON)
    glVertex2f(200.01526,205.29252)
    glVertex2f(202.3616,209.4257)
    glVertex2f(202.90656,209.14261)
    glVertex2f(203.39097,208.82176)
    glVertex2f(203.73913,208.44431)
    glVertex2f(204,208)
    glVertex2f(204.31437,207.5384)
    glVertex2f(204.58685,206.97222)
    glVertex2f(204.78364,206.27392)
    glVertex2f(204.84419,205.59449)
    glVertex2f(204.85932,204.87732)
    glVertex2f(204.72308,204.02803)
    glVertex2f(204.55657,203.44297)
    glVertex2f(204.25382,202.85791)
    glVertex2f(203.90565,202.3106)
    glVertex2f(203.49693,201.80103)
    glVertex2f(202.98225,201.42357)
    glVertex2f(202.46757,201.04611)
    glVertex2f(202.0473,200.82158)
    glVertex2f(201.57022,200.55164)
    glVertex2f(201.04202,200.42418)
    glVertex2f(199.13368,200.42418)
    glVertex2f(198.55436,200.55164)
    glVertex2f(197.88985,200.84904)
    glVertex2f(197.2935,201.16769)
    glVertex2f(196.69714,201.59255)
    glVertex2f(196.25413,202.12362)
    glVertex2f(195.81113,202.63346)
    glVertex2f(195.43627,203.35572)
    glVertex2f(195.16366,204.26917)
    glVertex2f(195.0811,205.08326)
    glVertex2f(195.1596,206.03747)
    glVertex2f(195.367,206.93022)
    glVertex2f(195.82276,207.79172)
    glVertex2f(196.33733,208.5249)
    glVertex2f(196.8666,209.01981)
    glVertex2f(197.64237,209.47805)
    glEnd()
    glPopMatrix()


def lawan1():
    glPushMatrix()
    glTranslate(0, dy_lw1, 0)
    glBegin(GL_QUADS)
    glColor3ub(37, 244, 37)
    glVertex2f(102, 229)
    glVertex2f(119, 229)
    glVertex2f(119, 246)
    glVertex2f(102, 246)
    glEnd()
    glPopMatrix()
 
def lawan2():
    glPushMatrix()
    glTranslate(0, dy_lw2, 0)
    glBegin(GL_QUADS)
    glColor3ub(37, 244, 37)
    glVertex2f(280, 170)
    glVertex2f(297, 170)
    glVertex2f(297, 187)
    glVertex2f(280, 187)
    glEnd()
    glPopMatrix()

def lawan3():
    glPushMatrix()
    glTranslate(dx_lw3, 0, 0)
    glBegin(GL_QUADS)
    glColor3ub(37, 244, 37)
    glVertex2f(228, 57)
    glVertex2f(245, 57)
    glVertex2f(245, 74)
    glVertex2f(228, 74)
    glEnd()
    glPopMatrix()

def lawan4():
    glPushMatrix()
    glTranslate(dx_lw4, 0, 0)
    glColor3ub(37, 244, 37)
    glBegin(GL_QUADS)
    glVertex2f(261, 306)
    glVertex2f(278, 306)
    glVertex2f(278, 323)
    glVertex2f(261, 323)
    glEnd()
    glPopMatrix()

def lawan5():
    glPushMatrix()
    glColor3ub(37, 244, 37)
    glTranslate(0, dy_lw5, 0)
    glBegin(GL_QUADS)
    glVertex2f(245, 252)
    glVertex2f(262, 252)
    glVertex2f(262, 269)
    glVertex2f(245, 269)
    glEnd()
    glPopMatrix()

def lawan6():
    glPushMatrix()
    glColor3ub(37, 244, 37)
    glTranslate(0, dy_lw6, 0)
    glBegin(GL_QUADS)
    glVertex2f(137, 243)
    glVertex2f(154, 243)
    glVertex2f(154, 260)
    glVertex2f(137, 260)
    glEnd()
    glPopMatrix()

point = [gp_1, gp_2, gp_3, gp_4, gp_5, gp_6, gp_7, gp_8, gp_9, gp_10]
lawan = [lawan1, lawan2, lawan3, lawan4, lawan5, lawan6]
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

    point[index]()
    kotakPoint()
    skor_display(angka)

    if sesi[0] == True:
        lawan[0]()
    if sesi[1] == True:
        lawan[1]()
    if sesi[2] == True:
        lawan[2]()
    if sesi[3] == True:
        lawan[3]()
    if sesi[4] == True:
        lawan[4]()
    if sesi[5] == True:
        lawan[5]()
    
    # kotak()
    if arah_karakter == 'kanan':
        karakter_kanan()
    elif arah_karakter == 'bawah':
        karakter_bawah()
    elif arah_karakter == 'kiri':
        karakter_kiri()
    elif arah_karakter == 'atas':
        karakter_atas()

    glFlush()
    glutSwapBuffers()

# inisialisasi
glutInit(sys.argv)  # inisialisasi glut
glutInitDisplayMode(GLUT_RGBA) # mengatur layar supaya berwarna
glutInitWindowSize(600, 600) # mengatur ukuran layar/window
glutInitWindowPosition(750, 0) # mangatur posisi window
glutCreateWindow("Snake Man") # untuk memberi nama window
glutDisplayFunc(showScreen) # untuk menampilkan objek pada layar
glutIdleFunc(showScreen) # untuk menuruh opengl untuk selalu menampilkan dan membuka objek
glutSpecialFunc(keyboard_coba)
glutTimerFunc(50, update, 0)
glutTimerFunc(0, timer1, 0)
glutMainLoop() #untuk memulai segalanya
