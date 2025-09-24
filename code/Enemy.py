from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]  # velocidade que as imagens de fundo se movem

