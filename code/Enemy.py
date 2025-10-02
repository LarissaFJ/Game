import pygame
from code.Const import ENTITY_SPEED, WIN_WIDTH, ENTITY_HEALTH
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.original_surf = self.surf.copy()  # Guarda imagem original
        self.max_health = ENTITY_HEALTH[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]  # velocidade que as imagens de fundo se movem
        
        # Aplica efeito roxo se vida < 25%
        if self.health < self.max_health * 0.25:
            self.surf = self.original_surf.copy()
            self.surf.fill((200, 100, 255), special_flags=pygame.BLEND_MULT)
        else:
            self.surf = self.original_surf.copy()

