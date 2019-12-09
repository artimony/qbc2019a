import math
import numpy as np
#from scipy.integrate import odeint
print('Starting')
T = 3
#CONSTS
x = 0.
th = 0.
TIMESTEP = 0.01
L0, k = 0.3, 40.
m = 0.3
g = 9.81

thd = thdd = xd = xdd = 0

def getxdd():
    return (L0 + x)* thd * thd - k * x / m + g * np.cos(th)
def getthdd():
    return -g*np.sin(th)-2*xd*thd/(L0 + x)

for t in np.arange(0, T, TIMESTEP):
    print('X, XD, XDD; TH, THD, THDD = '+str(x)+' '+str(xd)+' '+str(xdd)+' '+str(th)+' '+str(thd)+' '+str(thdd)+' ')
    thdd = getthdd()
    xdd = getxdd()
    th += thd * TIMESTEP
    x += xd * TIMESTEP
    thd += thdd * TIMESTEP
    xd += xdd * TIMESTEP