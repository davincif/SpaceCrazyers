# third party
from enum import Enum


# third party
import pygame


class CustomEvent(Enum):
    UNIVERSE_EVENT = pygame.USEREVENT + 1
    UNIVERSE_TICK = pygame.USEREVENT + 2
    UNIVERSE_DAY = pygame.USEREVENT + 3
    UNIVERSE_EVENT_F = pygame.USEREVENT + 4
