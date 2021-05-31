# third party
import pygame

# internals
from .player import Player
from .planet import Planet
from .basic_forms.triangle import Triangle
from .gui.health_bar import HealthBar


class Aircraft(Triangle):
    owner = None
    planet = None
    name = ''
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
        Triangle.__init__(
            self,
            pos=pos,
            size=size if size != -1 else 15,
            color=color,
        )

        # type checking
        if not isinstance(onwer, Player):
            raise(TypeError('owner must be a Player object'))

        if not isinstance(planet, Planet):
            raise(TypeError('planet must be a Planet object'))

        # setting ordinary variables
        self.max_health = max_health
        self.onwer = onwer
        self.name = name
        self.color = color
        self.swarm = swarm
        self.life_bar = HealthBar()

        # setting conditional variable
        if health == -1:
            self.health = self.max_health

    # public methods
    def draw(self, screen):
        super().draw(screen)

        if self.show_life_bar:
            self.life_bar.draw(screen, self.pos, self.health, self.max_health)
