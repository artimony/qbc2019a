#!/bin/bash
echo 'Compiling...'
gcc -Wall -c main.c -c lib/qbclib.c -c lib/qbcvec.c -lm -lglut -lGLU -lGL
echo 'Building...'
gcc -Wall main.o qbclib.o qbcvec.o -o main -lm -lglut -lGLU -lGL
echo 'Done?'
