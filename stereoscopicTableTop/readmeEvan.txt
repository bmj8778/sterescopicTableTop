README for Evan

As far as code repo goes I have currently been editing files at this repo 

(https://github.com/bmj8778/sterescopicTableTop)

This includes the project (development branch) from Erik (https://github.com/erikmessier/anatomy-puzzle/tree/development)

You may have to use code from the preformlabrit private repos, Gabe can easily add you if he has your github info.

You may want to ask Cristian/Gabe where the code should live. Using the repo on my page is fine but feel free to copy it to wherever might be more accessible (and controllable) for you/the other reu student.

Erik mentioned he could help out with understanding the game code a bit, I only looked at it for a minimal amount of time.

I've only really been editing through Vizard and the repo is located on this pc at

C:\Users\PerForMLab\Documents\GitHub\stereoscopicTableTop

Note that in the documents folder are the other github repos checked out on this machine, so I likely should have placed it there instead. To commit code I usually open the Github GUI (just run the application from windows search in bottom left) and then click settings in the top right and open a git terminal (which is actually just a windows powershell that already has the github user info). I will log out when I leave, so if you want to log in you can through the settings/options in the top right of the github GUI. I like the shell and I also don't think the GUI currently sees my repo.

For vrpn I have the source checked out and started working on building until Gabe reccomended getting the binaries. These folders are both in 

Libraries\Documents

vrpn-master is the source, and vrpn-windows-binaries-master is the binary files. Within the build folder there is the vrpn.cfg and vrpn_server.exe you will need when the tracker is hooked up. (Note: we also need a usb hub for this PC).

The bookmarks in chrome have some helpful links, a few vizard tutorials about the vrpn plugin and also a short vrpn tutorial for testing with a mouse. I believe we will only have to run the vrpn_server.exe and modify the vrpn.cfg files (once) to get the tracker available to add for vizconnect. Then as far as vizard knows the tracker object is a generic vrpn tracker. Not sure what the configuration file stuff will entail however.


