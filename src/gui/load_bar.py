# third party
import pygame

# internals
from . container import Container


class LoadBar(Container):
    damage = pygame.Color(171, 36, 9)
    life = pygame.Color(23, 130, 3)

    def __init__(self, pos, size=(30, 5), damage=None, life=None):
        Container.__init__(self, pos=pos, size=size)

        # setting conditional variables
        if damage is not None and not isinstance(damage, pygame.Color):
            self.damage = damage
        if life is not None and not isinstance(life, pygame.Color):
            self.life = life

    # public methods

    def draw(self, screen, filled: float):
        # treating entires
        if filled < 0:
            filled = 0
        elif filled > 1:
            filled = 1

        width = int(self.size[0] * filled)

        # life part
        rect = [
            self.pos[0],
            self.pos[1],
            width,
            self.size[1],
        ]
        pygame.draw.rect(
            screen,
            self.life,
            rect,
        )

        # damage part
        rect[0] = self.pos[0] + width
        rect[2] = self.size[0] - width
        pygame.draw.rect(
            screen,
            self.damage,
            rect,
        )
