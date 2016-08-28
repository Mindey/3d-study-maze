# -*- coding: utf-8 -*-
#
# The initial commit is based on parts of Panda3D sample program named "Bump-Mapping":
# http://www.panda3d.org/manual/index.php/Sample_Programs:_Normal_Mapping
# Licensed, probably, under http://www.panda3d.org/license.php
#

import sys, os
import direct.directbase.DirectStart
from panda3d.core import WindowProperties
from panda3d.core import Point2, Point3, Vec3
from direct.showbase.DirectObject import DirectObject
from direct.task.Task import Task

# https://www.panda3d.org/reference/1.9.0/python/panda3d.core.CardMaker.php
from pandac.PandaModules import CardMaker

class Wall(object):
    def __init__(self):
        # Draw a wall.
        self.cm = CardMaker('card')
                            #   x   y   z
        LeftBottom  = Point3( -15, 50, -10)
        RightBottom = Point3(  15, 50, -10)
        LeftTop     = Point3( -15, 50,  10)
        RightTop    = Point3(  15, 50,  10)
        # Set the size of the card.
        self.cm.setFrame( LeftBottom, RightBottom, RightTop, LeftTop )

        # Instantiate the card.
        self.card = render.attachNewNode(self.cm.generate())

        # Write "Hello" on the card.
        self.text = loader.loadTexture('hello.png')
        self.card.setTexture(self.text)

class Room(object):
    pass

class Port(object):
    pass

class XMaze(DirectObject):

    def maze(self):

        # The areas where we are allowed to go.
        self.maze_areas = []
        self.maze_areas.append(Wall())

    def __init__(self):

        # Set the current viewing target: facing y+, from (0,0,0)
        self.focus = Vec3(0,0,0)
        self.heading = 0
        self.pitch = 0
        self.mousex = 0
        self.mousey = 0
        self.last = 0
        self.mousebtn = [0,0,0]

        # Start the camera control task:
        taskMgr.add(self.control_camera, "camera-task")
        self.accept("escape",    os._exit, [0])
        self.accept("mouse1",    self.set_mouse_button, [0, 1])
        self.accept("mouse1-up", self.set_mouse_button, [0, 0])
        self.accept("mouse2",    self.set_mouse_button, [1, 1])
        self.accept("mouse2-up", self.set_mouse_button, [1, 0])
        self.accept("mouse3",    self.set_mouse_button, [2, 1])
        self.accept("mouse3-up", self.set_mouse_button, [2, 0])

        # Show framerate
        base.setFrameRateMeter(True)

        # Make the mouse invisible, turn off normal mouse controls.
        base.disableMouse()
        props = WindowProperties()
        props.setCursorHidden(True)
        base.win.requestProperties(props)

        # Where we can define maze in terms of objects, and maze areas.
        self.maze()

    def set_mouse_button(self, btn, value):
        self.mousebtn[btn] = value

    def control_camera(self, task):

        # How much the mouse has moved.
        md = base.win.getPointer(0)
        x = md.getX()
        y = md.getY()

        # Move mouse pointer.
        if base.win.movePointer(0, 100, 100):
            self.heading = self.heading - (x - 100) * 0.2
            self.pitch = self.pitch - (y - 100) * 0.2

        # Set limits up/down movement of the camera.
        if (self.pitch < -45): self.pitch = -45
        if (self.pitch >  45): self.pitch =  45
        base.camera.setHpr(self.heading,self.pitch,0)
        dir = base.camera.getMat().getRow3(1)

        # Set mouse buttons for forth/back movement.
        elapsed = task.time - self.last
        if (self.last == 0): 
            elapsed = 0
        if (self.mousebtn[0]):
            self.focus = self.focus + dir * elapsed*30
        if (self.mousebtn[1]) or (self.mousebtn[2]):
            self.focus = self.focus - dir * elapsed*30
        base.camera.setPos(self.focus - (dir*5))

        # Limits for camera movement, imitating the room's walls.

        # This needs to be adjusted, when based on maze logic.
        for area in self.maze_areas:
            pass

        if (base.camera.getX() < -59.0): base.camera.setX(-59)
        if (base.camera.getX() >  59.0): base.camera.setX( 59)
        if (base.camera.getY() < -59.0): base.camera.setY(-59)
        if (base.camera.getY() >  59.0): base.camera.setY( 59)
        if (base.camera.getZ() <   5.0): base.camera.setZ(  5)
        if (base.camera.getZ() >  45.0): base.camera.setZ( 45)

        # Location, Direction
        print 'LOCATION: (x=%02d, y=%02d, z=%02d), DIRECTION: ← →  %02d, ↑ ↓: %02d' % (base.camera.getX(), 
                                                                                       base.camera.getY(), 
                                                                                       base.camera.getZ(), 
                                                                                       self.heading,
                                                                                       self.pitch)

        self.focus = base.camera.getPos() + (dir*5)
        self.last = task.time
        return Task.cont

Maze = XMaze()

run()
