import pygame
import sys
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_WHITE, COLOR_PINK
from code.ScoreManager import ScoreManager

class ScoreScreen:
    def __init__(self, window):
        self.window = window
        self.score_manager = ScoreManager()
    
    def run(self):
        pygame.mixer.music.load('./asset/underwater.wav')
        pygame.mixer.music.play(-1)
        scores = self.score_manager.load_scores()
        
        while True:
            self.window.fill((0, 0, 0))
            
            # Título
            self.centered_text(24, "HIGH SCORES", COLOR_PINK, 30)
            
            # Scores
            y = 80
            if scores:
                for i, entry in enumerate(scores):
                    if isinstance(entry, dict):
                        text = f"{i+1}. {entry['name']} - {entry['score']}s"
                    else:
                        text = f"{i+1}. Anônimo - {entry}s"
                    self.centered_text(18, text, COLOR_WHITE, y)
                    y += 25
            else:
                self.centered_text(18, "No scores recorded", COLOR_WHITE, y)
            
            # Instruções
            self.centered_text(16, "ESC: Back | C: Clear Scores", COLOR_WHITE, WIN_HEIGHT - 30)
            
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    elif event.key == pygame.K_c:
                        self.score_manager.clear_scores()
                        scores = []  # Atualiza lista local
    
    def centered_text(self, text_size: int, text: str, text_color: tuple, y_pos: int):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=(WIN_WIDTH//2, y_pos))
        self.window.blit(source=text_surf, dest=text_rect)