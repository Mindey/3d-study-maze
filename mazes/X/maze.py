#-*- coding:utf-8 -*-
path = 'mazes/X/'
prerequisites = []

# All rooms have to be registered in a dictionary of the same name as the folder.
X = {}

X[1] = MazeRoom(root)
X[2] = X[1].front.hangTunnel()
X[3] = MazeRoom(X[2]) 
