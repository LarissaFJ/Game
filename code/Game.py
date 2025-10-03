import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.ScoreScreen import ScoreScreen
from code.PlayerNameScreen import PlayerNameScreen


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:  # NEW GAME
                name_screen = PlayerNameScreen(self.window)
                player_name = name_screen.run()
                level = Level(self.window, 'Level1', menu_return, player_name)
                level_return = level.run()
            elif menu_return == MENU_OPTION[1]:  # SCORE
                score_screen = ScoreScreen(self.window)
                score_screen.run()
            elif menu_return == MENU_OPTION[2]:  # EXIT
                pygame.quit()  # Close Window
                quit()  # end pygame
            else:
                pass
