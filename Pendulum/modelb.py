#A model for 3D small angle movement
import math, csv
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

print('3D small angle Cartesian coordinate model for QBC 2019a')
print('theory - P. Lynch, coder - A. Khrapov')

def get_r(x, y, z):
    return math.sqrt(x^2+y^2+z^2)

def get_ax(x):

    pass

def run_test(T, x, y, z, vx, vy, vz, TIMESTEP, L0, k, freq, m, g = 9.81, SIZE = 2.5, gif = 'pendulumB.gif'):
    ax = ay = az = 0

    

    pass

def run_test_stop(T, x, y, z, TIMESTEP, L0, k, freq, m, g = 9.81):
    run_test(T, x, y, z, 0, 0, 0, TIMESTEP, L0, k, freq, m, g)



with open('configB.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
        else:
            print(f'\tTest {line_count}:\n\tx(sm) = {row[0]}; y(sm) = {row[1]}; z(sm) = {row[2]};')
            print(f'\tvx = {row[3]}; vy = {row[4]}; vz(sm) = {row[5]};')
            print(f'\tL(m) = {row[6]}; k(N/m) = {row[7]}; m(kg) = {row[8]}; g(m/s^2) = {row[9]};')
            print(f'\tsize = {row[10]}; step = {row[11]}; freq = {row[12]}; duration(s) = {row[13]};')

            print(f'Running test {line_count}')
            run_test(row[13], row[0], row[1], row[2], row[3], row[4], row[5], row[11], row[6], row[7], row[12], row[8], row[9], row[10], f'pendulumB{line_count}.gif')

        line_count += 1
    print(f'Processed {line_count} lines.')
    if line_count == 0:
        print(f'NO test were found. Aborting.')
        csv_file.close()
        with open('configB.csv', 'x') as fileD:
            fileD.write('x(sm);y(sm);z(sm);vx(sm/s);vy(sm/s);vz(sm/s);L(m);k(N/m);m(kg);g(m/s^2);size;step(s);frequency;duration(s);')
            fileD.close()
            print(f'Template file created.')
        exit()
    csv_file.close()
    print(f'Found {line_count-1} tests.')
