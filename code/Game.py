import pygame

from code.Const import MENU_OPTION, WIN_WIDTH, WIN_HEIGHT
from code.Level import Level
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:  # 'NEW GAME'
                player_score = [0, 0]
                level = Level(self.window, 'Level1', menu_return)
                level.run(player_score)
            elif menu_return == MENU_OPTION[1]:  # 'SCORE'
                # Aqui você pode implementar a tela de score se desejar
                pass
            elif menu_return == MENU_OPTION[2]:  # 'EXIT'
                pygame.quit()
                break
