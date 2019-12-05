"""Player class for MacGyver game"""

import pygame as pg
from settings import *


class Player:
    """This class creates the player and the directions he can move"""
    def __init__(self, mac, map):
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
            if self.case_x < (width_sprites - 1):
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
            if self.case_y < (heigth_sprites - 2):
                if self.map.treated_map[self.case_y + 1][self.case_x] != "#":
                    self.case_y += 1
                    self.y = self.case_y * size_sprite

    def get_object(self):
        """Method to allow the player to pick up the objects and store them in
        the inventory, in the end automatically crafts the last object """
        if self.map.treated_map[self.case_y][self.case_x] == "1":
            self.map.treated_map[self.case_y][self.case_x] = " "
            self.map.treated_map[len(self.map.treated_map) - 1][self.nb_objects] = "1"
            self.nb_objects += 1
        if self.map.treated_map[self.case_y][self.case_x] == "2":
            self.map.treated_map[self.case_y][self.case_x] = " "
            self.map.treated_map[len(self.map.treated_map) - 1][self.nb_objects] = "2"
            self.nb_objects += 1
        if self.map.treated_map[self.case_y][self.case_x] == "3":
            self.map.treated_map[self.case_y][self.case_x] = " "
            self.map.treated_map[len(self.map.treated_map) - 1][self.nb_objects] = "3"
            self.nb_objects += 1
        if self.nb_objects == 3:
            self.map.treated_map[len(self.map.treated_map) - 1][0] = "4"
            self.map.treated_map[len(self.map.treated_map) - 1][1] = "."
            self.map.treated_map[len(self.map.treated_map) - 1][2] = "."

