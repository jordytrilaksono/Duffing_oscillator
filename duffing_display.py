import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import pandas as pd

#parameters
ncycle = 3000
nitt = 100

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

#declaring figure
fig = plt.figure()
ax = fig.add_subplot(111)

#x,y limits
xmin = np.floor(data[0].min())
xmax = np.ceil(data[0].max())
ymin = np.floor(data[1].min())
ymax = np.ceil(data[1].max())

#list of frames
def update(frame):
    ax.cla()
    ax.set_title('Poincare section of Duffing oscillator \n $\ddot{x}=-0.3\dot{x}+x-x^3+0.6\,\cos(1.5t) \quad \phi=%.2f\pi$' %(frame*2/nitt), fontsize=13)
    ax.set_xlabel('position', fontsize=13)
    ax.set_ylabel('velocity', fontsize=13)
    ax.set_xlim(xmin,xmax)
    ax.set_ylim(ymin,ymax)
    ax.plot(xsplit[frame], vsplit[frame], '.', markersize=1, color="black")

ani = animation.FuncAnimation(fig, update, nitt, interval=50)
ani.save('duffing.gif', writer="imagemagick")

plt.show()
