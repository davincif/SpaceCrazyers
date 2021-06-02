# third party
import pygame

# internals
from src.colors import Colors
from src.node import Node


class Circle(Node):
    radius = 0
    color = Colors.WHITE.value

    def __init__(self, pos, radius, color):
        Node.__init__(self, pos=pos)

        # setting ordinary variables
        self.radius = radius

        # setting conditional variables
        self.set_color(color)

    # getts and setters
    def set_color(self, value: tuple or list):
        if not isinstance(value, pygame.Color):
            self.color = pygame.Color(*value)

    # inherited
    def is_click(self, pos):
        if(self.pos.distance_to(pos) <= self.radius):
            return True
        else:
            return False

    def how_to_draw_me(self, screen):
        pygame.draw.circle(screen, self.color, self.relative_pos, self.radius)
