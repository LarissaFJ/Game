import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, WIN_HEIGHT, EVENT_ENEMY, SPAWN_TIME, WIN_WIDTH
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player
from code.ScoreManager import ScoreManager


class Level:
    def __init__(self, window, name, game_mode, player_name="Anônimo"):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.player_name = player_name
        self.entity_list : list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg')) #carrega a imagem do backgroung
        self.entity_list.append(EntityFactory.get_entity('Player')) #carrega a imagem do player
        self.timeout = 60000  # Tempo limite em milissegundos (60 segundos)
        self.current_spawn_time = SPAWN_TIME
        self.last_difficulty_increase = 0
        self.enemies_per_spawn = 1
        self.start_time = pygame.time.get_ticks()  # Tempo de início do jogo
        self.score = 0  # Score baseado no tempo de sobrevivência

        # Exibe tela de carregamento
        self.show_loading()
        
        pygame.time.set_timer(EVENT_ENEMY, self.current_spawn_time) #GERAÇÃO DO EVENTO


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
                    # Spawna múltiplos inimigos
                    for _ in range(self.enemies_per_spawn):
                        if self.score >= 20: #enemy3 só entra depois de 20s
                            choice = random.choice(('Enemy1','Enemy2','Enemy3'))
                        else:
                            choice = random.choice(('Enemy1','Enemy2'))
                        self.entity_list.append(EntityFactory.get_entity(choice))
                    
                    # Aumenta dificuldade apos 25 segundos
                    current_time = pygame.time.get_ticks()
                    if self.score >= 25:
                        # Após 25s: +2 inimigos a cada 2 segundos
                        if current_time - self.last_difficulty_increase >= 2000:
                            self.enemies_per_spawn += 2
                            self.last_difficulty_increase = current_time
                    elif current_time - self.last_difficulty_increase >= 4000:
                        # Antes de 25s: +1 inimigo a cada 4 segundos
                        self.enemies_per_spawn += 1
                        self.last_difficulty_increase = current_time

            # Atualiza o score (tempo de sobrevivência em segundos)
            current_time = pygame.time.get_ticks()
            self.score = (current_time - self.start_time) // 1000
            
            # Verifica se o player ainda está vivo e pega sua vida
            player = None
            for ent in self.entity_list:
                if isinstance(ent, Player):
                    player = ent
                    break
            
            if player is None:
                running = False
            
            #print na tela
            if player:
                self.level_text(16, f'Health: {player.health}', COLOR_WHITE, (WIN_WIDTH - 120, 10))
            self.level_text(16, f'Time: {self.score}s', COLOR_WHITE, (WIN_WIDTH//2 - 40, 10))
            self.level_text(16, f'Demo Version', COLOR_WHITE, (10, 10))
            self.level_text(14, f'fps: {clock.get_fps():0f}', COLOR_WHITE, (10, WIN_HEIGHT - 20))


            pygame.display.flip()
            #mediador = colisoes, vida e etc
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
            clock.tick(60)  # Limita a 60 FPS
        
        # Salva o score e mostra Game Over
        score_manager = ScoreManager()
        score_manager.save_score(self.player_name, self.score)
        self.show_game_over()
        return self.score



    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left = text_center_pos[0], top=text_center_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
    
    def centered_text(self, text_size: int, text: str, text_color: tuple, y_pos: int):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=(WIN_WIDTH//2, y_pos))
        self.window.blit(source=text_surf, dest=text_rect)
    
    def show_game_over(self):
        # Tela de Game Over com score final
        self.window.fill((0, 0, 0))
        self.centered_text(36, "GAME OVER", COLOR_WHITE, WIN_HEIGHT//2 - 50)
        self.centered_text(24, f"Survival Time: {self.score} seconds", COLOR_WHITE, WIN_HEIGHT//2)
        self.centered_text(18, "Press any key to continue", COLOR_WHITE, WIN_HEIGHT//2 + 50)
        pygame.display.flip()
        
        # Espera o jogador pressionar uma tecla
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    waiting = False
    
    def show_loading(self):
        self.window.fill((0, 0, 0))
        self.centered_text(24, f"Loading {self.name}...", COLOR_WHITE, WIN_HEIGHT//2 - 20)
        self.centered_text(18, f"Player: {self.player_name}", COLOR_WHITE, WIN_HEIGHT//2 + 20)
        pygame.display.flip()
        pygame.time.wait(1000)  # Pausa de 1 segundo
