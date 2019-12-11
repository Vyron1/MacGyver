"""Map class for MacGyver game"""

import pygame as pg
from random import randint
from settings import *


class Map:
    """This class creates the map level"""
    def __init__(self):
        self.treated_map = 0
        # loads the images
        self.wall = pg.image.load(image_wall).convert()
        self.floor = pg.image.load(image_floor).convert()
        self.start = pg.image.load(image_start).convert()
        self.finish = pg.image.load(image_finish).convert()
        self.inventory = pg.image.load(image_inventory).convert()
        # only the guard image as transparency
        self.guard = pg.image.load(image_guard).convert_alpha()
        self.object_1 = pg.image.load(image_object_1).convert()
        self.object_2 = pg.image.load(image_object_2).convert()
        self.object_3 = pg.image.load(image_object_3).convert()
        self.object_4 = pg.image.load(image_object_4).convert()


    def generate(self):
        """Method to generate the level from a txt file
        stocking it on a list and adding th inventory line at the end"""
        with open("map.txt", "r") as map:
            self.treated_map = []
            inventory_line = []
            for line in map:
                map_line = []
                for ch in line:
                    if ch != "\n":
                        map_line.append(ch)
                self.treated_map.append(map_line)
            for ch in range(len(self.treated_map[-1])):
                inventory_line.append(".")
            self.treated_map.append(inventory_line)


    def show_map(self, window):
        """Method to show the map from the list created by generate()"""
        numb_line = 0
        for line in self.treated_map:
            numb_ch = 0
            for ch in line:
                # converts from cases to pixels
                x = numb_ch * size_sprite
                y = numb_line * size_sprite
                if ch == "#":
                    # if the symbol on map is a # will put a wall image on its place
                    window.blit(self.wall, (x, y))
                elif ch == " ":
                    window.blit(self.floor, (x, y))
                elif ch == "s":
                    window.blit(self.start, (x, y))
                elif ch == "f":
                    window.blit(self.finish, (x, y))
                    window.blit(self.guard, (x, y))
                elif ch == "1":
                    window.blit(self.object_1, (x, y))
                elif ch == "2":
                    window.blit(self.object_2, (x, y))
                elif ch == "3":
                    window.blit(self.object_3, (x, y))
                elif ch == "4":
                    window.blit(self.object_4, (x, y))
                elif ch == ".":
                    window.blit(self.inventory, (x, y))
                numb_ch += 1
            numb_line += 1

    def randomize_object(self):
        """Method to randomize the objects showed in the map"""
        obj_x = []
        obj_y = []
        numb_line = 0
        for line in self.treated_map:
            numb_ch = 0
            for ch in line:
                # if the character is space we save their index in a list for
                # the x and the y.
                if ch == " ":
                    obj_x.append(numb_ch)
                    obj_y.append(numb_line)
                numb_ch += 1
            numb_line += 1
        # choose a position at random 3 times
        for i in range(3):
            pos = randint(0, len(obj_x) - 1)
            self.treated_map[obj_y[pos]][obj_x[pos]] = str(i+1)
            obj_y.pop(pos)
            obj_x.pop(pos)