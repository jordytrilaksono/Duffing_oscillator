import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import pandas as pd

import vtk
from mayavi import mlab

#def duffing(var, t, alpha, beta, gamma, delta, omega, theta):

#parameters
ncycle = 3000
nitt = 100
n = int(ncycle*nitt/100)
omega = 1.5

# read output data
df = pd.read_csv('duffing.csv', header=None)

# extract the normalized time
dbTime = df.iloc[:,0].values

# remove time axis
df = df.drop([0], axis=1)

# convert DataFrame into array
data = df.values
data = data.T
del df

# processing data into poincare map compatibles
tsplit = dbTime.reshape(ncycle, nitt)
xsplit = data[0].reshape(ncycle, nitt)
vsplit = data[1].reshape(ncycle, nitt)
xsplit = xsplit.T
vsplit = vsplit.T

# 3d plot
phase = dbTime*omega
x = (2.+data[0])*np.cos(phase)
y = (2.+data[0])*np.sin(phase)
z = data[1]

#mlab.plot3d([0.,0.], [0.,0.], [-2.,2.])#np.zeros(5), np.zeros(5), np.linspace(-2,2,5))
#ax_z.mlab_source.update()
mlab.figure(size=(1200,1050), bgcolor=(0,0,0), fgcolor=(1,1,1))
mlab.plot3d(x[:n], y[:n], z[:n], dbTime[:n], colormap='Blues')
mlab.orientation_axes()
f = mlab.gcf()
f.scene._lift()
plt3d = mlab.screenshot()
mlab.close()

#declaring figure
plt.style.use('dark_background')
fig, ax = plt.subplots(nrows=1, ncols=2, dpi=100, figsize=(13,5))

ax[0].imshow(plt3d)
ax[0].set_axis_off()

#x,y limits
xmin = np.floor(data[0].min())
xmax = np.ceil(data[0].max())
ymin = np.floor(data[1].min())
ymax = np.ceil(data[1].max())

ax[1].set_title('Poincare section of Duffing oscillator \n $\ddot{x}=-0.3\dot{x}+x-x^3+0.6\,\cos(1.5t) \quad \phi=%.2f\pi$' %(0*2/nitt), fontsize=13)
ax[1].set_xlabel('position', fontsize=13)
ax[1].set_ylabel('velocity', fontsize=13)
ax[1].set_xlim(xmin,xmax)
ax[1].set_ylim(ymin,ymax)
ax[1].plot(xsplit[0], vsplit[0], '.', markersize=1, color="white")

fig.tight_layout()

plt.show()

#list of frames
'''
def update(frame):
    ax.cla()
    ax.set_title('Poincare section of Duffing oscillator \n $\ddot{x}=-0.3\dot{x}+x-x^3+0.6\,\cos(1.5t) \quad \phi=%.2f\pi$' %(frame*2/nitt), fontsize=13)
    ax.set_xlabel('position', fontsize=13)
    ax.set_ylabel('velocity', fontsize=13)
    ax.set_xlim(xmin,xmax)
    ax.set_ylim(ymin,ymax)
    ax.plot(xsplit[frame], vsplit[frame], '.', markersize=1, color="white")

ani = animation.FuncAnimation(fig, update, nitt, interval=50)
ani.save('duffing_dark.gif', writer="imagemagick")

plt.show()
'''
