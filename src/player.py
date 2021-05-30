# standards
import random as rand


class Player():
    __id = -1

    pos = (0, 0)
    name = ''

    def __init__(self, pos, name):
        self.pos = pos
        self.name = name

        self.__id = rand.randint(0, 9999999)

    @property
    def id(self):
        return self.__id
