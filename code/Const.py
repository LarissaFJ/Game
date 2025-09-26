# C
import pygame

COLOR_BLUE = (11, 131, 229)
COLOR_PINK = (230, 37, 220)
COLOR_WHITE = (255, 255, 255)

# E
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
    'PlayerShot': 2,
    'EnemyShot': 1,
}

SHOOT_DELAY = {
    'Player': 1,
    'Enemy1': 1,
    'Enemy2': 1
}

EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Player': 1,
    'Enemy1': 60,
    'Enemy2': 5,
    'PlayerShot': 25
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Player': 300,
    'Enemy1': 60,
    'Enemy2': 50,
    'PlayerShot': 999
}

# M
MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT')

# S
SPAWN_TIME = 4000
# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
