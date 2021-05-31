# standards
import math

# third party
import pygame

# internals
from src.node import Node


class Triangle(Node):
    triangle = ()
    size = 0
    color = (255, 255, 255)

    def __init__(self, pos, size, color):
        # setting ordinary variables
        self.size = size
        self.triangle = (pygame.Vector2(), pygame.Vector2(), pygame.Vector2())

        Node.__init__(self, pos=pos)

        # setting conditional variables
        if not isinstance(color, pygame.Color):
            self.color = pygame.Color(color[0], color[1], color[2])
        else:
            self.color = color

    # getts and setters
    def set_pos_callback(self, value: tuple or list):
        self.__calc_triangle(value)
        return True

    def is_click(self, pos):
        return False

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.triangle)

    # private methods
    def __calc_triangle(self, newpos=None):
        if newpos is None:
            newpos = self.pos

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
