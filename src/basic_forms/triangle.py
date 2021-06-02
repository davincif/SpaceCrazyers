# standards
import math

# third party
import pygame

# internals
from src.colors import Colors
from src.node import Node


class Triangle(Node):
    triangle = ()
    size = 0
    color = Colors.WHITE.value

    def __init__(self, pos, size, color):
        # setting ordinary variables
        self.size = size
        self.triangle = (pygame.Vector2(), pygame.Vector2(), pygame.Vector2())

        Node.__init__(self, pos=pos)

        # setting conditional variables
        self.set_color(color)

    # getts and setters
    def set_color(self, value: tuple or list):
        if not isinstance(value, pygame.Color):
            self.color = pygame.Color(*value)

    def set_pos_callback(self, value: tuple or list):
        self.__calc_triangle(value)
        return True

    # inherited
    def is_click(self, pos):
        return False

    def how_to_draw_me(self, screen):
        pygame.draw.polygon(screen, self.color, self.triangle)

    # private methods
    def __calc_triangle(self, newpos=None):
        if newpos is None:
            newpos = self.relative_pos

        # thirty degrees
        td = math.pi / 6

        x = self.size * math.sin(td)
        y = self.size * math.cos(td)

        aux = round(newpos[1] + y)
        self.triangle[0].x = round(newpos[0] - x)
        self.triangle[0].y = aux
        self.triangle[1].x = round(newpos[0] + x)
        self.triangle[1].y = aux
        self.triangle[2].x = round(newpos[0])
        self.triangle[2].y = round(newpos[1] - y)
