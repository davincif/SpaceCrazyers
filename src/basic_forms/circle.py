# third party
import pygame

# internals
from src.node import Node


class Circle(Node):
    radius = 0
    color = (255, 255, 255)

    def __init__(self, pos, radius, color):
        Node.__init__(self, pos=pos)

        # setting ordinary variables
        self.radius = radius

        # setting conditional variables
        if not isinstance(color, pygame.Color):
            self.color = pygame.Color(color[0], color[1], color[2])
        else:
            self.color = color

    def is_click(self, pos):
        if(self.pos.distance_to(pos) <= self.radius):
            return True
        else:
            return False

    def how_to_draw_me(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)
