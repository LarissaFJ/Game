import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, WIN_HEIGHT, EVENT_ENEMY, SPAWN_TIME
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list : list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg')) #carrega a imagem do backgroung
        self.entity_list.append(EntityFactory.get_entity('Player')) #carrega a imagem do player
        self.timeout = 60000  # Tempo limite em milissegundos (60 segundos)

        # Exibe uma tela de carregamento rápida
        #self.window.fill((0, 0, 0))
        #font = pygame.font.Font(None, 40)
        #text = font.render("Carregando...", True, (255, 255, 255))
        #rect = text.get_rect(center=(self.window.get_width() // 2, self.window.get_height() // 2))
        #self.window.blit(text, rect)
        #pygame.display.update()

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME ) #GERAÇÃO DO EVENTO


    def run(self):
        #colocarmusica do level 1
        #pygame.mixer_music.load('./asset/Level1.mp3')
        running = True
        clock = pygame.time.Clock()
        while running:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, Player): #verifica se é player
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1','Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            #print na tela
            self.level_text(14 , f'{self.name} - Timeout:{self.timeout/1000 :.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():0f}', COLOR_WHITE, (10, WIN_HEIGHT - 20))


            pygame.display.flip()
            #mediador = colisoes, vida e etc
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
            clock.tick(60)  # Limita a 60 FPS



    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left = text_center_pos[0], top=text_center_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
