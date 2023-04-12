from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import numpy as np




def find_zone(dx, dy):
    if abs(dx) <= abs(dy):
        if dx >= 0 and dy >= 0:
            return 1
        elif dx <= 0 and dy >= 0:
            return 2
        elif dx >= 0 and dy <= 0:
            return 6
        elif dx <= 0 and dy <= 0:
            return 5
    else:
        if dx >= 0 and dy >= 0:
            return 0
        elif dx <= 0 and dy >= 0:
            return 3
        elif dx >= 0 and dy <= 0:
            return 7
        elif dx <= 0 and dy <= 0:
            return 4


def convert_to_zone0(z, x, y):
    if z == 0:
        return x, y
    if z == 1:
        return y, x
    if z == 2:
        return y, -x
    if z == 3:
        return -x, y
    if z == 4:
        return -x, -y
    if z == 5:
        return -y, -x
    if z == 6:
        return -y, x
    if z == 7:
        return x, -y


def convert_original(z, x, y):
    if z == 0:
        return x, y
    if z == 1:
        return y, x
    if z == 2:
        return -y, x
    if z == 3:
        return -x, y
    if z == 4:
        return -x, -y
    if z == 5:
        return -y, -x
    if z == 6:
        return y, -x
    if z == 7:
        return x, -y


def midpointline(x1, y1, x2, y2, z):
    dx = x2 - x1
    dy = y2 - y1

    d = (2 * dy) - dx
    e = 2 * dy
    ne = 2 * (dy - dx)

    x = x1
    y = y1

    while x < x2:
        px, py = convert_original(z, x, y)
        draw_points(px, py)
        if d < 0:
            x += 1
            d += e
        else:
            x += 1
            y += 1
            d += ne


