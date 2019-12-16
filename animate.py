import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import vtk
from mayavi import mlab

global alpha, beta, gamma, delta, omega, theta
global ncycle, nitt
global var, t

'''
#parameters
ncycle = 3000
nitt = 100
omega = 1.5

alpha, beta, gamma, delta, omega, theta = 1., -1., 0.6, -0.3, 1.5, 0.

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
'''

def label(alpha, beta, gamma, delta, omega, theta):
    c = [delta, alpha, beta, gamma, omega, theta]
    x = ['\dot{x}', 'x', 'x^3', '\,\cos(', 't', '']
    for i in range(6):
        temp = str(c[i])
        if c[i] == 1.:
            temp = ''
        elif c[i] == -1.:
            temp = '-'

        if (i != 0) & (i != 4) & (c[i] > 0):
            temp = '+' + temp

        if c[i] == 0.:
            temp = 'zero'

        c[i] = temp

    label = ''
    for i in range(6):
        if c[i] == 'zero':
            x[i] = ''
        else:
            x[i] = c[i] + x[i]

        label += x[i]

    label = '$\ddot{x}=' + label + ') \quad \phi='

    return label


def animate(var, t, alpha, beta, gamma, delta, omega, theta, ncycle, nitt):

    n = int(ncycle*nitt/10)

    # processing data into poincare map compatibles
    tsplit = t.reshape(ncycle, nitt)
    xsplit = var[0].reshape(ncycle, nitt)
    vsplit = var[1].reshape(ncycle, nitt)
    xsplit = xsplit.T
    vsplit = vsplit.T

    #x,y limits
    xmin = np.floor(var[0].min())
    xmax = np.ceil(var[0].max())
    ymin = np.floor(var[1].min())
    ymax = np.ceil(var[1].max())

    # 3d plot
    phase = t*omega
    x = (2.+var[0])*np.cos(phase)
    y = (2.+var[0])*np.sin(phase)
    z = var[1]

    # 3D plot w/ Mayavi
    plt3d = []
    fig = mlab.figure(size=(1200,1050), bgcolor=(0,0,0), fgcolor=(1,1,1))

    mlab.plot3d(x[:n], y[:n], z[:n], t[:n], colormap='Blues')
    ox = mlab.orientation_axes()
    ox.marker.set_viewport(0,0,0.3,0.3)

    # crosssection
    xx, zz = np.meshgrid([0., xmax-xmin], [ymin, ymax])
    yy = 0*xx
    cs = mlab.surf(xx.T, yy.T, zz.T, color=(1,1,1), opacity=1)

    cam = fig.scene.camera
    cam.zoom(1.5)

    for i in range(nitt):
        if i != 0:
            cs.actor.actor.rotate_z(360/nitt)
        f = mlab.gcf()
        f.scene._lift()
        plt3d.append(mlab.screenshot())
    mlab.close()

    # Matplolib figure initialization
    plt.style.use('dark_background')
    fig, ax = plt.subplots(nrows=1, ncols=2, dpi=100, figsize=(11,5))

    # Animation
    def update(frame):
        ax[0].cla()
        ax[1].cla()

        ax[0].imshow(plt3d[frame], interpolation='spline16')
        ax[0].set_axis_off()

        ax[1].set_title('Poincare section of Duffing oscillator \n' + \
                         label(alpha, beta, gamma, delta, omega, theta) + \
                         '%.2f\pi$' %(frame*2/nitt), fontsize=11)
        ax[1].set_xlabel('position', fontsize=13)
        ax[1].set_ylabel('velocity', fontsize=13)
        ax[1].set_xlim(xmin,xmax)
        ax[1].set_ylim(ymin,ymax)
        ax[1].plot(xsplit[frame], vsplit[frame], '.', markersize=1, color="white")
        ax[1].set_aspect('equal')

    ani = animation.FuncAnimation(fig, update, nitt, interval=50)
    ani.save('duffing.gif', writer="imagemagick")
