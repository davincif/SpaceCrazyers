# third party
import pygame

# internals
from src.colors import Colors
from src.node import Node


class Square(Node):
    color = Colors.WHITE.value
    dimension = pygame.Vector2(15, 15)

    def __init__(self, pos, dimension, color):
        Node.__init__(self, pos=pos)

        # setting conditional variables
        self.set_dimension(dimension)
        self.set_color(color)

    # getts and setters
    def set_dimension(self, value: tuple or list):
        if not isinstance(value, pygame.Vector2):
            self.dimension = pygame.Vector2(value[0], value[1])

    def set_color(self, value: tuple or list):
        if not isinstance(value, pygame.Color):
            self.color = pygame.Color(*value)

    # inherited
    def how_to_draw_me(self, screen):
        pygame.draw.rect(screen, self.color, (*self.pos, *self.dimension))

    def is_click(self, pos):
        return pygame.Rect.collidepoint(pos)
