# Recorded script from Mayavi2
from numpy import array
try:
    engine = mayavi.engine
except NameError:
    from mayavi.api import Engine
    engine = Engine()
from mayavi.core.engine import Engine
engine = Engine()
    engine.start()
if len(engine.scenes) == 0:
    engine.new_scene()
# ------------------------------------------- 
# scene.scene.light_manager = <tvtk.pyface.light_manager.LightManager object at 0x0000025275983410>
surface1 = engine.scenes[0].children[1].children[0].children[0].children[0].children[0]
surface1.actor.actor.orientation = array([ 0. , -0. ,  3.6])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 0.0001
surface1.actor.actor.render_time_multiplier = 0.23685105174774976
surface1.actor.actor.reference_count = 3
surface1.actor.actor.orientation = array([ 0. , -0. ,  7.2])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 4.066999827045947e-05
surface1.actor.actor.render_time_multiplier = 0.23853670019993292
surface1.actor.actor.orientation = array([ 0. , -0. , 10.8])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.24012254322987722
surface1.actor.actor.orientation = array([ 0. , -0. , 14.4])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 6.872399535495788e-05
surface1.actor.actor.render_time_multiplier = 0.241598947408763
surface1.actor.actor.orientation = array([ 0., -0., 18.])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.24295673843799076
surface1.actor.actor.orientation = array([ 0. , -0. , 21.6])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 5.826599954161793e-05
surface1.actor.actor.render_time_multiplier = 0.2441873032542479
surface1.actor.actor.orientation = array([ 0. , -0. , 25.2])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.24528268974916262
surface1.actor.actor.orientation = array([ 0. , -0. , 28.8])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 5.751899880124256e-05
surface1.actor.actor.render_time_multiplier = 0.24623570208325207
surface1.actor.actor.orientation = array([ 0. , -0. , 32.4])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.2470399895693637
surface1.actor.actor.orientation = array([ 0., -0., 36.])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 4.656300006899983e-05
surface1.actor.actor.render_time_multiplier = 0.2476901271603004
surface1.actor.actor.orientation = array([ 0. , -0. , 39.6])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.24818168570038981
surface1.actor.actor.orientation = array([ 0. , -0. , 43.2])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 3.6022000131197274e-05
surface1.actor.actor.render_time_multiplier = 0.24851129028999533
surface1.actor.actor.orientation = array([ 0. , -0. , 46.8])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.24867666536082944
surface1.actor.actor.orientation = array([ 0. , -0. , 50.4])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 2.6559999241726473e-05
surface1.actor.actor.render_time_multiplier = 0.24867666536082955
surface1.actor.actor.orientation = array([ 0., -0., 54.])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.24851129028999533
surface1.actor.actor.orientation = array([ 0. , -0. , 57.6])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 3.436199767747894e-05
surface1.actor.actor.render_time_multiplier = 0.24818168570038993
surface1.actor.actor.orientation = array([ 0. , -0. , 61.2])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.2476901271603005
surface1.actor.actor.orientation = array([ 0. , -0. , 64.8])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 3.959099922212772e-05
surface1.actor.actor.render_time_multiplier = 0.24703998956936354
surface1.actor.actor.orientation = array([ 0. , -0. , 68.4])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.24623570208325207
surface1.actor.actor.orientation = array([ 0., -0., 72.])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 9.17149955057539e-05
surface1.actor.actor.render_time_multiplier = 0.24528268974916262
surface1.actor.actor.orientation = array([ 0. , -0. , 75.6])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.24418730325424778
surface1.actor.actor.orientation = array([ 0. , -0. , 79.2])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 5.743599831475876e-05
surface1.actor.actor.render_time_multiplier = 0.24295673843799062
surface1.actor.actor.orientation = array([ 0. , -0. , 82.8])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.24159894740876306
surface1.actor.actor.orientation = array([ 0. , -0. , 86.4])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 6.274799670791253e-05
surface1.actor.actor.render_time_multiplier = 0.24012254322987728
surface1.actor.actor.orientation = array([ 0., -0., 90.])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.23853670019993292
surface1.actor.actor.orientation = array([ 0. , -0. , 93.6])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 7.436799933202565e-05
surface1.actor.actor.render_time_multiplier = 0.2368510517477498
surface1.actor.actor.orientation = array([ 0. , -0. , 97.2])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.235075587898
surface1.actor.actor.orientation = array([  0. ,  -0. , 100.8])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 7.287399785127491e-05
surface1.actor.actor.render_time_multiplier = 0.23322055414638987
surface1.actor.actor.orientation = array([  0. ,  -0. , 104.4])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.23129635342126817
surface1.actor.actor.orientation = array([  0.,  -0., 108.])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 7.544699474237859e-05
surface1.actor.actor.render_time_multiplier = 0.22931345261138747
surface1.actor.actor.orientation = array([  0. ,  -0. , 111.6])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.orientation = array([  0. ,  -0. , 115.2])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.22521321904668765
surface1.actor.actor.orientation = array([  0. ,  -0. , 118.8])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.orientation = array([  0. ,  -0. , 122.4])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 7.909899431979284e-05
surface1.actor.actor.render_time_multiplier = 0.22100171420392306
surface1.actor.actor.orientation = array([  0.,  -0., 126.])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.21887882264615507
surface1.actor.actor.orientation = array([  0. ,  -0. , 129.6])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 8.059299580054358e-05
surface1.actor.actor.render_time_multiplier = 0.21675698320490389
surface1.actor.actor.orientation = array([  0. ,  -0. , 133.2])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.21464508098806684
surface1.actor.actor.orientation = array([  0. ,  -0. , 136.8])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 8.407899440499023e-05
surface1.actor.actor.render_time_multiplier = 0.21255158308334093
surface1.actor.actor.orientation = array([  0. ,  -0. , 140.4])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.21048451510686472
surface1.actor.actor.orientation = array([  0.,  -0., 144.])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 8.175499533535913e-05
surface1.actor.actor.render_time_multiplier = 0.20845144507712773
surface1.actor.actor.orientation = array([  0. ,  -0. , 147.6])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.2064594740251606
surface1.actor.actor.orientation = array([  0. ,  -0. , 151.2])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 7.685799937462434e-05
surface1.actor.actor.render_time_multiplier = 0.20451523269268698
surface1.actor.actor.orientation = array([  0. ,  -0. , 154.8])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.20262488363360756
surface1.actor.actor.orientation = array([  0. ,  -0. , 158.4])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 7.287399785127491e-05
surface1.actor.actor.render_time_multiplier = 0.20079412801831859
surface1.actor.actor.orientation = array([  0.,  -0., 162.])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.19902821644213106
surface1.actor.actor.orientation = array([  0. ,  -0. , 165.6])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 7.660899427719414e-05
surface1.actor.actor.render_time_multiplier = 0.19733196305547923
surface1.actor.actor.orientation = array([  0. ,  -0. , 169.2])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.19570976236179202
surface1.actor.actor.orientation = array([  0. ,  -0. , 172.8])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 9.4038994575385e-05
surface1.actor.actor.render_time_multiplier = 0.19416560806605243
surface1.actor.actor.orientation = array([  0. ,  -0. , 176.4])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.19270311340062957
surface1.actor.actor.orientation = array([  0.,  -0., 180.])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 6.13369993516244e-05
surface1.actor.actor.render_time_multiplier = 0.19132553240263625
surface1.actor.actor.orientation = array([   0. ,   -0. , -176.4])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.1900357816668524
surface1.actor.actor.orientation = array([   0. ,   -0. , -172.8])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 6.374399526976049e-05
surface1.actor.actor.render_time_multiplier = 0.18883646214848476
surface1.actor.actor.orientation = array([   0. ,   -0. , -169.2])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.18772988063933338
surface1.actor.actor.orientation = array([   0. ,   -0. , -165.6])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 5.378399873734452e-05
surface1.actor.actor.render_time_multiplier = 0.1867180705882568
surface1.actor.actor.orientation = array([   0.,   -0., -162.])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.18580281198136017
surface1.actor.actor.orientation = array([   0. ,   -0. , -158.4])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 5.2704999689012766e-05
surface1.actor.actor.render_time_multiplier = 0.1849856500385541
surface1.actor.actor.orientation = array([   0. ,   -0. , -154.8])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.18426791252070931
surface1.actor.actor.orientation = array([   0. ,   -0. , -151.2])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 4.158299998380244e-05
surface1.actor.actor.render_time_multiplier = 0.18365072547544023
surface1.actor.actor.orientation = array([   0. ,   -0. , -147.6])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.18313502727961647
surface1.actor.actor.orientation = array([   0.,   -0., -144.])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 3.793100040638819e-05
surface1.actor.actor.render_time_multiplier = 0.18272158086317197
surface1.actor.actor.orientation = array([   0. ,   -0. , -140.4])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.18241098402193465
surface1.actor.actor.orientation = array([   0. ,   -0. , -136.8])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 3.4527998650446534e-05
surface1.actor.actor.render_time_multiplier = 0.18220367774737234
surface1.actor.actor.orientation = array([   0. ,   -0. , -133.2])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.render_time_multiplier = 0.18209995251875666
surface1.actor.actor.orientation = array([   0. ,   -0. , -129.6])
surface1.actor.actor.origin = array([0., 0., 0.])
surface1.actor.actor.position = array([0., 0., 0.])
surface1.actor.actor.scale = array([1., 1., 1.])
surface1.actor.actor.estimated_render_time = 2.5563998860889114e-05
surface1.actor.actor.render_time_multiplier = 0.1820999525187566
