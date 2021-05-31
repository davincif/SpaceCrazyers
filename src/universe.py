# third party
import pygame

# internals
from .planet import Planet
from .events import CustomEvent


class Universe():
    timer = None

    planets = []
    tick_time = 1000
    ticks_perday = 2.5

    def __init__(self, tick_time=None, ticks_perday=None):
        # setting ordinary variables
        if tick_time is not None:
            self.tick_time = tick_time
        if ticks_perday is not None:
            self.ticks_perday = ticks_perday

        self.timer = pygame.time.set_timer(CustomEvent.UNIVERSE_TICK.value, self.tick_time)

    def add_planet(self, planet):
        if not isinstance(planet, Planet):
            return

        self.planets.append(planet)
        return True

    def update(self, etype):
        if etype == CustomEvent.UNIVERSE_TICK.value:
            for plan in self.planets:
                plan.update()
        elif etype == CustomEvent.UNIVERSE_DAY.value:
            print('UNIVERSE_DAY', CustomEvent.UNIVERSE_DAY.value)
