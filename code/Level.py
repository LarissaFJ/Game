import pygame
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, screen, name, game_mode):
        self.screen = screen
        self.name = name
        self.game_mode = game_mode
        self.entity_list = []

        # Exibe uma tela de carregamento rápida
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 40)
        text = font.render("Carregando...", True, (255, 255, 255))
        rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text, rect)
        pygame.display.update()

        # Alteramos 'Level1BG' para 'Level1Bg' para casar com o match da EntityFactory
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        print(f"Entidades carregadas: {len(self.entity_list)}")  # Debug: quantas entidades foram carregadas
        pygame.display.update()

    def run(self, player_score):
        running = True
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            self.screen.fill((0, 0, 0))  # Limpa a tela antes de desenhar

            for entity in self.entity_list:
                if hasattr(entity, "move"):  # Atualiza a posição se houver método move()
                    entity.move()
                if hasattr(entity, "surf") and hasattr(entity, "rect"):
                    self.screen.blit(entity.surf, entity.rect)
                else:
                    print("Entidade sem surf ou rect:", entity)

            pygame.display.flip()
            clock.tick(60)  # Limita a 60 FPS
