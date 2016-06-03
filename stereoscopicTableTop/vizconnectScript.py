vrpn = viz.add('vrpn7.dle') 

#uses name from the vrpn.cfg file where vrpn server runs.
tracker1 = vrpn.addTracker('Tracker0@localhost') #Default sensor is 0 

#tracker2 = vrpn.addTracker('Tracker0@localhost',1)