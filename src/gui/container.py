# third party
import pygame

# internals
from src.node import Node


class Container(Node):
    size = (30, 10)

    def __init__(self, pos, size):
        Node.__init__(self, pos=pos)

        # setting conditional variables
        if not isinstance(size, pygame.Vector2):
            self.size = pygame.Vector2(size[0], size[1])
