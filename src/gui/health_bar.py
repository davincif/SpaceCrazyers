# third party
import pygame


class HealthBar():
    size = 30
    thickness = 5
    damage = pygame.Color(171, 36, 9)
    life = pygame.Color(23, 130, 3)

    def __init__(self, size=None, thickness=None, damage=None, life=None):
        # setting ordinary variables
        if size is not None:
            self.size = size
        if thickness is not None:
            self.thickness = thickness
        if damage is not None and not isinstance(damage, pygame.Color):
            self.damage = damage
        if life is not None and not isinstance(life, pygame.Color):
            self.life = life

    # public methods
    def draw(self, screen, pos, health, max_health):
        size = int(self.size * (health / max_health))

        # life part
        rect = [
            pos[0],
            pos[1],
            size,
            self.thickness,
        ]
        pygame.draw.rect(
            screen,
            self.life,
            rect,
        )

        # damage part
        rect[0] = pos[0] + size
        rect[2] = self.size - size
        pygame.draw.rect(
            screen,
            self.damage,
            rect,
        )
