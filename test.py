from mayavi import mlab
import vtk

currfig = mlab.test_plot3d()
mlab.orientation_axes()
#mlab.draw()

cam = currfig.scene.camera
cam.zoom(1.5)
#mlab.draw()

mlab.show()
