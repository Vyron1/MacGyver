# -*- coding: Utf-8 -*

"""
MacGyver Game
The objective is to get to the end of the maze with all 3 objects and
craft a syringe to put the Guard to sleep.

Script Python
Files : main.py, settings.py, map.py, player.py, map.txt, resources
"""

import pygame as pg
from pygame.locals import *
from settings import *
from map import Map
from player import Player

# initialization of pygame library
pg.init()
# window creation with size width and height
window = pg.display.set_mode((window_width, window_height))
# Set the window name to MacGyver and icon to a custom image.
pg.display.set_caption("MacGyver")
icon = pg.image.load(image_mac)
pg.display.set_icon(icon)

map = Map()
# creating the player
mac = Player(image_mac, map)
# Pygame function to keep the key pressed with (delay, interval)
pg.key.set_repeat(200, 150)

# Main loop
game_on = 1
while game_on:
    # Loading and adding the home screen image to the game screen
    home_screen = pg.image.load(image_home)
    window.blit(home_screen, (0, 0))
    # refresh the game screen
    pg.display.flip()

    # setting the home loop to 1 on each loop
    continue_home = 1

    # Home loop
    while continue_home:

        # Limiting the loop to 30 fps
        pg.time.Clock().tick(30)
        # if the player quits or press escape
        # we set the variables to 0 to stop the loop
        for event in pg.event.get():
            if event.type == QUIT:
                game_on = 0
                continue_home = 0
                continue_game = 0
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game_on = 0
                    continue_home = 0
                    continue_game = 0
                # If F1 is pressed we start the game
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

    # Game loop
    while continue_game:
        pg.time.Clock().tick(30)
        map.show_map(window)
        mac.get_object()

        for event in pg.event.get():
            # Quit to stop the game
            if event.type == QUIT:
                game_on = 0
                continue_home = 0
                continue_game = 0
            if event.type == KEYDOWN:
                # Escape to return to Home screen
                if event.key == K_ESCAPE:
                    game_on = 1
                    continue_home = 1
                    continue_game = 0
                # Player movement
                if event.key == K_RIGHT:
                    mac.move('right')
                elif event.key == K_LEFT:
                    mac.move('left')
                elif event.key == K_UP:
                    mac.move('up')
                elif event.key == K_DOWN:
                    mac.move('down')
        # refreshing player position
        window.blit(mac.mac, (mac.x, mac.y))
        # Refresh screen
        pg.display.flip()

        # if player is in the end of the map and has 3 objects on inventory
        # starts the won loop
        if map.treated_map[mac.case_y][mac.case_x] == "f" and mac.nb_objects == 3:
            won = 1
            win = pg.image.load(image_win).convert_alpha()
            window.blit(win, (0, 0))
            pg.display.flip()
            # Win loop
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

        # if player is in the end of the map but does'nt have all objects on inventory
        # starts the lost loop
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