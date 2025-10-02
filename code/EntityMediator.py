import pygame

from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity ): ##mod privado
        if isinstance(ent,Enemy) and  ent.rect.right < 0:
             ent.health = 0
        if isinstance(ent,PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(entity1, entity2):
        valid_interaction=False
        if isinstance(entity1, PlayerShot) and isinstance(entity2, Enemy):
            valid_interaction=True
        elif isinstance(entity1, Enemy) and isinstance(entity2, PlayerShot):
            valid_interaction=True
        elif isinstance(entity1, Player) and isinstance(entity2, Enemy):
            valid_interaction=True
        elif isinstance(entity1, Enemy) and isinstance(entity2, Player):
            valid_interaction=True

        if valid_interaction:
            if (entity1.rect.right >= entity2.rect.left and
                    entity1.rect.left <= entity2.rect.right and
                    entity1.rect.bottom >= entity2.rect.top and
                    entity1.rect.top <= entity2.rect.bottom):
                # Player recebe dano com invencibilidade temporária, evita colisões contínuas
                if isinstance(entity1, Player) and isinstance(entity2, Enemy):
                    current_time = pygame.time.get_ticks()
                    if current_time - entity1.invulnerable_time >= entity1.invulnerable_duration:
                        entity1.health -= 20
                        entity1.invulnerable_time = current_time
                    entity2.health -= entity1.damage
                elif isinstance(entity1, Enemy) and isinstance(entity2, Player):
                    current_time = pygame.time.get_ticks()
                    if current_time - entity2.invulnerable_time >= entity2.invulnerable_duration:
                        entity2.health -= 20
                        entity2.invulnerable_time = current_time
                    entity1.health -= entity2.damage
                else:
                    entity1.health -= entity2.damage
                    entity2.health -= entity1.damage
                    # Destrói o tiro após atingir o inimigo
                    if isinstance(entity1, PlayerShot) or isinstance(entity2, PlayerShot):
                        if isinstance(entity1, PlayerShot):
                            entity1.health = 0
                        if isinstance(entity2, PlayerShot):
                            entity2.health = 0
                entity1.last_damage = entity2.name
                entity2.last_damage = entity1.name

    @staticmethod
    def verify_collision(entity_list:list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i+1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)