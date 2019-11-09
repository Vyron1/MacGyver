
#############
#  Imports  #
#############
import pygame as pg
from pygame.locals import *
from settings import *
from map import *
from player import *


#####################
# INITIALIZE SCREEN #
#####################

pg.init()  # initialization of pygame library
window = pg.display.set_mode((side_window_width, side_window_height))  # window creation
map = Map()
map.generate()
map.randomize_token()

# Player creation
mac = Player(image_mac, map)

game_on = 1

while game_on:
    pg.time.Clock().tick(30)
    for event in pg.event.get():  # on parcours la liste des evenements
        if event.type == QUIT:  # si l'evenement est de type quit
            game_on = 0  # on arrete la boucle
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_on = 0  # on arrete la boucle

            elif event.key == K_RIGHT:
                mac.move('right')
            elif event.key == K_LEFT:
                mac.move('left')
            elif event.key == K_UP:
                mac.move('up')
            elif event.key == K_DOWN:
                mac.move('down')




    map.show_map(window)
    window.blit(mac.mac, (mac.x, mac.y))
    # Refresh screen
    pg.display.flip()
