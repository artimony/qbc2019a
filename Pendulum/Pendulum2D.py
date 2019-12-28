import math, os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as maxes
import matplotlib.animation as animation
import csv
print('Initialization...2D')
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

TNUM = 0
if(os.path.isfile(os.path.join('tests2d', 'num.txt'))):
    with open(os.path.join('tests2d', 'num.txt'), 'r') as text_file:
        TNUM = int(text_file.readline())
        text_file.close()
    with open(os.path.join('tests2d', 'num.txt'), 'w') as text_file:
        text_file.write(str(TNUM+1))
        text_file.close()
else:
    with open(os.path.join('tests2d', 'num.txt'), 'x') as text_file:
        text_file.write('0')
        text_file.close()

T = 6
#CONSTS
x = 0.05
th = 26*np.pi/180
TIMESTEP = 0.001
L0, k = 0.102, 13.8
freq = 20*2
m = 0.1
g = 9.81

thd = thdd = xd = xdd = 0
#Funcs
def getxdd():
    return (L0 + x)* thd * thd - k * x / m + g * np.cos(th)
def getthdd():
    return -g*np.sin(th)-2*xd*thd/(L0 + x)

def fpolar(length, phi):
    lineData = np.empty(2)
    lineData[0] = length * np.sin(phi)
    lineData[1] = length * np.cos(phi)
    return lineData
###/INSERTION
#########################################################################

print('est. pendulum frequency: '+str(np.sqrt(g/L0)/(2*np.pi))+' Hz')
print('est. spring frequency: '+str(np.sqrt(k/m)/(2*np.pi))+' Hz')
print('est. frequency ratio: '+str(np.sqrt(g*m/(L0*k))))

#CONST VALUES
SIZE = .50

with open(os.path.join('tests2d', f'params_{TNUM}.csv'), 'x') as fileD:
    fileD.write('x(sm);angle(rad);step(s);frequency;L(m);k(N/m);m(kg);g(m/s^2);size;\n')
    fileD.write(f'{x};{th};{TIMESTEP};{freq};{L0};{k};{m};{g};{SIZE};')
    fileD.close()

#SETUP
fig = plt.figure(1)
ax = plt.gca()

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

plt.figure(2)
ax2 = plt.gca()
plotx = np.empty(STEPMAX)
ploty = np.empty(STEPMAX)
for t in range(0, STEPMAX):
    plotx[t] = t * TIMESTEP
    ploty[t] = datax[t, 0]
ax2.set_xlabel('t Время, с')
ax2.set_ylabel('x Удлинение, м')
ax2.plot(plotx, ploty, 'g')
plt.savefig(os.path.join('tests2d', f'x-t_{TNUM}.png'))

plt.figure(3)
ax2 = plt.gca()
plotx = np.empty(STEPMAX)
ploty = np.empty(STEPMAX)
for t in range(0, STEPMAX):
    plotx[t] = t * TIMESTEP
    ploty[t] = datax[t, 1] * 180 / np.pi
ax2.set_xlabel('t Время, с')
ax2.set_ylabel('th Угол, градусы')
ax2.plot(plotx, ploty, 'b')
plt.savefig(os.path.join('tests2d', f'th-t_{TNUM}.png'))

plt.figure(1)

# Setting the axes properties
ax.set_xlim([-SIZE, SIZE])
ax.set_xlabel('X')

ax.set_ylim([SIZE, 0])
ax.set_ylabel('Z')

title = ax.text(0.5,0.85, "", bbox={'facecolor':'w', 'alpha':0.5, 'pad':5},
                transform=ax.transAxes, ha="left")
line, = ax.plot([], [])

def init():
    line.set_data([], [])
    return line,

def drawsphere(x0, y0, r):
    ax.scatter([x0], [y0], color="r", s=18)

def update_lines(num, data, time, f):
    title.set_text("Время = {0:.2f} с".format(num * time*f))
    data1 = fpolar(L0 + data[num*f, 0], np.sin(data[num*f, 1]))
    drawsphere(data1[0], data1[1], 0.01)
    line.set_data([0, data1[0]], [0, data1[1]])
    return line, title


#PROGRESS BAR
#https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

#STEPMAX = 100
line_ani = animation.FuncAnimation(fig, update_lines, init_func=init, frames=int(STEPMAX/freq), fargs=(datax, TIMESTEP, freq), interval=TIMESTEP * 1000*freq, blit=True)
print('Starting rendering the result. ' + str(int(STEPMAX/freq)) + ' frames')
printProgressBar(0, int(STEPMAX/freq), prefix = 'Progress:', suffix = 'Complete', length = 50)
line_ani.save(os.path.join('tests2d', f'pendulum2D_{TNUM}.gif'), writer='imagemagick', progress_callback =\
                    lambda i, n: printProgressBar(i+1, n, prefix = 'Progress:', suffix = 'Complete', length = 50) 
              #print(f'Saving frame {i} of {n}')
              , metadata = [['comment', T], ['TIMESTEP', TIMESTEP]])
print('finished')
plt.show()