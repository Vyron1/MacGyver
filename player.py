import pygame as pg
from settings import *
from map import *

class Player:

    def __init__(self, mac, map):
        self.mac = pg.image.load(mac).convert_alpha()
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.map = map

    def move(self, direction):

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

