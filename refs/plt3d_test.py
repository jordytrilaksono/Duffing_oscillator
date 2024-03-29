from scipy.integrate import odeint
import numpy as np
import vtk
from mayavi import mlab

#parameters
ncycle = 3000
nitt = 100
n = int(ncycle*nitt/100)

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

phase = t*omega
x = (2.+data[0])*np.cos(phase)
y = (2.+data[0])*np.sin(phase)
z = data[1]

#mlab.plot3d([0.,0.], [0.,0.], [-2.,2.])#np.zeros(5), np.zeros(5), np.linspace(-2,2,5))
#ax_z.mlab_source.update()
mlab.figure(size=(1200,1050), bgcolor=(0,0,0), fgcolor=(1,1,1))
mlab.plot3d(x[:n], y[:n], z[:n], t[:n], colormap='Blues')
#https://qiita.com/RyoNu/items/02a6df4118a6fa798485
mlab.orientation_axes()

# crosssection
phase = np.pi/2/2 * 0
x_ph  = np.cos(phase)*4.
y_ph  = np.sin(phase)*4.
x     = np.sort(np.linspace(0., x_ph, 3))
y     = np.sort(np.linspace(0., y_ph, 3))
xx, zz = np.meshgrid(x, [-2.,2.])
#print(np.mgrid[0.:x_ph:x_ph/3, -2.:2.:4./3])
#yy = np.tan(phase)*xx
yy = np.array([y, y])
#print(np.linspace(0, -2, 4))
print(xx.T)
print(yy.T)
print(zz.T)
print(np.linspace(0, -2, 5))
#xx = np.array([[-4, 0.],[-4., 0.]])

cs = mlab.surf(xx.T, np.sort(yy).T, zz.T, color=(1,1,1), opacity=1)




#cs.actor.actor.rotate_z(180)

# Output path for you animation images
out_path = './'
#out_path = os.path.abspath(out_path)
fps = 20
prefix = 'ani'
ext = '.png'

padding = len(str(nitt))

delay = int(10000/nitt)

@mlab.animate(delay=delay, ui=True, support_movie=True)
def anim():
    for i in range(nitt*1):
        dangle = 1/nitt *360
        cs.actor.actor.rotate_z(dangle)

        # create zeros for padding index positions for organization
        zeros = '0'*(padding - len(str(i)))

        # concate filename with zero padded index number as suffix
        filename = os.path.join(out_path, '{}_{}{}{}'.format(prefix, zeros, i, ext))
        mlab.savefig(filename=filename)

        yield

#mlab.start_recording(ui=True)
anim()
mlab.show()
#mlab.stop_recording(file='avi.py')

#@mlab.animate(delay=50)
#def anim():
#    for i in range(nitt*10):
#        phase = 2.*np.pi*(i+1)/100
#        x_ph  = np.cos(phase)*4.
#        y_ph  = np.sin(phase)*4.
        #xx, zz = np.meshgrid(np.sort([0, x_ph]), [-2,2])
        #xx    = np.sort(np.array([[0., x_ph], [0., x_ph]]))
        #yy    = np.sort(np.tan(phase)*xx)
#        xx, zz = np.meshgrid([0, x_ph], [-2,2])
        #yy     = np.tan(phase)*xx
#        yy     = np.array([[0, y_ph], [0, y_ph]])
#        cs.mlab_source.trait_set(x=xx.T, y=yy.T)
        #mlab.gcf().scene.reset_zoom()
#        yield

#anim()

#mlab.show()

import subprocess
#ffmpeg_fname = os.path.join(out_path, '{}_%0{}d{}'.format(prefix, padding, ext))
#cmd = 'ffmpeg -f image2 -r {} -i {} -vcodec mpeg4 -y {}.mp4'.format(fps,
#                                                                    ffmpeg_fname,
#                                                                    prefix)
#print(cmd)
#subprocess.check_output(['bash','-c', cmd])
cmd = ['convert', '-delay', str(int(delay/10)), '-loop', '0', '*'+ext, 'anim.gif']#.format(delay/10, ext, prefix)
cmd = ['convert', '-delay', '10', '-loop', '0', '*'+ext, 'anim.gif']#.format(delay/10, ext, prefix)
cmd = 'convert -delay {} -loop 0 *{} {}.gif'.format(str(int(delay/10)), ext, prefix)
print(cmd)
subprocess.run(cmd)
#subprocess.check_output(cmd)

# Remove temp image files with extension
#[os.remove(f) for f in os.listdir(out_path) if f.endswith(ext)]
