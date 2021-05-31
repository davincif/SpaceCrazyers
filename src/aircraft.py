# third party
import pygame

# internals
from .player import Player
from .planet import Planet
from .gui.health_bar import HealthBar
from . import basic_forms


class Aircraft():
    __triangle = None
    __pos = pygame.Vector2(15, 15)

    owner = None
    planet = None
    name = ''
    size = 15
    color = (0, 0, 180)
    max_health = 10
    health = 10
    swarm = 1

    show_life_bar = True
    life_bar = None

    def __init__(
        self,
        onwer,
        planet,
        pos,
        name,
        color,
        max_health,
        health=-1,
        size=-1,
        swarm=1,
    ):
        # type checking
        if not isinstance(onwer, Player):
            raise(TypeError('owner must be a Player object'))

        if not isinstance(planet, Planet):
            raise(TypeError('planet must be a Planet object'))

        if not isinstance(color, pygame.Color):
            raise(TypeError('color must be a pygame.Color object'))

        # stting pos
        self.__pos = pygame.Vector2(pos[0], pos[1])
        self.__triangel = basic_forms.triangle(self.__pos, self.size)

        # setting ordinary variables
        self.max_health = max_health
        self.onwer = onwer
        self.name = name
        self.color = color
        self.swarm = swarm
        self.life_bar = HealthBar()

        # setting conditional variables
        if size != -1:
            self.size = size

        if health == -1:
            self.health = self.max_health

    # getts and setters
    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, value: tuple):
        if not isinstance(value, pygame.Vector2):
            value = pygame.Vector2(value[0], value[1])

        self.__pos = value
        self.__triangel = basic_forms.triangle(self.__pos, self.size)

    # public methods
    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.__triangel)
        if self.show_life_bar:
            self.life_bar.draw(screen, self.__pos, self.health, self.max_health)