def draw_mpline(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    zone = find_zone(dx, dy)

    px1, py1 = convert_to_zone0(zone, x1, y1)
    px2, py2 = convert_to_zone0(zone, x2, y2)

    midpointline(px1, py1, px2, py2, zone)


def fill_rec(xmin, ymin, xmax, ymax):
    for i in range(xmin, xmax): # vertical lines
        draw_mpline(i, ymin, i, ymax)
    for i in range(ymin, ymax): # horizontal lines
        draw_mpline(xmin, i, xmax, i)

def circlePoints(x, y, x0, y0):
    draw_points(y + x0, x + y0)  # zone0
    draw_points(x + x0, y + y0)  # zone1
    draw_points(-x + x0, y + y0)  # zone2
    draw_points(-y + x0, x + y0)  # zone3
    draw_points(-y + x0, -x + y0)  # zone4
    draw_points(-x + x0, -y + y0)  # zone5
    draw_points(x + x0, -y + y0)  # zone6
    draw_points(y + x0, -x + y0)  # zone7


def midpointCircle(radius, x0, y0):  # good
    d = 1 - radius
    x = 0
    y = radius

    # circlePoints(x, y, x0, y0)

    while x < y:
        # print("y")
        if d < 0:
            # Choose East.
            d = d + 2 * x + 3
            x += 1
        else:
            # Choose South East.
            d = d + 2 * x - 2 * y + 5
            x += 1
            y = y - 1

        circlePoints(x, y, x0, y0)


def ul_shell(radius, x0, y0):
    d = 1 - radius
    x = 0
    y = radius

    # circlePoints(x, y, x0, y0)

    while x < y:
        # print("y")
        if d < 0:
            # Choose East.
            d = d + 2 * x + 3
            x += 1
        else:
            # Choose South East.
            d = d + 2 * x - 2 * y + 5
            x += 1
            y = y - 1
        # draw_points(-x + x0, y + y0)  # zone2
        draw_points(-y + x0, x + y0)  # zone3


def ur_shell(radius, x0, y0):
    d = 1 - radius
    x = 0
    y = radius

    # circlePoints(x, y, x0, y0)

    while x < y:
        # print("y")
        if d < 0:
            # Choose East.
            d = d + 2 * x + 3
            x += 1
        else:
            # Choose South East.
            d = d + 2 * x - 2 * y + 5
            x += 1
            y = y - 1
        draw_points(y + x0, x + y0)  # zone0
        # draw_points(x + x0, y + y0)  # zone1


def top_shell(radius, x0, y0):
    d = 1 - radius
    x = 0
    y = radius

    # circlePoints(x, y, x0, y0)

    while x < y:
        # print("y")
        if d < 0:
            # Choose East.
            d = d + 2 * x + 3
            x += 1
        else:
            # Choose South East.
            d = d + 2 * x - 2 * y + 5
            x += 1
            y = y - 1
        draw_points(x + x0, y + y0)  # zone1
        draw_points(-x + x0, y + y0)  # zone2


def bottom_shell(radius, x0, y0):
    d = 1 - radius
    x = 0
    y = radius

    # circlePoints(x, y, x0, y0)

    while x < y:
        # print("y")
        if d < 0:
            # Choose East.
            d = d + 2 * x + 3
            x += 1
        else:
            # Choose South East.
            d = d + 2 * x - 2 * y + 5
            x += 1
            y = y - 1

        draw_points(-x + x0, -y + y0)
        draw_points(x + x0, -y + y0)
        draw_points(-y + x0, -x + y0)  # zone4
        draw_points(y + x0, -x + y0)  # zone7


def bottom_shell_for_s3(radius, x0, y0):
    d = 1 - radius
    x = 0
    y = radius

    # circlePoints(x, y, x0, y0)

    while x < y:
        # print("y")
        if d < 0:
            # Choose East.
            d = d + 2 * x + 3
            x += 1
        else:
            # Choose South East.
            d = d + 2 * x - 2 * y + 5
            x += 1
            y = y - 1

        draw_points(-x + x0, -y + y0)
        draw_points(x + x0, -y + y0)
        draw_points(-y + x0, -x + y0)  # zone4
        draw_points(y + x0, -x + y0)  # zone7
        draw_points(-y+x0,x+y0)  # 3
        draw_points(y+x0,x+y0)  # 0


def egg_mouth(radius, x0, y0):
    d = 1 - radius
    x = 0
    y = radius

    # circlePoints(x, y, x0, y0)

    while x < y:
        # print("y")
        if d < 0:
            # Choose East.
            d = d + 2 * x + 3
            x += 1
        else:
            # Choose South East.
            d = d + 2 * x - 2 * y + 5
            x += 1
            y = y - 1
        draw_points(-x + x0, -y + y0)
        draw_points(x + x0, -y + y0)


def yolk(x0, y0):
    radius = 100
    d = 1 - radius
    x = 0
    y = radius

    # circlePoints(x, y, x0, y0)

    while x < y:
        # print("y")
        if d < 0:
            # Choose East.
            d = d + 2 * x + 3
            x += 1
        else:
            # Choose South East.
            d = d + 2 * x - 2 * y + 5
            x += 1
            y = y - 1
        draw_points(x + x0, y + y0 - 70)  # zone1
        draw_points(-x + x0, y + y0 - 70)  # zone2

        draw_points(-x + x0, -y + y0 + 70)  # zone5
        draw_points(x + x0, -y + y0 + 70)  # zone6

def rotate(x, y, angle):
    a = math.cos(math.radians(angle))
    b = math.sin(math.radians(angle))

    r = np.array([[a, -b, 0],
                  [b, a, 0],
                  [0, 0, 1]])

    v = np.array([[x],
                   [y],
                   [1]])

    r_v = np.matmul(r, v)
    return r_v



# This function is used to draw pixels.
def draw_points(x, y):
    # The parameter that is passed in the function dictates the size of the pixel.
    glPointSize(5)
    glBegin(GL_POINTS)

    # Think of this as a co-ordinate. At the given x and y position the pixel will be drawn.
    glVertex2f(x, y)

    glEnd()


def s1():
    # background
    #glColor3f(0.5, 0.5, 0.6)
    #fill_rec(1, 1, 999, 999)
    # glColor3f(0.4, 0.4, 0.4)
    # fill_rec(0, 0, 1000, 1000)
    # egg
    glColor3f(0.8, 0.5, 0.3)
    ul_shell(400, 950, 350 - 100)
    ur_shell(400, 550, 350 - 100)
    top_shell(120, 750, 545 - 100)
    bottom_shell(200, 750, 350 - 100)

    # egg eye
    glColor3f(0.7, 0.3, 0)
    top_shell(30, 700, 500 - 100)  # left eye
    top_shell(30, 800, 500 - 100)  # right eye

    # egg mouth
    glColor3f(0.7, 0.3, 0)
    egg_mouth(100, 750, 400 - 100)

    # egg left arm
    glColor3f(0.8, 0.5, 0.3)
    draw_mpline(600, 300, 850, 350)
    draw_mpline(600,270, 850, 320)
    draw_mpline(850, 350, 850, 320)

    # egg right arm
    draw_mpline(850, 400, 900, 650)
    draw_mpline(870, 400, 920, 650)
    draw_mpline(900, 650, 920, 650)

    # egg left leg
    draw_mpline(600, 200, 550, 100)
    draw_mpline(620, 200, 570, 100)
    draw_mpline(550, 100, 570, 100)

    # egg right leg
    draw_mpline(850, 200, 900, 100)
    draw_mpline(870, 200, 920, 100)
    draw_mpline(900, 100, 920, 100)

    # player body
    glColor3f(0.7, 0, 0)
    draw_mpline(150, 500, 300, 500)
    draw_mpline(150, 800, 300, 800)

    draw_mpline(150, 500, 150, 800)
    draw_mpline(300, 500, 300, 800)

    # player leg
    glColor3f(0.4, 0.5, 1)
    draw_mpline(170, 500, 280, 500)
    draw_mpline(180, 100, 270, 100)

    draw_mpline(170, 500, 180, 100)
    draw_mpline(280, 500, 270, 100)

    # player head
    glColor3f(0.9, 0.5, 0.4)
    midpointCircle(50, 225, 850)

    # player arm top
    glColor3f(0.7, 0, 0)
    draw_mpline(300, 800, 355, 700)
    draw_mpline(355, 700, 450, 700)

    # player arm bottom
    draw_mpline(300, 700, 350, 675)
    draw_mpline(350, 675, 450, 680)

    # player foot
    draw_mpline(190, 100, 170, 70)
    draw_mpline(250, 100, 300, 70)
    draw_mpline(170, 70, 300, 70)

    # hammer handle
    glColor3f(0.5, 0.1, 0.1)
    #            x     y    x    y
    draw_mpline(450, 650, 450, 750)
    draw_mpline(460, 650, 460, 750)
    draw_mpline(450, 650, 460, 650)

    # hammer body
    glColor3f(0.6, 0.7, 0.7)
    draw_mpline(370, 750, 550, 750)
    draw_mpline(370, 850, 550, 850)

    draw_mpline(370, 750, 370, 850)
    draw_mpline(550, 750, 550, 850)

    fill_rec(370, 750, 550, 850)


def s2():
    # player body
    glColor3f(0.7, 0, 0)
    draw_mpline(150, 500, 300, 500)
    draw_mpline(150, 800, 300, 800)

    draw_mpline(150, 500, 150, 800)
    draw_mpline(300, 500, 300, 800)

    # player legs
    glColor3f(0.4, 0.5, 1)
    draw_mpline(170, 500, 280, 500)
    draw_mpline(170, 100, 280, 100)

    draw_mpline(170, 500, 170, 100)
    draw_mpline(280, 500, 280, 100)

    draw_mpline(225, 500, 225, 100)

    # player hands
    glColor3f(0.7, 0, 0)
    draw_mpline(150, 770, 50, 650)
    draw_mpline(300, 770, 400, 642)

    # hammer handle
    glColor3f(0.5, 0.1, 0.1)
    glColor3f(1.0, 1.0, 0.0)

    draw_mpline(400, 640, 600, 640)
    draw_mpline(400, 610, 600, 610)

    draw_mpline(400, 640, 400, 610)
    draw_mpline(600, 640, 600, 610)

    # hammer body
    glColor3f(0.6, 0.7, 0.7)
    draw_mpline(600, 720, 600, 520)
    draw_mpline(600, 720, 700, 720)

    draw_mpline(600, 520, 700, 520)
    draw_mpline(700, 720, 700, 520)

    # head
    glColor3f(0.9,0.5,0.4)
    midpointCircle(50, 225, 850)

    # full egg
    glColor3f(0.8, 0.5, 0.3)
    ul_shell(400, 950, 350)
    ur_shell(400, 550, 350)
    top_shell(120, 750, 545)
    bottom_shell(200, 750, 350)



    # egg eyes

    draw_mpline(700, 450, 720, 470)
    draw_mpline(720, 470, 700, 490)

    draw_mpline(750, 470, 770, 490)
    draw_mpline(750, 470, 770, 450)

    # egg mouth
    glColor3f(0.7, 0.3, 0)
    draw_mpline(730, 350, 700, 300)
    draw_mpline(730, 350, 760, 300)

    # egg hands
    glColor3f(0.8, 0.5, 0.3)
    draw_mpline(620, 350, 460, 300)
    draw_mpline(900, 350, 1000, 300)

    # egg legs
    draw_mpline(660, 200, 650, 100)
    draw_mpline(840, 200, 850, 100)


def s3():
    # player body
    glColor3f(0.7, 0, 0)
    draw_mpline(150, 500, 300, 500)
    draw_mpline(150, 800, 300, 800)

    draw_mpline(150, 500, 150, 800)
    draw_mpline(300, 500, 300, 800)

    # player leg
    glColor3f(0.4, 0.5, 1)
    draw_mpline(170, 500, 280, 500)
    draw_mpline(180, 100, 270, 100)

    draw_mpline(170, 500, 180, 100)
    draw_mpline(280, 500, 270, 100)

    # player foot
    glColor3f(0.7, 0, 0)
    draw_mpline(190, 100, 170, 70)
    draw_mpline(250, 100, 300, 70)
    draw_mpline(170, 70, 300, 70)

    # player head
    glColor3f(0.9, 0.5, 0.4)
    midpointCircle(50, 225, 850)

    # Player hand
    glColor3f(0.7, 0, 0)
    draw_mpline(260, 740, 500, 740)
    draw_mpline(260, 700, 500, 700)

    #  hammer handle
    glColor3f(0.5, 0.1, 0.1)
    draw_mpline(500, 730, 700, 730)  # top line
    draw_mpline(500, 710, 700, 710)  # bottom line
    draw_mpline(500, 700, 500, 740)  # middle line

    # hammer body
    glColor3f(0.6, 0.7, 0.7)
    draw_mpline(700, 800, 840, 800)  # top line
    draw_mpline(700, 600, 840, 600)  # bottom line

    draw_mpline(700, 800, 700, 600)  # left
    draw_mpline(840, 800, 840, 600)  # right line

    # # egg part lower
    # glColor3f(0.8, 0.5, 0.3)
    # bottom_shell_for_s3(200, 750, 550 - 100)
    #
    # # upper part of broken egg
    # egg_mouth(195, 750, 720)

    # egg
    glColor3f(0.8, 0.5, 0.3)
    ul_shell(400, 950, 350 - 100)
    ur_shell(400, 550, 350 - 100)
    bottom_shell(200, 750, 350 - 100)

    # egg mouth
    glColor3f(0.8, 0.5, 0.3)
    egg_mouth(110, 750, 600+10)

    # egg mouth
    glColor3f(0.7, 0.3, 0)
    draw_mpline(730, 250, 700, 200)
    draw_mpline(730, 250, 760, 200)

    # egg eyes

    draw_mpline(700, 470-50, 720, 490-50)
    draw_mpline(720, 490-50, 700, 510-50)

    draw_mpline(750, 490-50, 770, 510-50)
    draw_mpline(750, 490-50, 770, 470-50)


def s4():
    # player body
    glColor3f(0.7, 0, 0)
    draw_mpline(150+200, 500, 300+200, 500)
    draw_mpline(150+200, 800, 300+200, 800)

    draw_mpline(150+200, 500, 150+200, 800)
    draw_mpline(300+200, 500, 300+200, 800)

    # player leg
    glColor3f(0.4, 0.5, 1)
    draw_mpline(170+200, 500, 280+200, 500)
    draw_mpline(180+200, 100, 270+200, 100)

    draw_mpline(170+200, 500, 180+200, 100)
    draw_mpline(280+200, 500, 270+200, 100)

    # player foot
    glColor3f(0.7, 0, 0)
    draw_mpline(190+200, 100, 170+200, 70)
    draw_mpline(250+200, 100, 300+200, 70)
    draw_mpline(170+200, 70, 300+200, 70)

    # player head
    glColor3f(0.9,0.5,0.4)
    midpointCircle(50, 225+200, 850)

    # hammer handle
    #            x     y    x    y
    # draw_mpline(450, 650, 450, 750)
    # draw_mpline(460, 650, 460, 750)
    # draw_mpline(450, 650, 460, 650)

    # hammer body
    # draw_mpline(370, 750, 550, 750) #r1r2
    # draw_mpline(370, 850, 550, 850) #r3r4

    # draw_mpline(370, 750, 370, 850)
    # draw_mpline(550, 750, 550, 850)

    # hammer body rotate
    glColor3f(0.6,0.7,0.7)
    r1 = rotate(370-370, 750-650, -140)
    r2 = rotate(550-370, 750-650, -140)
    r3 = rotate(370-370, 850-650, -140)
    r4 = rotate(550-370, 850-650, -140)
    draw_mpline(r1[0][0] + 370+250, r1[1][0] + 750-200, r2[0][0] + 370+250, r2[1][0] + 750-200)
    draw_mpline(r3[0][0] + 370+250, r3[1][0] + 750-200, r4[0][0] + 370+250, r4[1][0] + 750-200)
    draw_mpline(r1[0][0] + 370+250, r1[1][0] + 750-200, r3[0][0] + 370+250, r3[1][0] + 750-200)
    draw_mpline(r2[0][0] + 370+250, r2[1][0] + 750-200, r4[0][0] + 370+250, r4[1][0] + 750-200)

    # hammer handle rotate
    # hammer handle
    glColor3f(0.5, 0.1, 0.1)
    #            x     y    x    y
    # draw_mpline(450, 650, 450, 750) #h1h2
    # draw_mpline(460, 650, 460, 750) #h3h4
    # draw_mpline(450, 650, 460, 650)
    h1 = rotate(450-370, 650-650, -140)
    h2 = rotate(450-370, 750-650, -140)
    h3 = rotate(460-370, 650-650, -140)
    h4 = rotate(460-370, 750-650, -140)
    draw_mpline(h1[0][0] + 370 + 250, h1[1][0] + 650 - 100, h2[0][0] + 370 + 250, h2[1][0] + 650 - 100)
    draw_mpline(h3[0][0] + 370 + 250, h3[1][0] + 650 - 100, h4[0][0] + 370 + 250, h4[1][0] + 650 - 100)
    draw_mpline(h1[0][0] + 370 + 250, h1[1][0] + 650 - 100, h3[0][0] + 370 + 250, h3[1][0] + 650 - 100)
    #draw_mpline(h2[0][0] + 450 + 300, h2[1][0] + 750 - 300, h4[0][0] + 370 + 300, h4[1][0] + 650 - 300)

    # player hand
    glColor3f(0.7, 0, 0)
    draw_mpline(300 + 200, 800, h1[0][0] + 370 + 250, h1[1][0] + 650 - 100)
    draw_mpline(300 + 200, 650, h3[0][0] + 370 + 250, h3[1][0] + 650 - 100)

    # bottom shell
    glColor3f(0.8, 0.5, 0.3)
    bottom_shell(200, 750, 250)

    # egg left leg
    draw_mpline(600, 200, 550, 100)
    draw_mpline(620, 200, 570, 100)
    draw_mpline(550, 100, 570, 100)

    # egg right leg
    draw_mpline(850, 200, 900, 100)
    draw_mpline(870, 200, 920, 100)
    draw_mpline(900, 100, 920, 100)

    # cracked parts
    draw_mpline(550, 250, 600, 275)
    draw_mpline(600, 275, 700, 225)
    draw_mpline(700, 225, 750, 300)
    draw_mpline(750, 300, 800, 200)
    draw_mpline(800, 200, 950, 250)

    glColor3f(1.0, 1.0, 0.0)
    yolk(900, 50)


def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    # user inputs

    force = input("Apply force: ")
    inp = int(force)
    if inp <= 0:
        s1()
    elif inp < 50:
        s2()
    elif inp < 100:
        s3()
    else:
        s4()

    # (Red, Green, Blue)
    # drawEgg()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)

# Size of the window.
# Manipulating this value will let us change the size of the output widow where the pixel is shown.
glutInitWindowSize(1000, 1000)

glutInitWindowPosition(500, 0)

# window name
wind = glutCreateWindow(b"Project")

glutDisplayFunc(showScreen)

glutMainLoop()