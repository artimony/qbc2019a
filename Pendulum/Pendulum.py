import math
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import csv
print('Initialization...')
#########################################################################
###INSERTION

#CSV start

with open('config.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
    if line_count == 0:
        print(f'NO test were found. Aborting.')
        exit()
    print(f'Found {line_count-1} tests.')

    


T = 4
#CONSTS
x = 0.
th = 0.5
TIMESTEP = 0.001
L0, k = 2., 5.
freq = 20*2
m = 0.2
g = 9.81

thd = thdd = xd = xdd = 0
#Funcs
def getxdd():
    return (L0 + x)* thd * thd - k * x / m + g * np.cos(th)
def getthdd():
    return -g*np.sin(th)-2*xd*thd/(L0 + x)

def fpolar(length, circle, phi):
    lineData = np.empty(3)
    lineData[0] = length * np.sin(phi) * np.cos(circle)
    lineData[1] = length * np.sin(phi) * np.sin(circle)
    lineData[2] = length * np.cos(phi)
    return lineData
###/INSERTION
#########################################################################

print('est. pendulum frequency: '+str(np.sqrt(g/L0)/(2*np.pi))+' Hz')
print('est. spring frequency: '+str(np.sqrt(k/m)/(2*np.pi))+' Hz')
print('est. frequency ratio: '+str(np.sqrt(g*m/(L0*k))))

#CONST VALUES
SIZE = 2.5

#SETUP
fig = plt.figure()
ax = p3.Axes3D(fig)
print('Setting up the graph with the size of '+str(SIZE)+' meters')

STEPMAX = math.floor(T/TIMESTEP)
datax = np.empty((STEPMAX, 2))

print('Starting data generation for the plot, '+str(STEPMAX)+' entries to be generated')
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

# Setting the axes properties
ax.set_xlim3d([-SIZE, SIZE])
ax.set_xlabel('X')

ax.set_ylim3d([-SIZE, SIZE])
ax.set_ylabel('Y')

ax.set_zlim3d([SIZE, 0])
ax.set_zlabel('Z')

title = ax.text(0.5,0.85, 0.0, "", bbox={'facecolor':'w', 'alpha':0.5, 'pad':5},
                transform=ax.transAxes, ha="left")
line, = ax.plot([], [], [])

def init():
    line.set_data([], [])
    line.set_3d_properties([])
    return line,

def drawsphere(x0, y0, z0, r):
    ax.scatter([x0], [y0], [z0], color="r", s=25)

def update_lines(num, data, time, f):
    title.set_text("Время = {0:.2f} с".format(num * time*f))
    data1 = fpolar(L0 + data[num*f, 0], 0, np.sin(data[num*f, 1]))
    drawsphere(data1[0], data1[1], data1[2], 0.01)
    line.set_data([0, data1[0]], [0, data1[1]])
    line.set_3d_properties([0, data1[2]])
    return line, title

#STEPMAX = 100
line_ani = animation.FuncAnimation(fig, update_lines, init_func=init, frames=int(STEPMAX/freq), fargs=(datax, TIMESTEP, freq), interval=TIMESTEP * 1000*freq, blit=True)
print('Starting rendering the result')
#line_ani.save('pendulum.gif', writer='imagemagick', progress_callback =\
#                    lambda i, n: print(f'Saving frame {i} of {n}'))
print('finished')
plt.show()

