import math
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import csv
print('Initialization...')
#########################################################################
###INSERTION

T = 2
#CONSTS
x = 0.
th = 0.5
TIMESTEP = 0.01
L0, k = 0.3, 40.
m = 0.3
g = 9.81

thd = thdd = xd = xdd = 0

def getxdd():
    return (L0 + x)* thd * thd - k * x / m + g * np.cos(th)
def getthdd():
    return -g*np.sin(th)-2*xd*thd/(L0 + x)
STEPMAX = math.floor(T/TIMESTEP)
datax = np.empty((STEPMAX, 2))
print('Starting data generation for the graph, '+str(STEPMAX)+' entries to be generated')
for t in range(0, STEPMAX):
    datax[t, 0] = x
    datax[t, 1] = th
    #print('X, XD, XDD; TH, THD, THDD = '+str(x)+' '+str(xd)+' '+str(xdd)+' '+str(th)+' '+str(thd)+' '+str(thdd)+' ')
    thdd = getthdd()
    xdd = getxdd()
    th += thd * TIMESTEP
    x += xd * TIMESTEP
    thd += thdd * TIMESTEP
    xd += xdd * TIMESTEP
print('data generated')
###/INSERTION
#########################################################################

#CONST VALUES
SIZE = 0.5

#TIMESTEP = 1/28. #1sec DINIT?
#Pendulum creation
def fpolar(length, circle, phi):
    lineData = np.empty(3)
    lineData[0] = length * np.sin(phi) * np.cos(circle)
    lineData[1] = length * np.sin(phi) * np.sin(circle)
    lineData[2] = length * np.cos(phi)
    return lineData
#LOAD DATA

#data = fpolar(0.3, 1, 1)

#SETUP
print('Setting up the graph with the size of '+str(SIZE)+' meters')
fig = plt.figure()
ax = p3.Axes3D(fig)
# Setting the axes properties
ax.set_xlim3d([-SIZE, SIZE])
ax.set_xlabel('X')

ax.set_ylim3d([-SIZE, SIZE])
ax.set_ylabel('Y')

ax.set_zlim3d([SIZE, 0])
ax.set_zlabel('Z')

#ax.set_title('Время = 0 с')

def drawsphere(x0, y0, z0, r):
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = np.cos(u)*np.sin(v)*r*0.9 + x0
    y = np.sin(u)*np.sin(v)*r*0.9 + y0
    z = np.cos(v)*r/2 + z0
    ax.plot_wireframe(x, y, z, color="r")

def update_lines(num, data, i):
    #ax.set_title('Время = '+str(num * TIMESTEP)+' с')
    #data1 = fpolar(L0, 0, np.sin(num))
    data1 = fpolar(L0 + data[num, 0], 0, np.sin(data[num, 1]))
    drawsphere(data1[0], data1[1], data1[2], 0.01)
    line, = ax.plot([0, data1[0]], [0, data1[1]], [0, data1[2]])
    return line,

#ax.plot([0, data[0]], [0, data[1]], [0, data[2]])
#drawsphere(data[0], data[1], data[2], 0.03)
#lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]
#plt.plot(lines) fargs=(datax)

line_ani = animation.FuncAnimation(fig, update_lines, STEPMAX, fargs=(datax, 0), interval=100, blit=True)
print('Starting rendering the result')
#line_ani.save('pendulum.gif')
plt.show()