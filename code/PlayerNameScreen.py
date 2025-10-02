import pygame
import sys
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_WHITE, COLOR_PINK, COLOR_BLUE

class PlayerNameScreen:
    def __init__(self, window):
        self.window = window
        self.player_name = ""
    
    def run(self):
        while True:
            self.window.fill((0, 0, 0))
            
            self.centered_text(24, "ENTER YOUR NAME", COLOR_PINK, 100)
            self.centered_text(20, self.player_name + "_", COLOR_WHITE, 150)
            self.centered_text(16, "Press ENTER to confirm", COLOR_WHITE, 200)
            
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and self.player_name.strip():
                        return self.player_name.strip()
                    elif event.key == pygame.K_BACKSPACE:
                        self.player_name = self.player_name[:-1]
                    elif event.unicode.isprintable() and len(self.player_name) < 15:
                        self.player_name += event.unicode
    
    def centered_text(self, text_size: int, text: str, text_color: tuple, y_pos: int):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=(WIN_WIDTH//2, y_pos))
        self.window.blit(source=text_surf, dest=text_rect)