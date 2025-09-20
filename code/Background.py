from abc import ABC

import pygame

from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity


class Background(Entity, ABC):

    def __init__(self, name, position: tuple):
        super().__init__(name, position)
        self.speed = 1  # Velocidade do parallax (ajuste conforme necessário)

    def move(self):
        self.rect.x -= self.speed
        # Quando a imagem sair totalmente da tela, reposiciona à direita
        if self.rect.right < 0:
            self.rect.left = WIN_WIDTH