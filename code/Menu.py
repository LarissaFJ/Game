import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
import pygame

from code.Const import WIN_WIDTH,MENU_OPTION, COLOR_WHITE, COLOR_PINK, COLOR_BLUE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBG.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        #pygame.mixer_music.load('./asset/Menu.mp3')
        #pygame.mixer_music.play(-1)

        title_text = "Battle in the Deep"
        title_font_size = 50
        option_font_size = 28
        option_spacing = 40

        # Calcula altura total do título e opções
        title_height = title_font_size
        options_height = len(MENU_OPTION) * option_font_size + (len(MENU_OPTION) - 1) * option_spacing
        gap = 120  # valor aumentado para afastar mais as opções do título

        total_height = title_height + gap + options_height
        y_start = (self.window.get_height() - total_height) // 2

        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)

            # Desenha o título centralizado em uma linha
            self.menu_text(title_font_size, title_text, COLOR_PINK, (WIN_WIDTH // 2, y_start + title_font_size // 2))

            # Desenha as opções centralizadas abaixo do título
            y = y_start + title_height + gap
            for i in range(len(MENU_OPTION)):
                color = COLOR_BLUE if i == menu_option else COLOR_WHITE
                self.menu_text(option_font_size, MENU_OPTION[i], color, (WIN_WIDTH // 2, y + option_font_size // 2))
                y += option_font_size + option_spacing

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_option = (menu_option + 1) % len(MENU_OPTION)
                    if event.key == pygame.K_UP:
                        menu_option = (menu_option - 1) % len(MENU_OPTION)
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
