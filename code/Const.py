#C
import pygame

COLOR_BLUE = (11, 131,229)
COLOR_PINK = (230, 37, 220)
COLOR_WHITE = (255, 255, 255)

#E
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Player': 3,
    'Enemy1': 2,
    'Enemy2': 1,
}

EVENT_ENEMY = pygame.USEREVENT + 1

#M
MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT')

#S
SPAWN_TIME = 4000
#W
WIN_WIDTH = 576
WIN_HEIGHT = 324