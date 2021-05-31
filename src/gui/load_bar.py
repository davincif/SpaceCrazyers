# third party
import pygame

# internals
from src.node import Node


class LoadBar(Node):
    size = 30
    thickness = 5
    background = pygame.Color(171, 36, 9)
    filled = pygame.Color(23, 130, 3)

    def __init__(self, pos, size=None, thickness=None, background=None, filled=None):
        Node.__init__(self, pos=pos)
        # setting ordinary variables
        if size is not None:
            self.size = size
        if thickness is not None:
            self.thickness = thickness
        if background is not None and not isinstance(background, pygame.Color):
            self.background = background
        if filled is not None and not isinstance(filled, pygame.Color):
            self.filled = filled

    # public methods
    def how_to_draw_me(self, screen, filled: float):
        # treating entires
        if filled < 0:
            filled = 0
        elif filled > 1:
            filled = 1

        size = int(self.size * filled)

        # filled part
        rect = [
            self.pos[0],
            self.pos[1],
            size,
            self.thickness,
        ]
        pygame.draw.rect(
            screen,
            self.filled,
            rect,
        )

        # background part
        rect[0] = self.pos[0] + size
        rect[2] = self.size - size
        pygame.draw.rect(
            screen,
            self.background,
            rect,
        )
