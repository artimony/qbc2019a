/**
 * Vector in 2D
 * */
struct Vec2{
    float x;
    float y;
};

#define PI 3.141592

struct Vec2 getOrigin(void);

void deb(char*);
int printvec(struct Vec2*);


void rotate(struct Vec2*, struct Vec2, float);
void drotate(struct Vec2*, struct Vec2, float);
