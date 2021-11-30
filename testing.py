import OpenGL.GL
from OpenGL.GL.glget import GLsize
import OpenGL.GLUT
import OpenGL.GLU

# program pertama
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from gambar import *
from angka import *


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
colosionX1 = 195
colosionX2 = 205
colosionY1 = 200
colosionY2 = 210
gerakKotakX = 1
gerakKotakY = 1

# karakter lain ?? coming soon


def keyboard_coba(key, x, y):
    global boolGerakX
    global boolGerakY
    global boolgerakHorizontal
    global recordK1

    recordK1.pop()
    if key == GLUT_KEY_UP:
        boolgerakHorizontal=False
        boolGerakY = True
        recordK1.append('atas')
    elif  key == GLUT_KEY_DOWN:
        boolgerakHorizontal=False
        boolGerakY = False
        recordK1.append('bawah')
        
    elif key == GLUT_KEY_RIGHT:
        boolgerakHorizontal=True
        boolGerakX = True
        recordK1.append('kanan')
       
    elif key==GLUT_KEY_LEFT:
        boolgerakHorizontal=True
        boolGerakX = False
        recordK1.append('kiri')
       





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
    

    
    glutTimerFunc(1000//30, timer1, 0) 

    # kotak
    if boolGerakY == True and colosionY2<374 and boolgerakHorizontal==False :
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

        # colosion maze : dari kiri atau kanan
        # gambar 1
        if ((324<=colosionY1<=350 or 324<=colosionY2<=350) and 60<=colosionX1<=100) or ((324<=colosionY1<=350 or 324<=colosionY2<=350) and 60<=colosionX2<=100):
            boolgerakHorizontal = False
        # gambar 2
        elif ((324<=colosionY1<=350 or 324<=colosionY2<=350) and 120<=colosionX1<=168) or ((324<=colosionY1<=350 or 324<=colosionY2<=350) and 120<=colosionX2<=168):
            boolgerakHorizontal = False
        # gambar 3
        elif ((324<=colosionY1<=374 or 324<=colosionY2<=374) and 191<=colosionX1<=206) or ((324<=colosionY1<=374 or 324<=colosionY2<=374) and 191<=colosionX2<=206):
            boolGerakY = False
            boolgerakHorizontal = False
        # gambar 4
        elif ((324<=colosionY1<=350 or 324<=colosionY2<=350) and 230<=colosionX1<=279) or ((324<=colosionY1<=350 or 324<=colosionY2<=350) and 230<=colosionX2<=279):
            boolgerakHorizontal = False
        # gambar 5
        elif ((324<=colosionY1<=350 or 324<=colosionY2<=350) and 300<=colosionX1<=340) or ((324<=colosionY1<=350 or 324<=colosionY2<=350) and 300<=colosionX2<=340):
            boolgerakHorizontal = False
        # gambar 6
        elif ((289<=colosionY1<=303 or 289<=colosionY2<=303) and 60<=colosionX1<=100) or ((289<=colosionY1<=303 or 289<=colosionY2<=303) and 60<=colosionX2<=100):
            boolgerakHorizontal = False
        # gambar 7
        elif ((220<=colosionY1<=303 or 220<=colosionY2<=303) and 120<=colosionX1<=134) or ((220<=colosionY1<=303 or 220<=colosionY2<=303) and 120<=colosionX2<=134):
            boolgerakHorizontal = False
        # gambar 8
        elif ((288<=colosionY1<=303 or 288<=colosionY2<=303) and 157<=colosionX1<=242) or ((288<=colosionY1<=303 or 288<=colosionY2<=303) and 157<=colosionX2<=242):
            boolgerakHorizontal = False
        # gambar 9
        elif ((220<=colosionY1<=303 or 220<=colosionY2<=303) and 265<=colosionX1<=279) or ((220<=colosionY1<=303 or 220<=colosionY2<=303) and 265<=colosionX2<=279):
            boolgerakHorizontal = False
        # gambar 10
        elif ((289<=colosionY1<=303 or 289<=colosionY2<=303) and 300<=colosionX1<=340) or ((289<=colosionY1<=303 or 289<=colosionY2<=303) and 300<=colosionX2<=340):
            boolgerakHorizontal = False
        # gambar 11
        elif ((220<=colosionY1<=267 or 220<=colosionY2<=267) and 30<=colosionX1<=100) or ((220<=colosionY1<=267 or 220<=colosionY2<=267) and 30<=colosionX2<=100):
            boolgerakHorizontal = False
        # gambar 12
        elif ((147<=colosionY1<=196 or 147<=colosionY2<=196) and 30<=colosionX1<=100) or ((147<=colosionY1<=196 or 147<=colosionY2<=196) and 30<=colosionX2<=100):
            boolgerakHorizontal = False
        # gambar 13
        elif ((147<=colosionY1<=196 or 147<=colosionY2<=196) and 120<=colosionX1<=135) or ((147<=colosionY1<=196 or 147<=colosionY2<=196) and 120<=colosionX2<=135):
            boolgerakHorizontal = False
        # gambar 14
        elif ((181<=colosionY1<=267 or 181<=colosionY2<=267) and 156<=colosionX1<=167) or ((181<=colosionY1<=267 or 181<=colosionY2<=267) and 156<=colosionX2<=167):
            boolgerakHorizontal = False
        # gambar 15
        elif ((181<=colosionY1<=267 or 181<=colosionY2<=267) and 231<=colosionX1<=242) or ((181<=colosionY1<=267 or 181<=colosionY2<=267) and 231<=colosionX2<=242):
            boolgerakHorizontal = False
        # # gambar 16
        # elif ((220<=colosionY1<=303 or 220<=colosionY2<=303) and 265<=colosionX1<=279) or ((220<=colosionY1<=303 or 220<=colosionY2<=303) and 265<=colosionX2<=279):
        #     boolgerakHorizontal = False
        # gambar 17
        elif ((147<=colosionY1<=196 or 147<=colosionY2<=196) and 265<=colosionX1<=279) or ((147<=colosionY1<=196 or 147<=colosionY2<=196) and 265<=colosionX2<=279):
            boolgerakHorizontal = False
        # gambar 18
        elif ((220<=colosionY1<=267 or 220<=colosionY2<=267) and 300<=colosionX1<=367) or ((220<=colosionY1<=267 or 220<=colosionY2<=267) and 300<=colosionX2<=367):
            boolgerakHorizontal = False
        # gambar 19
        elif ((147<=colosionY1<=196 or 147<=colosionY2<=196) and 300<=colosionX1<=367) or ((147<=colosionY1<=196 or 147<=colosionY2<=196) and 300<=colosionX2<=367):
            boolgerakHorizontal = False
        # gambar 20
        elif ((75<=colosionY1<=91 or 75<=colosionY2<=91) and 30<=colosionX1<=63) or ((75<=colosionY1<=91 or 75<=colosionY2<=91) and 30<=colosionX2<=63):
            boolgerakHorizontal = False
        # gambar 21
        elif ((75<=colosionY1<=127 or 75<=colosionY2<=127) and 85<=colosionX1<=100) or ((75<=colosionY1<=127 or 75<=colosionY2<=127) and 85<=colosionX2<=100):
            boolgerakHorizontal = False
        # gambar 22
        elif ((110<=colosionY1<=127 or 110<=colosionY2<=127) and 120<=colosionX1<=170) or ((110<=colosionY1<=127 or 110<=colosionY2<=127) and 120<=colosionX2<=170):
            boolgerakHorizontal = False
        # gambar 23
        elif ((147<=colosionY1<=163 or 147<=colosionY2<=163) and 156<=colosionX1<=241) or ((147<=colosionY1<=163 or 147<=colosionY2<=163) and 156<=colosionX2<=241):
            boolgerakHorizontal = False
        # gambar 24
        elif ((110<=colosionY1<=127 or 110<=colosionY2<=127) and 227<=colosionX1<=279) or ((110<=colosionY1<=127 or 110<=colosionY2<=127) and 227<=colosionX2<=279):
            boolgerakHorizontal = False
        # gambar 25
        elif ((75<=colosionY1<=127 or 75<=colosionY2<=127) and 300<=colosionX1<=315) or ((75<=colosionY1<=127 or 75<=colosionY2<=127) and 300<=colosionX2<=315):
            boolgerakHorizontal = False
        # gambar 26
        elif ((40<=colosionY1<=55 or 40<=colosionY2<=55) and 60<=colosionX1<=169) or ((40<=colosionY1<=55 or 40<=colosionY2<=55) and 60<=colosionX2<=169):
            boolgerakHorizontal = False
        # gambar 27
        elif ((75<=colosionY1<=90 or 75<=colosionY2<=90) and 155<=colosionX1<=242) or ((75<=colosionY1<=90 or 75<=colosionY2<=90) and 155<=colosionX2<=242):
            boolgerakHorizontal = False
        # gambar 28
        elif ((40<=colosionY1<=55 or 40<=colosionY2<=55) and 229<=colosionX1<=340) or ((40<=colosionY1<=55 or 40<=colosionY2<=55) and 229<=colosionX2<=340):
            boolgerakHorizontal = False
        # gambar 29
        elif ((75<=colosionY1<=91 or 75<=colosionY2<=91) and 337<=colosionX1<=367) or ((75<=colosionY1<=91 or 75<=colosionY2<=91) and 337<=colosionX2<=367):
            boolgerakHorizontal = False
        




        # colosion point
        # # point 1
        # elif ((349<=colosionY1<=366 or 349<=colosionY2<=366) and 36<=colosionX1<=53) or ((349<=colosionY1<=366 or 349<=colosionY2<=366) and 36<=colosionX2<=53):
        #     boolgerakHorizontal = False
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
        if ((100>=colosionX1>=60 or 60<=colosionX2<=100) and 350>=colosionY2>=324) or ((100>=colosionX1>=60 or 60<=colosionX2<=100) and 350>=colosionY1>=324):
            boolgerakHorizontal = True
        # gambar 2
        elif ((168>=colosionX1>=120 or 120<=colosionX2<=168) and 350>=colosionY2>=324) or ((168>=colosionX1>=120 or 120<=colosionX2<=168) and 350>=colosionY1>=324):
            boolgerakHorizontal = True
        # gambar 3
        elif ((206>=colosionX1>=191 or 191<=colosionX2<=206) and 350>=colosionY2>=324) or ((206>=colosionX1>=191 or 191<=colosionX2<=206) and 350>=colosionY1>=324):
            boolgerakHorizontal = True
        # gambar  4
        elif ((279>=colosionX1>=230 or 230<=colosionX2<=279) and 350>=colosionY2>=324) or ((279>=colosionX1>=230 or 230<=colosionX2<=279) and 350>=colosionY1>=324):
            boolgerakHorizontal = True
        # gambar  5
        elif ((340>=colosionX1>=300 or 300<=colosionX2<=340) and 350>=colosionY2>=324) or ((340>=colosionX1>=300 or 300<=colosionX2<=340) and 350>=colosionY1>=324):
            boolgerakHorizontal = True
        # gambar  6
        elif ((100>=colosionX1>=60 or 60<=colosionX2<=100) and 303>=colosionY2>=289) or ((100>=colosionX1>=60 or 60<=colosionX2<=100) and 303>=colosionY1>=289):
            boolgerakHorizontal = True
        # gambar  7
        elif ((134>=colosionX1>=120 or 120<=colosionX2<=134) and 303>=colosionY2>=220) or ((134>=colosionX1>=120 or 120<=colosionX2<=134) and 303>=colosionY1>=220):
            boolgerakHorizontal = True
        # gambar  8
        elif ((242>=colosionX1>=157 or 157<=colosionX2<=242) and 303>=colosionY2>=288) or ((242>=colosionX1>=157 or 157<=colosionX2<=242) and 303>=colosionY1>=288):
            boolgerakHorizontal = True
        # gambar  9
        elif ((279>=colosionX1>=265 or 265<=colosionX2<=279) and 303>=colosionY2>=220) or ((279>=colosionX1>=265 or 265<=colosionX2<=279) and 303>=colosionY1>=220):
            boolgerakHorizontal = True
        # gambar  10
        elif ((340>=colosionX1>=300 or 300<=colosionX2<=340) and 303>=colosionY2>=289) or ((340>=colosionX1>=300 or 300<=colosionX2<=340) and 303>=colosionY1>=289):
            boolgerakHorizontal = True
        # gambar  11
        elif ((100>=colosionX1>=30 or 30<=colosionX2<=100) and 267>=colosionY2>=220) or ((100>=colosionX1>=30 or 30<=colosionX2<=100) and 267>=colosionY1>=220):
            boolgerakHorizontal = True
        # gambar  12
        elif ((100>=colosionX1>=30 or 30<=colosionX2<=100) and 196>=colosionY2>=147) or ((100>=colosionX1>=30 or 30<=colosionX2<=100) and 196>=colosionY1>=147):
            boolgerakHorizontal = True
        # gambar  13
        elif ((135>=colosionX1>=120 or 120<=colosionX2<=135) and 196>=colosionY2>=147) or ((135>=colosionX1>=120 or 120<=colosionX2<=135) and 196>=colosionY1>=147):
            boolgerakHorizontal = True
        # gambar  14
        elif ((167>=colosionX1>=156 or 156<=colosionX2<=167) and 267>=colosionY2>=181) or ((167>=colosionX1>=156 or 156<=colosionX2<=167) and 267>=colosionY1>=181):
            boolgerakHorizontal = True
        # gambar  15
        elif ((242>=colosionX1>=231 or 231<=colosionX2<=242) and 267>=colosionY2>=181) or ((242>=colosionX1>=231 or 231<=colosionX2<=242) and 267>=colosionY1>=181):
            boolgerakHorizontal = True
        # # gambar  16
        # elif ((279>=colosionX1>=265 or 265<=colosionX2<=279) and 303>=colosionY2>=220) or ((279>=colosionX1>=265 or 265<=colosionX2<=279) and 303>=colosionY1>=220):
        #     boolgerakHorizontal = True
        # gambar  17
        elif ((279>=colosionX1>=265 or 265<=colosionX2<=279) and 196>=colosionY2>=147) or ((279>=colosionX1>=265 or 265<=colosionX2<=279) and 196>=colosionY1>=147):
            boolgerakHorizontal = True
        # gambar  18
        elif ((367>=colosionX1>=300 or 300<=colosionX2<=367) and 196>=colosionY2>=147) or ((367>=colosionX1>=300 or 300<=colosionX2<=367) and 196>=colosionY1>=147):
            boolgerakHorizontal = True
        # gambar  19
        elif ((367>=colosionX1>=300 or 300<=colosionX2<=367) and 196>=colosionY2>=147) or ((367>=colosionX1>=300 or 300<=colosionX2<=367) and 196>=colosionY1>=147):
            boolgerakHorizontal = True
        # gambar  20
        elif ((63>=colosionX1>=30 or 30<=colosionX2<=63) and 91>=colosionY2>=75) or ((63>=colosionX1>=30 or 30<=colosionX2<=63) and 91>=colosionY1>=75):
            boolgerakHorizontal = True
        # gambar  21
        elif ((100>=colosionX1>=85 or 85<=colosionX2<=100) and 127>=colosionY2>=75) or ((100>=colosionX1>=85 or 85<=colosionX2<=100) and 127>=colosionY1>=75):
            boolgerakHorizontal = True
        # gambar  22
        elif ((170>=colosionX1>=120 or 120<=colosionX2<=170) and 127>=colosionY2>=110) or ((170>=colosionX1>=120 or 120<=colosionX2<=170) and 127>=colosionY1>=110):
            boolgerakHorizontal = True
        # gambar  23
        elif ((241>=colosionX1>=156 or 156<=colosionX2<=241) and 163>=colosionY2>=147) or ((241>=colosionX1>=156 or 156<=colosionX2<=241) and 163>=colosionY1>=147):
            boolgerakHorizontal = True
        # gambar  24
        elif ((279>=colosionX1>=227 or 227<=colosionX2<=279) and 127>=colosionY2>=110) or ((279>=colosionX1>=227 or 227<=colosionX2<=279) and 127>=colosionY1>=110):
            boolgerakHorizontal = True
        # gambar  25
        elif ((315>=colosionX1>=300 or 300<=colosionX2<=315) and 127>=colosionY2>=75) or ((315>=colosionX1>=300 or 300<=colosionX2<=315) and 127>=colosionY1>=75):
            boolgerakHorizontal = True
        # gambar  26
        elif ((169>=colosionX1>=60 or 60<=colosionX2<=169) and 55>=colosionY2>=40) or ((169>=colosionX1>=60 or 60<=colosionX2<=169) and 55>=colosionY1>=40):
            boolgerakHorizontal = True
        # gambar  27
        elif ((242>=colosionX1>=155 or 155<=colosionX2<=242) and 90>=colosionY2>=75) or ((242>=colosionX1>=155 or 155<=colosionX2<=242) and 90>=colosionY1>=75):
            boolgerakHorizontal = True
        # gambar  28
        elif ((340>=colosionX1>=229 or 229<=colosionX2<=340) and 55>=colosionY2>=40) or ((340>=colosionX1>=229 or 229<=colosionX2<=340) and 55>=colosionY1>=40):
            boolgerakHorizontal = True
        # gambar  29
        elif ((367>=colosionX1>=337 or 337<=colosionX2<=367) and 91>=colosionY2>=75) or ((367>=colosionX1>=337 or 337<=colosionX2<=367) and 91>=colosionY1>=75):
            boolgerakHorizontal = True
        



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
    # point5()
    # point6()
    # point7()
    # point8()
    # point9()
    # point10()

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

