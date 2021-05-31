# third party
import pygame

# internals
from .player import Player
from .basic_forms.circle import Circle


class Planet(Circle):
    __last_processed_ms = 0
    __resources = 0

    # need initialization
    owner = None
    name = ''
    max_health = 10
    resource_gen_s = 10

    # auto initialized
    health = 10

    def __init__(self, onwer, pos, name, color, max_health, resource_gen_s, health=-1, radius=-1):
        Circle.__init__(
            self,
            pos=pos,
            radius=radius if radius != -1 else 15,
            color=color,
        )

        # type checking
        if (not isinstance(onwer, Player)):
            raise(TypeError('onwer must be a Player object'))

        # setting ordinary variables
        self.max_health = max_health
        self.onwer = onwer
        self.name = name
        self.resource_gen_s = resource_gen_s

        # setting conditional variables
        if health == -1:
            self.health = self.max_health

    # getts and setters

    @property
    def resources(self):
        return self.__resources

    @resources.setter
    def resources(self, value):
        aux = self.__resources + value
        if self.__resources >= 0:
            self.__resources = aux

    # public methods
    def update(self):
        self.__resources += self.resource_gen_s

    def click(self):
        pass
