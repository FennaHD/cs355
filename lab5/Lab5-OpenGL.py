import sys

try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GL import glOrtho
    from OpenGL.GLU import gluPerspective
    from OpenGL.GL import glRotated
    from OpenGL.GL import glTranslated
    from OpenGL.GL import glLoadIdentity
    from OpenGL.GL import glMatrixMode
    from OpenGL.GL import GL_MODELVIEW
    from OpenGL.GL import GL_PROJECTION
except:
    print("ERROR: PyOpenGL not installed properly. ")

DISPLAY_WIDTH = 500.0
DISPLAY_HEIGHT = 500.0

CAM_X, CAM_Y, CAM_Z, ANGLE = 0, 0, -20, 0
cam_x, cam_y, cam_z, angle = 0, 0, -20, 0
is_perspective = True
tires_angle = 0
FRONT_TIRES_X, BACK_TIRES_X, CAR_X = 2, -2, 0
front_tires_x, back_tires_x, car_x = 2, -2, 0


def init(): 
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)

def drawHouse (x_offset=0, y_offset=0, z_offset=0):
    glLineWidth(2.5)
    glColor3f(1.0+x_offset, 0.0, 0.0)
    #Floor
    glBegin(GL_LINES)
    glVertex3f(-5.0, 0.0, -5.0)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 0, 5)
    glVertex3f(5, 0, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 0, -5)
    #Ceiling
    glVertex3f(-5, 5, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(-5, 5, 5)
    glVertex3f(-5, 5, 5)
    glVertex3f(-5, 5, -5)
    #Walls
    glVertex3f(-5, 0, -5)
    glVertex3f(-5, 5, -5)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 0, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 5, 5)
    #Door
    glVertex3f(-1, 0, 5)
    glVertex3f(-1, 3, 5)
    glVertex3f(-1, 3, 5)
    glVertex3f(1, 3, 5)
    glVertex3f(1, 3, 5)
    glVertex3f(1, 0, 5)
    #Roof
    glVertex3f(-5, 5, -5)
    glVertex3f(0, 8, -5)
    glVertex3f(0, 8, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(-5, 5, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(0, 8, -5)
    glEnd()


def drawCar():
    glLineWidth(2.5)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    #Front Side
    glVertex3f(-3, 2, 2)
    glVertex3f(-2, 3, 2)
    glVertex3f(-2, 3, 2)
    glVertex3f(2, 3, 2)
    glVertex3f(2, 3, 2)
    glVertex3f(3, 2, 2)
    glVertex3f(3, 2, 2)
    glVertex3f(3, 1, 2)
    glVertex3f(3, 1, 2)
    glVertex3f(-3, 1, 2)
    glVertex3f(-3, 1, 2)
    glVertex3f(-3, 2, 2)
    #Back Side
    glVertex3f(-3, 2, -2)
    glVertex3f(-2, 3, -2)
    glVertex3f(-2, 3, -2)
    glVertex3f(2, 3, -2)
    glVertex3f(2, 3, -2)
    glVertex3f(3, 2, -2)
    glVertex3f(3, 2, -2)
    glVertex3f(3, 1, -2)
    glVertex3f(3, 1, -2)
    glVertex3f(-3, 1, -2)
    glVertex3f(-3, 1, -2)
    glVertex3f(-3, 2, -2)
    #Connectors
    glVertex3f(-3, 2, 2)
    glVertex3f(-3, 2, -2)
    glVertex3f(-2, 3, 2)
    glVertex3f(-2, 3, -2)
    glVertex3f(2, 3, 2)
    glVertex3f(2, 3, -2)
    glVertex3f(3, 2, 2)
    glVertex3f(3, 2, -2)
    glVertex3f(3, 1, 2)
    glVertex3f(3, 1, -2)
    glVertex3f(-3, 1, 2)
    glVertex3f(-3, 1, -2)
    glEnd()


def drawTire():
    glLineWidth(2.5)
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES)
    #Front Side
    glVertex3f(-1, .5, .5)
    glVertex3f(-.5, 1, .5)
    glVertex3f(-.5, 1, .5)
    glVertex3f(.5, 1, .5)
    glVertex3f(.5, 1, .5)
    glVertex3f(1, .5, .5)
    glVertex3f(1, .5, .5)
    glVertex3f(1, -.5, .5)
    glVertex3f(1, -.5, .5)
    glVertex3f(.5, -1, .5)
    glVertex3f(.5, -1, .5)
    glVertex3f(-.5, -1, .5)
    glVertex3f(-.5, -1, .5)
    glVertex3f(-1, -.5, .5)
    glVertex3f(-1, -.5, .5)
    glVertex3f(-1, .5, .5)
    #Back Side
    glVertex3f(-1, .5, -.5)
    glVertex3f(-.5, 1, -.5)
    glVertex3f(-.5, 1, -.5)
    glVertex3f(.5, 1, -.5)
    glVertex3f(.5, 1, -.5)
    glVertex3f(1, .5, -.5)
    glVertex3f(1, .5, -.5)
    glVertex3f(1, -.5, -.5)
    glVertex3f(1, -.5, -.5)
    glVertex3f(.5, -1, -.5)
    glVertex3f(.5, -1, -.5)
    glVertex3f(-.5, -1, -.5)
    glVertex3f(-.5, -1, -.5)
    glVertex3f(-1, -.5, -.5)
    glVertex3f(-1, -.5, -.5)
    glVertex3f(-1, .5, -.5)
    #Connectors
    glVertex3f(-1, .5, .5)
    glVertex3f(-1, .5, -.5)
    glVertex3f(-.5, 1, .5)
    glVertex3f(-.5, 1, -.5)
    glVertex3f(.5, 1, .5)
    glVertex3f(.5, 1, -.5)
    glVertex3f(1, .5, .5)
    glVertex3f(1, .5, -.5)
    glVertex3f(1, -.5, .5)
    glVertex3f(1, -.5, -.5)
    glVertex3f(.5, -1, .5)
    glVertex3f(.5, -1, -.5)
    glVertex3f(-.5, -1, .5)
    glVertex3f(-.5, -1, -.5)
    glVertex3f(-1, -.5, .5)
    glVertex3f(-1, -.5, -.5)
    glEnd()

def display():
    glClear (GL_COLOR_BUFFER_BIT)
    glColor3f (1.0, 1.0, 1.0)
    # viewing transformation

    #Your Code Here
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    if is_perspective:
        gluPerspective(150, DISPLAY_WIDTH / DISPLAY_HEIGHT, 1, 100)
    else:
        glOrtho(-32, 32, -32, 32, -0.01, 100.0)
    glRotated(angle, 0, 1, 0)
    glTranslated(cam_x, cam_y, cam_z)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glPushMatrix()
    drawHouse()
    glPopMatrix()

    glPushMatrix()
    glTranslate(25, 0, 0)
    drawHouse()
    glPopMatrix()

    glPushMatrix()
    glTranslate(-25, 0, 0)
    drawHouse()
    glPopMatrix()

    glPushMatrix()
    glTranslate(25, 0, 40)
    glRotatef(180, 0, 1, 0)
    drawHouse()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0, 0, 40)
    glRotatef(180, 0, 1, 0)
    drawHouse()
    glPopMatrix()

    glPushMatrix()
    glTranslate(-25, 0, 40)
    glRotatef(180, 0, 1, 0)
    drawHouse()
    glPopMatrix()

    glPushMatrix()
    glTranslate(-40, 0, 20)
    glRotatef(90, 0, 1, 0)
    drawHouse()
    glPopMatrix()

    # Car
    glPushMatrix()
    glTranslate(car_x, 0, 10)
    drawCar()
    glPopMatrix()

    # Front-right
    glPushMatrix()
    glTranslate(front_tires_x, 0, 12)
    glRotatef(tires_angle, 0, 0, 1)
    drawTire()
    glPopMatrix()

    # Front-left
    glPushMatrix()
    glTranslate(front_tires_x, 0, 8)
    glRotatef(tires_angle, 0, 0, 1)
    drawTire()
    glPopMatrix()

    # Back-left
    glPushMatrix()
    glTranslate(back_tires_x, 0, 8)
    glRotatef(tires_angle, 0, 0, 1)
    drawTire()
    glPopMatrix()

    # Back-right
    glPushMatrix()
    glTranslate(back_tires_x, 0, 12)
    glRotatef(tires_angle, 0, 0, 1)
    drawTire()
    glPopMatrix()

    glFlush()


