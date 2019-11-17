#include "lib/qbclib.h"

struct Vec2 ORIGIN;

void display()
{
    deb("start draw");
    int t, gtime;
    struct Vec2 *v = malloc(sizeof(v));
    v->x = 1.0f;
    v->y = 1.0f;
    printvec(v);
    printvec(v);
    for (t = 0; t < 10000; t++) {

        drotate(v, ORIGIN, 0.0625f);

        glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);

        gtime = time(NULL) % 10;
        glBegin(GL_QUADS);
        glColor3f(gtime % 2 / 2.1f + 0.1f, gtime % 4 / 4.1f + 0.1f,
              gtime % 4 / 4.1f + 0.1f);
        drawvec(v);
        drotate(v, ORIGIN, 90);
        drawvec(v);
        drotate(v, ORIGIN, 90);
        drawvec(v);
        drotate(v, ORIGIN, 90);
        drawvec(v);
        drotate(v, ORIGIN, 90);
        glEnd();

        glFlush();
    }
}

int main(int argc, char **argv)
{
    ORIGIN = getOrigin();
    struct Vec2 est = getOrigin();
    struct Vec2 *test = &est;
    struct Vec2 *notTest;
    notTest = malloc(sizeof(notTest));
    int k;
    notTest->x = 1;
    notTest->y = 1;
    printvec(test);
    for (k = 0; k < 4; k++) {
	printvec(notTest);
	drotate(notTest, ORIGIN, 90);
    }
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE);
    glutInitWindowSize(WIDTH, HEIGHT);
    glutInitWindowPosition(100, 100);
    glutCreateWindow(PROJECT_NAME);
    glutDisplayFunc(display);
    glutMainLoop();
    return 0;
}
