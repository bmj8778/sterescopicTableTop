#Test file for displaying sterescopic scene using the rear projection setup.

import viz

viz.window.setFullscreenMonitor(2)
viz.go(viz.QUAD_BUFFER)

viz.window.setFullscreen(viz.ON)

#viz.MainWindow.setStereoSwap(viz.TOGGLE)

piazza = viz.addChild('piazza.osgb')
