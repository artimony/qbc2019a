#include "qbclib.h"

void drawvec(struct Vec2 *v)
{
    glVertex2f(v->x / 2, v->y / 2);
}

void drawved(struct Vec2 *v)
{
    drawvec(v);
    printvec(v);
}
