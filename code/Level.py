import pygame
from pygame import surface

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list : list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

        # Exibe uma tela de carregamento rápida
        #self.window.fill((0, 0, 0))
        #font = pygame.font.Font(None, 40)
        #text = font.render("Carregando...", True, (255, 255, 255))
        #rect = text.get_rect(center=(self.window.get_width() // 2, self.window.get_height() // 2))
        #self.window.blit(text, rect)
        #pygame.display.update()


    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            pygame.display.flip()
            clock.tick(60)  # Limita a 60 FPS
