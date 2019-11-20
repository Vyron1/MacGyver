
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
window = pg.display.set_mode((window_width, window_height))  # window creation
pg.display.set_caption("MacGyver")


map = Map()
mac = Player(image_mac, map)
pg.key.set_repeat(200, 150)  # delay and interval
game_on = 1

while game_on:
    home_screen = pg.image.load(image_home)
    window.blit(home_screen, (0, 0))
    pg.display.flip()

    continue_game = 0
    continue_home = 1
    while continue_home:

        pg.time.Clock().tick(30)
        for event in pg.event.get():  # on parcours la liste des evenements
            if event.type == QUIT:  # si l'evenement est de type quit
                game_on = 0 # on arrete la boucle
                continue_home = 0
                continue_game = 0
                check_win = 0
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game_on = 0  # on arrete la boucle
                    continue_home = 0
                    continue_game = 0
                elif event.key == K_F1:
                    map.generate()
                    map.randomize_object()
                    continue_home = 0
                    continue_game = 1
                    mac.nb_objects = 0
                    mac.case_x = 0
                    mac.case_y = 0
                    mac.x = 0
                    mac.y = 0


    while continue_game:
        pg.time.Clock().tick(30)
        map.show_map(window)
        mac.get_object()

        for event in pg.event.get():
            if event.type == QUIT:
                game_on = 0  # on arrete la boucle
                continue_home = 0
                continue_game = 0
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game_on = 1
                    continue_home = 1
                    continue_game = 0
                if event.key == K_RIGHT:
                    mac.move('right')
                elif event.key == K_LEFT:
                    mac.move('left')
                elif event.key == K_UP:
                    mac.move('up')
                elif event.key == K_DOWN:
                    mac.move('down')

        window.blit(mac.mac, (mac.x, mac.y))
        # Refresh screen
        pg.display.flip()


        if map.treated_map[mac.case_y][mac.case_x] == "f" and mac.nb_objects == 3:
            won = 1
            win = pg.image.load(image_win).convert_alpha()
            window.blit(win, (0, 0))
            pg.display.flip()
            while won:
                for event in pg.event.get():
                    if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                        game_on = 0
                        continue_home = 0
                        continue_game = 0
                        won = 0
                    if event.type == KEYDOWN:
                        if event.key == K_F1:
                            continue_home = 1
                            continue_game = 0
                            won = 0




        if map.treated_map[mac.case_y][mac.case_x] == "f" and mac.nb_objects < 3:
            lost = 1
            lose = pg.image.load(image_lose).convert_alpha()
            window.blit(lose, (0, 0))
            pg.display.flip()
            while lost:
                for event in pg.event.get():
                    if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                        game_on = 0
                        continue_home = 0
                        continue_game = 0
                        lost = 0
                    if event.type == KEYDOWN:
                        if event.key == K_F1:
                            continue_home = 1
                            continue_game = 0
                            lost = 0