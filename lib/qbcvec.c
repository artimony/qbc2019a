#include <stdio.h>
#include <math.h>
#include "qbcvec.h"


/**Origin vector
 *  Do not change!*/
struct Vec2 ORIGIN_0 = { 0, 0 };

struct Vec2 getOrigin(void)
{
    return ORIGIN_0;
}

/**
 * Fast output for debugging
 * */
void deb(char *str)
{
    printf("%s", str);
}

/**
 * Prints vector's coordinates {x, y}
 **/
int printvec(struct Vec2 *vec)
{
    return printf("{%lf, %lf}\n", vec->x, vec->y);
}


//Temporary variable for rotation
float t0;


/**
 *  Rotates the vector using a matrix(angle in radians)
 *  Not sure if it's useful because there are built-in functions for it but... who knows?
 **/
void rotate(struct Vec2 *vec, struct Vec2 origin, float angle)
{
    vec->x = vec->x - origin.x;
    vec->y = vec->y - origin.y;
    t0 = vec->x;
    vec->x = vec->x * cos(angle) - vec->y * sin(angle);
    vec->y = t0 * sin(angle) + vec->y * cos(angle);

    vec->x = vec->x + origin.x;
    vec->y = vec->y + origin.y;
}

/**
 *  Rotates the vector using a matrix(angle in degrees)
 **/
void drotate(struct Vec2 *vec, struct Vec2 origin, float angle)
{
    rotate(vec, origin, angle * PI / 180);
}
