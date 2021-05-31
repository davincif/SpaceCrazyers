# third party
import pygame

# internals
from src.node import Node


class Container(Node):
    size = (30, 10)
    background_color = pygame.Color(0, 0, 0)

    def __init__(self, pos, size, background_color=None):
        Node.__init__(self, pos=pos)

        # setting conditional variables
        if not isinstance(size, pygame.Vector2):
            self.size = pygame.Vector2(size[0], size[1])
        if background_color is not None and not isinstance(background_color, pygame.Color):
            self.background_color = background_color
