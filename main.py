
#############
#  Imports  #
#############
import pygame as pg
from pygame.locals import *
from settings import *
from map import *


#####################
# INITIALIZE SCREEN #
#####################

pg.init()  # initialization of pygame library
window = pg.display.set_mode((side_window_width, side_window_height))  # window creation
map = Map()
map.generate()
map.randomize_token()
game_on = 1

while game_on:
    pg.time.Clock().tick(30)
    for event in pg.event.get():  # on parcours la liste des evenements
        if event.type == QUIT:  # si l'evenement est de type quit
            game_on = 0  # on arrete la boucle
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_on = 0  # on arrete la boucle



    map.show_map(window)
    # Rafraichissement
    pg.display.flip()
