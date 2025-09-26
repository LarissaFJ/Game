from abc import ABC

import pygame

from code.Const import WIN_HEIGHT, WIN_WIDTH, ENTITY_SPEED, SHOOT_DELAY
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity, ABC):

    def __init__(self, name, position):
        super().__init__(name, position)
        self.shoot_delay = SHOOT_DELAY[self.name]
        self.last_shot = 0

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


    def shoot(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_SPACE]:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_shot >= self.shoot_delay * 100: #10 tiros por segundo
                self.last_shot = current_time
                return PlayerShot('PlayerShot', (self.rect.centerx + 10, self.rect.centery))
        return None

