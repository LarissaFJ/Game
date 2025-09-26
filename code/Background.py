from abc import ABC

import pygame

from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity


class Background(Entity):

    def __init__(self, name, position):
        super().__init__(name, position)


    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name] #velocidade que as imagens de fundo se movem
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
        pass


