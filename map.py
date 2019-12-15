"""Map class for MacGyver game"""

#############
#  Imports  #
#############

import pygame as pg
from random import randint
from settings import *

###########
#  Class  #
###########

class Map:
    """This class creates the map level"""
    def __init__(self):
        self.treated_map = 0
        # loads the images
        # only the guard image as transparency
        self.guard = pg.image.load(image_guard).convert_alpha()
        self.wall = pg.image.load(image_wall).convert()
        self.floor = pg.image.load(image_floor).convert()
        self.start = pg.image.load(image_start).convert()
        self.finish = pg.image.load(image_finish).convert()
        self.inventory = pg.image.load(image_inventory).convert()
        self.object_1 = pg.image.load(image_object_1).convert()
        self.object_2 = pg.image.load(image_object_2).convert()
        self.object_3 = pg.image.load(image_object_3).convert()
        self.object_4 = pg.image.load(image_object_4).convert()


    def generate(self):
        """Method to generate the level from a txt file
        stocking it on a list and adding th inventory line at the end"""
        # we open the file and read it
        with open("map.txt", "r") as map:
            map_list = []
            inventory_line = []
            # we go trough each line of the file
            for line in map:
                map_line = []
                # we go trough each character of the line
                for ch in line:
                    # we ignore the end line
                    if ch != "\n":
                        # we add the character to the line list
                        map_line.append(ch)
                # we add the line to map_list
                map_list.append(map_line)
            # we add the same number of . as the length of the last
            # line in map_list to create the inventory line
            for length in range(len(map_list[-1])):
                inventory_line.append(".")
            # we add the inventory line to the end of the map_list
            map_list.append(inventory_line)
            # we save the treated map
            self.treated_map = map_list


    def show_map(self, window):
        """Method to show the map from the list created by generate()"""
        numb_line = 0
        for line in self.treated_map:
            numb_ch = 0
            for ch in line:
                # converts from cases to pixels
                x = numb_ch * size_sprite
                y = numb_line * size_sprite
                if ch == "#": # (#) = wall
                    # if the symbol on map is a # will put a wall image on its
                    # x and y which are now pixel coordinates on the screen
                    window.blit(self.wall, (x, y))
                elif ch == " ": # ( ) = floor
                    window.blit(self.floor, (x, y))
                elif ch == "s": # (s) = start line
                    window.blit(self.start, (x, y))
                elif ch == "f": # (f) = finish line and guard
                    # first we show the finish tile then we put put the guard on
                    # top of it and because of transparency we can see the floor behind
                    window.blit(self.finish, (x, y))
                    window.blit(self.guard, (x, y))
                elif ch == "1": # (1) = object n°1 (ether)
                    window.blit(self.object_1, (x, y))
                elif ch == "2": # (2) = object n°2 (needle)
                    window.blit(self.object_2, (x, y))
                elif ch == "3": # (3) = object n°3 (plastic tube)
                    window.blit(self.object_3, (x, y))
                elif ch == "4": # (4) = object n°4 (syringe)
                    window.blit(self.object_4, (x, y))
                elif ch == ".": # (.) = inventory background
                    window.blit(self.inventory, (x, y))
                # we add 1 to the character variable to then convert
                # the x position into pixels
                numb_ch += 1
            # we do the same for the line variable for the y position
            numb_line += 1

    def randomize_object(self):
        """Method to randomize the objects showed in the map
        we use the same basic algorithm as in show map to go through every
         line and character"""
        # we create 2 lists to save the indexes of the free spaces
        obj_x = []
        obj_y = []
        numb_line = 0
        for line in self.treated_map:
            numb_ch = 0
            for ch in line:
                # if the character is a space (floor) we save their index in a list for
                # the x and the y.
                if ch == " ":
                    obj_x.append(numb_ch)
                    obj_y.append(numb_line)
                numb_ch += 1
            numb_line += 1
        # then we choose a position at random 3 times
        for i in range(3):
            # we take a random number from 0 to the length of one of the free spaces list
            pos = randint(0, len(obj_x) - 1)
            # then we use that number (index) to replace that random free space for
            # an object with each loop being a different object
            self.treated_map[obj_y[pos]][obj_x[pos]] = str(i+1)
            # in the end we remove the used number from the free spaces list
            # that way we wont have 2 objects in the same space
            obj_y.pop(pos)
            obj_x.pop(pos)