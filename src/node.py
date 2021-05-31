# third party
import pygame


class Node():
    # "private" variables
    is_visible = True

    # public variables
    pos = pygame.Vector2(0, 0)

    # constuctor
    def __init__(self, pos=None):
        if pos is not None:
            self.set_pos(pos)

    # getts and setters
    def get_is_visible(self):
        return self.is_visible

    def set_is_visible(self, value: bool):
        self.is_visible = bool(value)

    def get_pos(self):
        return self.__pos

    def set_pos(self, value: tuple or list):
        if not isinstance(value, pygame.Vector2):
            value = pygame.Vector2(value[0], value[1])

        if self.set_pos_callback(value):
            self.pos = value

    # Public methods, but DO NOT OVERWRITE!
    # unless you REALLY know what you're doing
    def draw(self, screen, *args, **kargs) -> bool:
        if(self.is_visible):
            self.how_to_draw_me(screen, *args, **kargs)

    # Public methods
    def set_pos_callback(self, value: tuple or list) -> bool:
        return True

    def is_click(self, pos: tuple or list) -> bool:
        return False

    def click(self):
        pass

    def how_to_draw_me(self, screen, *args, **kargs) -> bool:
        pass
