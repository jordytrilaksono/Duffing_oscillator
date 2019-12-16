# Duffing (Scipy Odeint)

from scipy.integrate import odeint
import numpy as np
#import matplotlib.pyplot as plt

from duffing import duffing

# parameters
#alpha, beta, gamma, delta, omega, theta = 1, -1, 0.3, 0.2, 1, 0
alpha, beta, gamma, delta, omega, theta = -1, 1, 0.6, 0.3, 1.5, 0
ncycle = 3000    #number of cycle (number of points in poincare map)
nitt = 100       #number of time step for each cycle

# initial conditions
var = np.array([0.,1.])
#poincare = np.array([0.,1.])

# Time steps
period = 2*np.pi/omega
#periods = np.arange(0., 20000., period)
t = np.arange(0, ncycle*period, period/nitt)

# Solver
var = odeint(duffing, var, t, args=(alpha, beta, gamma, delta, omega, theta))
var = var.T

#output data
outdata = np.vstack((t, var)).T
np.savetxt("duffing.csv", outdata, delimiter=",")

#poincare = odeint(duffing, poincare, periods, args=(alpha, beta, gamma, delta, omega, theta))
'''
var = var.T

print("ODE has been solved.")

tsplit = t.reshape(ncycle, nitt)
xsplit = var[0].reshape(ncycle, nitt)
vsplit = var[1].reshape(ncycle, nitt)
xsplit = xsplit.T
vsplit = vsplit.T

plt.plot(xsplit[2], vsplit[2], '.')

plt.show()
'''
