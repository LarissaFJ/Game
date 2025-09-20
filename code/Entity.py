from abc import ABC, abstractmethod
import os

import pygame


class Entity(ABC):
    def __init__(self, name, position: tuple):
        self.name = name
        asset_path = './asset/' + name + '.png'
        if not os.path.exists(asset_path):
            # Cria uma imagem placeholder se não encontrar a imagem real
            print(f"Imagem não encontrada: {asset_path}. Criando placeholder.")
            placeholder = pygame.Surface((100, 100))  # Ajuste o tamanho conforme necessário
            placeholder.fill((255, 0, 0))
            os.makedirs('./asset', exist_ok=True)
            pygame.image.save(placeholder, asset_path)
        self.surf = pygame.image.load(asset_path).convert_alpha()
        self.rect = self.surf.get_rect(topleft=position)
        self.speed = 0

    @abstractmethod
    def move(self):
        pass