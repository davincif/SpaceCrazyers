# third party
import pygame

# internals
from .player import Player


class Planet():
    __last_processed_ms = 0
    __pos = pygame.Vector2(15, 15)
    __resources = 0

    # need initialization
    owner = None
    name = ''
    size = 15
    color = (0, 0, 180)
    max_health = 10
    resource_gen_s = 10

    # auto initialized
    health = 10

    def __init__(self, onwer, pos, name, color, max_health, resource_gen_s, health=-1, size=-1):
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
        self.__pos = pygame.Vector2(pos[0], pos[1])
        self.name = name
        self.resource_gen_s = resource_gen_s

    # getts and setters
    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, value: tuple):
        if not isinstance(value, pygame.Vector2):
            value = pygame.Vector2(value[0], value[1])

    @property
    def resources(self):
        return self.__resources

    @resources.setter
    def resources(self, value):
        aux = self.__resources + value
        if self.__resources >= 0:
            self.__resources = aux

    # public methods
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.size)

    def update(self):
        self.__resources += self.resource_gen_s

    def is_click(self, pos):
        if(self.pos.distance_to(pos) <= self.size):
            return True
        else:
            return False

    def click(self):
        pass
