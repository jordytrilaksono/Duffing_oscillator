import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import *

#from matplotlib.collections import PolyCollection
#from matplotlib.colors import colorConverter
from matplotlib.patches import FancyArrowPatch, Circle

n = 100
r   = np.ones(n)
phi = np.linspace(0,1,n)*2*np.pi
z   = np.ones(n)*0.5

x = r*np.cos(phi)
y = r*np.sin(phi)

#fig, ax = plt.subplots(nrows=1, ncols=1, projection='3d')

fig = plt.figure()#figsize=(5,8))
ax = fig.add_subplot(111, projection='3d')
#ax.set_aspect('equal')
ax.axis('off')
#ax.set_axis_off()

#Polar axis
p = Circle((0, 0), 1, color='whitesmoke', alpha=0.5, ec=None)
ax.add_patch(p)
art3d.pathpatch_2d_to_3d(p, z=0, zdir="z")

a = 1/np.sqrt(2)
ax.plot([-1,1], [ 0,0], [0,0], c='lightgrey', zorder=-1)
ax.plot([ 0,0], [-1,1], [0,0], c='lightgrey', zorder=-1)
ax.plot([-a,a], [-a,a], [0,0], c='lightgrey', zorder=-1)
ax.plot([-a,a], [a,-a], [0,0], c='lightgrey', zorder=-1)

ax.plot(1.00*x, 1.00*y, 0*z, c='k'        , zorder=-1)
ax.plot(0.50*x, 0.50*y, 0*z, c='lightgrey', zorder=-1)
ax.plot(0.25*x, 0.25*y, 0*z, c='lightgrey', zorder=-1)
ax.plot(0.75*x, 0.75*y, 0*z, c='lightgrey', zorder=-1)

text_options = {'horizontalalignment': 'center',
                'verticalalignment': 'center',
                'fontsize': 14}

ax.text( 1.2,   0, 0,'$0$', **text_options)
ax.text(   0, 1.2, 0,'$\\frac{1}{2}\pi$', **text_options)
ax.text(-1.2,   0, 0,'$\pi$', **text_options)
ax.text(   0,-1.2, 0,'$\\frac{3}{2}\pi$', **text_options)

# crosssection
phase = np.pi/2
x_ph  = np.cos(phase)
y_ph  = np.sin(phase)
xx, zz = np.meshgrid([0, x_ph], [0,1])
ax.plot_surface(xx, np.tan(phase)*xx, zz, alpha=0.5, facecolors='c0')

# For arrows, see
# https://stackoverflow.com/questions/29188612/arrows-in-matplotlib-using-mplot3d
arrowprops = dict(mutation_scale=20, linewidth=2,
arrowstyle='-|>', color='k',
shrinkA=0, shrinkB=0)

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

a = Arrow3D([0,0], [0,0], [0,1], **arrowprops)
ax.add_artist(a)
a = Arrow3D([0,x_ph], [0,y_ph], [0,0], **arrowprops)
ax.add_artist(a)

#phase = 0
#verts = [np.array([(0,0), (1,0), (1,1), (0,1)])]
#poly = PolyCollection(verts, facecolors='C0', alpha=0.5)
#ax.add_collection3d(poly, zs=[0], zdir='y')

ax.plot(0.5*x, 0.5*y, z)

ax.set_zlim(-1,1)

plt.show()
