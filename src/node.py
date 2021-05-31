# third party
import pygame


class Node():
    pos = pygame.Vector2(0, 0)

    def __init__(self, pos=None):
        if pos is not None:
            self.set_pos(pos)

    # getts and setters
    def get_pos(self):
        return self.__pos

    def set_pos(self, value: tuple or list):
        if not isinstance(value, pygame.Vector2):
            value = pygame.Vector2(value[0], value[1])

        if self.set_pos_callback(value):
            self.pos = value

    # Public methods
    def set_pos_callback(self, value: tuple or list) -> bool:
        return True

    def is_click(self, pos: tuple or list) -> bool:
        return False

    def click(self):
        pass

    def draw(self, screen):
        pass
