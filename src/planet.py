# third party
import pygame

# standards
from .player import Player


class Planet():
    owner = None
    pos = (15, 15)
    name = ''
    size = 15
    color = (0, 0, 180)
    max_health = 10
    health = 10

    def __init__(self, onwer, pos, name, color, max_health, health=-1, size=-1):
        # type checking
        if (not isinstance(onwer, Player)):
            raise(TypeError('onwer must be a Player object'))

        # setting conditional variables
        if size != -1:
            self.size = size
        self.color = color
        self.max_health = max_health

        if health == -1:
            self.health = self.max_health

        # setting ordinary variables
        self.onwer = onwer
        self.pos = pos
        self.name = name

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.size)
