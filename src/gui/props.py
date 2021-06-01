# third party
from enum import Enum


class AlignProp(Enum):
    UP_LEFT = 0
    CENTER = 1
    DOWN_RIGHT = 2


class JustifyProp(Enum):
    START = 0
    CENTER = 1
    END = 2
    SPACE_BETWEEN = 3


class GrowthDirectionProp(Enum):
    HORIZONTAL = 0
    VERTICAL = 1
