from abc import ABC

import pygame

from code.Const import WIN_HEIGHT, WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity


class Player(Entity, ABC):

    def __init__(self, name, position):
        super().__init__(name, position)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_keys[pygame.K_s] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_keys[pygame.K_a] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_keys[pygame.K_d] and self.rect.right < WIN_WIDTH:
                self.rect.centerx += ENTITY_SPEED[self.name]

