
import viz
import vizconnect
import vizcave 

# Declare constants 
C0 = 0,6,0   # Front  Wall: C1,C2,C5,C6 
C1 = 0,6,8   # Left   Wall: C0,C1,C4,C5 
C2 = 8,6,8   # Right  Wall: C2,C3,C6,C7 
C3 = 8,6,0   # Bottom Wall: C5,C6,C4,C7 
C4 = 0,0,0 
C5 = 0,0,8 
C6 = 8,0,8 
C7 = 8,0,0

#Create front wall 
FrontWall = vizcave.Wall(   upperLeft=C1, 
                            upperRight=C2, 
                            lowerLeft=C5, 
                            lowerRight=C6, 
                            name='Front Wall' ) 

cave = vizcave.Cave()
cave.addWall(FrontWall, mask=viz.MASTER)


viz.window.setFullscreenMonitor(1)
viz.window.setFullscreen(viz.ON)
vizconnect.go('test_projection_config.py')


viz.vsync(viz.ON)

#viz.MainWindow.setStereoSwap(viz.TOGGLE)

piazza = viz.addChild('piazza.osgb')
