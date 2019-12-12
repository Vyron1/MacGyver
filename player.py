"""Player class for MacGyver game"""

#############
#  Imports  #
#############

import pygame as pg
from settings import *

###########
#  Class  #
###########

class Player:
    """This class creates the player and the directions he can move"""
    def __init__(self, mac, map):
        # we load the player image with transparency
        self.mac = pg.image.load(mac).convert_alpha()
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.map = map
        self.nb_objects = 0

    def move(self, direction):
        """Method to allow the player to move and verify collisions
        with walls and the edge of the screen"""
        if direction == "right":
            # checks if player is on the edge of the screen
            if self.case_x < (width_sprites - 1):
                # checks if the next block on the direction we want to turn is a wall
                # if not it allows the player to move
                if self.map.treated_map[self.case_y][self.case_x + 1] != "#":
                    self.case_x += 1
                    self.x = self.case_x * size_sprite

        if direction == "left":
            if self.case_x > 0:
                if self.map.treated_map[self.case_y][self.case_x - 1] != "#":
                    self.case_x -= 1
                    self.x = self.case_x * size_sprite

        if direction == "up":
            if self.case_y > 0:
                if self.map.treated_map[self.case_y - 1][self.case_x] != "#":
                    self.case_y -= 1
                    self.y = self.case_y * size_sprite

        if direction == "down":
            # checks if player is on the edge of the screen but ignoring
            # the inventory line
            if self.case_y < (heigth_sprites - 2):
                if self.map.treated_map[self.case_y + 1][self.case_x] != "#":
                    self.case_y += 1
                    self.y = self.case_y * size_sprite

    def get_object(self):
        """
        Method to allow the player to pick up the objects and store them in
        the inventory, if player position is the same as an object.
         """
        if self.map.treated_map[self.case_y][self.case_x] == "1":
            # we change the object number to a space that way the object disappears
            # from the maze
            self.map.treated_map[self.case_y][self.case_x] = " "
            # we change the first place in inventory to the number of the object
            # picked up so it appears in inventory
            self.map.treated_map[len(self.map.treated_map) - 1][self.nb_objects] = "1"
            # we increase the value of number of objects
            self.nb_objects += 1
        if self.map.treated_map[self.case_y][self.case_x] == "2":
            self.map.treated_map[self.case_y][self.case_x] = " "
            self.map.treated_map[len(self.map.treated_map) - 1][self.nb_objects] = "2"
            self.nb_objects += 1
        if self.map.treated_map[self.case_y][self.case_x] == "3":
            self.map.treated_map[self.case_y][self.case_x] = " "
            self.map.treated_map[len(self.map.treated_map) - 1][self.nb_objects] = "3"
            self.nb_objects += 1
        # if player as 3 objects
        if self.nb_objects == 3:
            # we place the final object on the first place in the inventory
            # and remove the rest of the objects from inventory
            self.map.treated_map[len(self.map.treated_map) - 1][0] = "4"
            self.map.treated_map[len(self.map.treated_map) - 1][1] = "."
            self.map.treated_map[len(self.map.treated_map) - 1][2] = "."

