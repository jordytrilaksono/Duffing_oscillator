# Duffing (Scipy Odeint)

from scipy.integrate import odeint
import numpy as np
#import matplotlib.pyplot as plt

from duffing import duffing
from animate import *

#global alpha, beta, gamma, delta, omega, theta
#global ncycle, nitt
#global var, t

# parameters
alpha, beta, gamma, delta, omega, theta = 1., -1., 0.6, -0.3, 1.5, 0.
ncycle = 3000    #number of cycle (number of points in poincare map)
nitt = 100       #number of time step for each cycle

# initial conditions
var = np.array([0.,1.])

# Time steps
period = 2*np.pi/omega
t = np.arange(0, ncycle*period, period/nitt)

# Solver
var = odeint(duffing, var, t, args=(alpha, beta, gamma, delta, omega, theta))
var = var.T

animate(var, t, alpha, beta, gamma, delta, omega, theta, ncycle, nitt)

#output data
#outdata = np.vstack((t, var)).T
#np.savetxt("duffing.csv", outdata, delimiter=",")
