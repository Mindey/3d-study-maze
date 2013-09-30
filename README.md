3d-study-maze
=============

"The software would allow teachers to design their labyrinth rooms, where each room's walls and doors would be easily editable, and the labyrinth files exportable/sharable, and interconnect into one large maze, with custom rewards in each following room."

Reference: http://www.halfbakery.com/idea/3D_20Study_20Maze 

******************************************************************************

In order to run this program, install Panda3D SDK ( http://www.panda3d.org )
It was developed and tested with Panda3D SDK version 1.8.0.

If you are a Ubuntu 12.04 user, "you can well install Panda's official 11.10 (Oneiric) packages.
All you need is two 11.10 packages -- libcv2.1 and libhighgui2.1, which you can remove once the official builds are up."

******************************************************************************
If you are running Ubuntu 12.04 (64 bit version), you can run this in 4 steps:

1. Install:
http://mindey.com/panda3d/libcv2.1_2.1.0-7build1_amd64.deb

2. Install:
http://mindey.com/panda3d/libhighgui2.1_2.1.0-7build1_amd64.deb

3. Install:
http://mindey.com/panda3d/panda3d1.8_1.8.0-oneiric_amd64.deb

4. Run:
python main.py

******************************************************************************

Hello world:

# maze.py
X = {}
X[1] = MazeRoom(root)
X[2] = X[1].front.hangTunnel()
X[3] = MazeRoom(X[2]) 

******************************************************************************

Try out a sample maze: http://mindey.com/3dmaze.zip

