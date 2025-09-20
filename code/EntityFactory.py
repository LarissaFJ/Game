import os
from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
import pygame
import random

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(6):  # level1bg images number
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg



def draw_battle_title(screen, font, color, win_width):
    # "Battle" na linha 1
    text1 = font.render("Battle", True, color)
    rect1 = text1.get_rect(center=(win_width // 2, 70))
    screen.blit(text1, rect1)
    # "in the" na linha 2
    text2 = font.render("in the", True, color)
    rect2 = text2.get_rect(center=(win_width // 2, 120))
    screen.blit(text2, rect2)
    # "Deep" na linha 3
    text3 = font.render("Deep", True, color)
    rect3 = text3.get_rect(center=(win_width // 2, 170))
    screen.blit(text3, rect3)