def timer(value):
    global tires_angle, front_tires_x, back_tires_x, car_x

    tires_angle -= 5
    front_tires_x += 1
    back_tires_x += 1
    car_x += 1


    glutPostRedisplay()
    glutTimerFunc(1000, timer, 1)


def keyboard(key, x, y):

    global CAM_X, CAM_Y, CAM_Z, cam_x, cam_y, cam_z, angle, is_perspective
    global front_tires_x, back_tires_x, car_x, FRONT_TIRES_X, BACK_TIRES_X, CAR_X

    if key == chr(27):
        import sys
        sys.exit(0)
  
    if key == b'w':
        cam_z += 1

    if key == b's':
        cam_z -= 1

    if key == b'a':
        cam_x += 1

    if key == b'd':
        cam_x -= 1

    if key == b'r':
        cam_y -= 1

    if key == b'f':
        cam_y += 1

    if key == b'q':
        angle -= 10

    if key == b'e':
        angle += 10

    if key == b'p':
        is_perspective = True

    if key == b'o':
        is_perspective = False

    if key == b'h':
        cam_x, cam_y, cam_z, angle = CAM_X, CAM_Y, CAM_Z, ANGLE
        front_tires_x, back_tires_x, car_x = FRONT_TIRES_X, BACK_TIRES_X, CAR_X


    glutPostRedisplay()


glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (int(DISPLAY_WIDTH), int(DISPLAY_HEIGHT))
glutInitWindowPosition (100, 100)
glutCreateWindow (b'OpenGL Lab')
init ()
glutDisplayFunc(display)
glutTimerFunc(1000, timer, 1)
glutKeyboardFunc(keyboard)
glutMainLoop()
